---
title: "Companion Bridge — Emergence-SDF-Vault / CADENCE-SDF"
aliases: ["Companion Bridge", "SPUMA-SDF Bridge"]
created: 2026-09-20
updated: 2026-09-20
tags: [spuma-vacui, companion, bridge]
status: "canonical"
license: "MIT"
---

# Companion Bridge — Emergence-SDF-Vault / CADENCE-SDF
## پل به مخزن همتا

> **Structural Causal Chain (SPUMA):**
> Intrinsic Harmonics → **Companion Spectral Support** → τ_d, c_eff, Boundary Term

## 1. Shared Constants / ثابت‌های مشترک

| ثابت | مقدار | در SPUMA | در همتا (Emergence-SDF-Vault) |
|---|---|---|---|
| δθ | 7.356103° | تفکیک زوج/فرد هارمونی، رجیستر بافت | کسری پنج‌ضلعی — ریشهٔ گیت مصنوعی و بدهی فاز |
| φ_max | π/√18 = 0.7405 | سقف چگالش کاواک | سقف اشباع تراکم |
| κ_hop | 0.025 g² ω₀، g∈[0.7,0.9] | نرخ دینامیک لبه | نرخ هاپ CROW؛ τ_d = π/2κ_hop |
| f_c | κ_hop/π ≈ 30 THz | لبهٔ انجماد K1 (h·f_c ≈ 0.12 eV) | لبهٔ پنجرهٔ باریک گرانشی |
| ناسازگاری رجیستر | 12.3% pitch (K4) | وال‌پیپر قطبی دائمی | انباشت بدهی فازی |

## 2. Mechanism Correspondence / تناظر سازوکارها

| SPUMA | همتا | وضعیت تناظر |
|---|---|---|
| سوگیری لبه‌ای (K1) | یک‌سوژه‌سازی نوفه؛ نوسان‌گر بدهی فازی | دقیق — هر دو rectified noise |
| دیوارهٔ محبوس (K2) | راکتیو-ماندگار مرزی؛ R_loss→0، ذخیرهٔ راکتیو | دقیق — میدان محبوس = ذخیرهٔ راکتیو |
| هارمونی از تقابل (A4) | ω_c از گیت C_id؛ طیف زوج/فرد | ساختاری — فرمول نهایی باز است |
| تورم ناحیه‌ای نوفه‌ای | انبساط به‌مثابه آرامش پله‌ای (Void_Expansion_Engine) | ساختاری — اصطلاح ΔH_boundary مشترک |

## 3. What SPUMA Adds / افزودن SPUMA

- **خاستگاه حفره**: همتا، حفره را «دادهٔ هندسی» می‌گیرد (چهار کرهٔ متقاطع)؛ SPUMA چگونگی **متولد شدن و هم‌گن ماندن** آن را از دو حد قیدی می‌سازد.
- **چرایی قطبدگی**: در همتا قطبیدگی حفره پیش‌فرض شبکه است؛ SPUMA آن را از سوگیری لبه‌ای **اشتقاق** می‌کند.
- **ممنوعیت مونوپل به‌مثابه قید تولد**: نه فقط نتیجهٔ هندسه، بلکه شرط ساخت کاواک.

## 4. Open Questions / پرسش‌های باز

1. فرمول بستهٔ ω_n (اصلاح زوج/فرد ε_n) از تقابل — نیازمند مدل دیواره با μ(x) صریح.
2. ~~توزیع اندازهٔ کاواک‌ها در رژیم لبه‌تیز~~ — **حل شد** (v0.2.0): سه رژیم، b_c = 0.126، D = 1.78، فرم گذار-اول p_f = e^{−2bm₀} با κ = 3.17 → `02_Constraints/K1-Cavity-Size-Distribution`.
3. آیا لبهٔ انجماد K1 همان گذار ℏκ~k_BT مدل همتاست؟ (مقیاس کاری متفاوت: 0.12 eV در برابر 0.026 eV — نسبت ≈ 4.6 برای توضیح دادن).

## 5. Bridge to LIMEN-VACUI / پل به LIMEN-VACUI (خواهر سوم)

[github.com/adelgachkar/LIMEN-VACUI](https://github.com/adelgachkar/LIMEN-VACUI) روایتِ «قبل از» SPUMA را می‌سازد (چرا مرزی هست که فوم در آن متولد شود) و از این نوبت **نگاشت پارامتری کمّی** دوطرفه برقرار است:

$$\text{LIMEN}(g_{\max}=0.297,\ \tau_q=40,\ \kappa=0.03) \;\Longleftrightarrow\; \text{SPUMA}(b=0.285)$$

- در کسری منجمد مشترک p_f، نسبت میانگین اندازهٔ خوشه R = s̄_LIMEN/s̄_SPUMA ∈ **[0.90, 0.98]** در جفت‌شدگی لاپلاسی ضعیف (κ≤0.10) — یعنی در حد بی‌جفت‌شدگی، ثبت LIMEN دقیقاً در کلاس universalی iid نقشهٔ K1 است.
- در κ بزرگ، مرزِ ساکت LIMEN تار پوشاست (p_f>0.42، نقطهٔ کانونی T1: p_f=0.912) — فاز دیگرِ همان فرایند ثبت.
- تفصیل، جدول‌ها و برچسب‌ها: نوت `Limen-Spuma-Parameter-Bridge` در مخزن LIMEN (+ آینهٔ EN)؛ ابزار `tools/limen_spuma_bridge.py`.
- برچسب‌ها: p_f و لنگر بازسنجیده (0.2992/2.32) [exact]؛ منحنی‌ها [measured]؛ حد iid [structural]؛ شناسایی «ثبت = انجماد» [model].

## 6. Repositories / مخزن‌ها

- همتا: `github.com/adelgachkar/Emergence-SDF-Vault` (v30.3) — این پروژه از ثابت‌های مشتق‌شدهٔ آن (κ_hop، τ_d، δθ) تغذیه می‌کند.
- همتای دوم: `github.com/adelgachkar/CADENCE-SDF` (v3.5.1) — اصطلاحات ΔH_boundary، نقطهٔ صفر مرزی، R_loss.
- خواهر سوم: `github.com/adelgachkar/LIMEN-VACUI` — پل کمّی §5.
