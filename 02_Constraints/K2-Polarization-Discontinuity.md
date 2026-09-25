---
title: "K2 — Polarization-Tension Discontinuity Constraint"
aliases: ["K2 Polarization Wall", "Unbounded Polarization Tension"]
created: 2026-09-20
updated: 2026-09-25
tags: [spuma-vacui, constraint, numerics]
status: "canonical"
license: "MIT"
lang: "en"
---

# K2 — Polarization-Tension Discontinuity Constraint

> **Structural Causal Chain (SPUMA):**
> Near-Homogeneous Cavities → **Polarization Sheet** → Trapped-Field Wall → 1/r^3 → 1/r^4 → 1/r^5

## 1. Constraint Statement

At the cavity boundary the polarization becomes **sharp** (discontinuous) and its tension is not bounded from above — "unbounded polarization tension" means the polarization layer can balance any redistributive pressure without softening:

$$\mathbf{P}(x) = P_0\,\Theta_{\text{wall}}(\mathbf{x}),\qquad
\nabla\cdot\mathbf{P} = -P_0\,\delta_{\text{wall}} \quad \text{(polarization charges only on the wall)}$$

## 2. Trapped-Field Wall

Two opposed polarization sheets of thickness w — the exact 1D solution (test K3 in `tools/spuma_constraints.py`):

$$\mathbf{E} = \begin{cases}0 & z<0\\ \hat{z}\,\sigma/\varepsilon_0 & 0<z<w\\ 0 & z>w\end{cases}$$

**The field lives only inside the wall; outside it is exactly zero** — "edge-hugging". Consequence: no monopole flux leaks outward; the cavity wall is a permanent-magnet crack, not a lone pole.

## 3. Decay Ladder

| Configuration | Polar moment | Field decay | Numerical test |
|---|---|---|---|
| Single polarized dipole | dipole | 1/r³ | B_single at L=40d |
| Opposite-polarity pair | unity (m=0) | **1/r⁴** | \|pair/single\| = 3d/L exact (0.075 at L=40d) |
| Quadrupole | — | **1/r⁵** | near/far dominance error confirmed |
| Monopole | — | **forbidden** | ≡ 0 at all L (flag < 10⁻⁶) |

## 4. Broken Magnet

`attachments/broken-magnet-weave.png`: the weave of paths before and after the break — breaking a magnet gives **two complete dipoles** (each chunk builds its own polarized wall). In SPUMA: adjacent cavities with opposite-polarity walls form 1/r⁴ pairs; neutralization is possible only by **fusion** (removing both layers) — never by separation. This is the "non-continuity": polarization cannot be taken continuously to zero without destroying the cavity itself.

## 5. Status

**Model-building constraint** — falsifiable: observing a pure 1/r² field component (monopole) from a single cavity violates K2.
