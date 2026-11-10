# Arabic Grammar & Spelling Guide for UX Writing

This reference covers the grammar, spelling, and formatting rules that matter most in Arabic UX microcopy. These aren't academic rules — they're the specific patterns that cause the worst readability problems in real Arabic interfaces.

---

## Grammar Rules

### 1. Verb-first word order (VSO)

Arabic's natural sentence structure is Verb-Subject-Object. UX copy should follow it, especially for actions.

| ✅ Natural Arabic | ❌ عرنجي / Unnatural |
|-------------------|----------------------|
| `حمّل التطبيق` | `قم بتحميل التطبيق` |
| `أنشئ حسابًا` | `قم بإنشاء حساب` |
| `اختر موعدًا` | `قم باختيار موعد` |
| `أرسل الطلب` | `قم بإرسال الطلب` |

### 2. Eliminate "تم" + مصدر

This is the #1 marker of عرنجي writing. It's a calque from English passive ("was done"). But the fix is **not** always the Arabic passive (مبني للمجهول) — sometimes the passive sounds heavy or forced too. You have three alternatives; pick the lightest one for each context.

**Alternative 1 — Arabic passive (مبني للمجهول):**
Works best when the verb is short and light on the tongue: حُفظ، حُذف، أُلغي، أُرسل.
Feels heavy when the verb has تشديد or multiple syllables: سُجِّل، أُضيف، اسْتُكْمِل.

| ✅ Passive works here | ❌ تم + مصدر |
|------------------------|--------------|
| `حُفظت التغييرات` | `تم حفظ التغييرات` |
| `أُرسلت الرسالة` | `تم إرسال الرسالة` |
| `أُلغي الطلب` | `تم إلغاء الطلب` |
| `حُذف الملف` | `تم حذف الملف` |

**Alternative 2 — Active with نحن (we did it):**
Adds warmth — the product feels like a team helping you. Best for success messages.

| ✅ Active with نحن | ❌ تم + مصدر |
|---------------------|--------------|
| `سجّلنا حسابك` | `تم تسجيل حسابك` |
| `حفظنا التغييرات` | `تم حفظ التغييرات` |
| `أرسلنا الرسالة` | `تم إرسال الرسالة` |
| `حدّثنا بياناتك` | `تم تحديث بياناتك` |

**Alternative 3 — Nominal sentence (skip the verb entirely):**
Tell the user the result, not the process. Often the best UX choice.

| ✅ Nominal sentence | ❌ تم + مصدر |
|----------------------|--------------|
| `حسابك جاهز` | `تم تسجيل حسابك` |
| `تسجيلك مكتمل` | `تم التسجيل بنجاح` |
| `طلبك في الطريق` | `تم إرسال طلبك` |
| `التغييرات محفوظة` | `تم حفظ التغييرات` |

**Quick decision rule:** Read the مبني للمجهول version out loud. If it flows easily (حُفظت، أُلغي) → use it. If it feels heavy or awkward (سُجِّلت، اسْتُكْمِلت) → use نحن active or a nominal sentence instead.

**The one valid `تم`:** when تمّ carries its real meaning — a process that genuinely *reaches completion*: `تمّ التحميل`، `تمّ الدفع` (and `اكتمل التحميل` is usually cleaner). Outside that, `تم` + مصدر is the passive calque regardless of register — its heavy presence in official/legal Arabic is the calque spreading, not a license to keep it.

### 3. Eliminate "قام بـ" / "القيام بـ"

Another common calque. Replace with the direct verb.

| ✅ Direct verb | ❌ قام بـ |
|----------------|----------|
| `سجّل الدخول` | `قام بتسجيل الدخول` |
| `حدّث التطبيق` | `قم بتحديث التطبيق` |
| `ألغِ الاشتراك` | `قم بإلغاء الاشتراك` |

### 4. Eliminate "لقد قمت بـ"

The triple-filler construction. Rewrite completely.

| ✅ Clean | ❌ لقد قمت بـ |
|----------|--------------|
| `حسابك جاهز` or `سجّلناك` | `لقد قمت بالتسجيل بنجاح` |
| `وصلنا بلاغك` | `لقد قمت برفع بلاغ` |
| `موعدك محجوز` or `حجزنا موعدك` | `لقد قمت بحجز الموعد` |

### 5. Drop unnecessary "هو" / "هي"

Arabic nominal sentences don't need a copula.

| ✅ Without copula | ❌ With unnecessary copula |
|-------------------|--------------------------|
| `حسابك جاهز` | `حسابك هو جاهز` |
| `كلمة المرور مطلوبة` | `كلمة المرور هي مطلوبة` |
| `التطبيق متاح مجانًا` | `التطبيق هو متاح مجانًا` |

### 6. Possessive pronouns vs. "الخاص بك"

Use the pronoun suffix. "الخاص بك" is wordy and unnatural.

