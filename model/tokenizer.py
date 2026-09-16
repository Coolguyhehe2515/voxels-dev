import re
import json

TOKEN_PATTERN = re.compile(
    r'''//[^\n]*|#[^\n]*|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'|[A-Za-z_][A-Za-z0-9_]*|\d+(?:\.\d+)?|==|!=|<=|>=|=>|->|::|&&|\|\||\+\+|--|[{}()\[\],.:;+\-*/%=<>!?#@]|\n|[ \t]+'''
)


class Tokenizer:
    def __init__(self, text=None, tokens=None):
        if tokens is not None:
            self.tokens = tokens
        else:
            self.tokens = self.tokenize(text or "")

        self.stoi = {
            token: i for i, token in enumerate(self.tokens)
        }

        self.itos = {
            i: token for i, token in enumerate(self.tokens)
        }

    @staticmethod
    def tokenize(text):
        return TOKEN_PATTERN.findall(text)

    @property
    def vocab_size(self):
        return len(self.tokens)

    def encode(self, text):
        return [
            self.stoi[token]
            for token in self.tokenize(text)
            if token in self.stoi
        ]

    def decode(self, ids):
        return "".join(
            self.itos[int(token)]
            for token in ids
            if int(token) in self.itos
        )

    def save(self, path):
        with open(path, "w", encoding="utf-8") as f:
            json.dump(
                {"tokens": self.tokens},
                f,
                ensure_ascii=False,
                indent=2
            )

    @classmethod
    def load(cls, path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)

        return cls(tokens=data["tokens"])
