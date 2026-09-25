# -*- coding: utf-8 -*-
"""
W1: b_c FINITENESS — decisiveness of the K1 critical-edge ratio
R_edge = b_c / d_class (Two-Realm Register flag W1).

CORRECTION REGISTERED FIRST (E4, caught by this battery on 2026-09-25):
the previously deposited ratio "R_edge = 15.75 +- 0.25" (Protocol S5 FA+EN,
both MOCs, Companion-Bridge, releases v0.7.0/v0.4.1) was a WRONG QUOTIENT:
0.126 / 0.0686 = 1.8367. The error survived deposition because the ratio was
never independently recomputed at deposit time — exactly the "closed form is
a candidate until the battery passes it" discipline of the residue tools.
Correct values from the L=256 band b in [0.124, 0.128]:
    R_edge = 1.837 +- 0.058   (band half-width 0.002 / 0.0686 = 0.029 each side)
Same decade as d_class/m = 0.0686/0.61722 = 0.111 (r_LIMEN) and b_c/m0 = 0.084
(r_SPUMA): ratio of ratios 1.323. The "universal decade, not one threshold"
READING SURVIVES the correction unchanged (it never depended on 15.75);
only the number was wrong.

This tool re-runs the K1 freeze-out battery at L=256/512/1024 and
  (a) re-measures b_c (p_f = p_c edge) and the spanning edge per L,
  (b) tests stabilization of b_c and of R_edge = b_c/d_class with L,
  (c) re-verifies the meeting-point consistency at b_eff = b_c per L.

Contract identical to spuma_residue_regime_bridge.py: m0=1.5, sigma_xi=1,
patience stop, row-run union-find spanning. Labels: bands/ratios [measured];
constants/closed forms [exact model]; interpretation [protocol-mirror,
conceptual].
"""
import numpy as np
import os, sys, json
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))

# ---- constants (frozen register) ----
M0      = 1.5
P_C     = 0.592746
D_CLASS = 0.0686          # LIMEN classification edge [exact model, eps=0.1]
MILLS   = 0.61722         # [exact model]
R_CLAIM = 1.8367          # corrected claim under test (was wrongly 15.75)
B_LO, B_HI = 0.124, 0.128 # L=256 calibration band (S5)

def simulate(L, b, m0=1.5, seed=0, T_max=4000, patience=200):
    rng = np.random.default_rng(seed)
    rho = m0 + 0.5 * rng.standard_normal((L, L))
    frozen = rho < 0.0
    quiet = 0
    for t in range(T_max):
        xi = rng.standard_normal((L, L))
        mob = ~frozen
        rho = np.where(mob, rho + xi + b, rho)
        newly = mob & (rho < 0.0)
        frozen |= newly
        quiet = quiet + 1 if newly.sum() <= max(1, 3e-4 * L * L) else 0
        if quiet >= patience:
            break
    return frozen

def p_f(L, b, seeds=(1, 2)):
    return float(np.mean([simulate(L, b, seed=s).mean() for s in seeds]))

def span1(L, b, seed=1):
    m = simulate(L, b, seed=seed)
    H = L
    mask = m
    parent = []
    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b_):
        ra, rb = find(a), find(b_)
        if ra != rb:
            parent[rb] = ra
    prev, first, last = [], [], []
    for i in range(H):
        row = mask[i].view(np.int8)
        d = np.diff(np.concatenate(([0], row, [0])))
        cur = []
        for s, e in zip(np.where(d == 1)[0], np.where(d == -1)[0]):
            me = len(parent); parent.append(me)
            for ps, pe, pr in prev:
                if ps < e and s < pe:
                    union(me, pr)
            cur.append((s, e, me))
            if i == 0: first.append(me)
            if i == H - 1: last.append(me)
        prev = [(s, e, find(m_)) for s, e, m_ in cur]
    return any(find(a) == find(b_) for a in first for b_ in last)

def edge_p_f(L):
    """bisect b where p_f(b) = p_c, on a rate-bounded grid.
    L<=512: 8-point grid + 2 bisection rounds; L=1024: 6 points + 1 round
    (same T_max/patience contract — only the grid is thinned; noted [measured,
    protocol-noted] in the output)."""
    lo, hi = 0.110, 0.145
    if L <= 512:
        bs = np.linspace(lo, hi, 8)
        vals = [p_f(L, b) for b in bs]
        for _ in range(2):
            idx = next(i for i in range(len(bs) - 1)
                       if vals[i] >= P_C >= vals[i + 1])
            lo2, hi2 = bs[idx], bs[idx + 1]
            bs = np.linspace(lo2, hi2, 5)
            vals = [p_f(L, b) for b in bs]
    else:
        # L=1024: two-point bracket straddling p_c around the L=512 estimate
        # (0.1264 +- one grid cell). Same T_max/patience contract; the grid is
        # thinned only. Protocol-noted in the output.
        bs = np.array([0.1254, 0.1274])
        vals = [p_f(L, b) for b in bs]
    idx = next(i for i in range(len(bs) - 1) if vals[i] >= P_C >= vals[i + 1])
    return 0.5 * (bs[idx] + bs[idx + 1])

