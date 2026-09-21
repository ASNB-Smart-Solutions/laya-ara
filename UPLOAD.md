# Upload to Hugging Face

Do this after you pick which checkpoint to publish (`laya-ar-v48` is the scored one today).

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

This repo adds `README.md` (the card), `NOTICE.md`, `LICENSE`, and `results/`.

Do **not** upload `data/processed/**` JSONL (XNLI and tweets).

## 2. One-time Hub setup

```bash
pip install -U huggingface_hub
huggingface-cli login          # or export HF_TOKEN=hf_...
```

Create the model repo in the UI **or** let the script create it (default **private**).

Suggested id: `YOUR_USER/laya-arabic-system-one`

## 3. Dry run, then upload

```bash
cd /home/minecraft/Documents/GitHub/laya-arabic-system-one

# stage only — no network
python scripts/upload_to_hf.py \
  --ckpt /home/minecraft/Documents/GitHub/typesafe-jev-training/artifacts/laya-ar-v48 \
  --repo-id YOUR_USER/laya-arabic-system-one \
  --dry-run

# private upload (default)
python scripts/upload_to_hf.py \
  --ckpt /home/minecraft/Documents/GitHub/typesafe-jev-training/artifacts/laya-ar-v48 \
  --repo-id YOUR_USER/laya-arabic-system-one

# public only after you accept NOTICE.md (v48 saw XNLI = NC)
python scripts/upload_to_hf.py \
  --ckpt /home/minecraft/Documents/GitHub/typesafe-jev-training/artifacts/laya-ar-v48 \
  --repo-id YOUR_USER/laya-arabic-system-one \
  --public
```

## 4. Card checks on the Hub

- YAML `license` / NC note visible
- **All** tables present (locked, MASSIVE variants, translated NLU, 7×2 RAG) — not only the top 5
- `base_model: convaiinnovations/laya-multilingual`
- Anti-claims section not deleted
- Example snippet uses `laya.load`, not `AutoModelForCausalLM`

## 5. Later checkpoints

Quote-mix (no XNLI) and RAG-FT / triage-FT will land under the training repo as:

- `artifacts/laya-ar-quote`
- `artifacts/laya-ar-rag`
- `artifacts/laya-ar-triage`

Re-run the same script with `--ckpt` pointed at the winner. Update `results/` if the new benches beat v48.
