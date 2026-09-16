import torch

def create_dataset(tokens, context_size):
    inputs = []
    targets = []

    for i in range(len(tokens) - context_size):
        inputs.append(tokens[i:i + context_size])
        targets.append(tokens[i + 1:i + context_size + 1])

    return (
        torch.tensor(inputs, dtype=torch.long),
        torch.tensor(targets, dtype=torch.long)
    )
