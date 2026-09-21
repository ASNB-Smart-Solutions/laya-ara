# Results — laya-ara

Frozen Laya JSONL. Stock is `convaiinnovations/laya-multilingual`. Relative lift is *(model − stock) / stock*.

Card: [`README.md`](README.md) · JSON: [`nlu_benches.json`](https://huggingface.co/Wouze/laya-ara/blob/main/results/nlu_benches.json) · all models: [`all_cards.json`](https://huggingface.co/Wouze/laya-ara/blob/main/results/all_cards.json) · RAG: [`laya-ara-rag/RESULTS.md`](https://huggingface.co/Wouze/laya-ara-rag/blob/main/RESULTS.md)

## Highlights vs base

| Arabic task | *n* | Base | laya-ara | Δ rel. |
|---|---:|---:|---:|---:|
| Intent, 20 options (MASSIVE ar-SA) | 2974 | 0.386 | **0.816** | **+111%** |
| Scenario, 18-way | 2974 | 0.427 | **0.865** | **+103%** |
| Hierarchical intent | 2694 | 0.536 | **0.893** | **+67%** |
| OSACT4-A macro-F1 | 1000 | 0.726 | **0.862** | **+19%** |
| XNLI-ar | 5010 | 0.686 | **0.723** | +5% |

## Zero-shot NLU (this mix)

| Task | *n* | Base | laya-ara |
|---|---:|---:|---:|
| OSACT4-HS (acc / F1) | 1000 | 0.932 / 0.655 | 0.875 / 0.645 |
| AJGT | 360 | 0.833 | 0.756 |
| LABR binary | 2348 | 0.759 | 0.766 |
| ASTD hold (acc / F1) | 1500 | 0.295 / 0.286 | 0.326 / 0.297 |
| TyDiQA-ar sentence pick | 298 | 0.359 / 0.155 | 0.413 / 0.170 |

## Short-list rerank (this card, no MIRACL train)

| Task | *n* | Base | laya-ara | Δ rel. |
|---|---:|---:|---:|---:|
| Mr.TyDi-ar | 2000 | 0.176 | 0.260 | +48% |
| SadeemQuestion | 2089 | 0.168 | 0.242 | +44% |
| MLQA-ar | 2000 | 0.133 | 0.214 | +61% |
| MIRACL-ar (dev) | 2896 | 0.153 | 0.210 | +37% |
| XPQA-ar | 750 | 0.213 | 0.281 | +32% |
| PublicHealthQA-ar | 86 | 0.116 | 0.244 | +110% |
| Mintaka-ar | 2203 | 0.285 | 0.311 | +9% |

Specialist rerank numbers: [`laya-ara-rag`](https://huggingface.co/Wouze/laya-ara-rag).

Contact: [Mohammad Alkhenizan](https://www.linkedin.com/in/mohammad-alkhenizan-537623257).
