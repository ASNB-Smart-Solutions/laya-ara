"""Hub loader. AutoModel.from_pretrained(..., trust_remote_code=True) calls laya.load."""

from __future__ import annotations

import os

import torch
from torch import nn
from transformers import PreTrainedModel

from .configuration_laya import LayaConfig


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
        except ImportError as exc:
            raise ImportError("Install the Laya runtime first: pip install 'laya==0.3.4'") from exc
        agent = laya.load(str(pretrained_model_name_or_path), token=token)
        if config is None:
            config = LayaConfig()
        model = cls(config)
        model.agent = agent
        return model


class LayaForSequenceClassification(LayaModel):
    """Same loader. The text-classification snippet asks for this class name."""
