from ..base import BaseGPTQModel


class StableLMEpochGPTQ(BaseGPTQModel):
    base_modules = ["model.embed_tokens", "model.norm"]

    layers_node = "model.layers"
    layer_type = "DecoderLayer"
    layer_modules = [
        ["self_attn.k_proj", "self_attn.v_proj", "self_attn.q_proj"],
        ["self_attn.o_proj"],
        ["mlp.up_proj", "mlp.gate_proj"],
        ["mlp.down_proj"],
    ]
