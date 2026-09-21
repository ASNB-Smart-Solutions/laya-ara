# laya-ara

<p align="center">
  <img src="assets/logo.jpg" alt="laya-ara" width="280">
</p>

Arabic typed decisions (`choice` / `noul`) on [`convaiinnovations/laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual). Author: **Mohammad Alkhenizan**.

Not a chat model. Not a retriever. Not TypeSafe Jev.

**MASSIVE-ar intent, 20 options: 0.386 → 0.816.** Scenario 0.865 is a different (easier) exam.

XNLI-ar was in the mix (**CC BY-NC**). Research weights. [`NOTICE.md`](NOTICE.md) · full numbers [`results/v48_all_benches.json`](results/v48_all_benches.json) · extra tracks [`FINDINGS.md`](FINDINGS.md).

```python
import laya
agent = laya.load("Wouze/laya-ara")
```

## vs stock

Same frozen questions. Stock = `laya-multilingual`.

| Task | n | Stock | laya-ara |
|---|---:|---:|---:|
| MASSIVE-ar intent, 20-opt | 2974 | 0.386 | **0.816** |
| MASSIVE-ar scenario, 18-way | 2974 | 0.427 | **0.865** |
| MASSIVE-ar hierarchical intent | 2694 | 0.536 | **0.893** |
| XNLI-ar | 5010 | 0.686 | **0.723** |
| OSACT4-A offense (F1) | 1000 | 0.726 | **0.862** |

Sentiment / hate transfer is weak on this card (AJGT and OSACT-HS went down). TyDiQA sentence pick: 0.359 → 0.413.

## RAG (k≤12 rerank, not nDCG@10)

This card had **no** MIRACL train. Listwise only:

| Task | n | Stock | laya-ara |
|---|---:|---:|---:|
| Mr.TyDi-ar | 2000 | 0.176 | **0.260** |
| SadeemQuestion | 2089 | 0.168 | **0.242** |
| MLQA-ar | 2000 | 0.133 | **0.214** |
| MIRACL-ar dev | 2896 | 0.153 | **0.210** |

All seven listwise files moved up. Hard pairwise (MIRACL human, Mr.TyDi BM25) still favors stock.

## Other mixes

Later specialists. They do **not** replace this card on MASSIVE / XNLI.

| Mix | What it wins | Caveat |
|---|---|---|
| **quote** (no XNLI) | AJGT 0.875 · LABR 0.834 | Fine-tune, not zero-shot. Loses MASSIVE (0.822 vs 0.865) |
| **rag-ft** (MIRACL train) | MIRACL rerank **0.536** · Sadeem 0.781 | Still k≤12. Not a retriever |
| **triage** | Smoke churn 0.03 → 0.91 | Synthetic labels. Urgency still weak |

## Limits

Research / NC (XNLI). No span NER/QA. Do not deploy unattended moderation.

```bibtex
@misc{alkhenizan2026layaara,
  title        = {laya-ara},
  author       = {Alkhenizan, Mohammad},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/Wouze/laya-ara}}
}
```
