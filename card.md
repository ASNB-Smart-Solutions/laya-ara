# laya-ara

Arabic NLU for typed decisions — intent, NLI, and short-list ranking on [`laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual).

<p align="center">
  <img src="assets/logo.jpg" alt="laya-ara" width="280">
</p>

**Mohammad Alkhenizan** · 21 September 2026 · [LinkedIn](https://www.linkedin.com/in/mohammad-alkhenizan-537623257)

[![downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fmodels%2FWouze%2Flaya-ara&query=%24.downloads&label=downloads%2030d&color=yellow)](https://huggingface.co/Wouze/laya-ara)

[`Hugging Face`](https://huggingface.co/Wouze/laya-ara) · [`GitHub`](https://github.com/ASNB-Smart-Solutions/laya-ara) · RAG sibling: [`laya-ara-rag`](https://huggingface.co/Wouze/laya-ara-rag)

## Highlights vs `laya-multilingual`

Relative lift is *(fine-tune − stock) / stock* on the same frozen Laya templates.

| Arabic task | *n* | Base | **laya-ara** | Relative lift |
|---|---:|---:|---:|---:|
| Intent, 20 options (MASSIVE ar-SA) | 2974 | 0.386 | **0.816** | **+111%** |
| Scenario, 18-way (MASSIVE ar-SA) | 2974 | 0.427 | **0.865** | **+103%** |
| Hierarchical intent | 2694 | 0.536 | **0.893** | **+67%** |
| Offensive language, macro-F1 (OSACT4-A) | 1000 | 0.726 | **0.862** | **+19%** |
| Natural language inference (XNLI-ar) | 5010 | 0.686 | **0.723** | +5% |

Full tables: [`RESULTS.md`](https://huggingface.co/Wouze/laya-ara/blob/main/RESULTS.md). This card’s JSON: [`nlu_benches.json`](https://huggingface.co/Wouze/laya-ara/blob/main/results/nlu_benches.json). All cards: [`all_cards.json`](https://huggingface.co/Wouze/laya-ara/blob/main/results/all_cards.json).

## Abstract

**laya-ara** is a fine-tune of [`convaiinnovations/laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual) (mmBERT-base with a Laya typed-decision head, ~322M) for Arabic *System One* inference: discrete `choice`, binary `noul`, and optional ordinal `score`. It is not a generative language model. Training uses official Laya RLCD on two RTX 3090 GPUs. The released mix is MASSIVE-ar, OSACT4-A, and a capped XNLI-ar sample. XNLI is CC BY-NC 4.0, so these weights are **research / non-commercial** ([`NOTICE.md`](https://huggingface.co/Wouze/laya-ara/blob/main/NOTICE.md)).

## Inference

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ASNB-Smart-Solutions/laya-ara/blob/master/examples/colab_nlu.ipynb)

`laya` is the [ConvAI Laya](https://pypi.org/project/laya/) runtime (`pip install laya==0.3.4`). The Hub **Use this model** snippet passes `trust_remote_code=True` and then calls `laya.load`. After loading, call `predict` (or `model.predict` if you used the Hub snippet). The snippet also prints this example.

```bash
pip install "laya==0.3.4"
export USE_TF=0
```

```python
import os
import laya

agent = laya.load("Wouze/laya-ara", token=os.environ.get("HF_TOKEN"))
out = agent.predict(
    {"message": "الحوالة ما وصلت، أبي استرجاع وإلا بنقلع"},
    {
        "queue": {
            "type": "choice",
            "instructions": "Support queue",
            "criteria": {
                "billing": "payments, refunds",
                "technical": "bugs, outages",
                "other": "none of the above",
            },
        },
        "refund": {"type": "noul", "instructions": "Asks for a refund?"},
    },
)
print(out["answers"])
```

Local weights: `laya.load("/path/to/artifacts/laya-ar-v48")`. Demo: [`examples/predict_triage.py`](https://huggingface.co/Wouze/laya-ara/blob/main/examples/predict_triage.py). This card’s scores: [`nlu_benches.json`](https://huggingface.co/Wouze/laya-ara/blob/main/results/nlu_benches.json).

## Method

- **Base.** `laya-multilingual` (Apache-2.0). English `convaiinnovations/laya` is a different checkpoint.
- **Objective.** Official Laya RLCD (policy gradient + soft cross-entropy, group size 4), DDP, fp16.
- **Mix.** MASSIVE-ar train, OSACT4 Subtask A, XNLI-ar cap. Hybrid temperature calibration (`choice:11+` floor 3.75).
- **Protocol.** Identical frozen JSONL for stock and fine-tune. Question answering is sentence selection, not span EM/F1. Retrieval transfer is top-1 among *k*≤12, not corpus nDCG@10.

## Classification

| Task | *n* | Base | laya-ara | Δ rel. |
|---|---:|---:|---:|---:|
| MASSIVE-ar intent (20 options) | 2974 | 0.386 | **0.816** | +111% |
| MASSIVE-ar scenario (18-way) | 2974 | 0.427 | **0.865** | +103% |
| MASSIVE-ar hierarchical intent | 2694 | 0.536 | **0.893** | +67% |
| XNLI-ar | 5010 | 0.686 | **0.723** | +5% |
| OSACT4-A (macro-F1) | 1000 | 0.726 | **0.862** | +19% |

Published stock MASSIVE-ar intent on the Laya harness is about 0.38–0.40. XNLI remains below typical AraBERT fine-tunes (~0.80). Zero-shot AJGT and OSACT-HS decrease relative to stock. TyDiQA-ar sentence selection is 0.359 → 0.413.

## Short-list reranking (this card)

No MIRACL train in this mix. Metric: top-1 among ≤12. The dedicated reranker is [`laya-ara-rag`](https://huggingface.co/Wouze/laya-ara-rag).

| Task | *n* | Base | laya-ara | Δ rel. |
|---|---:|---:|---:|---:|
| Mr.TyDi-ar | 2000 | 0.176 | **0.260** | +48% |
| SadeemQuestion | 2089 | 0.168 | **0.242** | +44% |
| MLQA-ar | 2000 | 0.133 | **0.214** | +61% |
| MIRACL-ar (dev) | 2896 | 0.153 | **0.210** | +37% |

All seven listwise files improve. Pairwise Wikipedia/BM25 relevance can still favor stock.

## Related models

| Model | Role |
|---|---|
| **laya-ara** (this) | Arabic intent, NLI, offensive-language A |
| [`laya-ara-rag`](https://huggingface.co/Wouze/laya-ara-rag) | Arabic short-list relevance / rerank |

## Contact

Licensing, evaluation access, or collaboration: [Mohammad Alkhenizan on LinkedIn](https://www.linkedin.com/in/mohammad-alkhenizan-537623257).

## Limitations

No token-level NER or span-extraction head. Offensive-language F1 is a research score, not a moderation guarantee. Diglossia is unmeasured beyond MASSIVE (ar-SA MSA) and OSACT tweets. Citations: [`citations.bib`](https://huggingface.co/Wouze/laya-ara/blob/main/citations.bib).

```bibtex
@misc{alkhenizan2026layaara,
  title        = {laya-ara: Arabic typed-decision fine-tuning of laya-multilingual},
  author       = {Alkhenizan, Mohammad},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/Wouze/laya-ara}}
}
```
