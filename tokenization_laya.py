"""Point AutoTokenizer at tokenizer/, where the Laya checkpoint keeps it."""


class LayaTokenizer:
    @classmethod
    def register_for_auto_class(cls, auto_class="AutoTokenizer"):
        return

    @classmethod
    def from_pretrained(cls, pretrained_model_name_or_path, *inputs, **kwargs):
        for key in ("trust_remote_code", "config", "subfolder", "_from_auto", "code_revision"):
            kwargs.pop(key, None)
        from transformers import PreTrainedTokenizerFast

        return PreTrainedTokenizerFast.from_pretrained(
            pretrained_model_name_or_path,
            *inputs,
            subfolder="tokenizer",
            **kwargs,
        )