| ✅ Pronoun suffix | ❌ الخاص بك |
|-------------------|------------|
| `حسابك` | `الحساب الخاص بك` |
| `طلبك` | `الطلب الخاص بك` |
| `ملفاتك` | `الملفات الخاصة بك` |
| `إعداداتك` | `الإعدادات الخاصة بك` |

### 7. "لـ" vs. "من أجل"

Use the shorter preposition when it works (which is almost always in UX).

| ✅ Short | ❌ Verbose |
|----------|----------|
| `لحفظ التغييرات` | `من أجل حفظ التغييرات` |
| `لمتابعة التسوق` | `من أجل متابعة عملية التسوق` |
| `لإنشاء حسابك` | `من أجل القيام بإنشاء حسابك` |

### 8. Verb-subject gender agreement — pick a strategy and be consistent

Arabic verbs conjugate for gender. The critical rule is **consistency across the product** — don't mix imperative and masdar in the same interface.

**Three product-level strategies:**

| Strategy | Button example | Tone | When to use |
|----------|---------------|------|-------------|
| **1. Masculine throughout** | `أضف عنوانًا` | Direct, warm | Default for most products. المذكر هو الأصل في العربية. |
| **2. Masdar throughout** | `إضافة عنوان` | Neutral, formal | Products wanting a gender-neutral tone throughout. |
| **3. Personalized + masculine fallback** | `أضف` (male) / `أضيفي` (female) / `أضف` (unknown) | Personal, best UX | Products with gender data. When gender is unknown, default to masculine — it's the grammatical أصل. |

**The rule:** apply one strategy across the entire product. Never mix.

| ✅ Consistent | ❌ Mixed |
|---------------|---------|
| `أضف عنوانًا` → `أكمل الطلب` → `ادفع` | `إضافة عنوان` → `أكمل الطلب` → `دفع` |
| `إضافة عنوان` → `إكمال الطلب` → `دفع` | `أضف عنوانًا` → `إكمال الطلب` → `ادفع` |

### 8b. Gender of common interface nouns

Beyond verb strategy, watch agreement with nouns whose gender is often mistaken. Source: مصطفى جواد، *قل ولا تقل*.

| Noun | Gender | ✅ Correct agreement | ❌ Wrong |
|------|--------|----------------------|----------|
| `مستشفى` | masculine | `هذا مستشفًى جديد` | `هذه مستشفًى جديدة` |
| `باب` | masculine | `البابُ مفتوح` | `البابُ مفتوحة` |
| `سِنّ` (tooth) | feminine | `سِنٌّ مكسورة` | `سِنٌّ مكسور` |

For products using personalized/gendered copy, `عضوة` is the feminine of `عضو` — use it for women (`أنتِ عضوة`), not the masculine default. This reinforces strategy 3 in section 8.

### 9. Don't separate مضاف and مضاف إليه

The possessive construct (إضافة) must not be split by conjunctions.

| ✅ Correct | ❌ Split إضافة |
|-----------|---------------|
| `جمال التصميم وروعته` | `جمال وروعة التصميم` |
| `سهولة الاستخدام وسرعته` | `سهولة وسرعة الاستخدام` |

### 10. Conditional "كلما" — don't repeat it

| ✅ Correct | ❌ Repeated |
|-----------|-----------|
| `كلما أسرعت، ضمنت مكانك` | `كلما أسرعت، كلما ضمنت مكانك` |

### 11. Don't lead with existential "هناك"

Arabic doesn't need an existential opener the way English uses "there is/there are." Front-load the content instead. This is one of the most common structural calques identified in العرنجية (الغامدي).

| ✅ Natural Arabic | ❌ هناك calque |
|-------------------|---------------|
| `في سلتك ٣ عناصر` | `هناك ٣ عناصر في سلتك` |
| `لا رسائل جديدة` | `لا يوجد هناك رسائل جديدة` |
| `خطوتان متبقيتان` | `هناك خطوتان متبقيتان` |
| `تحديث متاح` | `هناك تحديث متاح` |

### 12. "عندما" (temporal) vs. "إذا" (conditional)

Arabic distinguishes temporal "when" (عندما — something that happens in time) from conditional "when/if" (إذا — a choice or possibility). English "when" covers both, so writers default to عندما everywhere.

In UX, most instances are conditional — the user *might* do something. Use إذا or إن.

| ✅ Correct | ❌ Confused |
|-----------|-----------|
| `إذا أردت الاستمرار، اضغط التالي` | `عندما تريد الاستمرار، اضغط التالي` |
| `إن واجهت مشكلة، تواصل معنا` | `عندما تواجه مشكلة، تواصل معنا` |
| `عندما يكتمل التحميل، ستُنبَّه` ✅ | — (genuinely temporal, عندما is correct) |

### 13. Avoid "بشكل" + adjective as an adverb

English adverbs ("-ly") have no direct Arabic equivalent. Writers calque them as بشكل + adjective. Arabic uses the مصدر, the حال (accusative), or a direct adverb instead.

