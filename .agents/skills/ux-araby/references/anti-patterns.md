# Arabic UX Anti-Patterns — كاشف العرنجي

This reference lists the most common Arabic UX writing anti-patterns. Use it as a checklist when reviewing any Arabic interface text.

> **Terminology:** "Calque" here is an internal English label for عرنجية. In any Arabic-facing copy or review note, write `عرنجية` (or `ترجمة حرفية` / `نقل حرفي`); never transliterate the English word as «كالك» or «كالق», since a transliterated loanword is itself عرنجية.

---

## Category 1: Calques (ترجمة حرفية)

These patterns enter Arabic UX text because writers translate English UI patterns word-for-word instead of reimagining them in Arabic.

### Pattern: "تم" + مصدر
**Severity:** High — this is the single most common عرنجي marker.
**Source:** English passive voice ("was saved", "has been sent")

The fix is NOT always المبني للمجهول — sometimes the passive sounds heavy too (especially with مشدّد verbs like سُجِّل). Pick the lightest alternative:

| ❌ Calque | ✅ Natural Arabic | Strategy |
|-----------|-------------------|----------|
| `تم حفظ التغييرات` | `حُفظت التغييرات` | Arabic passive — verb is short and light ✅ |
| `تم إرسال الرسالة` | `أرسلنا الرسالة` | Active with نحن — adds warmth |
| `تم تسجيل حسابك` | `سجّلناك` or `حسابك جاهز` | نحن active or nominal — سُجِّل is heavy |
| `تم تحديث بياناتك` | `حدّثنا بياناتك` or `بياناتك محدَّثة` | نحن active or nominal |
| `تم إلغاء الطلب` | `أُلغي طلبك` | Arabic passive — verb is light ✅ |
| `تم رفع البلاغ` | `وصلنا بلاغك` | Reimagine entirely |

**Weight test:** Read the مبني للمجهول out loud. If it flows (حُفظ، حُذف، أُلغي، أُرسل) → use it. If it's heavy (سُجِّل، اسْتُكْمِل، أُضيف) → switch to نحن active or nominal sentence.

### Pattern: "قم بـ" + مصدر
**Severity:** High
**Source:** English imperative ("do X", "proceed to X")

| ❌ Calque | ✅ Natural Arabic | Strategy |
|-----------|-------------------|----------|
| `قم بتسجيل الدخول` | `سجّل الدخول` | Direct imperative |
| `قم بتحديث التطبيق` | `حدّث التطبيق` | Direct imperative |
| `قم بالتحقق من بريدك` | `تحقق من بريدك` | Direct imperative |
| `قم بإنشاء كلمة مرور` | `أنشئ كلمة مرور` | Direct imperative |

### Pattern: "لقد قمت بـ"
**Severity:** Critical — triple filler
**Source:** English "You have done X"

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `لقد قمت بالتسجيل بنجاح` | `حسابك جاهز` or `سجّلناك` |
| `لقد قمت بإضافة المنتج` | `أُضيف المنتج` or `المنتج في سلتك` |
| `لقد قمت برفع بلاغ بنجاح` | `وصلنا بلاغك` |

### Pattern: "الخاص بك" instead of pronoun suffix
**Severity:** Medium
**Source:** English "your X" → "the X that belongs to you"

| ❌ Verbose | ✅ Natural Arabic |
|-----------|-------------------|
| `الحساب الخاص بك` | `حسابك` |
| `الطلب الخاص بك` | `طلبك` |
| `الإعدادات الخاصة بك` | `إعداداتك` |

### Pattern: "من أجل" where "لـ" works
**Severity:** Low-medium
**Source:** English "in order to"

| ❌ Verbose | ✅ Concise |
|-----------|----------|
| `من أجل إكمال التسجيل` | `لإكمال التسجيل` |
| `من أجل الاستمرار` | `للاستمرار` |
| `من أجل حفظ التغييرات` | `لحفظ التغييرات` |

---

## Category 2: Over-Formality (مبالغة في الرسمية)

These patterns make Arabic UI text feel like a government form rather than a helpful interface.

### Pattern: Constant "يرجى"
**When it's OK:** Error messages, sensitive actions, situations needing genuine politeness.
**When it's عرنجي:** Every single instruction.

