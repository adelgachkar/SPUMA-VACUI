---
title: "Intrinsic Cavity Harmonics"
aliases: ["Intrinsic Harmonics", "Cavity Antagonism Spectrum"]
created: 2026-09-20
updated: 2026-09-25
tags: [spuma-vacui, harmonics, numerics]
status: "canonical"
license: "MIT"
lang: "en"
---

# Intrinsic Cavity Harmonics

> **Structural Causal Chain (SPUMA):**
> Near-Homogeneous Polarized Cavities → Interior Field ⨯ Edge Sweep → Intrinsic Harmonics → Companion Spectral Support

## 1. Source of the Harmonics

Every cavity is an oscillator fed by the **antagonism** of two agents (axiom [[A4-Intrinsic-Harmonics-Antagonism]]):

$$\ddot{q}_n + \omega_n^2 q_n = 0,\qquad
\omega_n^2 = \omega_{\text{field}}^2 + \omega_{\text{edge}}^2 + 2\Gamma_n\,\omega_{\text{field}}\,\omega_{\text{edge}}$$

- ω_field² ∝ P₀²/μ_wall: the energy trapped in the polarized wall ([[K2-Polarization-Discontinuity]])
- ω_edge² ∝ b/τ_rect: the rectified edge stabilization ([[K1-Vacuum-Discontinuity]])
- The antagonistic term 2Γ_n ω_f ω_e: even/odd mode discrimination — even modes preserve the antagonism, odd modes reset it.

## 2. Quantized Ceiling

Cavity densification is bounded by the Kepler ceiling (companion test K3):

$$\phi_{\max} = \frac{\pi}{\sqrt{18}} = 0.7405$$

No cavities denser than the pentagonal state exist in the fractional spectrum (the angular deficit is a footnote) — the saturation ceiling is a packing constraint, not a dynamical tuning.

## 3. Spectral Support for the Companion

The intrinsic harmonics provide the **spectral support** of the companion lattice (`04_Companion_Mapping/Companion-Bridge`):

| Quantity | Value | Role in the companion |
|---|---|---|
| δθ (pentagonal deficit) | 7.356103° = 0.02044×2π | harmonic even/odd discrimination factor |
| f_c = κ_hop/π | ≈ 30 THz (g=0.8, λ₀=320nm) | the companion's narrow gravitational window |
| h·f_c | ≈ 0.12 eV | the K1 freezing quantum edge |
| Weave register mismatch | 12.3% pitch | permanent polar wallpaper (K4) |

## 4. Testable Signatures

1. A constant even/odd spectral ratio δθ/2π across the cavity family.
2. Selective collapse of even modes upon removal of the edge sweep.
3. Trapped-flux neutralization only via opposite-polarity fusion — never monopole radiation.
