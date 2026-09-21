---
language:
  - ar
license: other
license_name: xnli-cc-by-nc
license_link: https://creativecommons.org/licenses/by-nc/4.0/legalcode
base_model: convaiinnovations/laya-multilingual
datasets:
  - AmazonScience/massive
  - facebook/xnli
tags:
  - arabic
  - laya
  - laya-ara
  - typed-decisions
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
          name: Intent (20-option)
        dataset:
          type: AmazonScience/massive
          name: MASSIVE ar-SA
          config: ar-SA
          split: test
        metrics:
          - type: accuracy
            value: 0.816
            name: Accuracy
      - task:
          type: text-classification
          name: Scenario (18-way)
        dataset:
          type: AmazonScience/massive
          name: MASSIVE ar-SA
          config: ar-SA
          split: test
        metrics:
          - type: accuracy
            value: 0.865
            name: Accuracy
      - task:
          type: text-classification
          name: NLI
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
          name: Offensive language
        dataset:
          type: osact4
          name: OSACT4-A
          split: validation
        metrics:
          - type: f1
            value: 0.862
            name: Macro-F1
---

# laya-ara

Arabic typed decisions (`choice` / `score` / `noul`) on [`convaiinnovations/laya-multilingual`](https://huggingface.co/convaiinnovations/laya-multilingual). Author: **Mohammad Alkhenizan**.

Not a chat model. Not a retriever. Not TypeSafe Jev.

**Headline:** MASSIVE-ar intent, 20 options, **0.386 → 0.816**. Scenario 0.865 is a different (easier) exam.

XNLI-ar was in the mix (**CC BY-NC**). Research / non-commercial weights. See [`NOTICE.md`](NOTICE.md).

```python
import laya
agent = laya.load("Wouze/laya-ara")
```

## Results (stock → this card)

Same frozen JSONL. 21 Sep 2026.

| Task | n | Stock | laya-ara |
|---|---:|---:|---:|
| MASSIVE-ar intent, 20-opt | 2974 | 0.386 | **0.816** |
| MASSIVE-ar scenario, 18-way | 2974 | 0.427 | **0.865** |
| MASSIVE-ar hierarchical intent | 2694 | 0.536 | **0.893** |
| XNLI-ar | 5010 | 0.686 | **0.723** |
| OSACT4-A macro-F1 | 1000 | 0.726 | **0.862** |

v48 is worse than stock on AJGT and OSACT-HS. Full tables: [`results/v48_all_benches.json`](results/v48_all_benches.json). Other mixes: [`FINDINGS.md`](FINDINGS.md).

## Limits

- Short-list RAG only (k≤12). Not MIRACL nDCG@10.
- No span NER / span QA.
- Do not deploy as unattended moderation.

## Cite

```bibtex
@misc{alkhenizan2026layaara,
  title        = {laya-ara},
  author       = {Alkhenizan, Mohammad},
  year         = {2026},
  howpublished = {\url{https://huggingface.co/Wouze/laya-ara}}
}
```

Encoder: Marone et al. 2025 (mmBERT). Datasets: see [`citations.bib`](citations.bib).
