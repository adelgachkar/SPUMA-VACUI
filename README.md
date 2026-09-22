# SPUMA-VACUI

**فومِ خلأ** — Vacuum-Foam Genesis from Two Binding Constraints

> SPUMA-VACUI (*spuma vacui*, "foam of the vacuum") is the structural-companion
> project to [Emergence-SDF-Vault](https://github.com/adelgachkar/Emergence-SDF-Vault)
> and [CADENCE-SDF](https://github.com/adelgachkar/CADENCE-SDF): it derives the
> birth, homogeneity, and permanent polarization of cavities ("voids") from
> exactly **two binding constraints** acting on a noise-carrying vacuum foam.

## Core Claim

$$\text{SPUMA} = \text{Foam} + \underbrace{K1}_{\text{vacuum discontinuity}} + \underbrace{K2}_{\text{polarization-tension non-continuity}}$$

- **K1 — Vacuum Discontinuity:** noise is *rectified* at a freeze edge ρ₀;
  below it steps are rejected (frozen), above it the fluid carries a regional
  expansion bias → near-homogeneous cavities with sharp boundaries.
- **K2 — Polarization-Tension Non-Continuity:** the cavity wall is a sharp
  polarization sheet; the field is trapped *inside* the wall (two-sheet wall,
  exact result) → decay ladder 1/r³ → 1/r⁴ → 1/r⁵ with the **monopole channel
  identically zero** — the "broken magnet" is two wall-polarized magnets, never
  two free poles.

## Executed Numerical Verification (tools/)

| Test | Result |
|---|---|
| Freeze-edge rectification (200k walkers) | sharp frozen cut: 71% of population in two bins at the edge, zero in the frozen bulk |
| Two-domain polarization ladder | pair/single ratio = 3d/L (exact); monopole ≡ 0 at all distances |
| Two-sheet wall | field lives only inside the wall; exactly zero outside |
| Weave-registry frustration | 12.3% pitch mismatch vs pentagonal deficit → permanent polar wallpaper |

## Experimental Anchor

2026 graphene-wrinkle experiment (quantum orbital flexoelectricity,
*Advanced Materials*): polarization from shape alone, "battery-like without
storing/delivering energy", sharpness-over-size — mapped claim-by-claim in
[`04_Companion_Mapping/Reactive-Capsule-Graphene-Anchor.md`](04_Companion_Mapping/Reactive-Capsule-Graphene-Anchor.md),
with a quantitative, threshold-armed falsification protocol in
[`04_Companion_Mapping/Sharpness-Falsification-Test.md`](04_Companion_Mapping/Sharpness-Falsification-Test.md)
(reactive-capsule vs substrate vs pseudo-gauge channels; synthetic validation
100% correct assignment at 4% noise).

## Epistemic Status

Model-level claims with executed numerical protocols; no empirical cosmological
claim is made. Companion constants (δθ = 7.356103°, φ_max = 0.7405, f_c ≈ 30 THz)
are imported from the companion repositories and labeled as such.

## License

MIT — Adel Gachkar
