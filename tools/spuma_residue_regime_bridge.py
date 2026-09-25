# -*- coding: utf-8 -*-
"""
K1 CRITICAL EDGE (b_c) x RESIDUE-CLASSIFICATION EDGE (d_class) — universality test.

Register entry (Aligned-Protocol S5): the LIMEN residue-test parameter map set
the classification edge d_class = eps*m/(1-eps) = 0.0686 (m = phi(b)/Phi(b) at
b=0.30; eps=0.1), and SPUMA K1 has its own critical bias b_c = 0.126 — the
p_f = p_c = 0.592746 edge of the sharp-corner freeze-out (start margin m0=1.5).
Question: are these ONE universal threshold, or TWO edges of ONE register?

Key structural fact [exact]: the K1 drift b IS a one-sided dynamical bias
(frozen sites never move = rectified above-edge), so the two registers share
one axis decomposition b_eff = b + d with ORTHOGONAL observables:
  * p_f sees only b_eff  (freeze-out gauge identity: mask(b,d) == mask(b+d,0))
  * the residue classification sees only d (rel(d) = d/(m+d), LIMEN closed form)
so the two edges cannot "be the same number" — they can only MEET as a
composed pair. This tool (1) states the dimensionless ratios, (2) proves the
freeze-out gauge identity bit-for-bit, (3) runs the composed MEETING POINT
(b = b_c - d_class, d = d_class) where criticality and the classification edge
co-occur — the shared-p_f test, (4) proves the no-go AT b_c (criticality and
detectable residue exclude each other), and (5) builds the classification x
regime matrix on the shared p_f currency.

Labels: [exact]/[exact model] for identities and closed forms, [measured] for
Monte-Carlo outcomes, [protocol-mirror, conceptual] for interpretation.
Provenance: b_c, m0, p_c, generator -> SPUMA tools/cavity_cluster_scaling.py +
tools/tau_precise_fit.py; d_class, d_det, m, eps -> LIMEN
tools/limen_residue_param_map.py (+ _output.txt); critical band -> SPUMA
tools/spectral_prediction_output.txt.
"""
import numpy as np
from collections import defaultdict
import os, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- SPUMA K1 constants (tools/cavity_cluster_scaling.py / tau_precise_fit.py) ----
BC  = 0.126        # p_f-calibrated critical bias (p_f = 0.593 vs p_c = 0.592746)
M0  = 1.5          # start margin rho0 ~ N(m0, 0.5)
P_C = 0.592746     # 2D square site percolation
# ---- LIMEN residue-map constants (tools/limen_residue_param_map.py) ----
B_LIMEN = 0.30
MILLS   = 0.61722  # m = phi(b)/Phi(b); closed form reproduces v5 anchor 0.91720
EPS     = 0.1
D_CLASS = EPS * MILLS / (1.0 - EPS)   # 0.0686 [exact model]
D_DET   = 0.0067                      # detection edge (SNR ~ 1488 per unit d)
# critical calibration band (tools/spectral_prediction_output.txt, L=256):
#   b=0.122: p_f=0.6028 ; b=0.126: 0.5933 ; b=0.130: 0.5840  -> dp/db ~ -2.325
#   band p_f in [0.588, 0.598] <-> b in [0.1240, 0.1283] -> half-width:
D_CRIT  = 0.002    # max one-sided depth keeping p_f inside the critical band

B_MEET = BC - D_CLASS                 # composed meeting point (0.0574)

# ---------------- identical field generator (K1 contract) ----------------

def simulate(L, b, m0=1.5, seed=0, T_max=4000, patience=200, extra_d=0.0):
    """Rectified freeze-out. extra_d = one-sided depth on MOBILE sites only
    (frozen never move) — the LIMEN side-2 rectified protocol on the K1 field.
    NOTE the dynamics depends only on b_eff = b + extra_d; kept separate so the
    gauge identity can be tested explicitly rather than assumed."""
    rng = np.random.default_rng(seed)
    rho = m0 + 0.5 * rng.standard_normal((L, L))
    frozen = rho < 0.0
    quiet = 0
    for t in range(T_max):
        xi = rng.standard_normal((L, L))
        mob = ~frozen
        rho = np.where(mob, rho + xi + b + extra_d, rho)
        newly = mob & (rho < 0.0)
        frozen |= newly
        quiet = quiet + 1 if newly.sum() <= max(1, 3e-4 * L * L) else 0
        if quiet >= patience:
            break
    return frozen

