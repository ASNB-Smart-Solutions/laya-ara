# Notices

## Base model

`convaiinnovations/laya-multilingual` — Apache-2.0 (mmBERT-base encoder + Laya System One head).

This repository is not TypeSafe Jev, not English `convaiinnovations/laya`, and not the NLU card [`Wouze/laya-ara`](https://huggingface.co/Wouze/laya-ara).

## Sources

| Source | Role | License |
|---|---|---|
| In-house Arabic retrieval logs | Train (not redistributed) | Proprietary. Cite this card. |
| Teacher ranks | Distillation labels | Not released. Hold scores are teacher agreement. |
| Human hold-out | Sealed eval | Not released. |
| MIRACL-ar train | Replay | Zhang et al. 2023. Do not re-host passages from this repo. |
| AmazonScience/massive ar-SA (2k) | Choice-marker replay | CC BY 4.0 |
| facebook/xnli | Not used | These weights are not the XNLI NC card. |

Eval-only public sets (Mr.TyDi, Sadeem, MLQA, XPQA, Mintaka, PublicHealthQA) are not in the mix. PublicHealthQA is CC BY-NC-SA.

## Scope

This model ranks a short list. It is not a first-stage retriever, not official MIRACL nDCG@10, and not a generative assistant.

Contact: [Mohammad Alkhenizan on LinkedIn](https://www.linkedin.com/in/mohammad-alkhenizan-537623257).
