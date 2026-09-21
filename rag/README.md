# laya-ara-rag

Arabic short-list reranker — passage relevance and *k*≤12 ranking on [`laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual).

<p align="center">
  <img src="assets/logo.jpg" alt="laya-ara-rag" width="280">
</p>

**Mohammad Alkhenizan** · 21 September 2026 · [LinkedIn](https://www.linkedin.com/in/mohammad-alkhenizan-537623257)

[`Hugging Face`](https://huggingface.co/Wouze/laya-ara-rag) · [`GitHub`](https://github.com/ASNB-Smart-Solutions/laya-ara) · NLU: [`laya-ara`](https://huggingface.co/Wouze/laya-ara)

## Highlights vs `laya-multilingual`

Relative lift is *(fine-tune − stock) / stock*. Metric is top-1 among ≤12 candidates, not corpus nDCG@10.

| Arabic task | *n* | Base | **laya-ara-rag** | Relative lift |
|---|---:|---:|---:|---:|
| MIRACL-ar rerank (dev) | 2896 | 0.153 | **0.588** | **+284%** (3.8×) |
| Mr.TyDi-ar rerank | 2000 | 0.176 | **0.632** | **+259%** (3.6×) |
| MLQA-ar rerank | 2000 | 0.133 | **0.582** | **+338%** (4.4×) |
| SadeemQuestion rerank | 2089 | 0.168 | **0.871** | **+418%** (5.2×) |
| XPQA-ar rerank | 750 | 0.213 | **0.665** | **+212%** (3.1×) |
| In-domain pairwise relevance | 112 | 0.812 | **0.938** | **+16%** |

Mintaka entity ranking does not improve (0.403 predecessor vs 0.388). Full tables: [`RESULTS.md`](https://huggingface.co/Wouze/laya-ara-rag/blob/main/RESULTS.md). This card’s JSON: [`rag_all_benches.json`](https://huggingface.co/Wouze/laya-ara-rag/blob/main/results/rag_all_benches.json). All cards: [`all_cards.json`](https://huggingface.co/Wouze/laya-ara-rag/blob/main/results/all_cards.json).

## Abstract

**laya-ara-rag** is a fine-tune of [`convaiinnovations/laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual) (mmBERT-base with a Laya typed-decision head, ~322M) for Arabic pairwise relevance (`noul`) and listwise reranking (`choice`). It is not generative and not a first-stage retriever. Training uses official Laya RLCD on two RTX 3090 GPUs.

The mix continues from a MIRACL-ar Wikipedia specialist, then adds in-house Arabic retrieval logs plus a MIRACL-ar train replay and a small MASSIVE-ar cap. **XNLI is withheld.** Evaluation is top-1 among a shortlist of *k*≤12.

## Inference

