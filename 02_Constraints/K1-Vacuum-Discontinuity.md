---
title: "K1 — Vacuum Discontinuity Constraint"
aliases: ["K1 Freeze Edge", "Vacuum Discontinuity"]
created: 2026-09-20
updated: 2026-09-20
tags: [spuma-vacui, constraint, numerics]
status: "canonical"
license: "CC-BY-4.0"
---

# K1 — Vacuum Discontinuity Constraint
## حد قیدی ۱ — حد انفصال خلأ

> **Structural Causal Chain (SPUMA):**
> Vacuum Foam → **Freeze-Edge Rectification** → Sharp Cavity Boundary → Near-Homogeneous Cavities

## 1. Constraint Statement / گزاره قید

نوفهٔ فوم در لبهٔ انجماد **یک‌سوژه** می‌شود:

$$\Delta\rho_{t+1} = \begin{cases}\xi_t - b\sigma & \rho_t \ge \rho_0 \quad (\text{سیال؛ سوگیری انبساط ناحیه‌ای})\\ 0 & \rho_t < \rho_0 \quad (\text{منجمد؛ گام پس زده می‌شود})\end{cases}$$

ξ ~ N(0, σ²)، b بی‌بعد سوگیری. **قید** این است که گذار فاز-سوییچ تیز باشد — هیچ میان‌بُعدی بین منجمد و سیال مجاز نیست؛ همین، «حد انفصال خلأ» است.

## 2. Numerical Verification / راستی‌آزمایی عددی

`tools/spuma_constraints.py` (خروجی ثبت‌شده `tools/spuma_output.txt`)، ۲۰۰٬۰۰۰ پیماینده:

| کمیت | نتیجه |
|---|---|
| جمعیت بالای لبه | تیز: ۲۴٫۸% + ۷۱٫۲% در دو لایهٔ چسبیده به ρ₀؛ **صفر** در عمق زیر لبه |
| کسری سیال پس از ۳۰ گام | ۵۲٫۰% → ۰٫۵% → ۰٫۰% (انجماد سریع، سپس قفل) |
| پشته شدن کنار لبه | توزیع یک‌طرفه — امضای یک‌سوژه‌سازی |

این سه ویژگی = کاواک‌های تقریباً هم‌گن با مرز تیز و سوگیری لبه‌ای، **بدون هیچ پارامتر تنظیمی** (تنها b و σ دینامیک را مقیاس می‌دهند، شکل را نه).

## 3. Physical Reading / خوانش فیزیکی

- **تورم ناحیه‌ای**: ناحیه‌های سیال، سوگیری انبساطی b دارند → رشد تقریباً هم‌جهت؛ ناحیه‌های منجمد ثابت می‌مانند.
- **سوگیری لبه‌ای**: چون فقط لبه (نه عمق) گام می‌پذیرد، پویایی در لبه متمرکز است — لبه «جاروبکننده» است.
- پیوند به مدل همتا: لبهٔ کوانتومی h·f_c ≈ 0.12 eV در مقیاس کاری کاواک (Companion-Bridge]]).

## 4. Status

**قید مدل‌ساز** — برخورد پذیرفتنی: اگر آزمایش/شبیه‌سازی لبهٔ نرم (پس‌رونده تدریجی) نشان دهد، K1 نقض می‌شود.