| ✅ Natural Arabic | ❌ بشكل calque |
|-------------------|---------------|
| `يعمل صحيحًا` or `يعمل كما ينبغي` | `يعمل بشكل صحيح` |
| `اكتمل` | `اكتمل بشكل ناجح` |
| `يعمل دائمًا` | `يعمل بشكل دائم` |
| `عولجت آليًا` | `تمت المعالجة بشكل آلي` |

---

## Spelling Rules

### 1. Use "أو" not "/"
- ✅ `البريد الإلكتروني أو رقم الهاتف`
- ❌ `البريد الإلكتروني/رقم الهاتف`

### 2. No extra alif on present-tense verbs ending in و
- ✅ `نرجو` / `يدعو` / `يرجو`
- ❌ `نرجوا` / `يدعوا` / `يرجوا`

(The alif only appears with the plural: `يرجون` → `يرجوا` in conditional/jussive, but NOT in the indicative.)

### 3. Tanween + hamza after alif
- ✅ `مساءً` / `بناءً` / `أداءً`
- ❌ `مساءًا` / `بناءًا` / `أداءًا`

### 4. Taa marbuta (ة) vs. Haa (ه)
Test by converting to dual:
- `رسالة ← رسالتان` → taa marbuta ✅
- `وجه ← وجهان` → haa ✅

Common UX terms to get right: `خدمة`, `رسالة`, `صفحة`, `ميزة`, `إشارة`

### 5. Hamzat al-wasl (ا) vs. Hamzat al-qat' (أ/إ)
Add و before the word: if the hamza is pronounced, it's qat' (أ/إ); if silent, it's wasl (ا).

Common UX terms:
- `استخدام` (wasl) — `واستخدام` ← hamza drops
- `إرسال` (qat') — `وإرسال` ← hamza stays
- `اشتراك` (wasl) — `واشتراك` ← hamza drops
- `إلغاء` (qat') — `وإلغاء` ← hamza stays

---

## Morphology Rules (قواعد صرفية)

### 14. اسم التفضيل — when أَفْعَل works and when it doesn't

اسم التفضيل on the pattern أَفْعَل can only be derived from a verb that is: ثلاثي (triliteral), مثبت (affirmative), متصرف (conjugatable), تام (complete), قابل للتفاوت (admits degrees), مبنيّ للمعلوم (active voice). If any condition fails, use أكثر/أشد + the adjective instead.

Source: الصرف الصغير، العيوني، قسم اسم التفضيل.

| ✅ Valid أَفْعَل | ❌ Invalid | ✅ Correct alternative |
|-----------------|-----------|----------------------|
| `أسهل` (from سَهُلَ — triliteral ✅) | `أطبع` (from طبيعي، نسبة adjective, not a verb) | `أقرب للطبيعي` or `أسلس` |
| `أوضح` (from وَضَحَ ✅) | `أروع` is sometimes misused for non-triliteral senses | `أكثر روعة` |
| `أسرع` (from سَرُعَ ✅) | | |
| `أبسط` (from بَسُطَ ✅) | | |

In UX, this matters mostly in comparative/marketing copy and feature descriptions.

### 15. اسم المفعول as a lighter alternative to المبني للمجهول

اسم المفعول (مَفْعول from الثلاثي, مُفْعَل/مُفَعَّل from المزيد) carries the same meaning as the passive verb but is lighter in UI because it's a noun — it fits naturally into nominal sentences (جمل اسمية).

**Decision rule:** describing a **state** (status badge, settings, profile) → اسم المفعول is better. Describing an **event** that just happened (success toast, confirmation) → passive verb or نحن active is better.

| Context | ✅ اسم مفعول (state) | ✅ Verb (event) |
|---------|---------------------|----------------|
| Settings screen | `حسابك مُفعَّل` | — |
| Success toast | — | `فعّلنا حسابك` |
| Status badge | `مُرسَل` / `محفوظ` / `مُعلَّق` | — |
| Confirmation | — | `أُرسل طلبك` or `أرسلنا طلبك` |
| File state | `مسودة` / `منشور` / `مؤرشف` | — |

---

## Punctuation Rules

- Use Arabic comma (،) not English comma (,)
- Avoid the em dash (—) in Arabic copy; it is a Latin mark with no native place in Arabic. Use the Arabic comma (،), a colon, parentheses, or split into two sentences.
- Use punctuation sparingly — microcopy doesn't need heavy punctuation
- No `!!` or `!!!` — one `!` maximum, and rarely
- No `...` for trailing off — be direct
- No colon after headings unless it introduces a list
- Question marks are fine for actual questions: `هل تريد المتابعة؟`

---

## Formatting

- Arabic text is RTL — check that mixed Arabic/English strings display correctly
- Numbers: use Western Arabic numerals (1, 2, 3) in most tech contexts, or Eastern Arabic (١، ٢، ٣) per regional preference. Be consistent within a product.
- Avoid diacritics (حركات/تشكيل) unless absolutely needed to prevent ambiguity
- For currency, units, and codes, place them according to the RTL reading direction
