# Findings after three specialist tracks

**laya-ara** (v48 weights) remains the **public MASSIVE / XNLI / OSACT-A** card (research / NC). The later tracks did not beat that locked suite. They produced **three other checkpoints**, each winning a different exam.

| Checkpoint | Mix | Use | Do not use for |
|---|---|---|---|
| **laya-ara** (`artifacts/laya-ar-v48`) | MASSIVE + OSACT-A + capped XNLI | Locked NLU. Headline: MASSIVE-ar **20-opt intent 0.386 → 0.816** | Sentiment/hate (AJGT, OSACT-HS got worse). Commercial dump (XNLI CC BY-NC) |
| **laya-ara-quote** (`artifacts/laya-ar-quote`) | MASSIVE + OSACT-A + OSACT-HS + AJGT + LABR + ASTD remainder. **No XNLI** | Commercial-friendlier sentiment / hate **fine-tunes** | Replacing laya-ara on MASSIVE / XNLI. ASTD 0.694 acc (F1 0.404) |
| **laya-ara-rag** (`artifacts/laya-ar-rag`) | MIRACL-ar **train** pair+rerank + 4k MASSIVE. **No XNLI** | Arabic k≤12 relevance / rerank | First-stage retrieval. Official MIRACL nDCG@10 |
| **laya-ara-triage** (`artifacts/laya-ar-triage`) | 1200 authored Gulf lines from v48 | Product smoke: churn 0.03 → 0.91 | Production ticket accuracy. Urgency is still weak |

Same frozen JSONL for every row. Not generation. RAG is **top-1 among ≤12**, not nDCG@10.

## What we learned

1. **Specialists, not a better v48.** One more XNLI cycle does not move the public story. Training on the bench you want to quote does.
2. **Listwise RAG transfers; pairwise does not always.** After MIRACL train only, all seven reranks rose. Mintaka and MLQA **pairwise** fell.
3. **Quote-mix FT is not transfer.** AJGT / LABR / ASTD / OSACT-HS train splits were in the mix. Official tests/holds stayed sealed.
4. **Synthetic triage can fix churn, not urgency.** Do not cite hold200 as real-ticket scores.

## Shareable RAG-ft (second table)

Stock vs `laya-ara-rag`. MIRACL-ar **dev** is in-family (train was MIRACL). The other rows were **not** in the mix.

| Task | n | Kind | Stock | rag-ft | Δ | Cite |
|---|---:|---|---:|---:|---:|---|
| MIRACL-ar rerank (dev) | 2896 | in-family | 0.153 | **0.536** | +38.3 | Zhang et al. 2023 |
| Mr.TyDi-ar rerank | 2000 | transfer | 0.176 | **0.610** | +43.5 | Zhang et al. 2021 |
| SadeemQuestion rerank | 2089 | transfer | 0.168 | **0.781** | +61.3 | Sadeem 2024 |
| MLQA-ar rerank | 2000 | transfer | 0.133 | **0.507** | +37.5 | Lewis et al. 2020 |
| XPQA-ar rerank | 750 | transfer | 0.213 | **0.495** | +28.1 | Shen et al. 2023 |

Pairwise once, not as the hero: MIRACL pair 0.688 → **0.758**. Mintaka / MLQA pair went **down**.

Do not post 0.536 or 0.781 as a retriever.

## Quote-mix (footnote, not a swap)

`laya-ara-quote`, 1 epoch from stock, no XNLI. **Fine-tune**, not zero-shot.

- AJGT 0.833 → **0.875** · LABR 0.759 → **0.834** · OSACT-HS 0.932 → **0.963** (F1 0.655 → **0.677**)
- Loses MASSIVE 0.865 → 0.822 and XNLI 0.723 → 0.697 vs v48
- ASTD hold acc 0.694 / F1 **0.404** — majority-class, not balanced 4-way

## Machine-readable

[`results/v48_all_benches.json`](results/v48_all_benches.json) keys: `locked`, `quote_mix`, `rag`, `rag_ft`, `triage_synthetic`.
