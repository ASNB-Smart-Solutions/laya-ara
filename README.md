# laya-ara

Arabic typed-decision fine-tune of `laya-multilingual` (MASSIVE-ar, XNLI-ar, OSACT4-A).

<p align="center">
  <img src="assets/logo.jpg" alt="laya-ara mark" width="280">
</p>

**Mohammad Alkhenizan** · 21 September 2026

## Abstract

We release **laya-ara**, a fine-tune of [`convaiinnovations/laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual) (mmBERT-base with a Laya typed-decision head, ~322M) for Arabic *System One* inference: discrete `choice`, binary `noul`, and optional ordinal `score`. The model is not generative. Training uses official Laya RLCD on two RTX 3090 GPUs. The released weights correspond to the v48 mix (MASSIVE-ar, OSACT4-A, and a capped XNLI-ar sample). Because XNLI is CC BY-NC 4.0, these weights are **research / non-commercial** ([`NOTICE.md`](NOTICE.md)).

## Results

On a frozen evaluation protocol, 20-option MASSIVE-ar intent accuracy rises from 0.386 (stock) to **0.816**. 18-way scenario classification reaches 0.865; that is a different task and should not be reported as intent. XNLI-ar is 0.723 (stock 0.686). OSACT4-A macro-F1 is 0.862 (stock 0.726). Sentiment and hate-speech *transfer* from this mix is weak or negative. Short-list passage reranking (top-1 among *k*≤12) improves on seven Arabic sets; this is not corpus-level nDCG@10.

## Inference

`laya` is the [ConvAI Laya](https://pypi.org/project/laya/) runtime (`pip install laya==0.3.4`). It is a typed-decision engine, not Transformers `AutoModel`. `laya.load` accepts a Hub id or a local directory that contains `model.safetensors`, `rl_agent_config.json`, `encoder/`, and `tokenizer/`. The Hub repo is **private**: pass a write/read token or `huggingface-cli login`.

```bash
pip install "laya==0.3.4"
export USE_TF=0          # otherwise import can hang on a TensorFlow probe
export HF_TOKEN=hf_...   # required while Wouze/laya-ara is private
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

Local weights: `laya.load("/path/to/artifacts/laya-ar-v48")`. Longer demo: [`examples/predict_triage.py`](examples/predict_triage.py). Scores: [`results/v48_all_benches.json`](results/v48_all_benches.json). Follow-on mixes: [`FINDINGS.md`](FINDINGS.md).

## Method

- **Base.** `laya-multilingual` (Apache-2.0). English `convaiinnovations/laya` is a different checkpoint.
- **Objective.** Official Laya RLCD (policy gradient + soft cross-entropy, group size 4), DDP, fp16.
- **Mix (released card).** MASSIVE-ar train questions, OSACT4 Subtask A, XNLI-ar cap. Hybrid temperature calibration (`choice:11+` floor 3.75).
- **Protocol.** Identical frozen JSONL for stock and fine-tune. No generation. Question answering is sentence selection, not span EM/F1. Retrieval exams are pairwise relevance or listwise choice with *k*≤12.

## In-domain classification

| Task | *n* | Stock | laya-ara |
|---|---:|---:|---:|
| MASSIVE-ar intent (20 options) | 2974 | 0.386 | **0.816** |
| MASSIVE-ar scenario (18-way) | 2974 | 0.427 | **0.865** |
| MASSIVE-ar hierarchical intent | 2694 | 0.536 | **0.893** |
| XNLI-ar | 5010 | 0.686 | **0.723** |
| OSACT4-A (macro-F1) | 1000 | 0.726 | **0.862** |

Published stock MASSIVE-ar intent on the Laya harness is about 0.38–0.40. XNLI remains below typical AraBERT fine-tunes (~0.80).

Zero-shot transfer on the same card: AJGT and OSACT-HS **decrease** relative to stock. TyDiQA-ar sentence selection is 0.359 → 0.413.

## Short-list reranking

The released mix does **not** include MIRACL train. Metric: top-1 among ≤12 candidates.

| Task | *n* | Stock | laya-ara |
|---|---:|---:|---:|
| Mr.TyDi-ar | 2000 | 0.176 | **0.260** |
| SadeemQuestion | 2089 | 0.168 | **0.242** |
| MLQA-ar | 2000 | 0.133 | **0.214** |
| MIRACL-ar (dev) | 2896 | 0.153 | **0.210** |

All seven listwise files improve. Pairwise noul on human/BM25 Wikipedia negatives still favours stock.

## Follow-on checkpoints

Subsequent one-epoch specialists do not dominate the released card on MASSIVE / XNLI / OSACT-A.

| Checkpoint | Training distribution | Principal result | Scope |
|---|---|---|---|
| quote (no XNLI) | MASSIVE, OSACT-A/HS, AJGT, LABR, ASTD remainder | AJGT 0.875; LABR 0.834 | In-domain fine-tune. MASSIVE falls to 0.822. ASTD accuracy 0.694 vs macro-F1 0.404 |
| rag-ft (no XNLI) | MIRACL-ar train + 4k MASSIVE | MIRACL rerank 0.153 → 0.536 | Still *k*≤12. Not first-stage retrieval |
| triage | 1.2k authored Gulf lines | Smoke churn 0.03 → 0.91 | Synthetic labels. Urgency remains weak |

## Limitations

The model has no token-level NER or span-extraction head. Offensive-language F1 is a research score, not a moderation guarantee. Diglossia is unmeasured beyond MASSIVE (ar-SA MSA) and OSACT tweets. Full tables and citations: [`FINDINGS.md`](FINDINGS.md), [`citations.bib`](citations.bib).

```bibtex
@misc{alkhenizan2026layaara,
  title        = {laya-ara: Arabic typed-decision fine-tuning of laya-multilingual},
  author       = {Alkhenizan, Mohammad},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/Wouze/laya-ara}}
}
```