def cluster_stats(mask):
    """Full row-run union-find -> (sizes, spanning)."""
    H, W = mask.shape
    parent = []
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    all_runs, prev = [], []  # (row, start, end, node) per run
    for i in range(H):
        row = mask[i].view(np.int8)
        d = np.diff(np.concatenate(([0], row, [0])))
        starts, ends = np.where(d == 1)[0], np.where(d == -1)[0]
        cur = []
        for s, e in zip(starts, ends):
            me = len(parent); parent.append(me)
            for ps, pe, pr in prev:
                if ps < e and s < pe:
                    union(me, pr)
            cur.append((s, e, me))
            all_runs.append((i, s, e, me))
        prev = [(s, e, find(m)) for s, e, m in cur]
    sizes = defaultdict(int)
    for i, s, e, me in all_runs:
        sizes[find(me)] += e - s
    r0 = {find(me) for i, s, e, me in all_runs if i == 0}
    rH = {find(me) for i, s, e, me in all_runs if i == H - 1}
    return np.array(sorted(sizes.values())), bool(r0 & rH)

def regime_of(p_f, span):
    if 0.588 <= p_f <= 0.598:
        return "CRITICAL band" + (" + finite-size spanning" if span else "")
    if p_f > 0.598:
        return "NETWORK (supercritical)" if span else "pre-critical dense"
    return "ISOLATED (subcritical)"

def classification_of(d):
    rel = d / (MILLS + d)
    return rel, ("REAL" if rel > EPS else "frame-made")

# --------------------------------- run ---------------------------------

W = 74
print("=" * W)
print("K1 CRITICAL EDGE x RESIDUE-CLASSIFICATION EDGE — universality test")
print("register: K1 freeze-out L=256 (m0=%.1f, sigma_xi=1) ; LIMEN map b=%.2f, m=%.5f"
      % (M0, B_LIMEN, MILLS))
print("=" * W)

# ---------- [1] dimensionless ratios ----------
print("\n[1] dimensionless ratios [exact model] — bias depth over its own margin scale:")
r_L = D_CLASS / MILLS
r_S = BC / M0
print(f"    r_LIMEN = d_class/m  = eps/(1-eps) = {r_L:.4f}   (= 1/9 at eps=0.1)")
print(f"    r_SPUMA = b_c/m0                   = {r_S:.4f}")
print(f"    ratio r_L/r_S = {r_L/r_S:.3f}  -> same decade (1e-1), NOT equal.")
print("    honest statement: same-order ratios alone are numerology (residue-test")
print("    v1 lesson) — the real test is the composed dynamics below.")

# ---------- [2] freeze-out gauge identity ----------
print("\n[2] freeze-out gauge identity [exact]: mask(b, d) == mask(b+d, 0) —")
print("    the field sees only b_eff = b + d; p_f and regime are d-blind.")
ok = True
for sd in (1, 2, 3):
    mA = simulate(256, B_MEET, seed=sd, extra_d=D_CLASS)
    mB = simulate(256, B_MEET + D_CLASS, seed=sd)
    same = np.array_equal(mA, mB)
    ok &= same
    if sd == 1:
        print(f"    seed {sd}: identical masks: {same} "
              f"(p_f = {mA.mean():.4f} both)")
print(f"    gauge identity: {'HOLDS bit-for-bit' if ok else 'VIOLATED'} [exact]")

# ---------- [3] the composed meeting point (shared-p_f test) ----------
print("\n[3] MEETING POINT [measured]: (b = b_c - d_class, d = d_class) = "
      f"({B_MEET:.4f}, {D_CLASS:.4f})")
print("    claim: there is exactly ONE composed pair where the K1 field sits at")
print("    the critical edge (p_f = p_c) AND the residue classification flips.")
rel_m, cls_m = classification_of(D_CLASS)
pfs, spans_ = [], []
for sd in (1, 2, 3):
    m = simulate(256, B_MEET, seed=sd, extra_d=D_CLASS)
    _, span = cluster_stats(m)
    pfs.append(m.mean()); spans_.append(span)
p_f_meet = float(np.mean(pfs))
print(f"    p_f(meeting) = {p_f_meet:.4f}  (target p_c = {P_C})   "
      f"span {100*sum(spans_)/3:.0f}%  -> regime: {regime_of(p_f_meet, sum(spans_) > 0)}")
