# -*- coding: utf-8 -*-
"""Paper figures for the SPUMA-VACUI manuscript (IJTP submission).

Three data figures generated with the canonical tools of the repository
(no new physics — same simulate/clusters/spectral operators as the
registered protocols):

  Fig 1 — cavity snapshots in the three structural regimes (L=512),
  Fig 2 — cluster-size distribution at b_c with power-law fit,
  Fig 3 — fundamental-frequency spectra across the three regimes (log-log).

Parameters follow the registered calibrations quoted in the manuscript:
b_c = 0.1263 (L=256 calibration), critical point at L=512 (2 seeds),
isolated regime b = 0.30 (white), network regime b = 0.05 (white).
Outputs -> paper/figures/*.png (+ .pdf vector), 300 dpi.
"""
import sys, os
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# --- import the canonical operators (registered protocols) ---
from cavity_cluster_scaling import simulate as sim_scaling, cluster_stats, fit_tau
from spectral_regime_prediction import (clusters as spec_clusters,
                                        fundamental_omega,
                                        logbin_spec)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                   "..", "paper", "figures")
os.makedirs(OUT, exist_ok=True)

plt.rcParams.update({
    "font.family": "serif", "font.size": 9.5,
    "axes.linewidth": 0.8, "figure.dpi": 300,
    "savefig.bbox": "tight",
})

# ----------------------------------------------------------------------
# shared: run the registered K1 freeze-out (same simulator both tools use)
# ----------------------------------------------------------------------

def run(L, b, seed, lc=0):
    return sim_scaling(L, b, m0=1.5, lc=lc, seed=seed,
                       T_max=2000, patience=60)

# ======================================================================
# FIG 1 — snapshots of the three structural regimes (L=512)
# ======================================================================

def fig1():
    L = 512
    cfg = [("isolated  (b = 0.30)", 0.30),
           ("critical  (b = b_c = 0.126)", 0.126),
           ("network   (b = 0.05)", 0.05)]
    fig, axes = plt.subplots(1, 3, figsize=(10.5, 3.7))
    for ax, (title, b) in zip(axes, cfg):
        m = run(L, b, seed=1)
        ax.imshow(m[::-1], origin="lower", cmap="gray_r", interpolation="nearest")
        ax.set_title(title, fontsize=10)
        ax.set_xticks([]); ax.set_yticks([])
        ax.text(0.02, 0.02, f"$p_f$ = {m.mean():.3f}",
                transform=ax.transAxes, fontsize=9,
                color="0.15", va="bottom")
    fig.suptitle("Frozen-region snapshots, L = 512 (K1 freeze-out, seed 1)",
                 y=1.02, fontsize=11)
    fig.savefig(os.path.join(OUT, "fig1_regimes.png"))
    fig.savefig(os.path.join(OUT, "fig1_regimes.pdf"))
    plt.close(fig)
    print("fig1 done")

# ======================================================================
# FIG 2 — cluster-size distribution at b_c (pooled, power-law fit)
# ======================================================================

