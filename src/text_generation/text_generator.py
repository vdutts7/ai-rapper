import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def generate_text(prompt):
    model = AutoModelForCausalLM.from_pretrained('eminem').to("cuda")
    tokenizer = AutoTokenizer.from_pretrained('distilgpt2', use_fast=True)
    tokens = tokenizer.encode(prompt, return_tensors='pt')
    tokens = tokens.to("cuda")
    attn_mask = torch.ones_like(tokens)
    out = model.generate(tokens, attention_mask=attn_mask, num_beams=5, early_stopping=True, max_length=250, no_repeat_ngram_size=2)
    rap = tokenizer.decode(out[0])
    return out