#!/usr/bin/env python3
"""Upload laya-ara-rag weights + the RAG card. GitHub lives in this monorepo.

  python scripts/upload_rag_to_hf.py \\
      --ckpt /path/to/artifacts/laya-ara-rag \\
      --repo-id Wouze/laya-ara-rag --dry-run
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAG = ROOT / "rag"
REQUIRED = ["model.safetensors", "rl_agent_config.json"]
BLOCKED_NAMES = {
    "lists.jsonl",
    "fatwas.jsonl",
    "evaluation_questions.json",
    "qrels.tsv",
    "pairs.jsonl",
    "triples.jsonl",
}
BLOCKED_DIR_PARTS = {"ameen-training-export", "ameen_rag", "processed"}


def _refuse_if_dump(path: Path) -> None:
    parts = {p.lower() for p in path.parts}
    if parts & BLOCKED_DIR_PARTS:
        raise SystemExit(f"refusing to stage data dump path: {path}")
    if path.name.lower() in BLOCKED_NAMES:
        raise SystemExit(f"refusing to stage {path.name}")


def copy_ckpt(src: Path, dest: Path) -> None:
    src = src.resolve()
    _refuse_if_dump(src)
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
    for doc in (
        "NOTICE.md",
        "DATA.md",
        "LICENSE",
        "CITATION.cff",
        "citations.bib",
        "FINDINGS.md",
        "RESULTS.md",
        "UPLOAD.md",
    ):
        shutil.copy2(RAG / doc, dest / doc)
    shutil.copy2(RAG / "config.json", dest / "config.json")
    for name in (
        "tokenizer_config.json",
        "configuration_laya.py",
        "modeling_laya.py",
        "tokenization_laya.py",
    ):
        shutil.copy2(ROOT / name, dest / name)
    header = (RAG / "huggingface.yaml").read_text()
    body = (RAG / "README.md").read_text()
    (dest / "README.md").write_text(header.rstrip() + "\n\n" + body.lstrip())
    (dest / "results").mkdir(exist_ok=True)
    for name in ("rag_all_benches.json", "all_cards.json", "README.md"):
        shutil.copy2(ROOT / "results" / name, dest / "results" / name)
    (dest / "examples").mkdir(exist_ok=True)
    shutil.copy2(ROOT / "examples" / "predict_rerank.py", dest / "examples" / "predict_rerank.py")
    shutil.copy2(ROOT / "examples" / "colab_rag.ipynb", dest / "examples" / "colab_rag.ipynb")
    if (ROOT / "assets").is_dir():
        if (dest / "assets").exists():
            shutil.rmtree(dest / "assets")
        shutil.copytree(ROOT / "assets", dest / "assets")
    for p in dest.rglob("*"):
        if p.is_file():
            _refuse_if_dump(p)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--ckpt", type=Path, required=True)
    parser.add_argument("--repo-id", required=True)
    parser.add_argument("--staging", type=Path, default=ROOT / ".staging_upload_rag")
    parser.add_argument("--private", action="store_true", default=True)
    parser.add_argument("--public", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.staging.exists():
        shutil.rmtree(args.staging)
    copy_ckpt(args.ckpt.resolve(), args.staging)
    print("staged", args.staging, "files", sorted(p.name for p in args.staging.iterdir()))
    if args.dry_run:
        print("dry-run: not uploading.")
        return
    from huggingface_hub import HfApi

    api = HfApi()
    api.create_repo(args.repo_id, private=not args.public, exist_ok=True, repo_type="model")
    api.upload_folder(
        folder_path=str(args.staging),
        repo_id=args.repo_id,
        repo_type="model",
        commit_message="Add laya-ara-rag checkpoint and RAG benches",
    )
    print("uploaded", f"https://huggingface.co/{args.repo_id}")


if __name__ == "__main__":
    main()
