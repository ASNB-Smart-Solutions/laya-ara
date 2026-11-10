---
name: ux-araby
description: Write, edit, localize, and audit Arabic UX microcopy for apps, websites, and software interfaces. Use for Arabic buttons, labels, errors, success messages, empty states, forms, onboarding, tooltips, modals, notifications, headings, help text, localization review, terminology consistency, and Arabic voice/tone. Produces فصحى مبسطة that is purposeful, concise, natural, and clear; avoids عرنجي phrasing, stiff over-formality, literal English calques, verbosity, and common grammar/spelling issues. Includes guidance for RTL context, gender strategy, placeholders, plurals, numerals, formatting, prepositions, and Arabic UX-specific anti-patterns.
---

# ux-araby (كتابة تجربة المستخدم بالعربية)

## Purpose

Arabic UX writing is not translation with Arabic letters. Good Arabic interface copy must fit the user's task, the UI surface, right-to-left reading, Arabic morphology, regional expectations, and the product's voice. The target is **فصحى مبسطة**: correct, natural, concise Arabic that feels written for a product, not copied from a manual or translated from English.

Use this skill when creating, editing, localizing, or auditing Arabic interface text: buttons, labels, errors, success messages, empty states, forms, onboarding, tooltips, modals, notifications, headings, help text, settings, permissions, checkout, subscription flows, and Arabic terminology systems.

**Key sources:** This skill draws on أحمد الغامدي's العرنجية for structural and semantic calques from English, المرادي's الجنى الداني for preposition semantics, and العيوني's الصرف الصغير for morphology rules such as اسم التفضيل، اسم المفعول، and passive forms.

---

## Operating Workflow

Before writing or reviewing, identify the job type:

1. **Create**: the user needs new Arabic UI copy.
2. **Edit**: the user provides Arabic copy and asks to improve it.
3. **Localize**: the user provides source copy in another language and wants Arabic UX copy.
4. **Audit**: the user provides many strings, a screen, a flow, or asks whether the Arabic works.
5. **Define voice**: the user wants Arabic voice, tone, terminology, or product writing rules.

If the needed context is missing and the task is small, infer sensible defaults and proceed. If the missing context changes the answer materially, ask one concise question before writing.

### Context to Gather or Infer

- Product domain and user goal.
- UI element type: button, title, helper text, toast, modal, empty state, notification, form label, etc.
- Audience and locale: Saudi, Gulf, Egypt, Levant, pan-Arab, enterprise, youth, government, consumer.
- Register: فصحى مبسطة by default; formal only when context requires it.
- Gender strategy: masculine default, masdar labels, or personalized gendered copy.
- Space limits: character count, button width, notification title length, mobile constraints.
- Numeral style: Western Arabic numerals `1, 2, 3` or Eastern Arabic numerals `١، ٢، ٣`.
- Technical constraints: placeholders, variables, tags, links, product names, pluralization keys.
- Flow context: what happened before this message and what the user should do next.

### Default Assumptions

When the user gives no extra context, assume:

- Register: **فصحى مبسطة**.
- Tone: clear, warm, professional, not playful unless requested.
- Gender: masculine imperative for direct actions, unless the product uses masdar labels.
- Numerals: keep the style already present in the user's copy; otherwise use Western Arabic numerals in tech contexts.
- Diacritics: avoid تشكيل except where needed to prevent ambiguity.
- Product names, brand names, placeholders, and code-like strings: preserve exactly.

---

## Output Formats

For creation, put the recommended copy first and add alternatives only when useful:

```markdown
Recommended: `...`
Alternative: `...`
Why: ...
```

For a single edit or review:

```markdown
Better: `...`
Issue: ...
```

For audits, group by flow or surface and prioritize user-impacting problems first: unclear action, wrong meaning, broken placeholder/plural logic, severe عرنجي, then style polish.

```markdown
Original: `...`
Better: `...`
Issue: ...
Why: ...
```

For voice and terminology, return reusable rules: voice, tone shifts, terminology, and do/don't examples.

---

## Four Quality Standards

