---
title: "SPUMA-VACUI — Master Map"
aliases: ["SPUMA VACUI", "Spuma Vacui Master Map"]
created: 2026-09-20
updated: 2026-09-25
tags: [moc, spuma-vacui, index]
status: "canonical"
license: "MIT"
lang: "en"
---

# SPUMA-VACUI — Master Map

> **The most binding statement**: the cavity (structural void) is the result of noise freezing in a **narrow band** toward lower density — and every cavity is a **polar body whose field hugs its wall**.

## Purpose

SPUMA-VACUI (*spuma vacui* — the vacuum foam) is the structural companion of CADENCE-SDF / Emergence-SDF-Vault: the origin of near-homogeneous polarized cavities, from the opposition of **two binding constraints** on a foam-like substrate.

## The Two Binding Constraints

| Constraint | Statement | Manifestation |
|---|---|---|
| **K1 — Vacuum Discontinuity** | the noise is rectified at **mid-range** density; below the threshold ρ₀ it freezes (steps rejected), above ρ₀ it flows with a regional-expansion bias | edge freezing, regional inflation, edge sweeping |
| **K2 — Unbounded Polarization-Tension Discontinuity** | the cavity boundary is a **sharp polarity layer**; the field is trapped in the wall (the two-sheet wall) and builds the decay spectrum 1/r³→1/r⁴→1/r⁵ | wall = fixed polarization, an impermeable permeability barrier; the monopole forbidden |

## The Genesis Mechanism

Noise (the agent of regional inflation) → edge sweeping at the freezing edge → near-homogeneous cavities → path polarization (the weave-like tissue, picture broken-magnet-weave) → the wall envelope from the permeability envelope (the twin of the permanent-magnet crack; field trapped in the wall) → intrinsic harmonics from the **interior-field/edge-sweep antagonism**.

## Folder Map

- `01_Axioms/` — the axioms: A1 the vacuum foam (one degree of freedom at mid-range density, vacuum ≈ constant), A2 the two binding constraints, A3 edge polarization, A4 harmonics from antagonism.
- `02_Constraints/` — the quantitative formulations of K1 and K2 + the cavity-size distribution (three regimes, cluster-factor scaling) + the monopole prohibition.
- `03_Cavity_Harmonics/` — the intrinsic cavity harmonics, the map to the CADENCE spectrum, the Kepler densification ceiling, the **spectral prediction of the three regimes** (band/line vs power-law tail; the spectral-dimension discriminator d_s).
- `04_Companion_Mapping/` — the bridge to the companion + the reactive-capsule experimental anchor + the sharpness/substrate falsification test (a quantitative protocol) + the **quantitative bridge to LIMEN-VACUI** (the map LIMEN(g_max, τ_q, κ) ↔ SPUMA(b); R∈[0.90,0.98] under weak coupling).
- `00_MOC/` — this map.
- `tools/spuma_constraints.py` — the executable numerical core (deposited output: `tools/spuma_output.txt`).
- `tools/cavity_cluster_scaling.py` — the size-distribution simulator (output: `tools/cavity_scaling_output.txt`).
- `tools/spectral_regime_prediction.py` — the exact solve of ω₁ per cluster and the spectral signatures (output: `tools/spectral_prediction_output.txt`).
- `tools/spuma_residue_regime_bridge.py` — the K1 critical-edge × LIMEN residue-edge bridge: the dimensionless ratio, the gauge identity, the encounter point (output: `tools/spuma_residue_regime_bridge_output.txt`).

## Canonical Numbers

| Quantity | Value | Source |
|---|---|---|
| Pentagonal deficit | 7.356103° | 2π − 5·arccos(1/3) |
| Weave register mismatch | 12.3% pitch | K4 (permanent frost-polar) |
| Densification ceiling (Kepler) | φ = 0.7405 | K3 |
| Freezing quantum edge | h·fc ≈ 0.12 eV | fc = κ_hop/π ≈ 30 THz (companion, g=0.8) |
| Single-dipole polarity vanishing | < 10⁻⁶ | K1 |
| Non-power-law white/colored tails | R²≈0 in the s≤300 window | Spectral-Regime-Prediction |
| Precise τ (MLE) | 2.031 (2.022±0.019 at L=512; 2.034±0.008 at L=1024) | K1-Cavity-Size-Distribution §6 — confirms 187/91, rejects 187/48 |
| LIMEN↔SPUMA bridge | R ∈ [0.90, 0.98] at κ≤0.10; (g=0.297, τ_q=40, κ=0.03) ↔ b=0.285 at the shared p_f 0.299 | Companion-Bridge §5 (tool in LIMEN: `limen_spuma_bridge.py`) |
| K1 critical notch × residue edge | R_edge = b_c/d_class = 1.841 ± 0.002 (E4-corrected from 15.75; b_c = 0.1263 ± 0.0002 stable across L=256/512/1024) — a universal decade, not a threshold; encounter (0.0574, 0.0686) at b_eff = b_c with p_f = 0.5936; no-go: d_crit 0.002 < d_det 0.0067 < d_class 0.0686 — and the W3 update: the exemption is budget-limited (X* ≈ 10–12× canonical; LIMEN `limen_d_crit_price`) | Companion-Bridge §5 (`spuma_residue_regime_bridge`); Protocol §5 in LIMEN |

## Epistemic Status

The K1–K4 models are **executable, numerically verified protocols** (the sharp K1 cut edge, the vanishing K1/K2 monopole, the K3 field trapping); the cosmological interpretation is a research statement, not an empirical finding.