| Context | ❌ Over-formal | ✅ Natural |
|---------|---------------|-----------|
| Form field | `يرجى إدخال البريد الإلكتروني` | `أدخل بريدك الإلكتروني` |
| Button prompt | `يرجى الضغط على زر الإرسال` | `أرسل` |
| Error (OK here) | — | `يرجى التحقق من كلمة المرور` ✅ |
| Deletion warning (OK) | — | `يرجى التأكد قبل الحذف` ✅ |

### Pattern: "بنجاح" on every success
**Severity:** Low — but adds up across the product.

If the success message appeared, the user already knows it succeeded. "بنجاح" is almost always filler.

| ❌ Redundant | ✅ Clean |
|-------------|---------|
| `تم الحفظ بنجاح` | `حُفظت التغييرات` (passive — light verb) |
| `تم الإرسال بنجاح` | `أرسلنا الرسالة` (نحن active) |
| `تم التسجيل بنجاح` | `حسابك جاهز` (nominal — سُجِّل is heavy) |

### Pattern: "عملية" before actions
Adding "عملية" (process/operation) before a verb is bureaucratic filler.

| ❌ Bureaucratic | ✅ Direct |
|----------------|----------|
| `عملية الدفع` | `الدفع` |
| `إتمام عملية الشراء` | `إتمام الشراء` |
| `بدء عملية التسجيل` | `بدء التسجيل` |

---

## Category 3: Verbosity (إسهاب)

### Pattern: Telling the user what they just did
The UI already shows context. Don't narrate it.

| ❌ Narrating | ✅ Useful |
|-------------|---------|
| `أنت الآن في صفحة الإعدادات` | `الإعدادات` (as heading) |
| `هذه صفحة تفاصيل الطلب` | `تفاصيل الطلب` |
| `فيما يلي قائمة بطلباتك السابقة` | `الطلبات السابقة` |

### Pattern: Describing the UI interaction
Don't tell users to "click" or "press" — they know how buttons work.

| ❌ Describing interaction | ✅ Naming action |
|--------------------------|-----------------|
| `اضغط هنا لتسجيل الدخول` | `تسجيل الدخول` |
| `انقر على الزر أدناه لإرسال` | `إرسال` |
| `اضغط هنا لعرض التفاصيل` | `عرض التفاصيل` |

### Pattern: Double-stating in title + body
Notifications and dialogs should not repeat the same information in the title and the body text.

| ❌ Repetitive | ✅ Complementary |
|-------------|-----------------|
| Title: `حُذف الملف` Body: `تم حذف ملفك` | Title: `حُذف الملف` Body: `يمكنك استعادته خلال 30 يومًا.` |
| Title: `اكتمل الطلب` Body: `طلبك مكتمل الآن` | Title: `اكتمل الطلب` Body: `سيصلك إشعار عند الشحن.` |

---

## Category 4: Ambiguity (غموض)

### Pattern: Vague button labels

| ❌ Vague | ✅ Specific |
|---------|----------|
| `تأكيد` | `تأكيد الحجز` |
| `إرسال` | `إرسال الطلب` |
| `موافق` | `الموافقة على الشروط` |
| `التالي` (sometimes OK) | `الانتقال للدفع` (when context matters) |

### Pattern: Vague error messages

| ❌ Vague | ✅ Specific |
|---------|----------|
| `حدث خطأ` | `تعذّر الحفظ. تحقق من اتصالك.` |
| `خطأ في الإدخال` | `البريد الإلكتروني غير صحيح` |
| `العملية غير متاحة` | `الخدمة متوقفة حاليًا. حاول بعد ساعة.` |

---

## Category 5: Semantic Calques (تفرنج المعاني)

These patterns import English word meanings into Arabic, overriding the natural Arabic term. Identified by أحمد الغامدي in العرنجية as among the subtlest and most pervasive forms of تفرنج.

### Pattern: "شخص" overuse
**Severity:** Medium
**Source:** English "person" used generically where Arabic uses مَن or specific nouns.

Arabic has مَن for "whoever/the one who" and rarely needs the generic شخص in UX copy.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `أي شخص يمكنه التسجيل` | `يمكن لأي أحد التسجيل` or `يمكن لكل راغبٍ التسجيل` |
| `الشخص المسؤول` | `المسؤول` |
| `هو الشخص الذي يتابع طلبك` | `هو من يتابع طلبك` |

### Pattern: "هناك" existential
**Severity:** Medium
**Source:** English "there is / there are" — Arabic rarely needs an existential opener.