def fig2():
    L, b, seeds = 256, 0.126, (1, 2, 3, 4, 5, 6)
    all_sizes = []
    pfs = []
    for sd in seeds:
        m = run(L, b, seed=sd)
        pfs.append(m.mean())
        sizes, spanning = cluster_stats(m)
        all_sizes.extend(sizes.tolist())
    s = np.array(all_sizes, float)
    tau = fit_tau(s, s_min=2, s_max=40)
    print(f"fig2: pooled N={len(s)}, p_f={np.mean(pfs):.4f}, tau={tau:.3f}")

    fig, ax = plt.subplots(figsize=(4.8, 3.9))
    # binned density
    edges = np.logspace(0, np.log10(s.max() + 1), 16)
    cnt, _ = np.histogram(s, bins=edges)
    ctr = np.sqrt(edges[:-1] * edges[1:])
    width = edges[1:] - edges[:-1]
    dens = cnt / width / len(seeds)
    keep = dens > 0
    ax.loglog(ctr[keep], dens[keep], "o", ms=4.5, mfc="0.25", mec="0.25",
              label="binned $n(s)$ (6 seeds, L=256, pooled)")
    # power-law guide with fitted tau over the fit window
    sw = np.logspace(np.log10(2), np.log10(40), 32)
    c0 = dens[keep][0] * 1.1
    ax.loglog(sw, c0 * (sw / sw[0]) ** (-tau), "-", lw=1.6, color="0.55",
              label=rf"power law, $\tau$ = {tau:.2f} (fit $s\in[2,40]$)")
    ax.axvline(300, color="0.7", ls=":", lw=1.0)
    ax.text(310, dens[keep].max() * 0.4, "spectral window $s\\leq 300$",
            rotation=90, fontsize=8, color="0.45", va="bottom")
    ax.set_xlabel("cluster size $s$ (sites)")
    ax.set_ylabel("number density per seed, per unit $s$")
    ax.set_title("Cluster-size distribution at $b \\approx b_c$ = 0.126 (L=256)",
                 fontsize=10)
    ax.legend(frameon=False, fontsize=8.5, loc="best")
    fig.savefig(os.path.join(OUT, "fig2_cluster_distribution.png"))
    fig.savefig(os.path.join(OUT, "fig2_cluster_distribution.pdf"))
    plt.close(fig)
    print("fig2 done")

# ======================================================================
# FIG 3 — fundamental-frequency spectra in the three regimes (log-log)
# ======================================================================

def fig3():
    cfg = [
        ("isolated white noise (b = 0.30)", dict(b=0.30, lc=0, L=256,
                                                 seeds=(1, 2, 3, 4))),
        ("critical (b = 0.126, L=512)",     dict(b=0.126, lc=0, L=512,
                                                 seeds=(1, 2))),
        ("correlated noise (lc = 3 px, b = 0.30)", dict(b=0.30, lc=3, L=256,
                                                        seeds=(1, 2, 3, 4))),
    ]
    fig, ax = plt.subplots(figsize=(5.2, 3.9))
    style = [("o", "0.15"), ("s", "0.45"), ("^", "0.75")]
    for (label, c), (mk, mc) in zip(cfg, style):
        oms, szs, cov = [], [], dict(n_all=0, n_solved=0)
        n_all = n_solved = 0
        for sd in c["seeds"]:
            mm = run(c["L"], c["b"], seed=sd, lc=c["lc"])
            sizes, cd = spec_clusters(mm)
            for r, arr in cd.items():
                w1 = fundamental_omega(arr)
                if np.isnan(w1):
                    continue
                oms.append(w1); szs.append(sizes[r]); n_all += 1
        om = np.array(oms); wt = np.array(szs, float)
        n_solved = len(om)
        ctr, dens, keep = logbin_spec(om, wt, nb=18)
        dens_norm = dens / max(dens[keep].max(), 1)
        ax.loglog(ctr[keep], dens_norm[keep], marker=mk, ms=4.5, ls="-",
                  lw=0.9, color=mc, mfc=mc, mec="white", mew=0.5,
                  label=f"{label}  [$n_{{solved}}$={n_solved}]")
        print(f"fig3 [{label}]: solved={n_solved}/{n_all}, "
              f"omega range {om.min():.3f}-{om.max():.3f}")
    ax.set_xlabel(r"fundamental frequency $\omega_1=\sqrt{\lambda_1}$ "
                  "(lattice units)")
    ax.set_ylabel("weighted spectral density (normalized)")
    ax.set_title("Dirichlet cavity spectra across the three regimes",
                 fontsize=10)
    ax.legend(frameon=False, fontsize=8.5, loc="best")
    fig.savefig(os.path.join(OUT, "fig3_spectra.png"))
    fig.savefig(os.path.join(OUT, "fig3_spectra.pdf"))
    plt.close(fig)
    print("fig3 done")

if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("ALL FIGURES DONE ->", os.path.abspath(OUT))
