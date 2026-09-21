#!/usr/bin/env python3
"""Listwise short-list rerank + pairwise noul. Passages are invented."""

from __future__ import annotations

import os

os.environ.setdefault("USE_TF", "0")

import laya

# pip install laya==0.3.4
# Private Hub dump needs HF_TOKEN. Local: LAYA_AR_MODEL=/path/to/artifacts/laya-ara-rag
MODEL = os.environ.get("LAYA_AR_MODEL", "Wouze/laya-ara-rag")

STATE = {"query": "ما حكم الوضوء قبل قراءة القرآن؟"}

QUESTIONS = {
    "passage": {
        "type": "choice",
        "instructions": "Which passage is most relevant to the query?",
        "criteria": {
            "a": "الوضوء شرط للصلاة. أما قراءة القرآن من غير مس المصحف فالجمهور على الجواز.",
            "b": "زكاة الفطر تجب على كل مسلم قبل صلاة العيد صاعا من طعام.",
            "c": "صيام يوم عاشوراء سنة مؤكدة ويكفر سنة قبله.",
        },
    },
    "relevant_a": {
        "type": "noul",
        "instructions": "Is passage A relevant to the query about wudu before Quran recitation?",
    },
}


def main() -> None:
    agent = laya.load(MODEL, token=os.environ.get("HF_TOKEN"))
    print(agent.predict(STATE, QUESTIONS))


if __name__ == "__main__":
    main()
