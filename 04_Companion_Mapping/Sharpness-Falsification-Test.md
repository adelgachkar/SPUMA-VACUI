---
title: "Sharpness-vs-Substrate Falsification Test"
aliases: ["Sharpness Falsification Test", "Capsule vs Substrate vs Gauge"]
created: 2026-09-20
updated: 2026-09-20
tags: [spuma-vacui, falsification, protocol, numerics]
status: "canonical"
license: "MIT"
---

# Sharpness-vs-Substrate Falsification Test
## آزمون فالسیفایبل تیزی-در-برابر-بستر — مدل کمّی و توان‌های تفکیک

> **Structural Causal Chain (SPUMA):**
> Curvature Gradient → Polarization P(R) → Back-Reaction dR/R → **Exponent Discrimination** → Verdict

## 1. Quantitative Model / مدل کمّی

**قانون قطبش** (اندازه‌گیری مستقل: نقشهٔ پتانسیل موضعی):

$$P(R) = P_0\Big(\frac{a}{R}\Big)^{n_p},\qquad
n_p = 2\ \ \text{(حد گرادیانی کلاسیک: t/R}\to(a/R)^2\text{)}$$

**سه کانال رقیب برای بازخورد انتقال** (تغییر مقاومت نسبی dR/R):

| کانال | توان تیزی n_b (در a/R) | توان ارتفاع m_b (در H) | پایهٔ کتگوریک |
|---|---|---|---|
| **کپسول راکتیو** (ادعای SPUMA) | **n_b = n_p** (قطبش را دنبال می‌کند) | m_b ≈ 0 | حساس به گیت و واپاشی |
| گیج شبه-مکانیکی (伪 gauge) | n_b = 2 (hfc²~R⁻²) | m_b = 1/2 | بی‌حس |
| تماس بستر (MoS₂ strain) | n_b = 1 (ε² ~ H/R) | m_b = 1 | بی‌حس |

## 2. Overdetermined Verdict / حکم بیش‌تعیین‌شده

دو توان پیوسته + دو پایهٔ کتگوریک:

1. **گیت:** زیرلایهٔ رسانا (گرافن روی فلز) میدان گیت کپسول را می‌کُشد — اگر سیگنال ناپدید شد، کانال کپسول است.
2. **واپاشی:** لایهٔ hBN میانی، میدان کپسول را نمایی تضعیف می‌کند (طول واپاشی λ) — گیج/بستر بی‌حس‌اند.

$$\text{REJECT capsule} \iff |n_b-n_p|>0.25\ \ \text{یا}\ \ m_b>0.2\ \ \text{یا بی‌حسی به گیت/واپاشی}$$

## 3. Synthetic Validation / اعتبارسنجی سنتتیک

`tools/sharpness_vs_substrate_test.py` (خروجی: `tools/sharpness_test_output.txt`) — دادهٔ سنتزی با نوفهٔ ۴٪، بازیابی توان با برازش log-log:

| کانال تزریق‌شده | n_b بازیابی‌شده | m_b بازیابی‌شده | حکم ماتریس |
|---|---|---|---|
| capsule | 2.006 (هدف 2) | 0.008 (هدف 0) | ✅ capsule (رأی ۴) |
| gauge | 2.010 (هدف 2) | 0.505 (هدف 0.5) | ✅ gauge (رأی ۳) |
| substrate | 0.981 (هدف 1) | 0.997 (هدف 1) | ✅ substrate (رأی ۳) |

مرجع قطبش: n_p = 2.044 بازیابی شد (هدف 2.0)؛ P(1nm) ≈ 6.6 mC/m² در مقیاس لنگر — سازگار با رژیم مداری.

## 4. Experimental Recipe / دستور آزمایشی

1. نقشهٔ پتانسیل حول چین‌های با تیزی‌های متفاوت (STM/KPFM) → n_p (مرجع).
2. پیمایش R در H ثابت و پیمایش H در R ثابت روی dR/R انتقال → (n_b, m_b).
3. دو کلید کتگوریک: زیرلایهٔ رسانا (گیت) و میانی hBN (واپاشی).
4. حکم از ماتریس بیش‌تعیین‌شده — هیچ توان منفردی کافی نیست (n_b=2 بین کپسول و گیج مشترک است؛ تفکیک با m_b و کلیدها).

## 5. Status / وضعیت

**پروتکل مشخص + اعتبارسنجی سنتتیک کامل** — اجرای واقعی نیازمند دادهٔ آزمایشگاهی (نقشهٔ پتانسیل و انتقال همان نمونه‌های چین گسنگاه/MoS₂). فالسیفایبل بودن ادعای «کپسول راکتیو = قید مؤثر» اکنون کمّی و آستانه‌دار است: [[Reactive-Capsule-Graphene-Anchor]].
