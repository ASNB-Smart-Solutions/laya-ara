---
language:
  - ar
license: other
license_name: Research (XNLI CC BY-NC in the v48 mix)
license_link: NOTICE.md
base_model: convaiinnovations/laya-multilingual
tags:
  - arabic
  - laya
  - system-one
  - typed-decisions
  - massive
  - xnli
  - osact
  - rag
  - rerank
library_name: laya
pipeline_tag: text-classification
---

# Arabic Laya / System One (`laya-ar-v48`)

Fine-tune of [`convaiinnovations/laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual) (mmBERT-base + Laya head, ~322M) for **Arabic typed decisions**: `choice`, `score`, `noul`. Official Laya RLCD on 2×RTX 3090. Scored 21 Sep 2026.

**Not** TypeSafe Jev. **Not** a chat / generation model. **Not** a span-NER or span-QA head. **Not** a full-corpus MIRACL retriever.

v48 saw capped **XNLI-ar (CC BY-NC 4.0)** — treat these weights as **research / non-commercial**. Details in [`NOTICE.md`](NOTICE.md). Machine-readable numbers: [`results/v48_all_benches.json`](results/v48_all_benches.json).

Quote this number if you quote one: **MASSIVE-ar intent, 20 options, 0.386 → 0.816**. That is the Laya-card protocol (published stock ~0.38–0.40). Scenario 0.865 is an easier 18-way exam.

## Use

```bash
pip install laya
export USE_TF=0
```

```python
import laya
agent = laya.load("YOUR_USER/laya-arabic-system-one")
out = agent.predict(
    {"channel": "whatsapp", "message": "الحوالة ما وصلت، أبي استرجاع وإلا بنقلع"},
    {
        "queue": {
            "type": "choice",
            "instructions": "Which support queue?",
            "criteria": {
                "billing": "payments, refunds",
                "technical": "bugs, outages",
                "account": "login, KYC",
                "other": "none of the above",
            },
        },
        "refund": {"type": "noul", "instructions": "Does the user ask for a refund?"},
    },
)
```

Full demo: [`examples/predict_triage.py`](examples/predict_triage.py).

Same frozen JSONL for stock and v48. Stock is always `convaiinnovations/laya-multilingual`.

## Locked three (training mix)

| Task | n | Metric | Stock | v48 | Δ |
|---|---:|---|---:|---:|---:|
| MASSIVE-ar scenario (18-way, test) | 2974 | acc | 0.427 | **0.865** | +43.8 |
| XNLI-ar (test) | 5010 | acc | 0.686 | **0.723** | +3.7 |
| OSACT4-A offense (val) | 1000 | macro-F1 | 0.726 | **0.862** | +13.6 |

OSACT-A acc: 0.844 → 0.920. XNLI is mid — about the Laya-card stock (~0.73), not AraBERT-class (~0.80).

## MASSIVE-ar variants (same test utterances)

| Task | n | Stock | v48 | Δ |
|---|---:|---:|---:|---:|
| Intent, 20 options (card protocol) | 2974 | 0.386 | **0.816** | +43.0 |
| Hierarchical intent (k≥2) | 2694 | 0.536 | **0.893** | +35.7 |
| Scenario 18-way | 2974 | 0.427 | **0.865** | +43.8 |

Do not post 0.865 as “MASSIVE intent.”

## Translated popular Arabic NLU (zero-shot vs the mix)

Official labels. QA is **sentence selection**, not span EM/F1. Not token NER.

| Task | n | Metric | Stock | v48 | Δ |
|---|---:|---|---:|---:|---:|
| OSACT4-HS (hate noul) | 1000 | acc / F1 | **0.932 / 0.655** | 0.875 / 0.645 | −5.7 / −1.0 |
| AJGT sentiment | 360 | acc / F1 | **0.833 / 0.832** | 0.756 / 0.747 | −7.8 / −8.6 |
| LABR binary (drop 3★) | 2348 | acc / F1 | 0.759 / 0.758 | **0.766 / 0.764** | +0.7 / +0.6 |
| ASTD 4-way (hold 1500) | 1500 | acc / F1 | 0.295 / 0.286 | **0.326 / 0.297** | +3.1 / +1.1 |
| TyDiQA-ar sentence pick | 298 | acc / F1 | 0.359 / 0.155 | **0.413 / 0.170** | +5.4 / +1.5 |

AJGT and OSACT-HS: v48 is worse. Fine-tune did not make a general Arabic BERT. ASTD is below majority-class Objective (~0.65).

## Arabic RAG — all 7 tasks (not only the top 3)

Relevance / rerank. k≤12. Not generation. Not official MIRACL nDCG@10. Pairwise chance 0.50. Listwise chance ~0.083 (MIRACL 0.113).

| Task | Negatives | Pair n | Pair stock → v48 | Rank n | Rank stock → v48 |
|---|---|---:|---:|---:|---:|
| MIRACL-ar dev | human | 5792 | **0.688** → 0.629 | 2896 | 0.153 → **0.210** |
| Mr.TyDi-ar train 2k | BM25 | 4000 | **0.755** → 0.740 | 2000 | 0.176 → **0.260** |
| SadeemQuestion | random article | 4178 | 0.837 → **0.919** | 2089 | 0.168 → **0.242** |
| PublicHealthQA-ar | random FAQ | 172 | **0.791** → 0.773 | 86 | 0.116 → **0.244** |
| Mintaka-ar (entity) | random entity | 4406 | 0.537 → **0.616** | 2203 | 0.285 → **0.311** |
| MLQA ara-ara test 2k | random paragraph | 4000 | 0.731 → **0.784** | 2000 | 0.133 → **0.214** |
| XPQA ara-ara | random answer | 1500 | 0.623 → **0.697** | 750 | 0.213 → **0.281** |

v48 wins **7/7 listwise**. Pairwise wins the easy random-neg sets; stock wins MIRACL human hard-negs and Mr.TyDi BM25. PHQA rank n=86 is noisy.

## Product demo (WhatsApp triage)

v48 routes billing and refund on the Gulf example. **Urgency and churn were never in the mix** (0 score items). Do not ship this as a complete triage model.

## Not measured (on purpose)

- Token NER / BIO
- TyDiQA or ARCD span EM-F1
- Official MIRACL nDCG@10 over Arabic Wikipedia
- ALUE private tests
- AraBERT / MARBERT on these same Laya templates

## Training (v48)

- Recipe: official Laya RLCD (policy gradient + soft CE, group size 4), DDP 2×3090 fp16
- Mix: MASSIVE-ar train + OSACT4-A + capped XNLI-ar
- Hybrid temperatures after fit (`choice:11+` floor 3.75)
- Current scored dir on the train box: `artifacts/laya-ar-v48`

## How to upload these files to the Hub

See [`UPLOAD.md`](UPLOAD.md). Short form:

```bash
export HF_TOKEN=hf_...
python scripts/upload_to_hf.py \
  --ckpt /path/to/artifacts/laya-ar-v48 \
  --repo-id YOUR_USER/laya-arabic-system-one \
  --dry-run
python scripts/upload_to_hf.py \
  --ckpt /path/to/artifacts/laya-ar-v48 \
  --repo-id YOUR_USER/laya-arabic-system-one
```

Default create is **private**. `--public` only after you accept the NC note.

## Citation

```
@misc{laya-ar-v48,
  title  = {Arabic Laya System One (v48)},
  year   = {2026},
  note   = {Fine-tune of convaiinnovations/laya-multilingual. Research weights (XNLI CC BY-NC).}
}
```

Cite MASSIVE, XNLI, OSACT4, MIRACL, Mr.TyDi, MLQA, and the other eval sets if you report their numbers.
