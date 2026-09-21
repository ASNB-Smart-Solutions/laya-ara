# Training data

**laya-ara-rag** is trained on a public Wikipedia replay plus in-house Arabic retrieval logs. The in-house corpus is not redistributed with the weights.

## Public

- MIRACL-ar **train** pairwise and listwise (human positives / negatives). Dev stays frozen for evaluation.
- MASSIVE-ar, 2,000 items, so `choice` option markers remain stable.
- XNLI is not used.

## In-house Arabic retrieval

Production search logs over a Gulf / MSA fiqh collection (~31k documents; ~8.8k unique queries). Labels are cross-encoder teacher ranks, not clicks.

Training keeps pairs only when the teacher score gap is at least 0.08. Listwise gold is teacher rank-1; negatives are taken from much lower ranks. A sealed human hold-out and a 200-query teacher-agreement split never enter training.

Snippets are truncated so a 12-way `choice` fits `max_len` 1024. Total mix: **35,591** items, one epoch.

## Citation

Cite public rows from [`citations.bib`](citations.bib). For the in-house logs, cite this card and describe them as unreleased retrieval data.

Access or collaboration: [Mohammad Alkhenizan on LinkedIn](https://www.linkedin.com/in/mohammad-alkhenizan-537623257).