Every Arabic UX string must pass these standards in order:

### 1. هادف — Purposeful

The text must help the user do something, understand a state, recover from a problem, or make a decision. If it does not serve the user's immediate goal, remove it.

Ask:

- What is the user trying to do right now?
- What does this text clarify that the UI does not already show?
- Is the next step obvious?

### 2. موجز — Concise

Use the fewest Arabic words that preserve meaning, tone, and trust. Cut filler before cutting useful guidance.

| Element | Target |
|---|---|
| Buttons | 1-3 words, 4 max |
| Titles | 2-5 words |
| Errors | 8-15 words including recovery |
| Instructions | 15 words max |
| Notification title + body | 10-15 words total when possible |

### 3. طبيعي — Natural

Read the copy out loud. If it sounds like a translated manual, a government form, or a news broadcast, soften it. Use فصحى مبسطة that an educated Arabic speaker would naturally say in a product context.

### 4. واضح — Clear

The user should understand it in one read. Prefer specific verbs, concrete nouns, and direct recovery steps. Avoid ambiguity, decorative eloquence, and jargon unless the audience expects it.

---

## Core Arabic UX Rules

### Prefer Action-First Copy for Actions

For actions and instructions, Arabic usually feels more natural when the verb leads.

- Good: `حمّل التطبيق`
- Avoid: `قم بتحميل التطبيق`

Do not force verb-first wording everywhere. Headings, status labels, empty states, and badges often work better as nominal phrases.

- Good heading: `إعدادات الحساب`
- Good status: `الحساب مُفعّل`

### Avoid `تم` by Default

`تم` + مصدر is often an English passive calque. Before choosing the replacement, ask: **who performed the action?**

**The user performed the action themselves** (the app is just a tool):
- Use direct past tense addressed to the user: `سبّحت` · `أكملت القراءة` · `أنهيت التمرين`

**The user triggered it but the system executed it:**
- Pick ONE style for the whole product and use it everywhere:
  - Passive when light: `حُفظت التغييرات`
  - Active with نحن when warmer: `أرسلنا الرسالة`
  - Nominal when clearer: `حسابك جاهز`
- Do not mix styles: if the product uses نحن, use it for all system actions — not نحن here and passive there and nominal elsewhere.

**Weight test:** read the passive aloud. Short passives flow (حُفظ، حُذف، أُلغي، أُرسل). Heavy passives with تشديد don't (سُجِّل، اسْتُكْمِل) — switch to نحن active or nominal instead.

**The only valid `تم`:** when تمّ carries its real meaning — a process that genuinely *reaches completion*: `تمّ التحميل` · `تمّ الدفع` (and even here `اكتمل التحميل` is usually cleaner). Everything else (`تم الحفظ` = was saved, `تمت الموافقة` = was approved) is the passive calque, regardless of register — every such case has a light native passive (`حُفظ`، `أُرسل`، `أُجّل`), an active نحن, or a nominal sentence.

**Don't be fooled by the formal register:** `تم` + مصدر saturates official Arabic — bank messages, government portals, legalese (`تمت الموافقة`، `تم استلام طلبكم`). That prevalence is the calque spreading, not a license. Formality does not redeem it.

### Avoid `قم بـ` and `القيام بـ`

Use the direct verb.

- Good: `أنشئ حسابك`
- Avoid: `قم بإنشاء حسابك`

### Remove Filler Pronouns

Arabic nominal sentences do not need `هو` or `هي` as an English-style copula.

- Good: `حسابك جاهز`
- Avoid: `حسابك هو جاهز`

### Choose One Gender Strategy

Arabic verbs encode gender. Consistency matters more than the specific strategy.

| Strategy | Example | Use When |
|---|---|---|
| Masculine imperative | `أضف عنوانًا` | Default for most products; direct and natural. |
| Masdar labels | `إضافة عنوان` | Neutral, formal, menu-like interfaces. |
| Personalized | `أضف` / `أضيفي` | Product has reliable gender data and rendering support. When gender is unknown, default to masculine — it is the grammatical أصل in Arabic. |