Arabic front-loads the prepositional phrase or uses a verbless sentence. Leading with هناك is almost always an English calque.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `هناك ٣ عناصر في سلتك` | `في سلتك ٣ عناصر` |
| `هناك خطأ في البيانات` | `في البيانات خطأ` or `البيانات فيها خطأ` |
| `لا يوجد هناك رسائل جديدة` | `لا رسائل جديدة` |
| `هناك تحديث متاح` | `تحديث متاح` or `يتوفر تحديث` |

### Pattern: "فكرة" semantic bloat
**Severity:** Low
**Source:** English "idea" covers a wide range; Arabic has distinct words for each sense.

In UX, this mostly matters in helper text and onboarding copy where فكرة is used loosely.

| Context | ❌ Generic فكرة | ✅ Precise Arabic |
|---------|----------------|------------------|
| Opinion | `فكرة جيدة` | `رأي صائب` |
| Concept | `فكرة التطبيق` | `مفهوم التطبيق` or `الفكرة من التطبيق` |
| Suggestion | `عندك فكرة؟` | `عندك اقتراح؟` or `عندك مقترح؟` |

### Pattern: "بسيط" for سهل
**Severity:** Low
**Source:** Arabic "بسيط" means واسع/ممتد. "Simple/easy" meaning is from English "simple."

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `خطوات بسيطة` | `خطوات سهلة` أو `خطوات يسيرة` |
| `إعداد بسيط` | `إعداد سهل` |

### Pattern: "يشير إلى" for indicates
**Severity:** Medium
**Source:** English "indicates" — Arabic has يدل على / يعني.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `النجمة تشير إلى أن الحقل مطلوب` | `النجمة تعني أن الحقل مطلوب` |
| `اللون الأحمر يشير إلى وجود خطأ` | `اللون الأحمر يدل على خطأ` |

### Pattern: "تحت + اسم" for statuses
**Severity:** Medium
**Source:** English "under review" / "under maintenance" — Arabic uses "قيد."

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `تحت المراجعة` | `قيد المراجعة` |
| `تحت الصيانة` | `صيانة جارية` أو `الخدمة متوقفة للصيانة` |
| `تحت التنفيذ` | `قيد التنفيذ` |

### Pattern: "يدعم" for supports/compatible
**Severity:** Low
**Source:** English "supports" — Arabic "دعم" originally means physical propping.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `يدعم iOS 16 وأحدث` | `يعمل على iOS 16 وأحدث` أو `متوافق مع iOS 16` |
| `ندعم الدفع بالبطاقة` | `الدفع بالبطاقة متوفر` |

### Pattern: "نأسف" in error messages
**Severity:** Medium
**Source:** English "We're sorry" — Arabic الأسف = الحزن, not الاعتذار.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `نأسف، حدث خطأ` | `عذرًا، حدث خطأ` |
| `نأسف لعدم توفر الخدمة` | `الخدمة غير متوفرة حاليًا` |

### Pattern: "بناءً على" for based on
**Severity:** Low
**Source:** English "based on" — literal translation.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `بناءً على تفضيلاتك` | `وفق تفضيلاتك` أو `حسب تفضيلاتك` |
| `بناءً على موقعك` | `حسب موقعك` |

### Pattern: "استثنائي" for exceptional
**Severity:** Low
**Source:** English "exceptional" — Arabic has فريد، نادر، لا مثيل له.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `عرض استثنائي` | `عرض فريد` أو `عرض لا يُفوّت` |
| `أداء استثنائي` | `أداء فريد` |

### Pattern: "ذات صلة" for relevant
**Severity:** Low
**Source:** English "relevant."

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `نتائج ذات صلة` | `نتائج مناسبة` أو `نتائج ملائمة` |
| `محتوى ذو صلة` | `محتوى قريب من الموضوع` |

### Pattern: "موضوعي" for objective
**Severity:** Low
**Source:** English "objective."

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `تقييم موضوعي` | `تقييم عادل` أو `تقييم منصف` |

### Pattern: "جهود" for efforts
**Severity:** Low
**Source:** English "efforts" — Arabic says سعي، عمل.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `بفضل جهودكم` | `بفضل عملكم` أو `بفضل سعيكم` |

### Pattern: "فقدان" for loss
**Severity:** Low
**Source:** English "loss" — Arabic "ضياع" is more natural for data.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `فقدان البيانات` | `ضياع البيانات` |
| `لتجنب فقدان التقدم` | `لئلا يضيع تقدمك` |

