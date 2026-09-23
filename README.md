# laya-ara

Arabic typed-decision models on [`laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual): **NLU** and **short-list RAG**.

<p align="center">
  <img src="assets/logo.jpg" alt="laya-ara" width="280">
</p>

**Mohammad Alkhenizan** · 21 September 2026 · [LinkedIn](https://www.linkedin.com/in/mohammad-alkhenizan-537623257)

[![laya-ara downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fmodels%2FWouze%2Flaya-ara&query=%24.downloads&label=laya-ara%2030d&color=yellow)](https://huggingface.co/Wouze/laya-ara)
[![laya-ara-rag downloads](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fhuggingface.co%2Fapi%2Fmodels%2FWouze%2Flaya-ara-rag&query=%24.downloads&label=laya-ara-rag%2030d&color=yellow)](https://huggingface.co/Wouze/laya-ara-rag)

One GitHub repo. Two Hugging Face cards. Download counts are the Hub’s last-30-day figure.

| Model | Hub | In this repo |
|---|---|---|
| **laya-ara** — intent, NLI, OSACT-A | [`Wouze/laya-ara`](https://huggingface.co/Wouze/laya-ara) | [`RESULTS.md`](RESULTS.md) · [`results/nlu_benches.json`](results/nlu_benches.json) |
| **laya-ara-rag** — k≤12 rerank / relevance | [`Wouze/laya-ara-rag`](https://huggingface.co/Wouze/laya-ara-rag) | [`rag/`](rag/) · [`rag/RESULTS.md`](rag/RESULTS.md) · [`results/rag_all_benches.json`](results/rag_all_benches.json) |

Combined JSON: [`results/all_cards.json`](results/all_cards.json).

## Highlights vs `laya-multilingual`

Relative lift is *(fine-tune − stock) / stock* on the same frozen Laya templates.

### laya-ara (NLU)

| Arabic task | *n* | Base | **laya-ara** | Relative lift |
|---|---:|---:|---:|---:|
| Intent, 20 options (MASSIVE ar-SA) | 2974 | 0.386 | **0.816** | **+111%** |
| Scenario, 18-way (MASSIVE ar-SA) | 2974 | 0.427 | **0.865** | **+103%** |
| Hierarchical intent | 2694 | 0.536 | **0.893** | **+67%** |
| Offensive language, macro-F1 (OSACT4-A) | 1000 | 0.726 | **0.862** | **+19%** |
| Natural language inference (XNLI-ar) | 5010 | 0.686 | **0.723** | +5% |

XNLI in this mix is CC BY-NC 4.0 — NLU weights are **research / non-commercial** ([`NOTICE.md`](NOTICE.md)).

### laya-ara-rag (rerank)

Top-1 among ≤12 candidates, not corpus nDCG@10. XNLI withheld.

| Arabic task | *n* | Base | **laya-ara-rag** | Relative lift |
|---|---:|---:|---:|---:|
| MIRACL-ar rerank (dev) | 2896 | 0.153 | **0.588** | **+284%** (3.8×) |
| Mr.TyDi-ar rerank | 2000 | 0.176 | **0.632** | **+259%** (3.6×) |
| MLQA-ar rerank | 2000 | 0.133 | **0.582** | **+338%** (4.4×) |
| SadeemQuestion rerank | 2089 | 0.168 | **0.871** | **+418%** (5.2×) |
| XPQA-ar rerank | 750 | 0.213 | **0.665** | **+212%** (3.1×) |
| In-domain pairwise relevance | 112 | 0.812 | **0.938** | **+16%** |

Mintaka entity ranking does not improve. Write-up: [`rag/README.md`](rag/README.md) · data note: [`rag/DATA.md`](rag/DATA.md).

## Inference

`laya` is the [ConvAI Laya](https://pypi.org/project/laya/) runtime (`pip install laya==0.3.4`). The Hub **Use this model** snippet passes `trust_remote_code=True` and then calls `laya.load`.

```bash
pip install "laya==0.3.4"
export USE_TF=0
```

```python
import os
import laya

nlu = laya.load("Wouze/laya-ara", token=os.environ.get("HF_TOKEN"))
rag = laya.load("Wouze/laya-ara-rag", token=os.environ.get("HF_TOKEN"))
```

Demos: [`examples/predict_triage.py`](examples/predict_triage.py) · [`examples/predict_rerank.py`](examples/predict_rerank.py).

## Contact

Licensing, evaluation access, or collaboration: [Mohammad Alkhenizan on LinkedIn](https://www.linkedin.com/in/mohammad-alkhenizan-537623257).