Never mix imperative and masdar labels in the same flow without a deliberate reason.

### Cut Common Filler

- `الذي / التي / الذين` when padding: `حدد الموعد المناسب`, not `حدد الموعد الذي يناسبك`.
- `هذا / هذه` when obvious: `تفاصيل طلبك`, not `هذه تفاصيل طلبك`.
- `هنا / من هنا` when the UI location is obvious: `استعرض طلباتك`, not `استعرض طلباتك من هنا`.
- `بنجاح` in most success messages: `حُفظت التغييرات`, not `تم الحفظ بنجاح`.
- `عملية` before actions: `إتمام الدفع`, not `إتمام عملية الدفع`.
- `الخاص بك`: `حسابك`, not `الحساب الخاص بك`.

### Avoid Structural Calques

Check `references/anti-patterns.md` when reviewing for عرنجي. Common fixes:

- `بشكل دائم` → `دائمًا`
- `هناك 3 عناصر في سلتك` → `في سلتك 3 عناصر`
- `عندما تريد المتابعة` → `إذا أردت المتابعة`
- `المستخدم يمكنه التحديث` → `يمكنك التحديث`
- `من أجل إكمال التسجيل` → `لإكمال التسجيل`

---

## Production Localization Rules

### Preserve Technical Tokens Exactly

Do not change, reorder, translate, or remove placeholders unless explicitly asked.

Preserve:

- Variables: `{name}`, `{count}`, `%s`, `%d`, `$1`, `{{userName}}`.
- ICU syntax: `{count, plural, one {...} other {...}}`.
- Tags: `<strong>`, `</a>`, `<0>...</0>`.
- Links, URLs, emails, filenames, API names, plan IDs, and product names.

If Arabic grammar requires a different word order around a placeholder, move surrounding words but keep the placeholder intact.

- Source: `Welcome, {name}`
- Arabic: `مرحبًا، {name}`

### Handle Arabic Plurals Deliberately

Arabic plural logic is not English singular/plural. When count is dynamic, ask for the i18n system or provide count categories.

Use categories when possible:

| Count | Category | Example |
|---|---|---|
| 0 | zero | `لا توجد رسائل` |
| 1 | one | `رسالة واحدة` |
| 2 | two | `رسالتان` |
| 3-10 | few | `{count} رسائل` |
| 11+ | many/other | `{count} رسالة` |

Do not write one generic string if it will be wrong for common counts.

### Respect RTL and Mixed Text

Arabic is RTL, but product names, emails, codes, and many technical tokens are LTR. Keep mixed strings short and test visual order when possible.

- Good: `سجّل الدخول باستخدام Google`
- Good: `أرسلنا الرمز إلى name@example.com`
- Good: `استخدم الرمز SAVE20 عند الدفع`

Avoid slash alternatives in Arabic UI copy. Use `أو`.

- Good: `البريد الإلكتروني أو رقم الهاتف`
- Avoid: `البريد الإلكتروني/رقم الهاتف`

### Numerals, Currency, Dates, and Units

Numeral style is the writer's call, set once per product and locale, then applied consistently. If there's no existing convention:

- Western digits (`3`, `24`, `2026`) are common in tech products.
- Eastern digits (`٣`، `٢٤`، `٢٠٢٦`) suit products or locales that already use them.
- For Saudi/Gulf contexts, `ر.س` or `ريال` may both be acceptable; match product convention.
- Keep currency placement readable in RTL: `29 ريالًا شهريًا`, `ر.س 29` if that is the product standard.
- Dates and times should favor clarity over literal translation: `غدًا، 9:00 ص`.

Examples elsewhere in this skill (including the huroof reference) may use either digit style — treat their digits as illustrative, not as a numeral recommendation.

### Do Not Over-Translate

Keep these unchanged unless the user requests localization:

- Brand names: `Google`, `Apple Pay`, `Visa`.
- Product names and plan names.
- Code, filenames, coupon codes, SKUs.
- Legal names and API labels.

---

## UX Pattern Library

### Buttons

Use a specific action. The form depends on the product's gender strategy.

