#!/usr/bin/env python3
"""One Gulf WhatsApp pass: queue + urgency + refund + churn."""

from __future__ import annotations

import os

os.environ.setdefault("USE_TF", "0")

import laya

MODEL = os.environ.get("LAYA_AR_MODEL", "convaiinnovations/laya-multilingual")

STATE = {
    "channel": "whatsapp",
    "message": "الحوالة ما وصلت وصار لها يومين، أبي استرجاع الحين وإلا بنقلع",
}

QUESTIONS = {
    "queue": {
        "type": "choice",
        "instructions": "Which support queue?",
        "criteria": {
            "billing": "payments, refunds, charges",
            "technical": "bugs, outages, app issues",
            "account": "login, KYC, profile",
            "sales": "plans and pricing",
            "other": "none of the above",
        },
    },
    "urgency": {
        "type": "score",
        "instructions": "Urgency level?",
        "criteria": ["low", "medium", "high", "critical"],
    },
    "refund_requested": {"type": "noul", "instructions": "Does the user ask for a refund?"},
    "churn_threat": {"type": "noul", "instructions": "Does the user threaten to cancel or leave?"},
}


def main() -> None:
    agent = laya.load(MODEL)
    out = agent.predict(STATE, QUESTIONS)
    print(out)


if __name__ == "__main__":
    main()