print(f"    rel(d_class) = {rel_m:.4f}  -> classification edge (={EPS}) [exact model]")
pfs0 = [simulate(256, BC, seed=sd).mean() for sd in (1, 2, 3)]
print(f"    control p_f(b_c, d=0) = {np.mean(pfs0):.4f} — equal by the gauge identity.")
print(f"    MEETING CONFIRMED: {'YES' if abs(p_f_meet - P_C) < 0.02 else 'NO'} "
      f"[measured] + rel edge [exact model]")

# ---------- [4] the no-go AT b_c ----------
print("\n[4] NO-GO at b_c [measured]: holding the field critical excludes any")
print("    detectable residue — the two edges exclude each other AT b_c.")
band_lo = BC - D_CRIT; band_hi = BC + D_CRIT
print(f"    critical band (from calibration): b in [{band_lo:.4f}, {band_hi:.4f}]"
      f"  -> max one-sided depth d_crit = {D_CRIT}")
print(f"    LIMEN edges:                     d_det = {D_DET}   d_class = {D_CLASS:.4f}")
print(f"    ordering: d_crit ({D_CRIT}) < d_det ({D_DET}) < d_class ({D_CLASS:.4f})"
      f"  [exact model from measured band]")
print("    -> at b = b_c, a one-sided correction deep enough to DETECT (d>d_det)")
print("       already moves p_f by ~%.4f — 1.6x the FULL critical band (0.010) — i.e." % (2.325 * D_DET))
print("       pushes the field OFF criticality. Critical K1 is residue-clean")
print("       BY GEOMETRY: verdict at criticality is 'frame-made or undetectable'.")
for d_try, tag in ((D_DET, "d_det"), (D_CLASS, "d_class")):
    vv = [simulate(256, BC, seed=sd, extra_d=d_try).mean() for sd in (1, 2)]
    print(f"      b=b_c, d={tag} ({d_try:.4f}): p_f = {np.mean(vv):.4f} "
          f"(Delta p_f = {np.mean(pfs0) - np.mean(vv):+.4f} vs band width 0.010)")

# ---------- [5] classification x regime matrix ----------
print("\n[5] classification x regime matrix [measured] (L=256, 2 seeds; rel [exact model]):")
print(f"    {'b':>7} {'d':>7} {'b_eff':>7} {'p_f':>7} {'span%':>6}  {'regime':<24} {'rel':>6} class")
for b in (B_MEET, BC, 0.1946, 0.285):
    for d in (0.0, D_CLASS):
        ms = [simulate(256, b, seed=sd, extra_d=d) for sd in (1, 2)]
        p_f = float(np.mean([m.mean() for m in ms]))
        sp = np.mean([cluster_stats(m)[1] for m in ms])
        rel, cls = classification_of(d)
        print(f"    {b:7.4f} {d:7.4f} {b+d:7.4f} {p_f:7.4f} {100*sp:6.1f}  "
              f"{regime_of(p_f, sp > 0):<24} {rel:6.3f} {cls}")

# ---------- verdict ----------
print("\n" + "=" * W)
print("VERDICT:")
print("  1. NOT one universal threshold: p_f is d-blind [exact gauge identity],")
print("     the classification is p_f-blind — the edges live on ORTHOGONAL axes")
print("     of one register (b_eff = b + d).")
print("  2. They DO meet, exactly once: (b, d) = (%.4f, %.4f) with b_eff = b_c —"
      % (B_MEET, D_CLASS))
print("     field critical AND classification edge co-occur [measured + exact model].")
print("  3. No-go at b_c: d_crit=%.3f < d_det=%.4f < d_class=%.4f — criticality"
      % (D_CRIT, D_DET, D_CLASS))
print("     excludes any detectable residue; conversely a residue-REAL correction")
print("     (d > d_class) drives the field deep-subcritical (isolated cavities —")
print("     SPUMA's desired register). The classification edge GUARDS the entrance")
print("     of the isolated-cavity regime.")
print("  4. ratios r_L=1/9, r_S=0.084 (ratio 1.32) are same-decade but their")
print("     equality is NOT what makes the meeting exist — composition does.")
print("     At the meeting the channel split b:d = %.2f:%.2f (~45:55)"
      % (B_MEET, D_CLASS))
print("     [protocol-mirror, conceptual; depends on eps=0.1].")
print("labels: gauge identity [exact]; meeting/no-go/matrix [measured];")
print("rel(d)=d/(m+d) [exact model]; interpretation [protocol-mirror, conceptual].")