### Pattern: "حلم / يحلم بـ" for aspiration
**Severity:** Low
**Source:** English "dream of" — Arabic حلم = ما يُرى في المنام, not aspirations.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `حقق حلمك` | `حقق طموحك` |
| `نساعدك تحقق أحلامك` | `نساعدك تبلغ ما تصبو إليه` |

### Pattern: "حقل" for form field
**Severity:** Low
**Source:** English "field" — Arabic "حقل" = أرض زراعية.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `حقل الاسم` | `خانة الاسم` |
| `هذا الحقل مطلوب` | `هذه الخانة مطلوبة` |

### Pattern: "يستغرق" for takes time
**Severity:** Low
**Source:** English "takes (time)" — Arabic has يحتاج / يطول.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `يستغرق ٥ دقائق` | `يحتاج ٥ دقائق` |
| `يستغرق وقتًا طويلاً` | `يطول` أو `يحتاج وقتًا` |

### Pattern: "انتقادات" for criticisms/feedback
**Severity:** Low
**Source:** English "criticisms" — Arabic "ملاحظات" is softer and more precise in UX.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `انتقادات المستخدمين` | `ملاحظات المستخدمين` |

### Pattern: "إيجابي / سلبي" overuse
**Severity:** Low
**Source:** English "positive/negative" — Arabic has context-specific alternatives.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `تجربة إيجابية` | `تجربة حسنة` أو `تجربة طيبة` |
| `تعليق سلبي` | `تعليق سيئ` أو `ملاحظة` |

### Pattern: "مبرر" for justification
**Severity:** Low
**Source:** English "justification" — Arabic has سبب / عذر.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `بدون مبرر` | `بلا سبب` |

### Pattern: "تغطية" for network coverage
**Severity:** Low
**Source:** English "coverage" — Arabic "نطاق" is more precise for networks.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `تغطية الشبكة` | `نطاق الشبكة` |
| `خارج التغطية` | `خارج النطاق` |

---

## Category 6: Structural Calques (تفرنج التراكيب)

These patterns import English sentence structures into Arabic. The العرنجية calls this the most dangerous category because the words look Arabic but the skeleton is English.

### Pattern: "بشكل" + adjective (adverb calque)
**Severity:** High — extremely common in Arabic UX.
**Source:** English adverbs ("-ly") → Arabic has no equivalent suffix, so writers calque with بشكل + adjective.

Arabic uses the مصدر (verbal noun), the حال (adverbial accusative), or a direct adverb instead.

| ❌ Calque | ✅ Natural Arabic | Strategy |
|-----------|-------------------|----------|
| `يعمل بشكل صحيح` | `يعمل صحيحًا` or `يعمل كما ينبغي` | حال or idiomatic |
| `اكتمل بشكل ناجح` | `اكتمل` | Drop — اكتمل already implies success (and `بنجاح` is filler) |
| `يعمل بشكل دائم` | `يعمل دائمًا` | Direct adverb |
| `تمت المعالجة بشكل آلي` | `عولجت آليًا` | حال |

### Pattern: "عندما" as conditional (instead of "إذا")
**Severity:** Medium
**Source:** English "when" covers both temporal and conditional meanings. Arabic distinguishes them: عندما = temporal ("when it happened"), إذا = conditional ("if/when you want to").

In UX microcopy, most "when" instances are conditional — use إذا.

| ❌ Calque | ✅ Natural Arabic | Why |
|-----------|-------------------|-----|
| `عندما تريد الاستمرار، اضغط التالي` | `إذا أردت الاستمرار، اضغط التالي` | Conditional, not temporal |
| `عندما يكتمل التحميل` (OK) | `عندما يكتمل التحميل` ✅ | Genuinely temporal — this is fine |
| `عندما تواجه مشكلة، تواصل معنا` | `إن واجهت مشكلة، تواصل معنا` | Conditional |

### Pattern: "الآخرين" overuse
**Severity:** Low-medium
**Source:** English "others / other people" — Arabic uses الناس or specific nouns.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `سيراه الآخرون` | `سيراه الناس` or `سيراه المستخدمون` |
| `شاركه مع الآخرين` | `شاركه مع غيرك` or `شاركه` |

