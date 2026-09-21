---
language:
  - ar
license: other
license_name: Research (XNLI CC BY-NC in the v48 mix)
license_link: NOTICE.md
base_model: convaiinnovations/laya-multilingual
datasets:
  - AmazonScience/massive
  - facebook/xnli
tags:
  - arabic
  - laya
  - laya-ara
  - system-one
  - typed-decisions
  - massive
  - xnli
  - osact
  - rag
  - rerank
library_name: laya
pipeline_tag: text-classification
metrics:
  - accuracy
  - f1
model-index:
  - name: laya-ara
    results:
      - task:
          type: text-classification
          name: Intent classification (20-option Laya harness)
        dataset:
          type: AmazonScience/massive
          name: MASSIVE ar-SA (20-option intent)
          config: ar-SA
          split: test
        metrics:
          - type: accuracy
            value: 0.816
            name: Accuracy
      - task:
          type: text-classification
          name: Scenario classification (18-way)
        dataset:
          type: AmazonScience/massive
          name: MASSIVE ar-SA (scenario)
          config: ar-SA
          split: test
        metrics:
          - type: accuracy
            value: 0.865
            name: Accuracy
      - task:
          type: text-classification
          name: Natural language inference
        dataset:
          type: facebook/xnli
          name: XNLI-ar
          config: ar
          split: test
        metrics:
          - type: accuracy
            value: 0.723
            name: Accuracy
      - task:
          type: text-classification
          name: Offensive language (noul)
        dataset:
          type: osact4
          name: OSACT4 Subtask A (val)
          split: validation
        metrics:
          - type: f1
            value: 0.862
            name: Macro-F1
  - name: laya-ara-rag
    results:
      - task:
          type: text-classification
          name: Passage rerank (top-1 among k≤12; not nDCG@10)
        dataset:
          type: miracl
          name: MIRACL-ar dev (in-family; train was MIRACL)
          config: ar
          split: validation
        metrics:
          - type: accuracy
            value: 0.536
            name: Top-1@k≤12
      - task:
          type: text-classification
          name: Passage rerank (top-1 among k≤12; transfer)
        dataset:
          type: mr-tydi
          name: Mr.TyDi-ar train 2k
          config: arabic
        metrics:
          - type: accuracy
            value: 0.610
            name: Top-1@k≤12
      - task:
          type: text-classification
          name: Passage rerank (top-1 among k≤12; transfer)
        dataset:
          type: sadeem
          name: SadeemQuestion
        metrics:
          - type: accuracy
            value: 0.781
            name: Top-1@k≤12
      - task:
          type: text-classification
          name: Passage rerank (top-1 among k≤12; transfer)
        dataset:
          type: mlqa
          name: MLQA ara-ara test 2k
        metrics:
          - type: accuracy
            value: 0.507
            name: Top-1@k≤12
      - task:
          type: text-classification
          name: Passage rerank (top-1 among k≤12; transfer)
        dataset:
          type: xpqa
          name: XPQA ara-ara
        metrics:
          - type: accuracy
            value: 0.495
            name: Top-1@k≤12
  - name: laya-ara-quote
    results:
      - task:
          type: text-classification
          name: Sentiment (fine-tune; train split in mix)
        dataset:
          type: ajgt
          name: AJGT
          split: test
        metrics:
          - type: accuracy
            value: 0.875
            name: Accuracy
      - task:
          type: text-classification
          name: Review sentiment (fine-tune; train split in mix)
        dataset:
          type: labr
          name: LABR binary (drop 3★)
          split: test
        metrics:
          - type: accuracy
            value: 0.834
            name: Accuracy
---

# laya-ara

