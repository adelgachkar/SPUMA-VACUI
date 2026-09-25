---
title: "Sharpness-vs-Substrate Falsification Test"
aliases: ["Sharpness Falsification Test", "Capsule vs Substrate vs Gauge"]
created: 2026-09-20
updated: 2026-09-25
tags: [spuma-vacui, falsification, protocol, numerics]
status: "canonical"
license: "MIT"
lang: "en"
---

# Sharpness-vs-Substrate Falsification Test

> **Structural Causal Chain (SPUMA):**
> Curvature Gradient → Polarization P(R) → Back-Reaction dR/R → **Exponent Discrimination** → Verdict

## 1. Quantitative Model

**The polarization law** (independent measurement: the local-potential map):

$$P(R) = P_0\Big(\frac{a}{R}\Big)^{n_p},\qquad
n_p = 2\ \ \text{(the classical gradient limit: t/R}\to(a/R)^2\text{)}$$

**Three competing channels for the transport feedback** (the relative resistance change dR/R):

| Channel | sharpness exponent n_b (in a/R) | height exponent m_b (in H) | categorical basis |
|---|---|---|---|
| **Reactive capsule** (the SPUMA claim) | **n_b = n_p** (follows the polarization) | m_b ≈ 0 | sensitive to gate and decay |
| Quasi-mechanical gauge (伪 gauge) | n_b = 2 (hfc²~R⁻²) | m_b = 1/2 | insensitive |
| Substrate contact (MoS₂ strain) | n_b = 1 (ε² ~ H/R) | m_b = 1 | insensitive |

## 2. Overdetermined Verdict

Two continuous exponents + two categorical bases:

1. **Gate:** a conducting underlayer (graphene on metal) kills the capsule's gate field — if the signal vanishes, the channel is the capsule.
2. **Decay:** an intermediate hBN layer attenuates the capsule's field exponentially (decay length λ) — gauge/substrate are insensitive.

$$\text{REJECT capsule} \iff |n_b-n_p|>0.25\ \ \text{or}\ \ m_b>0.2\ \ \text{or insensitivity to gate/decay}$$

## 3. Synthetic Validation

`tools/sharpness_vs_substrate_test.py` (output: `tools/sharpness_test_output.txt`) — synthetic data with 4% noise, exponent recovery by log-log fitting:

| Injected channel | recovered n_b | recovered m_b | verdict matrix |
|---|---|---|---|
| capsule | 2.006 (target 2) | 0.008 (target 0) | ✅ capsule (4 votes) |
| gauge | 2.010 (target 2) | 0.505 (target 0.5) | ✅ gauge (3 votes) |
| substrate | 0.981 (target 1) | 0.997 (target 1) | ✅ substrate (3 votes) |

Polarization reference: n_p = 2.044 recovered (target 2.0); P(1nm) ≈ 6.6 mC/m² at the anchor scale — consistent with the orbital regime.

## 4. Experimental Recipe

1. Map the potential around folds of different sharpness (STM/KPFM) → n_p (reference).
2. Sweep R at fixed H and sweep H at fixed R on the transport dR/R → (n_b, m_b).
3. The two categorical keys: a conducting underlayer (gate) and an intermediate hBN (decay).
4. Verdict from the overdetermined matrix — no single exponent is sufficient (n_b=2 is shared between capsule and gauge; discrimination comes from m_b and the keys).

## 5. Status

**Specified protocol + full synthetic validation** — a real execution requires laboratory data (the potential and transport maps of the same graphene/MoS₂ fold samples). The falsifiability of the claim "reactive capsule = effective constraint" is now quantitative and thresholded: [[Reactive-Capsule-Graphene-Anchor]].
