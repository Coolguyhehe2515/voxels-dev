# voxeldev

voxeldev is an experimental AI coding agent built from scratch.

## voxeldev-core

The first version uses a tiny character-level Transformer implemented with PyTorch.

Pipeline:

text
↓
character tokenizer
↓
token IDs
↓
Transformer
↓
next-token prediction
↓
generated text

## Development

The project is designed to eventually become a coding agent capable of:

- understanding project context
- reading source files
- analyzing images
- inspecting ZIP/JAR archives
- searching project files
- detecting syntax errors
- editing files
- running tests
- generating code
