import torch
import torch.nn.functional as F

from tokenizer import CharTokenizer
from dataset import create_dataset
from model import TinyTransformer

with open("data/train.txt", "r", encoding="utf-8") as file:
    text = file.read()

tokenizer = CharTokenizer(text)

tokens = tokenizer.encode(text)

context_size = min(64, max(8, len(tokens) - 1))

x, y = create_dataset(tokens, context_size)

model = TinyTransformer(
    vocab_size=tokenizer.vocab_size,
    context_size=context_size
)

optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=3e-4
)

for step in range(1000):
    logits = model(x)

    loss = F.cross_entropy(
        logits.reshape(-1, tokenizer.vocab_size),
        y.reshape(-1)
    )

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    if step % 100 == 0:
        print(f"step={step} loss={loss.item():.4f}")

torch.save(
    {
        "model": model.state_dict(),
        "chars": tokenizer.chars,
        "context_size": context_size
    },
    "voxeldev-core.pt"
)

print("Training complete.")
