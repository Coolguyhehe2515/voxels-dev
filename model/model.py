import torch
import torch.nn as nn

class TinyTransformer(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        embed_dim: int = 128,
        heads: int = 4,
        layers: int = 4,
        context_size: int = 128
    ):
        super().__init__()

        self.context_size = context_size

        self.token_embedding = nn.Embedding(vocab_size, embed_dim)
        self.position_embedding = nn.Embedding(context_size, embed_dim)

        layer = nn.TransformerEncoderLayer(
            d_model=embed_dim,
            nhead=heads,
            batch_first=True
        )

        self.transformer = nn.TransformerEncoder(
            layer,
            num_layers=layers
        )

        self.output = nn.Linear(embed_dim, vocab_size)

    def forward(self, tokens):
        batch, length = tokens.shape

        positions = torch.arange(
            length,
            device=tokens.device
        )

        x = (
            self.token_embedding(tokens)
            + self.position_embedding(positions)
        )

        mask = torch.triu(
            torch.ones(
                length,
                length,
                device=tokens.device
            ),
            diagonal=1
        ).bool()

        x = self.transformer(x, mask=mask)

        return self.output(x)
