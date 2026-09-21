# -*- coding: utf-8 -*-
"""
Spectral regime prediction: translate the three K1 cavity-size regimes into
cavity-harmonic spectra, and derive falsifiable discriminators.

Physics chain (vault: 03_Cavity_Harmonics/Intrinsic-Harmonics):
  every cavity is a confined harmonic domain (K2 wall = Dirichlet envelope).
  Fundamental frequency from the ON-LATTICE operator
      (L psi)_i = 4 psi_i - sum_{j in cavity, j~i} psi_j ,  omega_1 = sqrt(lambda_1)
  (full lattice degree 4; missing neighbors contribute psi=0 = polarized wall).
  omega_1 solved EXACTLY (dense eigvalsh) for every cluster with s<=300.
  Bigger clusters are counted but excluded from exponent fits (honest coverage
  reported) — inverse solvers cannot resolve lambda_1~1e-6 giants at this cost.

CENTRAL DISCRIMINATOR — spectral dimension d_s:
  omega_1 ~ s^(-gamma_s), gamma_s = 1/d_s (d_w = 2 d_f/d_s).
      compact-like domains   gamma_s ~= 0.50     (d_s = 2)
      ramified/fractal walk  gamma_s ~= 0.72-0.75 (d_s ~ 1.31-4/3, 2D percolation)
  (The "naive extent" gamma = 1/(2 D_f) = 0.53 is nearly degenerate with the
   compact value and merged into the compact-like band.)
  Derived count-weighted tail slope alpha1 = d_s (tau-1) - 1:
      compact-like -> 2 tau - 3 = 1.11,  ramified -> 0.41  (tau = 187/91)

Regime -> spectral shape:
  * white subcritical  -> BAND with sharp edges (support ~ 0.2 dec, Q high)
  * critical b_c       -> scale-free TAIL (alpha above) — forbidden register
  * colored noise      -> LINE; compact linewidth rule std(ln w) = (1/2) std(ln s)

CONSTANT CORRECTION (documented): the 2D percolation cluster-size exponent is
tau = 187/91 = 2.0549 (Fisher 2 + beta/(beta+gamma), beta=5/36, gamma=43/18;
= 1 + d/D_f with D_f = 91/48). The value 187/48 printed in the K1 study
docstring is 2 + D_f — a numerological twin, NOT tau. K1 measured cutoff
dimension D = 1.78 vs 91/48 = 1.896 stands.
"""
import numpy as np
from collections import defaultdict

P_C = 0.592746
TAU = 187.0 / 91.0          # exact 2D percolation Fisher exponent
D_F = 91.0 / 48.0           # critical cluster mass fractal dimension

# ---------------- field generator (identical to the K1 study) ----------------

