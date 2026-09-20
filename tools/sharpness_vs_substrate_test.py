# -*- coding: utf-8 -*-
"""
Sharpness-vs-Substrate falsifiable test — quantitative model + synthetic power-law
discrimination (SPUMA-VACUI / Reactive-Capsule-Graphene-Anchor).

Claim under test: the effective cavity constraint IS the reactively stored
polarization (capsule channel), not substrate contact and not mechanical
pseudo-gauge curvature.

Three transport back-reaction channels, three competing signatures:
  CAPSULE   : n_b = n_p   (tracks polarization power) , m_b ~ 0 , gate/screening sensitive
  GAUGE     : n_b = 2     (|B_pseudo|^2 ~ R^-2)       , m_b = 1/2 , insensitive
  SUBSTRATE : n_b = 1     (contact strain^2 ~ H/R)    , m_b = 1 , insensitive

Polarization law (measured independently, e.g. potential map):
  P(R) = P0 * (a/R)^n_p ;  n_p = 2 classical-flexo gradient limit (t/R -> (a/R)^2)
  steepens near the atomic cutoff R -> a (orbital saturation).
"""
import numpy as np

rng = np.random.default_rng(11)
a = 0.246          # nm, graphene lattice constant
NOISE = 0.04       # 4% relative noise on synthetic transport data

def fit_power(x, y):
    """Generic log-log fit y = A*x^n -> (exponent n, amplitude A)."""
    A = np.vstack([np.log(x), np.ones_like(x)]).T
    n, c = np.linalg.lstsq(A, np.log(y), rcond=None)[0]
    return n, np.exp(c)

def simulate_channel(kind, R, H):
    """Synthetic relative resistance change dR/R for a given channel."""
    if kind == "capsule":
        base = 1.0 * (a / R) ** 2 * (H / H[0]) ** 0.0      # n_b = 2, m_b = 0
    elif kind == "gauge":
        base = 0.6 * (a / R) ** 2 * (H / H[0]) ** 0.5      # n_b = 2, m_b = 1/2
    elif kind == "substrate":
        base = 1.0 * (H / H[0]) ** 1.0 * (a / R) ** 1.0    # n_b = 1, m_b = 1
    else:
        raise ValueError(kind)
    return base * (1 + rng.normal(0, NOISE, np.size(base)))

def decision(n_p, n_b, m_b, gate_sensitive, screening_sensitive):
    """Overdetermined channel assignment (2 continuous + 2 categorical observables)."""
    votes = {"capsule": 0, "gauge": 0, "substrate": 0}
    if abs(n_b - n_p) < 0.25 and m_b < 0.2:            votes["capsule"] += 2
    if abs(n_b - 2.0) < 0.2 and abs(m_b - 0.5) < 0.15: votes["gauge"] += 2
    if abs(n_b - 1.0) < 0.2 and abs(m_b - 1.0) < 0.2:  votes["substrate"] += 2
    if gate_sensitive and screening_sensitive:         votes["capsule"] += 2
    if (not gate_sensitive) and (not screening_sensitive):
        votes["gauge"] += 1; votes["substrate"] += 1
    return votes

print("== 1) polarization exponent n_p (independent anchor measurement) ==")
R_fixH = np.array([0.6, 0.8, 1.0, 1.5, 2.0, 3.0])
H_fix = np.full_like(R_fixH, 5.0)
P_dat = 1e-1 * (a / R_fixH) ** 2 * (1 + rng.normal(0, 0.05, R_fixH.size))
n_p, P0 = fit_power(a / R_fixH, P_dat)      # exponent in sharpness variable u = a/R
print(f"   fitted n_p = {n_p:.3f}  (theory: 2.0 classical-gradient; steepens below R~a)")

print("\n== 2) synthetic transport back-reaction: exponent recovery per channel ==")
results = {}
for kind in ("capsule", "gauge", "substrate"):
    dR = simulate_channel(kind, R_fixH, H_fix)
    n_b, _ = fit_power(a / R_fixH, dR)                 # sharpness exponent (in u = a/R)
    # height sweep at fixed sharpness R = 1 nm
    H_sweep = np.array([2.0, 3.0, 5.0, 8.0, 12.0])
    R_fix = np.full_like(H_sweep, 1.0)
    dR_H = simulate_channel(kind, R_fix, H_sweep)
    m_b, _ = fit_power(H_sweep, dR_H)                  # height exponent (in H, increasing)
    results[kind] = (n_b, m_b)
    print(f"   {kind:9s}: n_b = {n_b:6.3f}  (target {2 if kind!='substrate' else 1})"
          f"   m_b = {m_b:6.3f}  (target {0 if kind=='capsule' else (0.5 if kind=='gauge' else 1)})")

print("\n== 3) decision matrix (with the categorical gate/screening legs) ==")
for kind in ("capsule", "gauge", "substrate"):
    n_b, m_b = results[kind]
    gate = screening = (kind == "capsule")
    votes = decision(n_p, n_b, m_b, gate, screening)
    winner = max(votes, key=votes.get)
    print(f"   injected {kind:9s} -> verdict {winner:9s}  votes={votes}"
          f"   {'OK' if winner==kind else 'MISASSIGNED'}")

print("\n== 4) anchor-scale numbers (R = 1 nm, H = 5 nm, lambda/hBN screening switch) ==")
R0, H0 = 1.0, 5.0
P1 = P0 * (a / R0) ** 2
print(f"   P(1nm) ~ {P1*1e3:.1f} mC/m^2  (orbital polarization, anchor-consistent)")
print(f"   capsule signature: dR/R vs R exponent must equal n_p = {n_p:.2f};"
      f" H-sweep exponent must vanish (m_b ~ 0).")
print(f"   falsification thresholds: |n_b - n_p| > 0.25  OR  m_b > 0.2"
      f"  OR gate/screening-insensitive -> capsule constraint REJECTED")
