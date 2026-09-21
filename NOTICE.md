# Notices

## Base model

`convaiinnovations/laya-multilingual` — Apache-2.0 (mmBERT-base encoder + Laya System One head).

This repository is **not** TypeSafe Jev and **not** English `convaiinnovations/laya`.

## Training data licenses (v48)

| Source | Role | License | Share impact |
|---|---|---|---|
| AmazonScience/massive ar-SA | Train + eval | CC BY 4.0 | Attribution required. Commercial OK. |
| OSACT4 Offensive Subtask A | Train + eval | Shared-task / research | Cite OSACT4. Confirm redistribution. |
| facebook/xnli Arabic | Train (capped) + eval | **CC BY-NC 4.0** | **v48 weights are research / non-commercial.** Do not ship as a commercial product dump. Do not upload raw XNLI text. |
| MIRACL-ar, Mr.TyDi, Sadeem, MLQA, XPQA, Mintaka, PublicHealthQA | Eval (all); MIRACL-ar **train** is in `laya-ara-rag` | See each dataset card | PublicHealthQA is CC BY-NC-SA (eval only). |

**laya-ara-quote** is trained **without XNLI** (MASSIVE + OSACT-A + OSACT-HS + AJGT + LABR + ASTD remainder). Commercial-friendlier than **laya-ara**. It wins the sentiment/hate **fine-tunes** vs stock and laya-ara; it does **not** beat laya-ara on MASSIVE / XNLI / OSACT-A. Pick the card by task. Do not treat quote XNLI 0.697 as an NLI train result (zero-shot).

**laya-ara-rag** is also **without XNLI** (MIRACL-ar train pair+rerank + 4k MASSIVE). Use for k≤12 relevance. Do not call it a retriever. It does not replace laya-ara on the locked suite.

## Citation

Cite [`CITATION.cff`](CITATION.cff) and the dataset paper for any reported row ([`citations.bib`](citations.bib)). Encoder: Marone et al. 2025 (mmBERT). Head: ConvAI `laya-multilingual`. Experimental note: [`FINDINGS.md`](FINDINGS.md).

## Anti-claims

Do not describe this model as: a chat LLM, a generative RAG writer, a token-NER tagger, a span-QA system, a full-corpus MIRACL retriever, a safe unattended moderator, or TypeSafe Jev.
