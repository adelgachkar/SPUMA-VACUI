---
title: "K1 — Vacuum Discontinuity Constraint"
aliases: ["K1 Freeze Edge", "Vacuum Discontinuity"]
created: 2026-09-20
updated: 2026-09-25
tags: [spuma-vacui, constraint, numerics]
status: "canonical"
license: "MIT"
lang: "en"
---

# K1 — Vacuum Discontinuity Constraint

> **Structural Causal Chain (SPUMA):**
> Vacuum Foam → **Freeze-Edge Rectification** → Sharp Cavity Boundary → Near-Homogeneous Cavities

## 1. Constraint Statement

The foam noise is **rectified** at the freezing edge:

$$\Delta\rho_{t+1} = \begin{cases}\xi_t - b\sigma & \rho_t \ge \rho_0 \quad \text{(fluid; regional-expansion bias)}\\ 0 & \rho_t < \rho_0 \quad \text{(frozen; the step is rejected)}\end{cases}$$

ξ ~ N(0, σ²), b the dimensionless bias. The **constraint** is that the phase-switch transition must be sharp — no intermediate dimension is allowed between frozen and fluid; this is precisely the "vacuum discontinuity".

## 2. Numerical Verification

`tools/spuma_constraints.py` (deposited output `tools/spuma_output.txt`), 200,000 walkers:

| Quantity | Result |
|---|---|
| Population above the edge | Sharp: 24.8% + 71.2% in the two layers adjacent to ρ₀; **zero** in the depth below the edge |
| Fluid fraction after 30 steps | 52.0% → 0.5% → 0.0% (fast freezing, then lock-in) |
| Pile-up beside the edge | One-sided distribution — the rectification signature |

These three features = near-homogeneous cavities with sharp boundaries and edge sweeping, **with no tuning parameter whatsoever** (b and σ only scale the dynamics, not the shape).

## 3. Physical Reading

- **Regional inflation**: fluid regions carry the expansion bias b → near-aligned growth; frozen regions stay put.
- **Edge sweeping**: since only the edge (not the depth) accepts steps, the dynamics concentrate at the edge — the edge is the "sweeper".
- Link to the companion model: the quantum edge h·f_c ≈ 0.12 eV at the working scale of the cavity ([[Companion-Bridge]]).

## 4. Status

**Model-building constraint** — collision admissible: if an experiment/simulation shows a soft (gradually receding) edge, K1 is violated.
