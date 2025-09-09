# Phase 4 — NLP & LLMs (Weeks 25–32)

## Foundations
- Tokenization: BPE/WordPiece/Unigram; byte‑level; special tokens.
- Transformer math: QKV projections; scaled dot‑product attention; MHA; position encodings (sinusoidal, RoPE, ALiBi).
- Pretraining objectives: CLM, MLM, seq2seq; pretraining vs finetuning vs instruction‑tuning.

## Finetuning & Inference
- Parameter‑efficient finetuning: LoRA, QLoRA, adapters, IA3; quantization (8/4/3‑bit).
- Inference: KV cache; paged attention; speculative decoding; beam vs nucleus vs temperature.
- Safety & alignment: instruction following, RLHF, DPO; red‑teaming basics.

## RAG Systems
- Indexing: chunking strategies; embeddings; vector DB tradeoffs.
- Retrieval: dense vs hybrid; rerankers; query‑rewriting; grounding.
- Evaluation: answer faithfulness, hallucination detection, exactness, latency/cost.

## Deliverables
- Build: Small domain RAG with eval harness (`ExactMatch`, `F1`, `Faithfulness`).
- Finetune: QLoRA on task dataset; compare vs RAG-only approach.
