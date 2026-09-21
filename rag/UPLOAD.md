# Upload to Hugging Face

Default public name is **`laya-ara-rag`**. Local weights: `artifacts/laya-ara-rag` (symlink to `artifacts/laya-ar-ameen`).

This **replaces** the MIRACL-only specialist as the Hub RAG card. Do not upload `artifacts/laya-ar-rag` under this name.

## 1. What goes up

```
model.safetensors
rl_agent_config.json
temperatures_train.json   # if present
train_report.json
encoder/
tokenizer/
```

GitHub `README.md` has the tables and **no** Hub YAML. Upload prepends `huggingface.yaml`. Also ships `RESULTS.md`, `FINDINGS.md`, `DATA.md`, `NOTICE.md`, `LICENSE`, citations, `results/`, `examples/`, `assets/`.

**Never upload**

- `ameen-training-export/`
- `data/processed/**` (fatwa JSONL, gold questions, teacher lists)
- `*.pt` item caches
- any `lists.jsonl` / `fatwas.jsonl` / `evaluation_questions.json`

The upload script refuses those names if they appear next to the checkpoint.

## 2. One-time Hub setup

```bash
pip install -U huggingface_hub
huggingface-cli login
```

Suggested id: `Wouze/laya-ara-rag` (sibling of `Wouze/laya-ara`).

## 3. Dry run, then upload

```bash
cd /home/minecraft/Documents/GitHub/laya-ara-rag

python scripts/upload_to_hf.py \
  --ckpt /home/minecraft/Documents/GitHub/typesafe-jev-training/artifacts/laya-ara-rag \
  --repo-id Wouze/laya-ara-rag \
  --dry-run

# private (default)
python scripts/upload_to_hf.py \
  --ckpt /home/minecraft/Documents/GitHub/typesafe-jev-training/artifacts/laya-ara-rag \
  --repo-id Wouze/laya-ara-rag

# public only after you accept NOTICE.md / DATA.md
python scripts/upload_to_hf.py \
  --ckpt /home/minecraft/Documents/GitHub/typesafe-jev-training/artifacts/laya-ara-rag \
  --repo-id Wouze/laya-ara-rag \
  --public
```

## 4. Card checks

- No fatwa dump in the file list
- `DATA.md` describes the logs without query strings or answers
- Anti-claims: not a retriever, not nDCG@10, not 21/21
- Example uses invented passages, `laya.load`, not `AutoModelForCausalLM`
- model-index matches `results/rag_all_benches.json` public rows
- NLU numbers stay on `Wouze/laya-ara`

## 5. Related checkpoints

| Local dir | Public name | Upload if |
|---|---|---|
| `artifacts/laya-ar-v48` | **laya-ara** | NLU card (XNLI = NC) |
| `artifacts/laya-ara-rag` (`laya-ar-ameen`) | **laya-ara-rag** | this card |
| `artifacts/laya-ar-rag` | — | ablation only; do not publish as laya-ara-rag |
| `artifacts/laya-ar-quote` | laya-ara-quote | sentiment / hate |
| `artifacts/laya-ar-triage` | laya-ara-triage | synthetic Gulf demo |
