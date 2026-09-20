---
title: "Intrinsic Cavity Harmonics"
aliases: ["Intrinsic Harmonics", "Cavity Antagonism Spectrum"]
created: 2026-09-20
updated: 2026-09-20
tags: [spuma-vacui, harmonics, numerics]
status: "canonical"
license: "CC-BY-4.0"
---

# Intrinsic Cavity Harmonics
## هارمونی درونی حفره

> **Structural Causal Chain (SPUMA):**
> Near-Homogeneous Polarized Cavities → Interior Field ⨯ Edge Sweep → Intrinsic Harmonics → Companion Spectral Support

## 1. Source of the Harmonics / خاستگاه هارمونی

هر کاواک یک نوسان‌گر است که از **تقابل** دو عامل تغذیه می‌شود (اصل A4-Intrinsic-Harmonics-Antagonism]]):

$$\ddot{q}_n + \omega_n^2 q_n = 0,\qquad
\omega_n^2 = \omega_{\text{field}}^2 + \omega_{\text{edge}}^2 + 2\Gamma_n\,\omega_{\text{field}}\,\omega_{\text{edge}}$$

- ω_field² ∝ P₀²/μ_wall: انرژی محبوس در دیوارهٔ قطبیده (K2-Polarization-Discontinuity]])
- ω_edge² ∝ b/τ_rect: پایدارسازی یک‌سوژه‌شدهٔ لبه (K1-Vacuum-Discontinuity]])
- جملهٔ تقابلی 2Γ_n ω_f ω_e: تفکیک زوج/فرد — مدهای زوج تقابل را حفظ می‌کنند، مدهای فرد بازنشست می‌کنند.

## 2. Quantized Ceiling / سقف کوانتیده

چگال‌سازی کاواک‌ها با سقف کپلر مقید است (تست عددی K3-همتا):

$$\phi_{\max} = \frac{\pi}{\sqrt{18}} = 0.7405$$

کاواک‌های متراکم‌تر از حالت پنج‌گانه در طیف کسری وجود ندارند (کسری زاویه‌ای فوتی) — سقف اشباع، قید بسته‌بندی است نه تنظیم دینامیکی.

## 3. Spectral Support for the Companion / پشتیبانی طیفی همتا

هارمونی درونی، **پشتیبانی طیفی** شبکهٔ همتا است (`04_Companion_Mapping/Companion-Bridge`):

| کمیت | مقدار | نقش در همتا |
|---|---|---|
| δθ (کسری پنج‌ضلعی) | 7.356103° = 0.02044×2π | ضریب تفکیک زوج/فرد هارمونیک |
| f_c = κ_hop/π | ≈ 30 THz (g=0.8, λ₀=320nm) | پنجرهٔ باریک گرانشی همتا |
| h·f_c | ≈ 0.12 eV | لبهٔ کوانتومی انجماد K1 |
| ناسازگاری رجیستر بافت | 12.3% pitch | وال‌پیپر قطبی دائمی (K4) |

## 4. Testable Signatures / امضاهای آزمون‌پذیر

1. نسبت طیفی زوج/فرد ثابت δθ/2π در خانوادهٔ کاواک‌ها.
2. فروپاشی انتخابی مدهای زوج با حذف سوگیری لبه‌ای.
3. حذف شار محبوس فقط با پیوند قطب‌مخالف — هیچ‌گاه تابش مونوپلی.