| Context | Good | Avoid |
|---|---|---|
| Save changes | `حفظ التغييرات` or `احفظ التغييرات` | `حفظ` |
| Delete account | `حذف الحساب` or `احذف الحساب` | `قم بحذف الحساب` |
| Start | `ابدأ` | `انقر هنا للبدء` |
| Sign in | `تسجيل الدخول` or `سجّل الدخول` | `اضغط لتسجيل الدخول` |

### Error Messages

Pattern: what happened + why if useful + how to recover.

| Good | Avoid |
|---|---|
| `كلمة المرور غير صحيحة. حاول مرة أخرى.` | `خطأ في الإدخال` |
| `تعذّر الحفظ. تحقق من اتصالك بالإنترنت.` | `حدث خطأ غير معروف` |
| `لا توجد مواعيد متاحة حاليًا. جرّب تاريخًا آخر.` | `حدث خطأ في الخادم. الرجاء الانتظار قليلًا أو معاودة المحاولة لاحقًا.` |

Avoid blame language like `بيانات خاطئة`. Prefer specific, recoverable language.

### Success Messages

Pattern: result first, next step only if useful. Who did the action determines the voice:

**User performed the action (app is a tool):**

| Good | Avoid |
|---|---|
| `سبّحت` | `تم الانتهاء من التسبيح` |
| `أكملت القراءة` | `تم إكمال القراءة بنجاح` |
| `أنهيت التمرين` | `تم الانتهاء من التمرين` |

**System executed the action (user triggered it):**

| Good | Strategy | Avoid |
|---|---|---|
| `حُفظت التغييرات` | Light passive | `تم حفظ التغييرات بنجاح` |
| `أرسلنا الرسالة` | Warm active | `تم إرسال الرسالة بنجاح` |
| `حسابك جاهز. يمكنك الآن تسجيل الدخول.` | Nominal + next step | `تمت عملية التسجيل. يمكنك الآن القيام بتسجيل الدخول.` |

Pick one strategy for system actions and use it consistently across the product.

### Empty States (الحالة الخالية)

Pattern: why it is empty + useful next step.

| Good | Avoid |
|---|---|
| `لا توجد رسائل بعد. ابدأ محادثة جديدة.` | `لا يوجد محتوى لعرضه في الوقت الحالي.` |
| `لا توجد نتائج لـ"قهوة". جرّب كلمات بحث مختلفة.` | `لم يتم العثور على نتائج.` |
| `قائمتك فارغة. أضف عناصر لتبدأ.` | `لا يوجد عناصر.` |

The examples above are fine, but tighter or warmer variants are often better:

- **Tighter:** `لا رسائل` (لا النافية للجنس) is more concise than `لا توجد رسائل` — both correct.
- **Active نحن** when the product is the one searching: `لم نجد نتائج لـ"قهوة"` reads more accurate than `لا توجد نتائج`.
- **Warmer/personal:** `ليس عندك رسائل بعد` or `لم ترِد عليك رسائل` feel closer to natural speech than `لا توجد رسائل بعد`.
- **`ما` as negation:** `ما وجدنا نتائج` is valid فصحى and feels natural. Use it as a locale/tone choice — `ما وجدنا` is fine فصحى, but `ما عندك` leans عامية, so reserve the `ما عندك`-type for products that intentionally use a lighter, Gulf-leaning register.

### Forms

- Labels: stable noun phrases like `البريد الإلكتروني`, `رقم الهاتف`, `تاريخ الميلاد`.
- Placeholders: examples, not instructions: `name@example.com`, `05XXXXXXXX`.
- Helper text: brief and specific: `8 أحرف على الأقل`.
- Do not hide the label inside the placeholder.
- Validation should say exactly what to fix: `أدخل بريدًا إلكترونيًا صحيحًا`.

### Notifications

Title and body must complement each other, not repeat.

- Title: `وصل الطلب`
- Body: `يمكنك تتبّع حالته من صفحة الطلبات.`

Keep titles under 40 characters when possible.

### Modals and Destructive Actions

Confirm the consequence, then give a clear action.

