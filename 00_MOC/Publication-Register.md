---
title: "Publication-Register — SPUMA-VACUI journal submission"
aliases: ["Publication Register", "IJTP Submission Timeline"]
created: 2026-09-29
updated: 2026-09-29
author: "Adel Gachkar"
license: "MIT"
zenodo_section: "Index"
status: "canonical"
tags: [spuma-vacui, publication-register, ijtp, technical-check, timeline]
lang: "en"
---

# Publication-Register — SPUMA-VACUI journal submission

> **Epistemic status:** this note is an administrative timeline, not physics content.
> It records the journal submission history of the SPUMA-VACUI manuscript with the
> same timestamp discipline the family applies to its numerical register (every claim
> dated, every state change logged). No acceptance, approval, or editorial endorsement
> is claimed or implied by any entry.

## 1. Manuscript identity

| Field | Value |
|---|---|
| Title | SPUMA-VACUI: Emergence of Near-Homogeneous Polarized Cavities in a Vacuum-Foam Substrate via Dual Boundary Constraints |
| Journal | International Journal of Theoretical Physics (Springer) |
| Type | Research (original article) |
| Submission ID | `9bea6606-4b8b-486b-9378-742cff6dc1b9` |
| Author | Adel Gachkar (ORCID 0009-0006-7713-6004), single author |
| Current version | v1.0 (initial submission) → v1.1 (post-TC revision, re-submitted) |

## 2. Timeline (every entry dated)

| # | Date (local) | Event | Evidence / artifact |
|---|---|---|---|
| 1 | 2026-09-28 | Initial submission (v1.0) via Springer Nature SNAPP system; PDF generated from repository v0.4.10 content | system Submission ID |
| 2 | 2026-09-29 ~12:53 | **Technical Check letter** — single point: author names missing in the manuscript; 2-day revision window (deadline 2026-10-01) | editorial letter (Preethi Srinivasan, Editorial Support) |
| 3 | 2026-09-29 ~15:45–16:15 | Revision produced: author byline "Adel Gachkar / ORCID 0009-0006-7713-6004" inserted on page 1 below the date; verified non-invasive (5 pages preserved; content otherwise identical — hash-verified base document `dc410b6f…`, revision `905bfde2…`) | `tools/` PDF workflow; desktop artifact |
| 4 | 2026-09-29 ~16:40 | Point-by-point response letter (1 page) generated and approved | `SPUMA_TC_response_letter.pdf` |
| 5 | 2026-09-29 ~16:45 | Revision uploaded: response letter + revised manuscript replace originals; Authors tab verified identical (single author, exact spelling) | SNAPP Files tab screenshot |
| 6 | **2026-09-29 17:05** | **Re-submission accepted by system — "Submission received"**; status: Technical Check stage | success page (SNAPP) |

## 2b. Artifact chain (each step hash- or screenshot-verified)

| Artifact | Role | Verification |
|---|---|---|
| Revised manuscript PDF | the only changed artifact (author byline, page 1) | md5 `905bfde2…` vs base `dc410b6f…`; page-1 visual check |
| Response letter | formal answer to TC point 1; statement of no-other-changes | 1-page PDF from `.fodt` source |
| Fig. 1–3 data figures | prepared **during** the TC wait, before any reviewer request — timestamps registered in git `947c907` | `tools/make_paper_figures.py` + `tools/paper_figures_output.txt` |

## 2c. Registered ready-state (pre-drafted for the next editorial step)

| Item | State |
|---|---|
| Three data figures | generated 2026-09-29 from the canonical tools (`947c907`); captions pending insertion into the revised source |
| External references block (8 items) | pre-drafted mapping to manuscript sections (Hinrichsen 2000; Bak–T|Wiesenfeld 1987; Kottos–Smilansky; Stauffer–Aharony; Kalinin–Meunier 2008; Iyengar et al. 2026; Lee et al. 2008; Chen et al. 2021) — to be inserted in the revision after peer-review invitation |
| Editable source (DOCX) | pending conversion from the `.fodt` source (system prefers editable formats; PDF accepted at v1.0/v1.1 TC) |

## 3. Interpretation rules (registered, not assumed)

- **No status is claimed beyond the logged facts.** "Submission received" ≠ review
  invitation ≠ acceptance. The current registered state is exactly: *re-submitted,
  awaiting second Technical Check outcome*.
- The 2-day TC deadline (2026-10-01) applies to the revision that has **already been
  submitted (2026-09-29)** — the deadline is met with ~1.5 days of margin.
- Any new editorial letter supersedes this register's "current status" and must be
  logged as a new timeline row with its own evidence artifact.
- Zenodo version DOI **10.5281/zenodo.23017334** (v0.4.10) is the citable snapshot of
  the repository content the manuscript synthesizes; its registration is recorded in
  `CITATION.cff` and the README badge (see the repository front matter, not this note).
