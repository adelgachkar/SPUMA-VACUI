---
title: "Reactive Capsule Constraint — Graphene Orbital Flexoelectricity Anchor"
aliases: ["Reactive Capsule", "Graphene Wrinkle Anchor"]
created: 2026-09-20
updated: 2026-09-25
tags: [spuma-vacui, anchor, experiment, flexoelectricity]
status: "canonical"
license: "MIT"
lang: "en"
---

# Reactive Capsule Constraint — Graphene Orbital Flexoelectricity Anchor

> **Structural Causal Chain (SPUMA):**
> Curvature Gradient (geometry) → Orbital Polarization → **Reactive Storage (no delivery)** → Back-Reaction = Effective Cavity Constraint

## 1. Claim Under Test

"Inside a capsule, reactive energy is conserved; an effective cavity constraint is established" — i.e., the wall polarization stores energy (non-dissipative, immobile) and this reactive storage plays the role of the **cavity-restraining constraint**.

## 2. Experimental Anchor (Advanced Materials, 2026)

Report of the experiment folding monolayer graphene down to the atomic limit (ZME Science republication, September 2026; the original paper in Advanced Materials):

| Experimental finding | SPUMA correspondence | Status |
|---|---|---|
| Polarization from **pure shape** (no free charge) — quantum orbital flexoelectricity | [[A3-Edge-Polarization-Wall-Envelope]]: birth geometry → polarity | exact |
| Quote: "the two ends of a microscopic battery — **storing and delivering no energy**" | reactive storage (R_loss→0 in the companion model; K2: the field trapped in the wall) | exact — the very claim |
| "The sharpness of the fold matters more than its height" | K1/K2: the constraint lives in the **discontinuity**, not in the volume | exact |
| 10⁵–10⁷× enhancement | strain gradient 1/R: a 1nm tip → 10⁹ m⁻¹ against bulk 10⁶ (×10³ geometric) + the orbital mechanism | quantitatively consistent |
| Folds change electrical resistance (2012) | **constraint feedback**: polarization acts back on transport = an effective constraint | exact |

## 3. Scaling Verification

Consistent with `tools/spuma_constraints.py`, the pressure-balance calculation:

$$p_{\text{elec}} = \frac{P^2}{2\varepsilon}\quad\text{vs}\quad p_{\text{cav}} \sim \frac{2\gamma}{R}$$

- P = 0.1 C/m² (orbital scale) → equilibrium at R ≈ 0.35 nm — sub-nanometer
- P = 0.01 C/m² → equilibrium at R ≈ 35 nm — nanometer scale

That is, nanometer capsules sit exactly in the regime where the orbital-polarization reactive pressure can be **comparable to** the confining pressure — the claim is scale-closed, although the direct measurement of the stored energy was not performed in the experiment.

## 4. Honest Gap

- The experiment shows polarization **produced by bending**; that this very reactive storage *itself* is the restrainer (self-fossorial) is a SPUMA-model extrapolation — in the experiment an external geometric constraint (the MoS₂ substrate) is also present.
- "Conserved" at the model level: the storage is time-invariant and recoverable; the energy accounting was not measured in the experiment.

## 5. Falsifiable Prediction

Tuning **sharpness** (not size) must tune the effective constraint: if removing the edge sharpness shifts the feedback effect (the transport/stability change of the fold) with the same dominant exponent as the polarization, then effective constraint = reactive storage is confirmed; if not, the constraint comes from elsewhere (substrate/van der Waals). The 2026 experiment has put the discriminating instrument on the table.