### Pattern: SVO word order forcing
**Severity:** High — affects the entire feel of the product.
**Source:** English requires Subject-Verb-Object. Arabic's natural order is VSO (Verb-Subject-Object).

UX copy that leads with the subject instead of the verb sounds translated.

| ❌ SVO (English order) | ✅ VSO (Arabic order) |
|------------------------|----------------------|
| `أنت الآن مسجّل` | `سُجّلت` or `اكتمل تسجيلك` |
| `النظام سيرسل لك إشعارًا` | `سيصلك إشعار` |
| `المستخدم يمكنه التحديث` | `يمكنك التحديث` |
| `هذا الخيار يتيح لك الوصول` | `يتيح لك هذا الخيار الوصول` |

### Pattern: Phrasal verb calques (أفعال مركبة)
**Severity:** Medium
**Source:** English phrasal verbs (turn away, find out, come up with) translated word-by-word into Arabic.

Arabic almost always has a single verb that carries the full meaning.

| ❌ Phrasal calque | ✅ Single Arabic verb |
|-------------------|---------------------|
| `أدار وجهه بعيدًا` (turned away) | `أعرض` |
| `أخفى مشاعره` (hid his feelings) | `كظم غيظه` / `تجلّد` |
| `جاء بفكرة` (came up with) | `اقترح` / `ابتكر` |
| `قام بالبحث عن` (looked for) | `بحث عن` |

### Pattern: "يمكنك" overuse
**Severity:** Medium
**Source:** English "You can..." to start every sentence. Arabic uses the direct imperative.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `يمكنك الآن تسجيل الدخول` | `سجّل الدخول` |
| `يمكنك تغيير كلمة المرور من الإعدادات` | `غيّر كلمة المرور من الإعدادات` |

### Pattern: "تأكد من" before instructions
**Severity:** Medium
**Source:** English "Make sure..." — filler before the actual instruction.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `تأكد من إدخال البريد الصحيح` | `أدخل البريد الصحيح` |
| `تأكد من اتصالك بالإنترنت` | `تحقق من اتصالك بالإنترنت` |

### Pattern: "لديك" to start notifications
**Severity:** Medium
**Source:** English "You have..." — Arabic front-loads the content.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `لديك رسالة جديدة` | `رسالة جديدة` أو `وصلتك رسالة` |
| `لديك ٣ إشعارات` | `٣ إشعارات` |
| `لديك ٣ محاولات متبقية` | `٣ محاولات متبقية` |

### Pattern: "من خلال" instead of "عبر"
**Severity:** Low
**Source:** English "through" — unnecessarily long.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `سجّل من خلال Google` | `سجّل عبر Google` أو `سجّل بـ Google` |
| `تواصل معنا من خلال التطبيق` | `تواصل معنا عبر التطبيق` |

### Pattern: "في حالة" instead of "إن"
**Severity:** Medium
**Source:** English "In case of..." — Arabic uses إن / إذا directly.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `في حالة وجود مشكلة، تواصل معنا` | `إن واجهت مشكلة، تواصل معنا` |
| `في حالة نسيان كلمة المرور` | `إن نسيت كلمة المرور` |

### Pattern: "يسمح لك بـ" / "يتيح لك"
**Severity:** Medium
**Source:** English "allows you to" / "enables you to" — Arabic just commands directly.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `يسمح لك التطبيق بمشاركة الصور` | `شارك صورك` |
| `هذه الميزة تتيح لك التحكم` | `تحكّم في إعداداتك` |

### Pattern: "نهاية" for consequence (عاقبة)
**Severity:** Low
**Source:** English "end" covers both ending and consequence. Arabic distinguishes them.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `نهاية الاشتراك` (if meaning consequence) | `عاقبة ذلك` أو `مآل الاشتراك` |
| `نهاية` for literal ending is fine | `نهاية الفترة التجريبية` ✅ |

### Pattern: "أي" as filler
**Severity:** Low
**Source:** English "any" used as padding.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `أي شخص يمكنه التسجيل` | `يمكن لكل أحد التسجيل` |
| `في أي وقت` | `متى شئت` أو `وقتما شئت` |

### Pattern: "بعبارة أخرى"
**Severity:** Low
**Source:** English "in other words" — Arabic has shorter equivalents.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `بعبارة أخرى` | `أي` أو `يعني` |

