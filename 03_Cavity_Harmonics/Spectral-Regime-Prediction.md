---
title: "Spectral Regime Prediction"
aliases: ["Spectral Prediction", "Cavity Size-Distribution Spectrum"]
created: 2026-09-21
updated: 2026-09-25
tags: [spuma-vacui, harmonics, numerics, falsifiable]
status: "canonical"
license: "MIT"
lang: "en"
---

# Spectral Regime Prediction

> **Central question:** what imprint does each of the three cavity-size regimes ([[K1-Cavity-Size-Distribution]]) leave on the **intrinsic harmonic spectrum** ([[Intrinsic-Harmonics]])? This note is built by **exactly solving the cavity operator on every simulated cluster** — not by a continuum ansatz — and delivers three falsifiable signatures.

## 1. Method — the exact operator, not an assumption

Every cavity is a confined harmonic domain (the polar K2 wall = a Dirichlet boundary). The fundamental frequency comes from the on-lattice operator:

$$\omega_1 = \sqrt{\lambda_1}\,,\qquad (L\psi)_i = 4\psi_i - \sum_{j\in\text{cavity},\,j\sim i}\psi_j$$

- Full lattice degree (4): a missing neighbor contributes ψ=0 = the polarized wall (K2). [exact]
- **Exact** solve (dense eigvalsh) for every cluster with s ≤ 300 — validation: the n×n square reproduces √(4−4cos(π/(n+1))) to 10⁻¹⁶ [test:passed]
- Larger clusters are counted but not solved (the honest coverage is printed).
- A percolating cluster (the cavity network) is removed by a **real boundary test**, not a size threshold.
- At critical L, each run's p_f is printed (0.5933 against the target 0.5927).

**Tool:** `tools/spectral_regime_prediction.py` — deposited output: `tools/spectral_prediction_output.txt`

## 2. Results — three regimes, three spectral shapes

| Regime | Spectral shape | Key number | A1 verdict |
|---|---|---|---|
| **Isolated white** (b=0.30) | a **band** with sharp edges | support 0.16 decades, Q=6.1; **non-power-law** (R²=0.007) | ≈ homogeneous (admissible) |
| **Critical** (b=0.126, L=512, p_f=0.593) | **power-law tail** (the theoretical shape); still transitional in the s≤300 window | α₁=+2.63 (R²=0.19) — a narrow window | forbidden (network) |
| **Colored noise** (lc=3) | a **line** (quasi-single-frequency) | Q=3.3, support 0.34 decades; non-power-law (R²=0.06) | homogeneous (strongest) |

Methodological finding: in the solved window (s≤300), the white/colored tail fits came out **explicitly non-power-law** — i.e., the band/line vs power-law discrimination was confirmed from the data itself; only the *within*-power-law discrimination (compact vs branching) needs a larger-s window.

## 3. The Spectral-Dimension Discriminator — d_s

For large clusters, ω₁ ~ s^(−γ_s) with γ_s = 1/d_s (spectral dimension; d_w = 2d_f/d_s):

| Geometric hypothesis | γ_s | d_s | predicted α₁ = d_s(τ−1)−1 |
|---|---|---|---|
| Compact (regular domain) | ≈0.50 | 2 | **1.11** |
| Branching (2D percolation/AO) | ≈0.72–0.75 | 4/3 | **+0.41** |

Two derivational points clarified/corrected in this note:
1. **Constant correction:** the exponent of the 2D percolation cluster-size distribution is **τ = 187/91 = 2.0549** (Fisher: 2 + β/(β+γ), β=5/36, γ=43/18; and the identity τ = 1 + d/D_f). The value `187/48` printed in the K1 study's docstring is in fact **2 + D_f** — a numerical twin, not τ. (The measured D=1.78 against D_f=91/48=1.896 stands.)
2. **α₂ stability:** the area-weighted slope α₂ = (τ−2)d_s − 1 ≈ −0.9 is **identical under both hypotheses** — the compact/branching discrimination is only possible with α₁ (count-weighted).

**Current measurement** (window 16≤s≤300, n=843): γ_s = 0.116 → d_s = 8.6 — outside both reference bands; interpretation: a size-limited transition (300-site clusters do not yet represent the large-scale regime) + the discrete saturation ω₁→2 for tiny clusters breaking the slope. Epistemic verdict: **determining d_s requires the s≫300 tail** — registered as open work.

## 4. Testable Signatures

For the companion model (spectroscopy of cavity resonances on the pentagonal lattice):

1. **Single-scale vs power-law:** if the cavity register sits in the isolated/colored regime → a **band/line** spectrum with α₁ "undefined" (R²≈0 under a power-law fit — exactly this simulation). If near-critical → a **power-law tail** with a shallow slope (\|α₁\|<2). Discrimination with a single log-log plot. [falsifiable criterion]
2. **α₂ stable:** area weighting (the radiative power) must give ≈ −0.9 in both worlds — a method-consistency test.
3. **Line width = size dispersion:** the compact rule std(ln ω) = ½ std(ln s); a positive deviation = wall crumpling/branching. [quantitatively consistent]

## 5. Epistemic Status

- **Exact:** the operator and solve (10⁻¹⁶ validation); the non-power-law character of white/colored tails in the s≤300 window (R²≈0).
- **Model:** the mapping ω₁ = √λ₁ on-lattice → intrinsic harmonics (the assumption ω² = ω_field² + ω_edge² + … of Intrinsic-Harmonics; the operator here only measures the geometric dimension).
- **Open:** determining d_s (the s≤300 window is insufficient); a smoothed iterative solver for s~10³–10⁴.

## Related

- [[K1-Cavity-Size-Distribution]] — the three distribution regimes (this note's data source)
- [[Intrinsic-Harmonics]] — the intrinsic harmonic spectrum (the prediction target)
- [[K2-Polarization-Discontinuity]] — the polar wall = the Dirichlet boundary
- [[K1-Vacuum-Discontinuity]] — the sharp-edge constraint
- [[MOC-SPUMA-VACUI]] — the Vault map
