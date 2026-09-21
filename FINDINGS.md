# Additional experiments

Companion note to the laya-ara card. All comparisons use the same frozen Laya JSONL. Stock is `convaiinnovations/laya-multilingual`. The released NLU card is the v48 mix. Tables: [`RESULTS.md`](RESULTS.md). JSON: [`results/nlu_benches.json`](results/nlu_benches.json) · [`results/all_cards.json`](results/all_cards.json). RAG sibling: [`../laya-ara-rag`](../laya-ara-rag).

## Setup

After the released mix, we trained three one-epoch specialists from stock (quote, rag-ft) or from v48 (triage). Official test and hold-out files were not rebuilt. RAG remains top-1 among *k*≤12, not nDCG@10 over a corpus.

| Checkpoint | Items | XNLI | Role |
|---|---:|---|---|
| laya-ara (released) | multi-cycle mix | yes (capped) | In-domain MASSIVE / OSACT-A / XNLI |
| laya-ara-quote | 56,070 | no | Sentiment and hate fine-tune |
| **laya-ara-rag** | **35,591** | no | Fatwa search logs (unreleased) + MIRACL replay; [sibling card](../laya-ara-rag) |
| MIRACL-only ablation | 11,995 | no | Wikipedia pair + listwise; not the Hub RAG name |
| laya-ara-triage | 1,200 + 2k MASSIVE | no | Synthetic Gulf support heads |

## Classification specialists

Quote-mix includes the *training* splits of AJGT, LABR, ASTD (minus a frozen 1,500 hold-out), and OSACT-HS. Gains on those tests are **in-domain**, not zero-shot transfer.

| Task | *n* | Kind | Stock | laya-ara | quote |
|---|---:|---|---:|---:|---:|
| MASSIVE-ar scenario | 2974 | in-mix | 0.427 | **0.865** | 0.822 |
| XNLI-ar | 5010 | quote: zero-shot | 0.686 | **0.723** | 0.697 |
| OSACT4-A (acc / F1) | 1000 | in-mix | 0.844 / 0.726 | **0.920 / 0.862** | 0.901 / 0.823 |
| OSACT4-HS (acc / F1) | 1000 | fine-tune | 0.932 / 0.655 | 0.875 / 0.645 | **0.963 / 0.677** |
| AJGT | 360 | fine-tune | 0.833 | 0.756 | **0.875** |
| LABR binary | 2348 | fine-tune | 0.759 | 0.766 | **0.834** |
| ASTD hold (acc / F1) | 1500 | fine-tune | 0.295 / 0.286 | 0.326 / 0.297 | **0.694 / 0.404** |

ASTD accuracy 0.694 with macro-F1 0.404 indicates majority-class improvement, not balanced four-way sentiment. Quote XNLI 0.697 is zero-shot (XNLI was withheld).

## Reranking specialist (**laya-ara-rag**)

The public RAG name is now the fatwa+MIRACL merge, not the Wikipedia-only 11,995-item run. Full tables: [`../laya-ara-rag`](../laya-ara-rag). Fatwa logs are described there and **not** uploaded.

| Task | *n* | Kind | Stock | laya-ara | MIRACL-only | **laya-ara-rag** |
|---|---:|---|---:|---:|---:|---:|
| MIRACL-ar rerank (dev) | 2896 | in-family | 0.153 | 0.210 | 0.536 | **0.588** |
| Mr.TyDi-ar | 2000 | transfer | 0.176 | 0.260 | 0.610 | **0.632** |
| SadeemQuestion | 2089 | transfer | 0.168 | 0.242 | 0.781 | **0.871** |
| MLQA-ar | 2000 | transfer | 0.133 | 0.214 | 0.507 | **0.582** |
| XPQA-ar | 750 | transfer | 0.213 | 0.281 | 0.495 | **0.665** |
| PublicHealthQA-ar | 86 | transfer | 0.116 | 0.244 | 0.326 | **0.488** |
| Mintaka-ar | 2203 | transfer | 0.285 | 0.311 | **0.403** | 0.388 |

Pairwise (`noul`): MIRACL 0.688 → **0.788**; Sadeem 0.837 → **0.941**. Mintaka / MLQA / XPQA pairwise still favor this NLU card (0.616 / 0.784 / 0.697). In-domain sealed fatwa pair 0.812 → **0.938** (queries not released). Do not advertise a 21-row listwise as 100%. Full grid: [`results/all_cards.json`](results/all_cards.json).

## Synthetic triage

Authored Gulf lines (1,200 train / 200 hold, seed 42). Not operational tickets. Smoke-line churn confidence 0.03 → 0.91. Hold-out: queue accuracy 0.75, churn F1 0.91, urgency nearest-class 0.33.

## Discussion

1. Additional cycles of the same MASSIVE+XNLI mix change locked scores by tenths of a point. Task-matched data moves the corresponding metric.
2. Listwise short-list ranking transfers more readily than pairwise relevance after MIRACL training.
3. In-domain sentiment fine-tuning is not a substitute for the released MASSIVE card.
4. Synthetic ordinal labels are insufficient for urgency.

## Limitations (repeated)

No span extraction, no token NER, no full-corpus IR. XNLI in the released mix restricts commercial use. Cite dataset papers in [`citations.bib`](citations.bib) when reporting a row.

Contact: [Mohammad Alkhenizan on LinkedIn](https://www.linkedin.com/in/mohammad-alkhenizan-537623257).
