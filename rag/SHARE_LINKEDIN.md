# laya-ara-rag — short announcement

Arabic short-list reranker on `laya-multilingual` (`choice` / `noul`, k≤12). Not nDCG@10, not a retriever.

Versus base:

| Task | Base → laya-ara-rag | Relative |
|---|---|---|
| MIRACL-ar rerank | 0.153 → 0.588 | **+284%** (3.8×) |
| Mr.TyDi-ar | 0.176 → 0.632 | **+259%** |
| MLQA-ar | 0.133 → 0.582 | **+338%** |
| SadeemQuestion | 0.168 → 0.871 | **+418%** |
| In-domain pairwise | 0.812 → 0.938 | **+16%** |

NLU sibling **laya-ara**: MASSIVE-ar intent **+111%** (0.386 → 0.816).

Collaboration: [linkedin.com/in/mohammad-alkhenizan-537623257](https://www.linkedin.com/in/mohammad-alkhenizan-537623257)