`laya` is the [ConvAI Laya](https://pypi.org/project/laya/) runtime (`pip install laya==0.3.4`).

```bash
pip install "laya==0.3.4"
export USE_TF=0
export HF_TOKEN=hf_...   # while Wouze/laya-ara-rag is private
```

```python
import os
import laya

agent = laya.load("Wouze/laya-ara-rag", token=os.environ.get("HF_TOKEN"))
out = agent.predict(
    {"query": "ما حكم الوضوء قبل قراءة القرآن؟"},
    {
        "passage": {
            "type": "choice",
            "instructions": "Which passage is most relevant to the query?",
            "criteria": {
                "a": "الوضوء شرط للصلاة لا للقراءة عند جمهور الفقهاء.",
                "b": "زكاة الفطر تجب على كل مسلم قبل صلاة العيد.",
                "c": "صيام عاشوراء سنة مؤكدة عند الحنابلة.",
            },
        },
        "relevant": {
            "type": "noul",
            "instructions": "Is passage A relevant to the query?",
        },
    },
)
print(out["answers"])
```

The example passages are illustrative. Demo: [`examples/predict_rerank.py`](https://huggingface.co/Wouze/laya-ara-rag/blob/main/examples/predict_rerank.py). Scores: [`rag_all_benches.json`](https://huggingface.co/Wouze/laya-ara-rag/blob/main/results/rag_all_benches.json).

## Method

- **Base.** `laya-multilingual` (Apache-2.0). Init from the MIRACL-ar specialist, not from laya-ara.
- **Objective.** Official Laya RLCD, DDP, fp16. One epoch, 35,591 items.
- **Public mix.** MIRACL-ar train pairwise + listwise; MASSIVE-ar cap 2,000.
- **In-house mix.** Arabic retrieval logs (not redistributed): teacher-distilled pairs with a minimum score gap, listwise gold = teacher rank-1, sealed hold-out. See [`DATA.md`](https://huggingface.co/Wouze/laya-ara-rag/blob/main/DATA.md).
- **Protocol.** Frozen JSONL. Pairwise snippets ~800 characters; listwise ~400 so *k* = 12 fits `max_len` 1024.

## Public listwise rerank (k ≤ 12)

Chance ≈ 0.08–0.11. MIRACL-ar **train** is in the mix (dev is in-family). Other rows are transfer.

| Task | *n* | Kind | Base | laya-ara | **laya-ara-rag** | Δ vs base |
|---|---:|---|---:|---:|---:|---:|
| MIRACL-ar (dev) | 2896 | in-family | 0.153 | 0.210 | **0.588** | +284% |
| Mr.TyDi-ar | 2000 | transfer | 0.176 | 0.260 | **0.632** | +259% |
| SadeemQuestion | 2089 | transfer | 0.168 | 0.242 | **0.871** | +418% |
| MLQA-ar | 2000 | transfer | 0.133 | 0.214 | **0.582** | +338% |
| XPQA-ar | 750 | transfer | 0.213 | 0.281 | **0.665** | +212% |
| PublicHealthQA-ar | 86 | transfer | 0.116 | 0.244 | **0.488** | +321% |
| Mintaka-ar (entity) | 2203 | transfer | 0.285 | 0.311 | 0.388 | +36% |

Mintaka listwise favors the Wikipedia-only predecessor (0.403). PublicHealthQA *n* is small.

## Public pairwise relevance

One gold + one negative. Chance = 0.50.

| Task | *n* | Base | laya-ara | **laya-ara-rag** |
|---|---:|---:|---:|---:|
| MIRACL-ar (dev) | 5792 | 0.688 | 0.629 | **0.788** |
| Mr.TyDi-ar | 4000 | 0.755 | 0.740 | **0.834** |
| SadeemQuestion | 4178 | 0.837 | 0.919 | **0.941** |
| PublicHealthQA-ar | 172 | 0.791 | 0.773 | **0.866** |
| Mintaka-ar | 4406 | 0.537 | **0.616** | 0.513 |
| MLQA-ar | 4000 | 0.731 | **0.784** | 0.706 |
| XPQA-ar | 1500 | 0.623 | **0.697** | 0.615 |

Listwise transfer does not imply pairwise transfer. Entity and product pairwise still favor the NLU card.

## In-domain exam

Sealed hold-out on the in-house Arabic retrieval stack (queries and passages not in this repository).

| Exam | *n* | Base | **laya-ara-rag** | Δ vs base |
|---|---:|---:|---:|---:|
| Human pairwise | 112 | 0.812 | **0.938** | +16% |
| Teacher pairwise hold | 400 | 0.640 | **0.792** | +24% |
| Teacher listwise hold | 200 | 0.110 | **0.575** | +423% |

Teacher-hold is distillation agreement, not clicks. The 21-query human listwise set is too small to headline.

## Related models

| Model | Role |
|---|---|
| [`laya-ara`](https://huggingface.co/Wouze/laya-ara) | Arabic intent, NLI, OSACT-A |
| **laya-ara-rag** (this) | Arabic short-list relevance / rerank |

## Contact

Licensing, evaluation access, or collaboration: [Mohammad Alkhenizan on LinkedIn](https://www.linkedin.com/in/mohammad-alkhenizan-537623257).

## Limitations

Not a first-stage retriever and not official MIRACL nDCG@10. No span extraction or token NER. Mintaka / MLQA / XPQA **pairwise** can drop versus laya-ara.

```bibtex
@misc{alkhenizan2026layaararag,
  title        = {laya-ara-rag: Arabic short-list reranking with laya-multilingual},
  author       = {Alkhenizan, Mohammad},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/Wouze/laya-ara-rag}}
}
```
