---
title: "K1 — Cavity Size Distribution (Sharp-Edge Regime)"
aliases: ["K1 Size Distribution", "Cavity Cluster Scaling"]
created: 2026-09-20
updated: 2026-09-25
tags: [spuma-vacui, constraint, numerics, scaling]
status: "canonical"
license: "MIT"
lang: "en"
---

# K1 — Cavity Size Distribution (Sharp-Edge Regime)

> **Structural Causal Chain (SPUMA):**
> Rectified Noise (K1) → Frozen Map → **Cluster Statistics** → Three Regimes → Homogeneity Criterion

## 1. Setup

`tools/cavity_cluster_scaling.py`: an L×L lattice, K1 relaxation with rectified noise sweeping ([[K1-Vacuum-Discontinuity]]); row-streaming union-find clustering; sweeps at L ∈ {64…384}, three-to-five seeds per point. Mapping: frozen site = cavity.

## 2. Phase Diagram of Regimes

| Regime | Parameter | Numerical result | Verdict |
|---|---|---|---|
| **Isolated cavities** (homogeneous) | b > b_c | mean size 2.34 cells; largest 36 at L=256; steeply falling n(s) | thin, near-homogeneous cavities — SPUMA's desired regime |
| **Critical** | b ≈ b_c = 0.126 | **s_c ~ L^1.78** (exponent 1.78 vs 1.90 for percolation criticality); scale-free truncation | scale-free distribution — a continuous cavity network |
| **Supercritical/network** | b < b_c | truncation at all L | fused cavities |
| **Colored noise** (lc=3px) | any b | **s_c ≈ 30–32, independent of L**; characteristic-size patches | cavity size registered from the noise correlation length |

## 3. First-Passage Confirmation

Analytic prediction p_f(b) = exp(−2b·m₀) (the final frozen fraction as a Markov first-passage):

$$\kappa_{\text{fit}} = 3.17 \pm 0.1 \quad\text{vs}\quad 2m_0 = 3.0 \quad \text{(5.7% error — finite-fluctuation correction)}$$

The exponential form confirmed; simulated b_c = 0.126 (first-passage estimate 0.174 — the deviation comes from field stochasticity, not from the form).

## 4. Cluster-Factor Scaling

- **Critical:** s_c = ⟨s²⟩/⟨s⟩ from 165 (L=64) to 3992 (L=384) — a power-law fit gives D = **1.78** against the theoretical 1.90; the scale-invariance signature at the transition point.
- **Supercritical (b_c+0.10):** s_c = 9.6 → 11.2 → 11.7 → 11.7 — **full saturation from L≈128**; a non-critical cluster factor, scale-independent (homogeneity registered).
- **Colored noise:** s_c independent of L at both L=128 and 256 — a characteristic size, not a power-law distribution.

## 5. Homogeneity Criterion

For "near-homogeneous" cavities (the A1 claim) two routes are admissible:

1. **Isolated regime** (b > b_c, white noise): steep distribution, mean of a few cells — statistical homogeneity.
2. **Correlated noise** (lc > 0): a characteristic-size distribution with s_c ~ lc² — structural homogeneity.

Forbidden route: proximity to b_c (scale-free distribution → a continuous network, not distinct cavities). This is itself a testable prediction for the companion model: the spectrum must switch between single-scale and power-law depending on the regime ([[Intrinsic-Harmonics]]).

## 6. Precise tau (2026-09-21 — open work resolved)

The quick first-pass fit (unnormalized log bins, 2.2) has been replaced by a rigorous fit — `tools/tau_precise_fit.py` (density-normalized bins + continuous MLE + jackknife + likelihood-ratio test, L=512 and 1024):

| L | Clusters | τ̂ (MLE ± jackknife) | Distance from 187/91 | Distance from 187/48 |
|---|---|---|---|---|
| 512 | 29,109 | **2.022 ± 0.019** | 1.6% | 48.1% |
| 1024 | 85,634 | **2.034 ± 0.008** | 1.0% | 47.8% |
| Pooled | 114,743 | **2.031** | 1.2% | 47.9% |

**Theoretical-constant correction:** the exponent of the 2D percolation cluster-size distribution is **τ = 187/91 = 2.0549** (Fisher: 2 + β/(β+γ) with β=5/36, γ=43/18; and the identity τ = 1 + d/D_f) — the value `187/48 = 3.896` previously printed in the tool's docstring is in fact **2 + D_f** (a numerical twin, not τ). The data reject 187/48 with thousands of nats of likelihood and confirm 187/91 at ΔLL ≈ +2 (effectively equivalent to the free optimum).

s_min sensitivity (the estimate drifts toward 187/91): s_min=8→2.03, 16→2.02, 32→2.00, 64→1.97 — a systematic improvement moving away from the size-limited transition. The first-run valid exponent (D = 1.78) stands. The giant component is culled with a 1% top guard (one cluster; the exponent lives in the tail).