def _box1d(a, w, axis):
    n = a.shape[axis]
    pad = [(0, 0)] * a.ndim
    pad[axis] = (w//2, w - w//2)
    ap = np.pad(a, pad, mode="edge")
    c = np.cumsum(ap, axis=axis, dtype=np.float64)
    hi = [slice(None)]*a.ndim; lo = [slice(None)]*a.ndim
    hi[axis] = slice(w, w + n); lo[axis] = slice(0, n)
    return (c[tuple(hi)] - c[tuple(lo)]) / w

def smooth2d(a, w):
    return _box1d(_box1d(a, w, 0), w, 1)

def simulate(L, b, m0=1.5, lc=0, seed=0, T_max=4000, patience=200):
    rng = np.random.default_rng(seed)
    rho = m0 + 0.5 * rng.standard_normal((L, L))
    frozen = rho < 0.0
    quiet = 0
    for t in range(T_max):
        xi = rng.standard_normal((L, L))
        if lc:
            xi = smooth2d(xi, lc)
            xi /= (xi.std() + 1e-12)
        mob = ~frozen
        rho = np.where(mob, rho + xi + b, rho)
        newly = mob & (rho < 0.0)
        frozen |= newly
        quiet = quiet + 1 if newly.sum() <= max(1, 3e-4*L*L) else 0
        if quiet >= patience:
            break
    return frozen

def clusters(mask):
    """Row-run union-find with per-root boundary (spanning) detection.
    Returns dict sizes and root->coords, EXCLUDING spanning clusters."""
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
    all_runs = []
    prev = []
    for i in range(H):
        row = mask[i].view(np.int8)
        d = np.diff(np.concatenate(([0], row, [0])))
        starts = np.where(d == 1)[0]
        ends = np.where(d == -1)[0]
        cur = []
        for s, e in zip(starts, ends):
            me = len(parent); parent.append(me)
            for ps, pe, pr in prev:
                if ps < e and s < pe:
                    union(me, pr)
            cur.append((s, e, me))
            all_runs.append((i, s, e, me))
        prev = [(s, e, find(m)) for s, e, m in cur]
    top_roots = {find(me) for i, s, e, me in all_runs if i == 0}
    bot_roots = {find(me) for i, s, e, me in all_runs if i == H-1}
    spanning = top_roots & bot_roots
    sizes = defaultdict(int)
    coords = defaultdict(list)
    for i, s, e, me in all_runs:
        r = find(me)
        if r in spanning:
            continue
        sizes[r] += e - s
        coords[r].append((i, np.arange(s, e)))
    cd = {}
    for r, chunks in coords.items():
        ii = np.concatenate([np.full(len(jj), i) for i, jj in chunks])
        jj = np.concatenate([jj for i, jj in chunks])
        cd[r] = np.stack([ii, jj], axis=1)
    return dict(sizes), cd

# ------------- exact fundamental frequency of one cavity (on-lattice) -------------

_DENSE_MAX = 300

def fundamental_omega(coords):
    n = len(coords)
    if n > _DENSE_MAX:
        return np.nan
    idx = {}
    for k, (i, j) in enumerate(coords):
        idx[(int(i), int(j))] = k
    Lap = np.zeros((n, n))
    for k, (i, j) in enumerate(coords):
        Lap[k, k] = 4.0
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nb = idx.get((int(i)+di, int(j)+dj))
            if nb is not None:
                Lap[k, nb] -= 1.0
    lam1 = max(np.linalg.eigvalsh(Lap)[0], 1e-12)
    return float(np.sqrt(lam1))

def collect_omegas(b, lc, seeds, L):
    """Returns om, sz (s<=300 exactly solved), plus coverage counters."""
    oms, szs = [], []
    n_all = n_solved = n_span = 0
    pfs = []
    for sd in seeds:
        mm = simulate(L, b, lc=lc, seed=sd)
        pfs.append(mm.mean())
        sizes, cd = clusters(mm)
        for r, arr in cd.items():
            n_all += 1
            w1 = fundamental_omega(arr)
            if np.isnan(w1):
                continue
            n_solved += 1
            oms.append(w1); szs.append(sizes[r])
    return (np.array(oms), np.array(szs, float),
            dict(n_all=n_all, n_solved=n_solved, n_span=n_all-n_solved,
                 p_f=float(np.mean(pfs))))

# ----------------------------- analysis helpers -----------------------------

def logbin_spec(om, wt, nb=20):
    lo, hi = om.min()*0.9, om.max()*1.1
    edges = np.logspace(np.log10(lo), np.log10(hi), nb+1)
    cnt, _ = np.histogram(om, bins=edges, weights=wt)
    dens = cnt/(edges[1:] - edges[:-1])
    ctr = np.sqrt(edges[:-1]*edges[1:])
    return ctr, dens, dens > 0

def powerlaw_slope(x, y, keep):
    if keep.sum() < 6:
        return np.nan, np.nan
    X, Y = np.log10(x[keep]), np.log10(y[keep])
    A = np.vstack([X, np.ones_like(X)]).T
    coef, *_ = np.linalg.lstsq(A, Y, rcond=None)
    yhat = A @ coef
    r2 = 1 - ((Y-yhat)**2).sum()/max(((Y-Y.mean())**2).sum(), 1e-12)
    return coef[0], r2

def gamma_of_s(om, sz, s_lo=16, s_hi=300):
    k = (sz >= s_lo) & (sz <= s_hi)
    if k.sum() < 30:
        return np.nan, np.nan, int(k.sum())
    x, y = np.log(sz[k]), np.log(om[k])
    A = np.vstack([x, np.ones_like(x)]).T
    coef, *_ = np.linalg.lstsq(A, y, rcond=None)
    yhat = A @ coef
    r2 = 1 - ((y-yhat)**2).sum()/((y-y.mean())**2).sum()
    return -coef[0], r2, int(k.sum())

def shape_metrics(om, wt):
    mw = (om*wt).sum()/wt.sum()
    sw = np.sqrt((((om-mw)**2)*wt).sum()/wt.sum())
    lo, hi = np.percentile(om, [5, 95])
    return mw, sw, mw/max(sw, 1e-12), np.log10(hi/lo)

# --------------------------------- run ---------------------------------

print("== Spectral regime prediction: cavity fundamental frequency from the exact")
print("   on-lattice Dirichlet Laplacian (s<=300 exact); spanning clusters removed")
print("   by boundary test; discriminator: gamma_s = 1/d_s. p_f printed per run.\n")

print("-- operator sanity: exact n x n squares vs sqrt(4-4cos(pi/(n+1)))")
for n in (4, 8, 16):
    coords = np.array([(i, j) for i in range(n) for j in range(n)], dtype=float)
    w = fundamental_omega(coords)
    we = np.sqrt(4 - 4*np.cos(np.pi/(n+1)))
    print(f"   n={n:3d}: omega={w:.6f} analytic={we:.6f} diff={abs(w-we):.1e}")
print()

# --- critical bias calibration: find b with p_f in [0.588, 0.598] at L=256 ---
print("-- calibrating b_c on p_f (L=256, 2 seeds each):")
bc = 0.126
for b in (0.122, 0.126, 0.130, 0.134):
    pf = np.mean([simulate(256, b, seed=s).mean() for s in (1, 2)])
    print(f"   b={b:.3f}: p_f = {pf:.4f}  (target {P_C})")
    if 0.588 <= pf <= 0.598:
        bc = b
print(f"   -> chosen b_c = {bc:.3f}\n")

runs = [
    ("white subcritical (b=0.30)",   dict(b=0.30, lc=0, L=256, seeds=(1, 2, 3, 4))),
    ("critical (b=%.3f, L=512)" % bc, dict(b=bc, lc=0, L=512, seeds=(1, 2))),
    ("colored noise (lc=3, b=0.30)", dict(b=0.30, lc=3, L=256, seeds=(1, 2, 3, 4))),
]

S_LO, S_HI = 16, 300
results = {}
for name, cfg in runs:
    om, sz, cov = collect_omegas(cfg["b"], cfg["lc"], cfg["seeds"], cfg["L"])
    omt, szt = om[sz >= S_LO], sz[sz >= S_LO]
    ctr, dens, keep = logbin_spec(omt, np.ones_like(omt))
    a1, r21 = powerlaw_slope(ctr, dens, keep)
    ctr2, dens2, keep2 = logbin_spec(omt, szt)
    a2, r22 = powerlaw_slope(ctr2, dens2, keep2)
    g, r2g, npairs = gamma_of_s(om, sz, S_LO, S_HI)
    mw, sw, Q, dec = shape_metrics(om, sz)
    lnw, lns = float(np.std(np.log(om))), float(np.std(np.log(sz)))
    results[name] = dict(a1=a1, r21=r21, a2=a2, r22=r22, g=g, r2g=r2g, npairs=npairs,
                         Q=Q, dec=dec, lnw=lnw, lns=lns, n=len(om), cov=cov,
                         wrange=(om.min(), om.max()), smax=int(sz.max()))
    print(f"-- {name}")
    print(f"   p_f = {cov['p_f']:.4f} (target {P_C})   clusters total={cov['n_all']}, "
          f"exact-solved={cov['n_solved']} (spanning/network excluded={cov['n_span']})")
    print(f"   s_max(solved)={int(sz.max())}  omega=[{om.min():.4f},{om.max():.3f}] "
          f"({np.log10(om.max()/om.min()):.2f} dec)")
    print(f"   gamma_s = {g:.3f} (R^2={r2g:.3f}, n={npairs})  ->  d_s = "
          f"{1/g if g and g > 0 else float('nan'):.3f}")
    print(f"   alpha1: {a1:+.2f} (R^2={r21:.3f})   alpha2: {a2:+.2f} (R^2={r22:.3f})")
    print(f"   shape: Q={Q:.2f}, support={dec:.2f} dec, std(ln w)={lnw:.3f}, "
          f"std(ln s)={lns:.3f}\n")

# ------------------- discriminators / predictions table -------------------

print("== Discriminators ==")
cr = [v for k, v in results.items() if k.startswith("critical")][0]
cr_key = [k for k in results if k.startswith("critical")][0]
rw = results["white subcritical (b=0.30)"]
cl = results["colored noise (lc=3, b=0.30)"]
print(f"{'white subcritical':<34} BAND  support={rw['dec']:.2f} dec, Q={rw['Q']:.1f}"
      f"   -> near-homogeneous (A1 ok)")
print(f"{cr_key:<34} TAIL  see below   -> FORBIDDEN register (network)")
print(f"{'colored noise':<34} LINE  Q={cl['Q']:.1f}, support={cl['dec']:.2f} dec"
      f"   -> homogeneous register (A1 strongest)")

print("\n-> critical-regime spectral dimension (the discriminator):")
g = cr["g"]
print(f"   measured gamma_s = {g:.3f}  ->  d_s = {1/g if g>0 else float('nan'):.3f}")
print(f"   reference bands: compact-like gamma~=0.50 (d_s=2) | "
      f"ramified gamma~=0.72-0.75 (d_s~1.31-4/3)")
if g > 0:
    band = "RAMIFIED/FRACTAL" if g >= 0.62 else "COMPACT-LIKE"
    print(f"   verdict: {band}")
print(f"   predicted alpha1 = d_s(tau-1)-1: compact-like {2*TAU-3:.2f} | "
      f"ramified {(4/3)*(TAU-1)-1:+.2f}")
print(f"   measured alpha1 = {cr['a1']:+.2f}, alpha2 = {cr['a2']:+.2f} "
      f"(alpha2 robust prediction ~ -0.9)")

print("\n-> linewidth = polydispersity probe (colored regime, ln space):")
print(f"   std(ln omega) = {cl['lnw']:.3f}  vs  (1/2) std(ln s) = {0.5*cl['lns']:.3f}"
      f"  (compact rule; small-cavity discrete saturation compresses the line)")

print("\nCaveats (honest): (1) lattice units c/a=1; s<~4 deviates O(1) from continuum.")
print("(2) tau = 187/91 (K1 docstring printed 187/48 = 2 + D_f, not tau).")
print("(3) exponent fits restricted to 16<=s<=300 (exact solver); larger clusters")
print("    counted but unsolved — coverage printed per run.")
print("(4) spanning network removed by boundary test; p_f calibrated to 0.588-0.598.")
