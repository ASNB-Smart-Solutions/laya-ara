"""Transformers config for the Hub "Use this model" button.

The checkpoint itself is a Laya agent. This class exists so AutoConfig can
load the repo when trust_remote_code=True.
"""

from transformers import PretrainedConfig


class LayaConfig(PretrainedConfig):
    model_type = "modernbert"

    def __init__(self, **kwargs):
        kwargs.setdefault("id2label", {0: "use-laya-predict"})
        kwargs.setdefault("label2id", {"use-laya-predict": 0})
        super().__init__(**kwargs)
