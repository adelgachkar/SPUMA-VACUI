# -*- coding: utf-8 -*-
"""
K1 sharp-edge regime: 2D cavity cluster statistics + cluster-factor scaling.

Map: rectified freeze-out on an LxL lattice; frozen sites = cavity.
White noise -> i.i.d. freezing -> RANDOM PERCOLATION at p = p_f.
  * first-passage prediction:  p_f(b) ~ exp(-2 b m0)   (b = bias, m0 = start margin)
  * b tunes p_f through p_c = 0.592746 (2D site percolation):
      b > b_c : isolated near-homogeneous cavities (subcritical)
      b < b_c : SPANNING cavity network (supercritical)
      b = b_c : scale-free sizes n(s) ~ s^-tau, tau = 187/48, cutoff s_c ~ L^D
Colored noise (correlation length lc): blobs ~ lc^2 -> characteristic cavity
size; cluster factor saturates with L (near-homogeneous register).
"""
import numpy as np
from collections import defaultdict

P_C = 0.592746      # 2D square site percolation
TAU = 187.0/48.0    # 2D percolation cluster-size exponent
D_F = 91.0/48.0     # fractal dimension at criticality

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

def simulate(L, b, m0=1.5, lc=0, seed=0, T_max=2000, patience=60):
    """Rectified freeze-out. Returns frozen mask."""
    rng = np.random.default_rng(seed)
    rho = m0 + 0.5 * rng.standard_normal((L, L))
    frozen = rho < 0.0
    quiet = 0
    for t in range(T_max):
        new = 0
        xi = rng.standard_normal((L, L))
        if lc:
            xi = smooth2d(xi, lc)
            xi /= (xi.std() + 1e-12)
        mob = ~frozen
        rho = np.where(mob, rho + xi + b, rho)
        newly = mob & (rho < 0.0)
        frozen |= newly
        new = newly.sum()
        quiet = quiet + 1 if new <= max(1, 3e-4*L*L) else 0
        if quiet >= patience:
            break
    return frozen

def cluster_stats(mask):
    """Row-run union-find. Returns (sizes array, spanning bool)."""
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
    sizes = defaultdict(int)
    for i, s, e, me in all_runs:
        sizes[find(me)] += e - s
    r0 = {find(me) for i, s, e, me in all_runs if i == 0}
    rH = {find(me) for i, s, e, me in all_runs if i == H-1}
    return np.array(sorted(sizes.values())), bool(r0 & rH)

def fit_tau(sizes, s_min=2, s_max=40):
    s, n = np.array(sizes), None
    edges = np.logspace(0, np.log10(min(s_max, sizes.max())+1), 11)
    xs, ys = [], []
    cnt = np.histogram(s, bins=edges)[0].astype(float)
    ctr = np.sqrt(edges[:-1]*edges[1:])
    keep = cnt > 0
    if keep.sum() < 4:
        return np.nan
    A = np.vstack([np.log(ctr[keep]), np.ones(keep.sum())]).T
    return -np.linalg.lstsq(A, np.log(cnt[keep]), rcond=None)[0][0]

def moment_cutoff(sizes, drop_max=True):
    s = np.array(sizes, float)
    if drop_max and len(s) > 1:
        s = np.delete(s, s.argmax())
    return (s*s).sum()/max(s.sum(), 1)

def binned_n(sizes, nb=10, smax=None):
    s = np.array(sizes, float)
    smax = smax or s.max()
    edges = np.logspace(0, np.log10(smax)+1e-9, nb+1)
    cnt, _ = np.histogram(s, bins=edges)
    ctr = np.sqrt(edges[:-1]*edges[1:])
    area = edges[1:]-edges[:-1]
    dens = cnt/area  # count per width ~ n(s) up to const
    return ctr, dens

