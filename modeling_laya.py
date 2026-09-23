"""Hub loader. AutoModel.from_pretrained(..., trust_remote_code=True) calls laya.load."""

from __future__ import annotations

import os

import torch
from torch import nn
from transformers import PreTrainedModel

from .configuration_laya import LayaConfig

# Same calls as the model card. The Hub Colab cell only loads the pipeline,
# so from_pretrained runs one of these and prints the answers.
_NLU_EXAMPLE = (
    {"message": "الحوالة ما وصلت، أبي استرجاع وإلا بنقلع"},
    {
        "queue": {
            "type": "choice",
            "instructions": "Support queue",
            "criteria": {
                "billing": "payments, refunds",
                "technical": "bugs, outages",
                "other": "none of the above",
            },
        },
        "refund": {"type": "noul", "instructions": "Asks for a refund?"},
    },
)
_RAG_EXAMPLE = (
    {"query": "ما حكم الوضوء قبل قراءة القرآن؟"},
    {
        "passage": {
            "type": "choice",
            "instructions": "Which passage is most relevant to the query?",
            "criteria": {
                "a": "الوضوء شرط للصلاة لا للقراءة عند جمهور الفقهاء.",
                "b": "زكاة الفطر تجب على كل مسلم قبل صلاة العيد.",
                "c": "صيام عاشوراء سنة مؤكدة عند الحنابلة.",
            },
        },
        "relevant": {"type": "noul", "instructions": "Is passage A relevant to the query?"},
    },
)


def _format_example(state: dict, questions: dict, answers: dict) -> str:
    lines = ["Example", ""]
    for key, value in state.items():
        lines.append(key)
        lines.append(f"  {value}")
        lines.append("")
    for qid, spec in questions.items():
        ans = answers[qid]
        title = spec.get("instructions") or qid
        lines.append(f"{qid}  ·  {title}")
        if ans["type"] == "choice":
            ranked = sorted(ans["probabilities"].items(), key=lambda item: item[1], reverse=True)
            criteria = spec.get("criteria") or {}
            width = max(len(str(key)) for key, _ in ranked)
            for key, prob in ranked:
                mark = "→" if key == ans["choice"] else " "
                gloss = criteria.get(key)
                extra = f"   {gloss}" if gloss else ""
                lines.append(f"  {mark} {key:<{width}}  {prob * 100:5.1f}%{extra}")
        elif ans["type"] == "noul":
            yes = float(ans["noul"])
            picked = "yes" if yes >= 0.5 else "no"
            for label, prob in (("yes", yes), ("no", 1.0 - yes)):
                mark = "→" if label == picked else " "
                lines.append(f"  {mark} {label:<3}  {prob * 100:5.1f}%")
        else:
            lines.append(f"  score {ans.get('score')}")
        lines.append("")
    return "\n".join(lines).rstrip()


def _print_example(agent, repo_id: str) -> None:
    state, questions = _RAG_EXAMPLE if "laya-ara-rag" in repo_id else _NLU_EXAMPLE
    answers = agent.predict(state, questions)["answers"]
    print(_format_example(state, questions, answers))


class LayaModel(PreTrainedModel):
    config_class = LayaConfig

    def __init__(self, config):
        super().__init__(config)
        self.agent = None
        # Pipeline init reads model.device via parameters(). Weights live on the agent.
        self.anchor = nn.Parameter(torch.zeros(1), requires_grad=False)

    def predict(self, state, questions):
        if self.agent is None:
            raise RuntimeError("Call from_pretrained before predict.")
        return self.agent.predict(state, questions)

    def show(self, state, questions):
        out = self.predict(state, questions)
        print(_format_example(state, questions, out["answers"]))
        return out

    def forward(self, input_ids=None, attention_mask=None, **kwargs):
        raise RuntimeError(
            "This checkpoint is a Laya typed-decision model. "
            "Call model.predict(state, questions). "
            "pip install 'laya==0.3.4'."
        )

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *model_args, **kwargs):
        config = kwargs.pop("config", None)
        token = kwargs.pop("token", None)
        os.environ.setdefault("USE_TF", "0")
        try:
            import laya
        except ImportError:
            import subprocess
            import sys

            install_error = None
            for cmd in (
                [sys.executable, "-m", "pip", "install", "laya==0.3.4"],
                ["pip", "install", "laya==0.3.4"],
            ):
                try:
                    subprocess.check_call(cmd)
                    install_error = None
                    break
                except (OSError, subprocess.CalledProcessError) as exc:
                    install_error = exc
            if install_error is not None:
                raise ImportError("Could not install laya==0.3.4. Run: pip install 'laya==0.3.4'") from install_error
            import laya
        agent = laya.load(str(pretrained_model_name_or_path), token=token)
        if config is None:
            config = LayaConfig()
        model = cls(config)
        model.agent = agent
        _print_example(agent, str(pretrained_model_name_or_path))
        return model


class LayaForSequenceClassification(LayaModel):
    """Same loader. The text-classification snippet asks for this class name."""
