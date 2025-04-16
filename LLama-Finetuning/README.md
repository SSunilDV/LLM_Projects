
# 🦙 LLaMA 3.2 Fine-Tuning for Conversational AI

NOte : Please Download the Ipynb file if preview doesnt work in Github.

This project demonstrates how to fine-tune Meta’s **LLaMA 3.2 (3B Instruct)** model using the **Unsloth** framework along with **LoRA (Low-Rank Adaptation)** for efficient, scalable training on conversational datasets.

---

## 🚀 Project Overview

Large Language Models (LLMs) are powerful, but tuning them for specific tasks or domains makes them even more impactful.  
In this project:

- The **mlabonne/FineTome-100k** dataset was used to fine-tune LLaMA 3 for conversation-based tasks.
- Efficient training was achieved using:
   - 4-bit quantized model loading via `Unsloth`.
   - Parameter-Efficient Fine-Tuning (LoRA).
- Structured prompts were used during inference for better response reliability, applying prompt templates similar to few-shot learning.

---

## ⚙️ Tech Stack

- [Unsloth](https://github.com/unslothai/unsloth) — optimized LLM loading and fine-tuning.
- [Huggingface Transformers](https://huggingface.co/docs/transformers/index) — model architecture and inference.
- [TRL (Huggingface)](https://huggingface.co/docs/trl/index) — supervised fine-tuning trainer (`SFTTrainer`).
- [Datasets](https://huggingface.co/docs/datasets/index) — for loading and managing `FineTome-100k`.

---

## 💡 Key Features

✅ **LoRA Fine-Tuning** — Parameter-efficient updates.  
✅ **4-bit Quantization** — Reduced VRAM usage.  
✅ **Chat Template Preparation** — Structured conversational input/output.  
✅ **Prompt Engineering** — Controlled inference behavior via prompt shots.

---

## 🧑‍💻 How to Run

1. Install dependencies:

```bash
pip install unsloth transformers trl datasets
```

2. Run the training script:

```python
from unsloth import FastLanguageModel
from datasets import load_dataset
from trl import SFTTrainer
from transformers import TrainingArguments
```

*(See the notebook for full code: [`LLama_3_2_Finetune.ipynb`](./LLama_3_2_Finetune.ipynb))*
