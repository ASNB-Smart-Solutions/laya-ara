# Results — laya-ara-rag

Frozen Laya JSONL. Stock is `convaiinnovations/laya-multilingual`. Listwise metric: top-1 among *k*≤12, not nDCG@10. Relative lift is *(model − stock) / stock*.

Hub: [`Wouze/laya-ara-rag`](https://huggingface.co/Wouze/laya-ara-rag). JSON: [`../results/rag_all_benches.json`](../results/rag_all_benches.json) · [`../results/all_cards.json`](../results/all_cards.json). NLU tables: [`../RESULTS.md`](../RESULTS.md).

## Highlights vs base

| Arabic task | *n* | Base | laya-ara-rag | Δ rel. |
|---|---:|---:|---:|---:|
| MIRACL-ar rerank | 2896 | 0.153 | **0.588** | **+284%** (3.8×) |
| Mr.TyDi-ar rerank | 2000 | 0.176 | **0.632** | **+259%** (3.6×) |
| MLQA-ar rerank | 2000 | 0.133 | **0.582** | **+338%** (4.4×) |
| SadeemQuestion rerank | 2089 | 0.168 | **0.871** | **+418%** (5.2×) |
| XPQA-ar rerank | 750 | 0.213 | **0.665** | **+212%** (3.1×) |
| In-domain pairwise | 112 | 0.812 | **0.938** | **+16%** |

## Listwise (k ≤ 12)

| Task | *n* | Kind | Base | laya-ara | MIRACL-only | laya-ara-rag | Δ vs base |
|---|---:|---|---:|---:|---:|---:|---:|
| MIRACL-ar (dev) | 2896 | in-family | 0.153 | 0.210 | 0.536 | **0.588** | +284% |
| Mr.TyDi-ar | 2000 | transfer | 0.176 | 0.260 | 0.610 | **0.632** | +259% |
| SadeemQuestion | 2089 | transfer | 0.168 | 0.242 | 0.781 | **0.871** | +418% |
| MLQA-ar | 2000 | transfer | 0.133 | 0.214 | 0.507 | **0.582** | +338% |
| XPQA-ar | 750 | transfer | 0.213 | 0.281 | 0.495 | **0.665** | +212% |
| PublicHealthQA-ar | 86 | transfer | 0.116 | 0.244 | 0.326 | **0.488** | +321% |
| Mintaka-ar | 2203 | transfer | 0.285 | 0.311 | **0.403** | 0.388 | +36% |

## Pairwise relevance

| Task | *n* | Base | laya-ara | MIRACL-only | laya-ara-rag |
|---|---:|---:|---:|---:|---:|
| MIRACL-ar (dev) | 5792 | 0.688 | 0.629 | 0.758 | **0.788** |
| Mr.TyDi-ar | 4000 | 0.755 | 0.740 | 0.811 | **0.834** |
| SadeemQuestion | 4178 | 0.837 | 0.919 | 0.913 | **0.941** |
| PublicHealthQA-ar | 172 | 0.791 | 0.773 | 0.843 | **0.866** |
| Mintaka-ar | 4406 | 0.537 | **0.616** | 0.526 | 0.513 |
| MLQA-ar | 4000 | 0.731 | **0.784** | 0.707 | 0.706 |
| XPQA-ar | 1500 | 0.623 | **0.697** | 0.625 | 0.615 |

## In-domain (logs not redistributed)

| Exam | *n* | Base | MIRACL-only | laya-ara-rag | Δ vs base |
|---|---:|---:|---:|---:|---:|
| Human pairwise | 112 | 0.812 | 0.732 | **0.938** | +16% |
| Teacher pairwise hold | 400 | 0.640 | 0.662 | **0.792** | +24% |
| Teacher listwise hold | 200 | 0.110 | 0.355 | **0.575** | +423% |

Contact: [Mohammad Alkhenizan](https://www.linkedin.com/in/mohammad-alkhenizan-537623257).
