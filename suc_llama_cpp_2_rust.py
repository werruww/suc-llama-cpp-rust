# -*- coding: utf-8 -*-
"""suc_llama-cpp-2_RUST.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1HrH9rtnYxNmTTndN7hA2d7DHhXj4nBwE
"""







"""https://github.com/Corallus-Caninus/rust-llama.cpp"""

!curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y

import os
os.environ['PATH'] += ":/root/.cargo/bin"

!cargo --version



!git clone --recursive https://github.com/utilityai/llama-cpp-rs

# Commented out IPython magic to ensure Python compatibility.
# %cd llama-cpp-rs

!cargo run --release --bin simple -- \
  --prompt "hi" \
  hf-model bartowski/Mistral-7B-Instruct-v0.3-GGUF Mistral-7B-Instruct-v0.3-Q4_K_M.gguf





!cargo run --release --bin simple -- \
  --prompt "Who is Napoleon Bonaparte?" \
  file /content/models/Mistral-7B-Instruct-v0.3-Q4_K_M.gguf

!cargo run --release --bin simple -- --help

!cargo run --release --bin simple -- \
  --prompt "Who is Napoleon Bonaparte?" \
  hf-model bartowski/Mistral-7B-Instruct-v0.3-GGUF Mistral-7B-Instruct-v0.3-Q4_K_M.gguf

bartowski/Mistral-7B-Instruct-v0.3-GGUF

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/models
!wget https://huggingface.co/bartowski/Mistral-7B-Instruct-v0.3-GGUF/resolve/main/Mistral-7B-Instruct-v0.3-IQ1_M.gguf

# Commented out IPython magic to ensure Python compatibility.
# %cd /content/llama-cpp-rs

!cargo run --release --bin simple -- \
  --prompt "Who is Napoleon Bonaparte?" \
  local /content/models/Mistral-7B-Instruct-v0.3-IQ1_M.gguf