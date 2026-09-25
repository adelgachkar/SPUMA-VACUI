---
title: "A3 — Edge Polarization and Wall Envelope"
aliases: ["A3 Wall Envelope", "Permanent-Magnet Crack Analogy"]
created: 2026-09-20
updated: 2026-09-25
tags: [spuma-vacui, axiom, polarization]
status: "canonical"
license: "MIT"
lang: "en"
---

# A3 — Edge Polarization and Wall Envelope

> **Structural Causal Chain (SPUMA):**
> Vacuum Foam → Edge Sweeping (K1) → Path Polarization → Wall Envelope (K2) → Intrinsic Harmonics

## 1. Path Polarization

The permeability envelope of the substrate is **weave-like** (picture `attachments/broken-magnet-weave.png`): paths carry direction, and edge sweeping (K1) locks this directionality onto every path:

$$\mathbf{p}_{\text{path}} \parallel \hat{n}_{\text{edge}},\qquad
\text{sign}(\mathbf{p}) = \text{sign}\big(\nabla\rho\cdot\hat{n}\big)$$

Consequence: every cavity born from edge sweeping is **polarized** — path-steering polarity and wall polarity together.

## 2. Wall Envelope from Permeability Envelope

The cavity wall is where the permeability envelope becomes discontinuous; there the polarization sharpens and the field gets trapped in the wall — the structural twin of the **crack in a permanent magnet** (second picture: a polarized bubble with field lines hugging the edge):

$$\mu(\mathbf{x}) = \mu_{\text{in}}\,\Theta_{\text{cavity}} + \mu_{\text{wall}}\,(1-\Theta_{\text{cavity}}),\qquad
\mathbf{B}_{\text{leak}} \approx 0\ \ \text{(outside the wall)}$$

## 3. Broken-Magnet Reading

"A broken magnet is not merely two pieces of metal" — breaking creates **two new polarized walls**. In SPUMA: the boundary of each cavity is a polarization surface with path correlations; fusing two cavities = neutralizing two opposed polarization layers (+/− joining). This reading is testable: fusing two cavities must **remove the trapped flux** rather than free a monopole ([[K2-Polarization-Discontinuity]], test K3).

## 4. Consequence

Every cavity is a **permanent polar wallpaper**: its polarity comes from the geometry of birth (edge sweeping) and is locked by edge freezing — subsequent noise cannot rotate it; it can only create new cavities.