### Pattern: "يعاني من" for problems
**Severity:** Low
**Source:** English "suffers from" — Arabic "يواجه" is more neutral in UX.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `يعاني من مشكلة في الاتصال` | `يواجه مشكلة في الاتصال` |
| `التطبيق يعاني من بطء` | `التطبيق بطيء` |

### Pattern: "تنعكس على"
**Severity:** Low
**Source:** English "reflects on" — Arabic "تؤثر في" is more direct.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `إعداداتك تنعكس على تجربتك` | `إعداداتك تؤثر في تجربتك` |

### Pattern: "اعتاد على"
**Severity:** Low
**Source:** English "used to" / "accustomed to" — Arabic has ألِف / تعوّد.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `إذا اعتدت على الواجهة القديمة` | `إذا ألفت الواجهة القديمة` |

### Pattern: "الانطباع الأول"
**Severity:** Low
**Source:** English "first impression" — reformulate the sentence.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `اترك انطباعًا أوليًا جيدًا` | `ابدأ بداية حسنة` |

### Pattern: "متواضع" for modest/limited
**Severity:** Low
**Source:** English "humble/modest" — Arabic "متواضع" means عكس المتكبر, not القليل.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `ميزانية متواضعة` | `ميزانية محدودة` |
| `خيارات متواضعة` | `خيارات يسيرة` |

### Pattern: "كم هو جميل" exclamative calque
**Severity:** Medium
**Source:** English "how + adjective!" exclamation. Arabic has a dedicated exclamative form: ما أفعله.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `كم هو جميل!` | `ما أجمله!` |
| `كم هي سهلة!` | `ما أسهلها!` |

### Pattern: "سوية" for "together"
**Severity:** Low-medium
**Source:** Colloquial/translated "together." Classical Arabic uses معًا; سوية here is non-standard.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `لنبدأ سوية` | `لنبدأ معًا` |
| `أنجزناه سوية` | `أنجزناه معًا` |

---

## Category 7: UX-Specific Calques (تفرنج واجهات المستخدم)

These patterns are specific to digital products and apps. They don't appear in الغامدي's العرنجية (which focuses on literary/academic Arabic) but follow the same principle: English structure dressed in Arabic words.

### Pattern: "نحن هنا لمساعدتك"
**Severity:** Medium
**Source:** English "We're here to help"

Filler sentence that takes space without helping. Replace with the actual help.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `نحن هنا لمساعدتك` | `كيف نساعدك؟` |
| `فريقنا هنا دائمًا لمساعدتك` | `تواصل معنا في أي وقت` |

### Pattern: "احصل على" overuse
**Severity:** Medium
**Source:** English "Get" used for everything — get a discount, get started, get access.

Arabic has more precise verbs for each context.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `احصل على خصم` | `لك خصم` أو `استفد من خصم` |
| `احصل على التطبيق` | `حمّل التطبيق` |
| `احصل على حسابك المجاني` | `أنشئ حسابك مجانًا` |

### Pattern: "بكل سهولة"
**Severity:** Low-medium
**Source:** English "with ease" / "easily" — marketing filler.

If the product is truly easy, the user will feel it. Saying it adds nothing.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `أنشئ حسابك بكل سهولة` | `أنشئ حسابك` |
| `تسوّق بكل سهولة` | `تسوّق` |
| `أدِر مشاريعك بكل سهولة وسرعة` | `أدِر مشاريعك` |

### Pattern: "في الوقت الحقيقي"
**Severity:** Medium
**Source:** English "in real time" / "real-time" — literal translation.

| ❌ Calque | ✅ Natural Arabic |
|-----------|-------------------|
| `تحديثات في الوقت الحقيقي` | `تحديثات فورية` أو `تحديثات مباشرة` |
| `تتبّع في الوقت الحقيقي` | `تتبّع لحظي` أو `تتبّع مباشر` |

### Pattern: "افتراضي" for both default and virtual
**Severity:** High — creates real ambiguity.
**Source:** English "default" and "virtual" both translated as "افتراضي."

The two meanings are unrelated. Using one word for both confuses users.

| Context | ❌ Ambiguous | ✅ Clear |
|---------|-------------|---------|
| Default setting | `الإعداد الافتراضي` | `الإعداد التلقائي` |
| Virtual meeting | `اجتماع افتراضي` | `اجتماع افتراضي` (مقبول هنا، المعنى واضح من السياق) |
| Default value | `القيمة الافتراضية` | `القيمة التلقائية` |
| Virtual reality | `الواقع الافتراضي` | `الواقع الافتراضي` (مصطلح مستقر) |