- Title: `حذف الحساب؟`
- Body: `سيُحذف حسابك وبياناتك نهائيًا. لا يمكن التراجع.`
- Primary: `حذف الحساب`
- Secondary: `إلغاء`

### Permission Prompts

Explain the benefit before asking for permission.

- Title: `فعّل الإشعارات`
- Body: `سننبهك عند تحديث حالة طلبك.`
- Primary: `تفعيل الإشعارات`
- Secondary: `ليس الآن`

---

## Full-Flow Examples

### Login Error

Bad: `حدث خطأ في عملية تسجيل الدخول. يرجى التأكد من البيانات الخاصة بك.`
Better: `تعذّر تسجيل الدخول. تحقق من بريدك الإلكتروني وكلمة المرور.`
Why: removes bureaucratic filler, names the failed action, and gives recovery.

### Payment Failure

Bad: `فشلت عملية الدفع الخاصة بك. يرجى المحاولة مرة أخرى لاحقًا.`
Better: `تعذّر الدفع. تحقق من البطاقة أو جرّب طريقة دفع أخرى.`
Why: concise, specific, and gives useful alternatives.

### Delete Account Modal

Bad: Title `هل أنت متأكد؟` Body `سيتم حذف الحساب الخاص بك بنجاح بعد الضغط على الزر.` Button `موافق`
Better: Title `حذف الحساب؟` Body `سيُحذف حسابك وبياناتك نهائيًا. لا يمكن التراجع.` Button `حذف الحساب`
Why: states the consequence and makes the destructive action explicit.

### Search Empty State

Bad: `لم يتم العثور على نتائج.`
Better: `لا توجد نتائج لـ"{query}". جرّب كلمة أخرى أو غيّر عوامل التصفية.`
Why: keeps the query visible and preserves `{query}` exactly.

### Subscription Cancellation

Bad: `لقد قمت بإلغاء الاشتراك بنجاح.`
Better: `أُلغِي الاشتراك. يمكنك استخدام الباقة حتى {date}.`
Why: removes filler and preserves useful entitlement context.

### Order Tracking Notification

Good: Title `طلبك في الطريق` Body `سيصل اليوم بين 4 و6 مساءً.`
Why: starts with user value and gives concrete timing.

---

## Voice and Tone

Voice stays consistent; tone changes by moment.

| Dimension | Spectrum |
|---|---|
| Register | فصحى رسمية ← فصحى مبسطة ← فصحى بلمسة عامية |
| Warmth | محايد ← ودود ← حميم |
| Authority | يرشد ← يقترح ← يرافق |
| Formality | مؤسسي ← مهني ← شخصي |

Tone by context:

- Error/failure: empathetic, specific, recovery-focused.
- Success/completion: brief, warm, restrained.
- Guidance: clear, confident, encouraging.
- Warning/destructive action: direct, calm, consequence-focused.
- Legal/privacy/payment: precise and slightly more formal.

### Dialect and Register

Colloquial words (`عشان`، `الحين`، `قدها`، `حنا`) are not errors in themselves. They sit at the `فصحى بلمسة عامية` end of the register spectrum above, so use them only when the product's voice deliberately lives there (a youthful or local brand), and use the فصحى equivalent otherwise (`عشان` → `لـ`/`حتى`، `الحين` → `الآن`).

When you flag a colloquial word, identify it simply as عامية. Name a specific region only when it is both accurate and changes the decision: `الحين` and `قدها` carry a clear Gulf/Saudi lean that affects audience fit, so noting it helps. But a pan-Arab word like `عشان` belongs to no single dialect, so calling it 'Saudi' is inaccurate. Frame any regional note as 'Gulf-leaning' or 'regional', not as belonging to one country.

---

## Terminology Consistency

Pick one term per concept and reuse it. If the product already has terminology, preserve it unless it is wrong or unclear.

