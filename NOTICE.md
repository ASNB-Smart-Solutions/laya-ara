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
| MIRACL-ar, Mr.TyDi, Sadeem, MLQA, XPQA, Mintaka, PublicHealthQA | Eval only | See each dataset card | PublicHealthQA is CC BY-NC-SA (eval only). |

A later **quote-mix** checkpoint (`laya-ar-quote`) is trained **without XNLI** and is the commercial-friendlier path if it beats v48 on the tasks you want to quote.

## Anti-claims

Do not describe this model as: a chat LLM, a generative RAG writer, a token-NER tagger, a span-QA system, a full-corpus MIRACL retriever, a safe unattended moderator, or TypeSafe Jev.
