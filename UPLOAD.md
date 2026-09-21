# Upload to Hugging Face

Do this after you pick which checkpoint to publish. Default public name is **`laya-ara`** (v48 weights at `artifacts/laya-ar-v48`).

## 1. What goes up

From the training box, a Laya dir looks like:

```
model.safetensors
rl_agent_config.json
temperatures_train.json
train_report.json
encoder/
tokenizer/
```

This repo adds the card (`README.md` with Hub `model-index` for v48 + rag-ft + quote), `FINDINGS.md`, `NOTICE.md`, `LICENSE`, `CITATION.cff`, `citations.bib`, `results/`, and `examples/`.

Do **not** upload `data/processed/**` JSONL (XNLI and tweets).

## 2. One-time Hub setup

```bash
pip install -U huggingface_hub
huggingface-cli login          # or export HF_TOKEN=hf_...
```

Create the model repo in the UI **or** let the script create it (default **private**).

Suggested id: `Wouze/laya-ara`

## 3. Dry run, then upload

```bash
cd /home/minecraft/Documents/GitHub/laya-ara

# stage only — no network
python scripts/upload_to_hf.py \
  --ckpt /home/minecraft/Documents/GitHub/typesafe-jev-training/artifacts/laya-ar-v48 \
  --repo-id Wouze/laya-ara \
  --dry-run

# private upload (default)
python scripts/upload_to_hf.py \
  --ckpt /home/minecraft/Documents/GitHub/typesafe-jev-training/artifacts/laya-ar-v48 \
  --repo-id Wouze/laya-ara

# public only after you accept NOTICE.md (v48 saw XNLI = NC)
python scripts/upload_to_hf.py \
  --ckpt /home/minecraft/Documents/GitHub/typesafe-jev-training/artifacts/laya-ar-v48 \
  --repo-id Wouze/laya-ara \
  --public
```

## 4. Card checks on the Hub

- YAML `license` / NC note visible
- **All** tables present (locked, MASSIVE variants, translated NLU, 7×2 RAG) — not only the top 5
- `base_model: convaiinnovations/laya-multilingual`
- Anti-claims section not deleted
- Example snippet uses `laya.load`, not `AutoModelForCausalLM`
- `CITATION.cff` + `citations.bib` + `FINDINGS.md` present; model-index metrics match `results/v48_all_benches.json`

## 5. Later checkpoints (training repo)

| Checkpoint | Status | Upload if |
|---|---|---|
| Local dir | Public name | Upload if |
|---|---|---|
| `artifacts/laya-ar-v48` | **laya-ara** | default Hub dump (research / NC) |
| `artifacts/laya-ar-quote` | laya-ara-quote | sentiment / hate product; **not** MASSIVE/XNLI winner |
| `artifacts/laya-ar-triage` | laya-ara-triage | product demo only; not production tickets |
| `artifacts/laya-ar-rag` | laya-ara-rag | k≤12 relevance / rerank; **not** a retriever, **not** locked-suite winner |

Re-run the same script with `--ckpt` pointed at the winner. Keep **laya-ara** (v48) as the Hub default unless the card is explicitly quote-mix.
