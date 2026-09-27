---
title: "A4 — Harmonics from Interior-Field/Edge-Sweep Antagonism"
aliases: ["A4 Intrinsic Harmonics", "Antagonism Harmonics"]
created: 2026-09-20
updated: 2026-09-25
tags: [spuma-vacui, axiom, harmonics]
status: "canonical"
license: "MIT"
lang: "en"
---

# A4 — Harmonics from Interior-Field/Edge-Sweep Antagonism

> **Structural Causal Chain (SPUMA):**
> Vacuum Foam → Near-Homogeneous Polarized Cavities → **Interior Field ⨯ Edge Sweep (antagonism)** → Intrinsic Harmonics → Companion Spectral Support

## 1. The Antagonism

Two opposing forces in every cavity:
- **Interior field**: from the wall polarization layer ([[A3-Edge-Polarization-Wall-Envelope]]) — an outward, cavity-erasing pressure.
- **Edge sweeping**: from the rectification of the noise ([[A2-Two-Binding-Constraints]], K1) — an outward structural pressure that stabilizes the cavity.

The equilibrium of the two builds the harmonic ground state of oscillation:

$$\omega_n^2 \;\sim\; \underbrace{\omega_{\text{field}}^2}_{\propto\, P_0^2/\mu_{\text{wall}}}\;+\;\underbrace{\omega_{\text{edge}}^2}_{\propto\, b/\tau_{\text{rect}}}\;+\;2\,\Gamma_{n}\,\omega_{\text{field}}\,\omega_{\text{edge}}$$

The effective oscillator mass = the energy trapped in the wall ([[K2-Polarization-Discontinuity]]); stability = the debt/release timescale separation (the slow oscillator of the companion model).

## 2. Spectrum

For an approximately spherical cavity with wall polarization, the rectified harmonic modes are:

$$f_n \;\approx\; \frac{c_{\text{wall}}}{2\pi R}\,n\,\Big(1 + \epsilon_n\,\frac{\delta\theta}{2\pi}\Big),\qquad
\epsilon_n = \begin{cases}1 & n\ \text{even (antagonism preserved)}\\ 0 & n\ \text{odd (reset)}\end{cases}$$

The pentagonal angle deficit δθ/2π = 0.02044 as the even/odd discrimination factor — a direct link to the CADENCE spectrum ([[Companion-Bridge]]).

> **W4 verdict (2026-09-27, registered in LIMEN `08_Protocol/Two-Realm-Register`):** the §2 parity prediction (ε_even = 1, ε_odd = 0, constant in n) was put to the banked "wall model with explicit μ(x)" test (LIMEN `tools/limen_w4_mu_wall.py` — variational two-phase μ(x) Helmholtz, five-fold wall modulation w(φ)=w₀(1+η·cos5φ), η = δθ/2π) and is **refuted in-model**: no even/odd alternation (even mean +0.220 vs odd +0.262; discrimination −0.042 ± 0.08 vs the predicted +1.0), the split is n-dependent, and the discrimination has no finite-size fixed point. **E4-corrected reading:** a magnitude-only five-fold wall couples all radial modes — parity must live in a direction-structured (five-phase chiral) register; δθ/2π is remeasured as the even/odd-FLATNESS amplitude of the magnitude channel (~0.02, the right order). Prediction 1 of §3 is thereby sharpened, not abandoned: the flattened ratio δθ/2π is the magnitude-channel signature; the parity split is a direction-register signature (flagged W4b). Nature-side status: F3.

## 3. Falsifiable Predictions

1. Same-family cavities must show an **even/odd-flattened** spectrum with the constant ratio δθ/2π.
2. Removing the edge sweep (neutralizing K1) must collapse the even modes, not the odd ones.
3. Fusing two opposite-polarity cavities must build the mid-harmonic (flux preserved), with no monopole radiation.
