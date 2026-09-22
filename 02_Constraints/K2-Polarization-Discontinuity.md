---
title: "K2 — Polarization-Tension Discontinuity Constraint"
aliases: ["K2 Polarization Wall", "Unbounded Polarization Tension"]
created: 2026-09-20
updated: 2026-09-20
tags: [spuma-vacui, constraint, numerics]
status: "canonical"
license: "MIT"
---

# K2 — Polarization-Tension Discontinuity Constraint
## حد قیدی ۲ — عدم پیوستگی بی‌نهایت تنش قطبیدگی

> **Structural Causal Chain (SPUMA):**
> Near-Homogeneous Cavities → **Polarization Sheet** → Trapped-Field Wall → 1/r^3 → 1/r^4 → 1/r^5

## 1. Constraint Statement / گزاره قید

در مرز کاواک، قطبش **تیز** می‌شود (ناپیوسته است) و کشش آن از بالا مقید نمی‌شود — «بی‌نهایت تنش قطبیدگی» یعنی لایهٔ قطبش می‌تواند هر فشار بازپخشی را متعادل کند بدون آنکه نرم شود:

$$\mathbf{P}(x) = P_0\,\Theta_{\text{wall}}(\mathbf{x}),\qquad
\nabla\cdot\mathbf{P} = -P_0\,\delta_{\text{wall}} \quad (\text{بارهای قطبش فقط روی دیواره})$$

## 2. Trapped-Field Wall / دیوارهٔ میدان محبوس

دو صفحهٔ قطبش مقابل (ضخامت w) — حل دقیق ۱بعدی (تست K3 در `tools/spuma_constraints.py`):

$$\mathbf{E} = \begin{cases}0 & z<0\\ \hat{z}\,\sigma/\varepsilon_0 & 0<z<w\\ 0 & z>w\end{cases}$$

**میدان فقط درون دیواره زندگی می‌کند؛ بیرون دقیقاً صفر است** — «در آغوش‌گرفتن لبه» (edge-hugging). نتیجه: هیچ شار مونوپلی به بیرون نشت نمی‌کند؛ دیواره حفره یک ترک آهنربای دائم است، نه یک قطب منفرد.

## 3. Decay Ladder / نردبان واپاشی

| پیکربندی | لحظهٔ قطبی | واپاشی میدان | تست عددی |
|---|---|---|---|
| تک‌دامنهٔ قطبیده | دیپل | 1/r³ | B_single در L=40d |
| جفت قطب‌مخالف | یکه (m=0) | **1/r⁴** | \|pair/single\| = 3d/L دقیق (۰٫۰۷۵ در L=40d) |
| چهارقطبه | — | **1/r⁵** | خطای تسلط نزدیک/دور تأیید شد |
| مونوپل | — | **ممنوع** | ≡ 0 در همه L (پرچم < 10⁻⁶) |

## 4. Broken Magnet / آهنربای شکسته

`attachments/broken-magnet-weave.png`: بافت مسیرها پیش و پس از شکست — شکست آهنربا **دو قطبیدهٔ کامل** می‌دهد (هر تکه دیوارهٔ قطبیدهٔ خودش را می‌سازد). در SPUMA: کاواک‌های مجاور با دیواره‌های قطب‌مخالف، جفت‌های 1/r⁴ می‌سازند؛ خنثی‌سازی فقط با **پیوند** (حذف دو لایه) ممکن است — نه با جداسازی. این، «عدم پیوستگی» است: قطبش را نمی‌توان پیوسته به صفر برد بدون آنکه کاواک از بین برود.

## 5. Status

**قید مدل‌ساز** — فالسیفایبل: مشاهدهٔ مؤلفهٔ میدانی 1/r² خالص (مونوپل) از یک کاواک منفرد، K2 را نقض می‌کند.