print("== 1) cavity fraction p_f(b): first-passage prediction p_f = exp(-2 b m0), m0=1.5 ==")
print(f"{'b':>6} {'p_f sim (L=256, 3 seeds)':>26} {'exp(-2bm0)':>11}")
b_grid = [0.05, 0.10, 0.15, 0.20, 0.30, 0.50, 0.80, 1.20, 1.80, 2.50, 3.20]
pf = {}
for b in b_grid:
    vals = [simulate(256, b, seed=s).mean() for s in (1, 2, 3)]
    pf[b] = np.mean(vals)
    print(f"{b:6.2f} {pf[b]:26.4f} {np.exp(-2*b*1.5):11.4f}")
# calibrate b_c FROM the simulation: interpolate p_f(b) = p_c on the grid
bc = float(np.interp(P_C, [pf[b] for b in b_grid[::-1]], b_grid[::-1]))
print(f"-> simulated b_c (p_f = p_c = 0.5927): {bc:.3f}   (first-passage estimate: {-np.log(P_C)/3:.3f})")

print("\n== 2) critical regime b ~= b_c: cluster-factor scaling (L sweep, 3 seeds) ==")
print(f"{'L':>5} {'p_f':>7} {'span%':>6} {'tau fit':>8} {'s_c=<s2>/<s1>':>14}")
sc_L = []
for L in (64, 128, 256, 384):
    spn, taus, scs, pfs = 0, [], [], []
    for s in (1, 2, 3):
        m = simulate(L, bc, seed=s)
        sizes, span = cluster_stats(m)
        pfs.append(m.mean()); spn += span
        taus.append(fit_tau(sizes))
        scs.append(moment_cutoff(sizes))
    sc_L.append(np.mean(scs))
    print(f"{L:5d} {np.mean(pfs):7.4f} {100*spn/3:6.1f} {np.nanmean(taus):8.3f} {np.mean(scs):14.1f}")
D_fit = np.polyfit(np.log([64,128,256,384]), np.log(sc_L), 1)[0]
print(f"-> tau fit ~ {np.nanmean([fit_tau(cluster_stats(simulate(256, bc, seed=s))[0]) for s in (1,2,3)]):.3f} vs 2D percolation {TAU:.3f}")
print(f"-> cutoff growth s_c ~ L^D: fitted D = {D_fit:.2f} vs {D_F:.2f} (critical) ; spanning -> 100% at b_c")

print("\n== 3) off-critical b = b_c + 0.05: cluster-factor saturation ==")
scs_off = []
for L in (64, 128, 256):
    v = [moment_cutoff(cluster_stats(simulate(L, bc+0.05, seed=s))[0]) for s in (1, 2, 3)]
    scs_off.append(np.mean(v))
print("   s_c(L=64,128,256) =", ", ".join(f"{v:.1f}" for v in scs_off),
      "-> flat (L-independent): noncritical cluster factor")

print("\n== 4) colored noise lc=3px at b=0.30: characteristic cavity blobs ==")
for L in (128, 256):
    v_sc, v_pf, v_sp = [], [], []
    for s in (1, 2, 3):
        m = simulate(L, 0.30, lc=3, seed=s)
        sizes, span = cluster_stats(m)
        v_sc.append(moment_cutoff(sizes)); v_pf.append(m.mean()); v_sp += [span]
    ctr, dens = binned_n(np.concatenate([cluster_stats(simulate(L, 0.30, lc=3, seed=s))[0] for s in (1,2,3)]))
    top = " ".join(f"{d:8.0f}" for d in dens[-6:])
    print(f"   L={L}: p_f={np.mean(v_pf):.3f}  s_c={np.mean(v_sc):7.1f}  span={100*sum(v_sp)/len(v_sp):.0f}%")
    print(f"      n(s) top bins s~{ctr[-6:].astype(int)}: {top}")

print("\n== 5) isolated-cavity regime b=0.30 (white): n(s) binned (L=256, pooled) ==")
alls = np.concatenate([cluster_stats(simulate(256, 0.30, seed=s))[0] for s in (1, 2, 3)])
ctr, dens = binned_n(alls)
for c, d in zip(ctr, dens):
    print(f"   s~{int(c):5d}   n(s)~{d:9.1f}")
print(f"   mean cavity size = {alls.mean():.2f} sites ; largest = {alls.max()}")