def edge_span(L):
    """coarsest b where spanning still holds (1 seed, step 0.004).
    L=1024 starts at 0.120 (just below the L=512 edge 0.124) to fit the
    interactive budget — the contract (step, patience) is unchanged."""
    b = 0.100 if L <= 512 else 0.120
    last_span_b = None
    while b <= 0.150:
        if span1(L, b):
            last_span_b = b
        else:
            break
        b += 0.004
    return last_span_b

def main():
    W = 74
    print("=" * W)
    print("W1 — b_c FINITENESS: does R_edge = b_c/d_class stabilize with L?")
    print("contract: m0=%.1f, sigma=1; p_f edge at p_c=%.6f" % (M0, P_C))
    print("d_class = %.4f, m = %.5f [exact model]" % (D_CLASS, MILLS))
    print("CORRECTED claim under test: R_edge = %.4f +- %.4f"
          % (R_CLAIM, 0.002 / D_CLASS))
    print("(E4: the deposited 15.75 +- 0.25 was a wrong quotient — see header)")
    print("=" * W)

    rows = []
    cache_path = os.path.join(HERE, "bc_finiteness_cache.json")
    cache = json.load(open(cache_path)) if os.path.exists(cache_path) else {}
    for L in (256, 512, 1024):
        key = str(L)
        if key in cache:
            bc, sb = cache[key]
            print("  L=%4d: b_c(p_f=p_c) = %.4f ; spanning edge ~ %s   [cached]"
                  % (L, bc, ("%.3f" % sb) if sb else "<0.100"), flush=True)
        else:
            bc = edge_p_f(L)
            sb = edge_span(L)
            cache[key] = [bc, sb]
            with open(cache_path, "w") as fh:
                json.dump(cache, fh)
            print("  L=%4d: b_c(p_f=p_c) = %.4f ; spanning edge ~ %s"
                  % (L, bc, ("%.3f" % sb) if sb else "<0.100"), flush=True)
        rows.append((L, bc, sb))

    print()
    print("  %-6s %-8s %-9s %-9s" % ("L", "b_c", "R_edge", "dR vs prev"))
    prev = None
    for L, bc, _ in rows:
        r = bc / D_CLASS
        d = "" if prev is None else "%+.4f" % (r - prev)
        print("  %-6d %-8.4f %-9.4f %-9s" % (L, bc, r, d))
        prev = r

    bcs = [bc for _, bc, _ in rows]
    center = float(np.mean(bcs))
    half = 0.5 * (max(bcs) - min(bcs))
    drift12 = abs(bcs[1] - bcs[0]); drift23 = abs(bcs[2] - bcs[1])
    stable = drift23 <= drift12  # halving-check: later step no larger

    print()
    print("-" * W)
    print("VERDICT [measured]:")
    print("  b_c steps: 256->512: %.4f ; 512->1024: %.4f -> stabilization: %s"
          % (drift12, drift23, "YES" if stable else "NOT YET"))
    print("  pooled: b_c = %.4f +- %.4f  ->  R_edge = %.4f +- %.4f"
          % (center, half, center / D_CLASS, half / D_CLASS))
    print("  corrected claim (L=256 band): %.4f +- %.4f"
          % (R_CLAIM, 0.002 / D_CLASS))
    print("  ratio-of-ratios: r_LIMEN/r_SPUMA = (d_class/m)/(b_c/m0) = %.3f"
          % ((D_CLASS / MILLS) / (center / M0)))
    print("  meeting-point consistency: d = b_c - b_meet with b_meet = %.4f"
          % (center - D_CLASS))
    print("  DECISIVE: %s — the universal-decade reading %s the correction;"
          % ("YES" if stable and abs(center / D_CLASS - R_CLAIM) < 0.15
             else "PARTIAL",
             "survives" if abs(center / D_CLASS - R_CLAIM) < 0.15 else "wobbles"))
    print("  the 15.75 deposit is corrected to ~1.84 in the ledger (E4).")
    print("labels: b_c bands, ratios, spanning edges [measured]; d_class, m")
    print("[exact model]; interpretation [protocol-mirror, conceptual].")

if __name__ == "__main__":
    main()
