# Additional experiments

Companion note to **laya-ara-rag**. Stock is `convaiinnovations/laya-multilingual`. NLU card: [`laya-ara`](https://huggingface.co/Wouze/laya-ara). Tables: [`RESULTS.md`](RESULTS.md). JSON: [`rag_all_benches.json`](https://huggingface.co/Wouze/laya-ara-rag/blob/main/results/rag_all_benches.json) · [`all_cards.json`](https://huggingface.co/Wouze/laya-ara-rag/blob/main/results/all_cards.json).

RAG is top-1 among *k*≤12, not nDCG@10.

## Setup

| Checkpoint | Items | XNLI | Role |
|---|---:|---|---|
| laya-ara (NLU) | multi-cycle mix | yes (capped) | MASSIVE / OSACT-A / XNLI |
| MIRACL-only predecessor | 11,995 | no | Wikipedia pair + listwise |
| **laya-ara-rag (this card)** | **35,591** | **no** | In-house retrieval logs + MIRACL replay + 2k MASSIVE |

This card is the public RAG name. The Wikipedia-only run is the ablation.

## In-domain vs Wikipedia-only

MIRACL teaches Wikipedia pos/neg. The in-house stack is Gulf + MSA, near-duplicate answers, and production hard negatives. Listwise skill transferred; pairwise on the sealed golds did not (0.732 vs stock 0.812) until the gap-filtered in-house pairs were added (0.938, **+16%** vs stock).

Teacher-hold rerank 0.110 → **0.575** (**+423%** vs stock) is the 200-query generalization number (teacher agreement, not human).

## Public transfer

Listwise **6/7** versus the Wikipedia-only predecessor. MIRACL-ar dev rose after the in-house epoch (rerank 0.536 → 0.588, pair 0.758 → 0.788). Mintaka entity ranking favors the predecessor.

## Limitations

No span extraction, no token NER, no full-corpus IR. Cite dataset papers in [`citations.bib`](citations.bib) when reporting a public row.

Contact: [Mohammad Alkhenizan on LinkedIn](https://www.linkedin.com/in/mohammad-alkhenizan-537623257).