| Concept | Recommended | Notes |
|---|---|---|
| Sign in | `تسجيل الدخول` | Existing account. |
| Sign up | `إنشاء حساب` or `التسجيل` | Choose one. |
| Log out | `تسجيل الخروج` | Common and clear. |
| Cart | `السلة` | E-commerce default. |
| Checkout | `إتمام الطلب` or `الدفع` | Depends on step. |
| Subscription | `الاشتراك` | The subscription itself. |
| Plan / tier | `الباقة` | Use `باقة` for a pricing tier/bundle. Avoid `الخطة` here — `خطة` means a course of action, so it's a calque for "plan." |
| Settings | `الإعدادات` | Stable noun. |
| Notifications | `الإشعارات` | Do not alternate with التنبيهات unless differentiated. |
| Privacy | `الخصوصية` | Legal/privacy surfaces. |
| Continue | `متابعة` or `تابع` | Match gender strategy. |
| Try again | `حاول مرة أخرى` | Errors. |

---

## Spelling and Formatting

Read `references/arabic-grammar-guide.md` for complete grammar and spelling guidance. Key rules:

- Use Arabic comma `،`, not English comma, inside Arabic sentences.
- Use `أو`, not `/`, for alternatives.
- No extra alif on present-tense verbs: `نرجو`, not `نرجوا`.
- Drop extra alif after tanween on hamza: `مساءً`, not `مساءًا`.
- Avoid diacritics unless needed for meaning.
- Distinguish taa marbuta `ة` from haa `ه`.
- Use punctuation sparingly; avoid `!!`, `...`, and decorative punctuation.
- Avoid the em dash (`—`) in Arabic copy; it is a Latin convention with no native place in Arabic. Use the Arabic comma `،`, a colon, parentheses, or split into two sentences.
- Name calques in Arabic: use `عرنجية` (or `ترجمة حرفية` / `نقل حرفي`). "Calque" is an internal English label only; never transliterate it as «كالك» or «كالق».

---

## When to Read References

- Read `references/anti-patterns.md` when auditing copy for عرنجي, literal translation, over-formality, verbosity, or stiff phrasing.
- Read `references/arabic-grammar-guide.md` when checking grammar, spelling, gender agreement, passive forms, اسم التفضيل, اسم المفعول, punctuation, or formatting.
- Read `references/arabic-huroof-reference.md` when choosing or reviewing prepositions, especially payment, price, location, destination, reporting, availability, linking accounts, and cause/purpose copy — and for verb–preposition government (which حرف a specific verb takes).

---

## Quick عرنجي Detector

Rewrite if the copy:

1. Uses `تم` + مصدر where a direct verb, passive, active نحن, or nominal sentence is better — unless it expresses genuine completion (`تمّ/اكتمل التحميل`).
2. Uses `قم بـ` or `القيام بـ`.
3. Uses `لقد قمت بـ`.
4. Uses `الخاص بك` instead of a possessive suffix.
5. Uses `من أجل` where `لـ` works.
6. Uses `يرجى` on routine instructions.
7. Adds `بنجاح` when success is already obvious.
8. Says `عملية` before ordinary actions.
9. Describes the UI interaction: `اضغط هنا`, `انقر على الزر`.
10. Uses `بشكل` + adjective as an English adverb calque.
11. Leads with existential `هناك`.
12. Uses `عندما` for conditional meaning instead of `إذا` or `إن`.
13. Forces English SVO structure where Arabic action-first copy is clearer.
14. Sounds like a literal translation when read aloud.

---

## Publishing Checklist

Before finalizing Arabic UX copy, verify:

1. It serves the user's immediate goal.
2. Every word earns its place.
3. It sounds natural in فصحى مبسطة.
4. The next step is clear.
5. The tone fits the moment.
6. Gender strategy is consistent.
7. Placeholders, tags, links, codes, and product names are preserved exactly.
8. Dynamic counts have correct Arabic plural handling.
9. Numerals, currency, dates, punctuation, and RTL mixed text follow product conventions.
10. It avoids the عرنجي patterns above unless there is a deliberate reason.

---

## Credits

Created by **Abad team (فريق أبـد)**, [abad.life](https://abad.life)

> لأن هناك أشياء صُنعت لأجل لحظة، وهناك أشياء تبقى للأبـد
