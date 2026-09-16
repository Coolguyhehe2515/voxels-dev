import torch

from tokenizer import CharTokenizer
from model import TinyTransformer

checkpoint = torch.load(
    "voxeldev-core.pt",
    map_location="cpu"
)

tokenizer = CharTokenizer("".join(checkpoint["chars"]))

model = TinyTransformer(
    vocab_size=len(checkpoint["chars"]),
    context_size=checkpoint["context_size"]
)

model.load_state_dict(checkpoint["model"])
model.eval()

prompt = input("Prompt: ")

tokens = tokenizer.encode(prompt)

x = torch.tensor(
    [tokens[-checkpoint["context_size"]:]],
    dtype=torch.long
)

with torch.no_grad():
    logits = model(x)

next_token = torch.argmax(
    logits[:, -1, :],
    dim=-1
).item()

tokens.append(next_token)

print(tokenizer.decode(tokens))