Fine-tune of [`convaiinnovations/laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual) (mmBERT-base + Laya head, ~322M) for **Arabic typed decisions**: `choice`, `score`, `noul`. Official Laya RLCD on 2×RTX 3090. Scored 21 Sep 2026. Author: **Abdulrahman Radhi**. Default weights are the v48 mix (`artifacts/laya-ar-v48` on the training box).

**Not** TypeSafe Jev. **Not** a chat / generation model. **Not** a span-NER or span-QA head. **Not** a full-corpus MIRACL retriever.

v48 saw capped **XNLI-ar (CC BY-NC 4.0)** — treat these weights as **research / non-commercial**. [`NOTICE.md`](NOTICE.md) · numbers [`results/v48_all_benches.json`](results/v48_all_benches.json) · BibTeX [`citations.bib`](citations.bib).

Quote this number if you quote one: **MASSIVE-ar intent, 20 options, 0.386 → 0.816**. That is the Laya-card protocol (published stock ~0.38–0.40). Scenario 0.865 is an easier 18-way exam.

Later tracks did **not** beat that locked suite. They produced three specialists. Full write-up: [`FINDINGS.md`](FINDINGS.md).

## Findings (three later tracks)

Specialists, not a better v48. Same-recipe XNLI cycles bought tenths of a point. Training on the exam you want to quote moved the scores.

| Checkpoint | Wins | Loses / do not claim |
|---|---|---|
| **laya-ara** (this card, v48) | MASSIVE 0.816 / 0.865 · XNLI 0.723 · OSACT-A F1 0.862 | AJGT / OSACT-HS. Commercial dump (XNLI NC) |
| **laya-ara-quote** (no XNLI) | AJGT **0.875** · LABR **0.834** · OSACT-HS **0.963** (FT) | MASSIVE 0.822 vs 0.865. ASTD acc 0.694 / F1 **0.404** |
| **laya-ara-rag** (no XNLI) | MIRACL rerank **0.536** · transfer reranks below | Retriever / nDCG@10. Mintaka & MLQA **pair** dropped |
| **laya-ara-triage** | Synthetic smoke churn 0.03 → **0.91** | Real tickets. Urgency nearest 0.33 |

### Shareable rag-ft listwise (second table)

`laya-ara-rag` = MIRACL-ar **train** + 4k MASSIVE. Top-1 among ≤12. **Not** nDCG@10.

| Task | n | Kind | Stock | rag-ft | Δ | Cite |
|---|---:|---|---:|---:|---:|---|
| MIRACL-ar rerank (dev) | 2896 | in-family | 0.153 | **0.536** | +38.3 | Zhang et al. 2023 |
| Mr.TyDi-ar rerank | 2000 | transfer | 0.176 | **0.610** | +43.5 | Zhang et al. 2021 |
| SadeemQuestion rerank | 2089 | transfer | 0.168 | **0.781** | +61.3 | Sadeem 2024 |
| MLQA-ar rerank | 2000 | transfer | 0.133 | **0.507** | +37.5 | Lewis et al. 2020 |
| XPQA-ar rerank | 750 | transfer | 0.213 | **0.495** | +28.1 | Shen et al. 2023 |

MIRACL pair 0.688 → **0.758**. Listwise rose on all seven files. Pairwise mixed.

Quote-mix is a **footnote**: those sentiment/hate train splits were in the mix. Do not swap the v48 NLU table for ASTD 0.694.

## Intended use

- Arabic **System One** decisions in one forward pass: routing (`choice`), binary flags (`noul`), optional ordinal `score`.
- Research on Arabic Laya / typed-decision heads vs stock `laya-multilingual`.
- Reproducing the tables below (same frozen JSONL protocol).

**Out of scope:** open-ended chat, span extraction, token NER, first-stage retrieval over Wikipedia, unattended hate-speech moderation, production triage on real tickets.

## How to use

```bash
pip install laya
export USE_TF=0
```

```python
import laya
agent = laya.load("Wouze/laya-ara")
out = agent.predict(
    {"channel": "whatsapp", "message": "الحوالة ما وصلت، أبي استرجاع وإلا بنقلع"},
    {
        "queue": {
            "type": "choice",
            "instructions": "Which support queue?",
            "criteria": {
                "billing": "payments, refunds",
                "technical": "bugs, outages",
                "account": "login, KYC",
                "other": "none of the above",
            },
        },
        "refund": {"type": "noul", "instructions": "Does the user ask for a refund?"},
    },
)
```

Demo: [`examples/predict_triage.py`](examples/predict_triage.py). Stock baseline is always `convaiinnovations/laya-multilingual`. Same frozen questions for every row below.

## Evaluation

All numbers are **this box, 21 Sep 2026**, stock vs `artifacts/laya-ar-v48`. Acc unless noted.

### Locked three (in the FT mix)

| Task | n | Metric | Stock | v48 | Δ | Cite |
|---|---:|---|---:|---:|---:|---|
| MASSIVE-ar scenario (18-way, test) | 2974 | acc | 0.427 | **0.865** | +43.8 | FitzGerald et al. 2023 |
| XNLI-ar (test) | 5010 | acc | 0.686 | **0.723** | +3.7 | Conneau et al. 2018 |
| OSACT4-A offense (val) | 1000 | macro-F1 | 0.726 | **0.862** | +13.6 | Mubarak et al. 2020 |

OSACT-A acc 0.844 → 0.920. XNLI is mid (Laya card stock ~0.73), not AraBERT-class (~0.80).

### MASSIVE-ar variants (same test utterances)

| Task | n | Stock | v48 | Δ |
|---|---:|---:|---:|---:|
| Intent, 20 options (card protocol) | 2974 | 0.386 | **0.816** | +43.0 |
| Hierarchical intent (k≥2) | 2694 | 0.536 | **0.893** | +35.7 |
| Scenario 18-way | 2974 | 0.427 | **0.865** | +43.8 |

Do not post 0.865 as “MASSIVE intent.”

### Translated popular Arabic NLU (zero-shot vs the mix)

Official labels. QA is **sentence selection**, not span EM/F1.

| Task | n | Metric | Stock | v48 | Δ | Cite |
|---|---:|---|---:|---:|---:|---|
| OSACT4-HS (hate noul) | 1000 | acc / F1 | **0.932 / 0.655** | 0.875 / 0.645 | −5.7 / −1.0 | Mubarak et al. 2020 |
| AJGT sentiment | 360 | acc / F1 | **0.833 / 0.832** | 0.756 / 0.747 | −7.8 / −8.6 | Alomari et al. 2017 |
| LABR binary (drop 3★) | 2348 | acc / F1 | 0.759 / 0.758 | **0.766 / 0.764** | +0.7 / +0.6 | Aly & Atiya 2013 |
| ASTD 4-way (hold 1500) | 1500 | acc / F1 | 0.295 / 0.286 | **0.326 / 0.297** | +3.1 / +1.1 | Nabil et al. 2015 |
| TyDiQA-ar sentence pick | 298 | acc / F1 | 0.359 / 0.155 | **0.413 / 0.170** | +5.4 / +1.5 | Clark et al. 2020 |

AJGT and OSACT-HS: v48 is worse. ASTD is below majority Objective (~0.65).

### Sister checkpoint: laya-ara-quote (no XNLI)

`laya-ara-quote` (`artifacts/laya-ar-quote`), 1 epoch from stock, 56,070 items. **Commercial-friendlier.** AJGT / LABR / ASTD / OSACT-HS are **fine-tune**, not zero-shot.

| Task | n | Stock | v48 | Quote |
|---|---:|---:|---:|---:|
| MASSIVE scenario | 2974 | 0.427 | **0.865** | 0.822 |
| XNLI-ar (quote zero-shot) | 5010 | 0.686 | **0.723** | 0.697 |
| OSACT-A acc / F1 | 1000 | 0.844 / 0.726 | **0.920 / 0.862** | 0.901 / 0.823 |
| OSACT-HS acc / F1 | 1000 | 0.932 / 0.655 | 0.875 / 0.645 | **0.963 / 0.677** |
| AJGT acc / F1 | 360 | 0.833 / 0.832 | 0.756 / 0.747 | **0.875 / 0.875** |
| LABR acc / F1 | 2348 | 0.759 / 0.758 | 0.766 / 0.764 | **0.834 / 0.834** |
| ASTD hold acc / F1 | 1500 | 0.295 / 0.286 | 0.326 / 0.297 | **0.694 / 0.404** |
| TyDiQA-sent acc / F1 | 298 | 0.359 / 0.155 | **0.413 / 0.170** | 0.406 / 0.140 |

Do not advertise ASTD 0.694 as balanced 4-way (macro-F1 0.404). Quote does not replace v48 on the locked suite.

### Arabic RAG — all 7 tasks

Relevance / rerank, k≤12. **Not** official MIRACL nDCG@10. Pairwise chance 0.50. Listwise chance ~0.083 (MIRACL 0.113).

| Task | Negatives | Pair n | Pair stock → v48 | Rank n | Rank stock → v48 | Cite |
|---|---|---:|---:|---:|---:|---|
| MIRACL-ar dev | human | 5792 | **0.688** → 0.629 | 2896 | 0.153 → **0.210** | Zhang et al. 2023 |
| Mr.TyDi-ar train 2k | BM25 | 4000 | **0.755** → 0.740 | 2000 | 0.176 → **0.260** | Zhang et al. 2021 |
| SadeemQuestion | random article | 4178 | 0.837 → **0.919** | 2089 | 0.168 → **0.242** | Sadeem 2024 |
| PublicHealthQA-ar | random FAQ | 172 | **0.791** → 0.773 | 86 | 0.116 → **0.244** | Lu 2024 |
| Mintaka-ar (entity) | random entity | 4406 | 0.537 → **0.616** | 2203 | 0.285 → **0.311** | Sen et al. 2022 |
| MLQA ara-ara test 2k | random paragraph | 4000 | 0.731 → **0.784** | 2000 | 0.133 → **0.214** | Lewis et al. 2020 |
| XPQA ara-ara | random answer | 1500 | 0.623 → **0.697** | 750 | 0.213 → **0.281** | Shen et al. 2023 |

v48 wins **7/7 listwise** vs stock. Pairwise: easy random-negs favor v48; MIRACL human / Mr.TyDi BM25 favor stock. PHQA rank n=86 is noisy.

### Sister checkpoint: laya-ara-rag (MIRACL train, no XNLI)

`laya-ara-rag` (`artifacts/laya-ar-rag`), 1 epoch from stock, 11,995 items (MIRACL-ar train pair+rerank + 4k MASSIVE). Frozen eval files unchanged. **Still k≤12 top-1, not nDCG@10.**

| Task | Pair stock / v48 / rag-ft | Rank stock / v48 / rag-ft |
|---|---|---|
| MIRACL-ar dev | 0.688 / 0.629 / **0.758** | 0.153 / 0.210 / **0.536** |
| Mr.TyDi-ar train 2k | 0.755 / 0.740 / **0.811** | 0.176 / 0.260 / **0.610** |
| SadeemQuestion | 0.837 / **0.919** / 0.913 | 0.168 / 0.242 / **0.781** |
| PublicHealthQA-ar | 0.791 / 0.773 / **0.843** | 0.116 / 0.244 / **0.326** |
| Mintaka-ar | 0.537 / **0.616** / 0.526 | 0.285 / 0.311 / **0.403** |
| MLQA ara-ara 2k | 0.731 / **0.784** / 0.707 | 0.133 / 0.214 / **0.507** |
| XPQA ara-ara | 0.623 / **0.697** / 0.625 | 0.213 / 0.281 / **0.495** |

Listwise **7/7**. Pairwise mixed (Mintaka / MLQA pair dropped). Sadeem rerank ECE 0.468 — overconfident. rag-ft does not replace v48 on the locked suite.

### Not measured

Token NER/BIO · TyDiQA/ARCD span EM-F1 · official MIRACL nDCG@10 · ALUE private tests · AraBERT/MARBERT on these Laya templates.

## Training

| | |
|---|---|
| Base | `convaiinnovations/laya-multilingual` (mmBERT-base + Laya head, Apache-2.0) |
| Recipe | Official Laya RLCD (policy gradient + soft CE, group size 4), DDP 2×3090 fp16 |
| Mix | MASSIVE-ar train + OSACT4-A + capped XNLI-ar |
| Calibration | Hybrid temperatures; `choice:11+` floor 3.75 |
| Hardware | 2×RTX 3090 (275 W cap), 32 GB RAM, PCIe Gen3 x8 |
| Last cycle | ~7 min / 34k items / 1 epoch (v48). First full train ~37 min |

## Limitations and bias

- **License.** XNLI in the mix → research / non-commercial weights. Do not upload raw XNLI or OSACT tweet dumps with the model.
- **Transfer.** Sentiment and hate (AJGT, OSACT-HS) got worse on **v48**. The later quote-mix checkpoint recovers those as in-mix FT; it still loses MASSIVE/XNLI/OSACT-A to v48. Neither is a general Arabic BERT.
- **XNLI.** 0.723 is usable, not strong.
- **RAG.** Short-list exam only. v48 0.26 top-1@12 is not a retriever. rag-ft MIRACL rerank 0.536 is still k≤12, not nDCG@10.
- **Triage.** laya-ara queue/refund work on the Gulf demo; churn was a miss (~0.03). Synthetic FT `laya-ara-triage` (1200/200, not real tickets) puts smoke churn at 0.91 and hold200 churn F1 at 0.91 / queue 0.75. Urgency stays weak.
- **Diglossia.** MASSIVE is ar-SA assistant MSA. OSACT is dialectal tweets. Gulf chat is not a measured slice.
- **Moderation.** Offensive-language F1 is a research score. Do not deploy unattended.

## How to upload

[`UPLOAD.md`](UPLOAD.md). Default Hub create is **private**.

```bash
export HF_TOKEN=hf_...
python scripts/upload_to_hf.py \
  --ckpt /path/to/artifacts/laya-ar-v48 \
  --repo-id Wouze/laya-ara \
  --dry-run
```

## Citation

If you use the **checkpoint**, cite this card and the encoder:

```bibtex
@misc{radhi2026layaara,
  title        = {laya-ara},
  author       = {Radhi, Abdulrahman},
  year         = {2026},
  note         = {Fine-tune of convaiinnovations/laya-multilingual (v48 mix). Research weights (XNLI CC BY-NC).},
  howpublished = {\url{https://huggingface.co/Wouze/laya-ara}}
}

@misc{marone2025mmbert,
  title         = {mm{BERT}: A Modern Multilingual Encoder with Annealed Language Learning},
  author        = {Marone, Marc and Weller, Orion and Fleshman, William and Yang, Eugene
                   and Lawrie, Dawn and Van Durme, Benjamin},
  year          = {2025},
  eprint        = {2509.06888},
  archivePrefix = {arXiv}
}

@misc{laya-multilingual,
  title        = {laya-multilingual},
  author       = {{ConvAI Innovations}},
  year         = {2025},
  howpublished = {\url{https://huggingface.co/convaiinnovations/laya-multilingual}}
}
```

If you report a **dataset number**, also cite that paper. Full `.bib`: [`citations.bib`](citations.bib). GitHub/Zenodo: [`CITATION.cff`](CITATION.cff).

| You report | Cite |
|---|---|
| MASSIVE-ar | FitzGerald et al. 2023 |
| XNLI-ar | Conneau et al. 2018 |
| OSACT / OffensEval | Mubarak et al. 2020; Zampieri et al. 2020 |
| AJGT / LABR / ASTD | Alomari et al. 2017; Aly & Atiya 2013; Nabil et al. 2015 |
| TyDiQA-ar | Clark et al. 2020 |
| MIRACL / Mr.TyDi | Zhang et al. 2023; Zhang et al. 2021 |
| MLQA / Mintaka / xPQA | Lewis et al. 2020; Sen et al. 2022; Shen et al. 2023 |
| PublicHealthQA / Sadeem | Lu 2024; Sadeem 2024 |