**القاعدة:** إذا كان المعنى "default" → استخدم "تلقائي." إذا كان المعنى "virtual" → "افتراضي" مقبول.

---

## Common Classical Slips (from قل ولا تقل)

Internal-Arabic usage points, not English calques. Only the first is a clear error to fix on sight; the rest are classically preferred but accepted in modern MSA — note them, don't auto-correct. Drawn from مصطفى جواد، *قل ولا تقل*.

**Clear error — fix it:**

| ❌ Wrong | ✅ Correct | Why |
|----------|-----------|-----|
| `سوف لن أفعل` · `سوف لا أفعل` | `لن أفعل` · `لا أفعل` | لن/لا already negate the future; سوف is redundant here. |

**Classically preferred, but contested today — use judgment:**

| Form | Classically preferred | Note |
|------|----------------------|------|
| `سبق وقلنا` | `سبق أن قلنا` | The intrusive واو is criticized by editors; «سبق أن» is the safe form, though «سبق و» is common. |
| `هل … أم` | `أ … أم` | With the balancing أم, classical Arabic opens with the hamza; «هل…أم» is widespread and accepted today. |
| `لا زال` | `ما زال` / `لا يزال` | Classically «لا زال» (past) is a du'a — «may it not cease» — while «ما زال»/«لا يزال» state the ongoing fact (this is the لا الدعائية). In modern MSA «لا زال» is widely accepted; **don't flag it as an error.** |

---

## Guardrail: don't over-correct toward classical purism

Prescriptive manuals (like قل ولا تقل) are excellent for verb government and translated structures, but **dangerous for word choice** — they reject vocabulary that has since become standard, natural فصحى. Do **not** "fix" the following; they are correct and natural in product copy today, and replacing them produces stiff, archaic text that violates فصحى مبسطة:

`جاهز` · `صمود` · `روتين` · `دكتاتور` · `أرستقراطي` · `مباشرة` · `على الأقل` · `تأكّد من` · `حاز على` · `يهدف إلى` · `تعرّف على` · `أكّد على`

Test every prescriptive ruling against one question: *would an educated Arabic speaker say this in a product context today?* If the "correct" form fails that test, keep the natural one.

---

## The Full عرنجي Checklist

Run through these questions on every piece of Arabic microcopy:

| # | Check | If yes → |
|---|-------|----------|
| 1 | Does it contain `تم` + مصدر? | Use Arabic passive or active verb |
| 2 | Does it contain `قم بـ`? | Use direct imperative |
| 3 | Does it contain `لقد قمت بـ`? | Rewrite completely |
| 4 | Does it use `الخاص بك`? | Use possessive pronoun suffix |
| 5 | Does it use `من أجل` where `لـ` works? | Shorten |
| 6 | Does it use `يرجى` outside error/sensitive contexts? | Drop it |
| 7 | Does it say `بنجاح`? | Probably remove it |
| 8 | Does it say `عملية` before an action? | Drop `عملية` |
| 9 | Does it narrate what the user can already see? | Remove the narration |
| 10 | Does it describe the interaction (اضغط هنا)? | Name the action instead |
| 11 | Does it repeat the title in the body text? | Make body add new info |
| 12 | Does it use `بشكل` + adjective as an adverb? | Use مصدر or حال |
| 13 | Does it lead with `هناك` existentially? | Front-load the prepositional phrase |
| 14 | Does it use `عندما` for a conditional (not temporal) meaning? | Use إذا or إن |
| 15 | Does it overuse `شخص` where مَن or a specific noun fits? | Replace |
| 16 | Does it force SVO order where VSO is more natural? | Lead with the verb |
| 17 | Does it say `نحن هنا لمساعدتك` or similar filler? | Replace with the actual help |
| 18 | Does it overuse `احصل على`? | Use a precise verb: حمّل، استفد، أنشئ |
| 19 | Does it say `بكل سهولة` or `بكل بساطة`? | Drop it — if it's easy the user will feel it |
| 20 | Does it say `في الوقت الحقيقي`? | Use فورًا or مباشرةً or لحظي |
| 21 | Does it use `افتراضي` for "default"? | Use تلقائي — save افتراضي for "virtual" |
| 22 | Would you say this to a friend out loud? | If no → rewrite |
