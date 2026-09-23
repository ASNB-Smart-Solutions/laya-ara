#!/usr/bin/env python3
"""Upload a local Laya checkpoint + this card to the Hugging Face Hub.

  export HF_TOKEN=hf_...
  python scripts/upload_to_hf.py --ckpt /path/to/laya-ar-v48 \\
      --repo-id Wouze/laya-ara --dry-run
  python scripts/upload_to_hf.py --ckpt /path/to/laya-ar-v48 \\
      --repo-id Wouze/laya-ara

Does not upload raw XNLI / OSACT tweet dumps. Weights that saw XNLI stay
research-only — the card says so.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = ["model.safetensors", "rl_agent_config.json"]


def copy_ckpt(src: Path, dest: Path) -> None:
    dest.mkdir(parents=True, exist_ok=True)
    for name in REQUIRED:
        p = src / name
        if not p.is_file():
            raise SystemExit(f"missing {p}")
        shutil.copy2(p, dest / name)
    for sub in ("encoder", "tokenizer"):
        if (src / sub).is_dir():
            if (dest / sub).exists():
                shutil.rmtree(dest / sub)
            shutil.copytree(src / sub, dest / sub)
    for extra in ("temperatures_train.json", "train_report.json"):
        if (src / extra).is_file():
            shutil.copy2(src / extra, dest / extra)
    for doc in ("NOTICE.md", "LICENSE", "CITATION.cff", "citations.bib", "FINDINGS.md", "RESULTS.md", "UPLOAD.md"):
        shutil.copy2(ROOT / doc, dest / doc)
    header = (ROOT / "huggingface.yaml").read_text()
    # GitHub README lists both models. The Hub NLU card is card.md only.
    body = (ROOT / "card.md").read_text()
    (dest / "README.md").write_text(header.rstrip() + "\n\n" + body.lstrip())
    for folder in ("results", "examples", "assets"):
        target = dest / folder
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(ROOT / folder, target)
    for name in (
        "config.json",
        "tokenizer_config.json",
        "configuration_laya.py",
        "modeling_laya.py",
        "tokenization_laya.py",
    ):
        shutil.copy2(ROOT / name, dest / name)
    leftover = dest / "results" / "v48_all_benches.json"
    if leftover.exists():
        leftover.unlink()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt", type=Path, required=True, help="local Laya dir")
    parser.add_argument("--repo-id", required=True, help="HF repo, e.g. user/laya-ara")
    parser.add_argument("--staging", type=Path, default=ROOT / ".staging_upload")
    parser.add_argument("--private", action="store_true", default=True)
    parser.add_argument("--public", action="store_true", help="create a public repo")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    private = not args.public
    if args.staging.exists():
        shutil.rmtree(args.staging)
    copy_ckpt(args.ckpt.resolve(), args.staging)
    print("staged", args.staging, "files", sorted(p.name for p in args.staging.iterdir()))
    if args.dry_run:
        print("dry-run: not uploading. Add --public only after you accept NOTICE.md.")
        return
    from huggingface_hub import HfApi

    api = HfApi()
    api.create_repo(args.repo_id, private=private, exist_ok=True, repo_type="model")
    api.upload_folder(
        folder_path=str(args.staging),
        repo_id=args.repo_id,
        repo_type="model",
        commit_message="Add laya-ara checkpoint and full bench tables",
    )
    print("uploaded", f"https://huggingface.co/{args.repo_id}")


if __name__ == "__main__":
    main()
