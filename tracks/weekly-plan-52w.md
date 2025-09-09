# Week-by-Week Plan (52 Weeks)

Each week lists **Targets**, **Study**, **Build**, **Assess**. Adjust pace if needed.

## Weeks 1–4: Math + Python + Data
### Week 1
- **Targets:** Vectors/matrices; Python refresh; Git workflow.
- **Study:** Dot products, norms, projections; Python typing, venv, logging.
- **Build:** PCA from scratch on a toy dataset; CLI `datasanity` skeleton.
- **Assess:** Write unit tests for PCA; checklist EDA on 1 dataset.

### Week 2
- **Targets:** Matrix factorization; pandas mastery; plotting.
- **Study:** SVD & low-rank approx; pandas joins/groupby; matplotlib.
- **Build:** Implement SVD-based image compression; profiling notebook.
- **Assess:** PR review checklist; performance report (CPU time/memory).

### Week 3
- **Targets:** Probability basics; experiment hygiene.
- **Study:** Bayes rule; expectation/variance; sampling.
- **Build:** Bootstrap CI for mean/median; A/B test simulator.
- **Assess:** Interpret p-values and CIs on simulations.

### Week 4
- **Targets:** Information theory; data validation.
- **Study:** Entropy, cross-entropy, KL; Great Expectations basics.
- **Build:** Data validation suite on a messy CSV.
- **Assess:** Write bug report + fixes for 3 data issues.

## Weeks 5–8: Software Eng + ML Intro
### Week 5
- **Targets:** OOP & dataclasses; CLI tooling.
- **Study:** Design small libraries; dependency mgmt.
- **Build:** `mltoolkit` skeleton: config, IO, metrics.
- **Assess:** Mypy/ruff clean; 80% unit test coverage.

### Week 6
- **Targets:** Regression.
- **Study:** OLS, ridge/lasso; bias-variance.
- **Build:** Train ridge/lasso on housing data with CV.
- **Assess:** Compare metrics; document regularization effects.

### Week 7
- **Targets:** Classification.
- **Study:** Logistic regression, calibration.
- **Build:** Credit default classifier with calibration plot.
- **Assess:** ROC-AUC vs PR-AUC; class imbalance tactics.

### Week 8
- **Targets:** Trees & ensembles.
- **Study:** CART, RF, XGBoost; feature importances.
- **Build:** Gradient boosting baseline; SHAP exploration.
- **Assess:** Overfitting analysis; feature leakage checklist.

## Weeks 9–12: Unsupervised + Experimentation
### Week 9
- **Targets:** Clustering.
- **Study:** k-means, GMM, silhouette.
- **Build:** Customer segmentation; compare k.
- **Assess:** Stability across seeds.

### Week 10
- **Targets:** Dimensionality reduction.
- **Study:** PCA, t-SNE, UMAP.
- **Build:** 2D embeddings visualization.
- **Assess:** Interpretability notes.

### Week 11
- **Targets:** Experiment design.
- **Study:** Cross-val, ablations.
- **Build:** `mltoolkit` CV module.
- **Assess:** Reproducibility checklist.

### Week 12
- **Targets:** Feature engineering.
- **Study:** Encoders, scaling, target leakage traps.
- **Build:** Feature pipeline; persist with joblib.
- **Assess:** Offline/online skew analysis.

## Weeks 13–16: DL Foundations
### Week 13
- **Targets:** PyTorch basics.
- **Study:** Autograd; optimizers.
- **Build:** MLP for MNIST.
- **Assess:** Unit tests for forward/backward.

### Week 14
- **Targets:** CNNs & regularization.
- **Study:** Conv, pooling; dropout, label smoothing.
- **Build:** CIFAR-10 CNN with augmentations.
- **Assess:** Learning curves; early stopping.

### Week 15
- **Targets:** RNN/LSTM/GRU.
- **Study:** Sequence modeling.
- **Build:** Char-level model.
- **Assess:** Perplexity tracking; gradient issues doc.

### Week 16
- **Targets:** Training at scale.
- **Study:** AMP, DDP, checkpointing.
- **Build:** Convert CIFAR run to AMP; measure speedup.
- **Assess:** Profiling report.

## Weeks 17–20: Transformers & LLM Basics
### Week 17
- **Targets:** Attention & Transformers.
- **Study:** QKV, MHA; positional embeddings.
- **Build:** Tiny Transformer from scratch.
- **Assess:** Compare to baseline RNN.

### Week 18
- **Targets:** Tokenization.
- **Study:** BPE/Unigram; special tokens.
- **Build:** Train a tiny tokenizer; visualize merges.
- **Assess:** OOV behavior notes.

### Week 19
- **Targets:** Pretraining objectives.
- **Study:** CLM vs MLM vs seq2seq.
- **Build:** Finetune a small model on toy corpus.
- **Assess:** Perplexity vs downstream accuracy.

### Week 20
- **Targets:** Inference & decoding.
- **Study:** Temp, top‑p, beams; KV cache.
- **Build:** Decoding lab notebook.
- **Assess:** Quality vs latency/cost tradeoffs.

## Weeks 21–24: Finetuning & RAG
### Week 21
- **Targets:** LoRA/QLoRA/Adapters.
- **Study:** PEFT landscape.
- **Build:** QLoRA finetune on classification.
- **Assess:** Memory/throughput logs.

### Week 22
- **Targets:** RAG indexing.
- **Study:** Chunking, embeddings, vector DBs.
- **Build:** Build FAISS/Chroma index.
- **Assess:** Recall@k experiments.

### Week 23
- **Targets:** RAG retrieval & reranking.
- **Study:** Hybrid retrieval; rerankers.
- **Build:** Add reranker + query rewrite.
- **Assess:** Faithfulness eval.

### Week 24
- **Targets:** Safety & alignment basics.
- **Study:** Prompt attacks, PII filters.
- **Build:** Guardrails + eval harness.
- **Assess:** Red‑team report.

## Weeks 25–28: RL & RL for LLMs
### Week 25
- **Targets:** MDPs and value methods.
- **Study:** TD, Q‑learning.
- **Build:** Tabular Q‑learning.
- **Assess:** Convergence plots.

### Week 26
- **Targets:** Policy gradients.
- **Study:** REINFORCE, variance reduction.
- **Build:** Policy gradient on CartPole.
- **Assess:** Baseline vs no‑baseline.

### Week 27
- **Targets:** PPO.
- **Study:** Clipping, advantage, entropy bonuses.
- **Build:** PPO on discrete env.
- **Assess:** Sample efficiency.

### Week 28
- **Targets:** RLHF/DPO.
- **Study:** Preference modeling.
- **Build:** Tiny preference dataset; DPO finetune.
- **Assess:** Human eval rubric.

## Weeks 29–36: Systems & (LL)MLOps
### Week 29
- **Targets:** Data engineering.
- **Study:** Lakehouse, Parquet/Delta.
- **Build:** Batch ETL with Prefect + DVC.
- **Assess:** Lineage diagram.

### Week 30
- **Targets:** Validation & drift.
- **Study:** Great Expectations; PSI.
- **Build:** Data contracts + alerts.
- **Assess:** Incident doc for drift.

### Week 31
- **Targets:** Experiment tracking.
- **Study:** MLflow.
- **Build:** Track all DL runs.
- **Assess:** Metric dashboards.

### Week 32
- **Targets:** Model registry & CI/CD.
- **Study:** Registries; canary/shadow.
- **Build:** CI pipeline template.
- **Assess:** Rollback plan.

### Week 33
- **Targets:** Serving LLMs.
- **Study:** Quantization; autoscaling.
- **Build:** Simple FastAPI inference server.
- **Assess:** Latency SLOs.

### Week 34
- **Targets:** Observability.
- **Study:** Traces, prompt drift.
- **Build:** Logging + tracing middleware.
- **Assess:** p95/p99 latency report.

### Week 35
- **Targets:** Eval harness.
- **Study:** Static/dynamic evals.
- **Build:** Eval suite: correctness, toxicity, cost.
- **Assess:** Gate thresholds.

### Week 36
- **Targets:** Governance & privacy.
- **Study:** PII, policy engines.
- **Build:** Privacy scrubber + audit logs.
- **Assess:** Threat model doc.

## Weeks 37–44: Agentic AI
### Week 37
- **Targets:** Agent frameworks.
- **Study:** ReAct, Reflexion patterns.
- **Build:** ReAct agent with 2 tools.
- **Assess:** Success@K on tasks.

### Week 38
- **Targets:** Planning & decomposition.
- **Study:** Planner controllers.
- **Build:** Hierarchical planner.
- **Assess:** Path length metrics.

### Week 39
- **Targets:** Memory.
- **Study:** Episodic/semantic; vector memory.
- **Build:** Agent memory with aging.
- **Assess:** Retrieval quality.

### Week 40
- **Targets:** Tool use & verification.
- **Study:** Function calling; schemas.
- **Build:** Verified tool execution.
- **Assess:** Error/side‑effect rate.

### Week 41
- **Targets:** Multi‑agent systems.
- **Study:** Protocols; blackboard pattern.
- **Build:** 3‑agent collaboration demo.
- **Assess:** Cost vs quality vs time.

### Week 42
- **Targets:** Orchestration.
- **Study:** LangGraph; state machines.
- **Build:** Robust retries/backoff/idempotency.
- **Assess:** Fault injection tests.

### Week 43
- **Targets:** Safety.
- **Study:** Capability whitelists; sandboxing.
- **Build:** Permissioned agent executor.
- **Assess:** Red‑team transcripts.

### Week 44
- **Targets:** Productionization.
- **Study:** SLOs, budgets.
- **Build:** Observability & kill‑switch.
- **Assess:** On‑call runbook.

## Weeks 45–52: Capstones & Principal Skills
### Week 45
- **Targets:** Capstone discovery.
- **Study:** Problem selection; ROI.
- **Build:** RFC draft.
- **Assess:** Review with mentors.

### Week 46
- **Targets:** Capstone v1.
- **Study:** Data/contracts.
- **Build:** MVP agent with evals.
- **Assess:** Baseline metrics.

### Week 47
- **Targets:** Scale‑up.
- **Study:** Serving & caching.
- **Build:** Optimize latency/cost.
- **Assess:** p99 & budget targets.

### Week 48
- **Targets:** Safety & governance.
- **Study:** Privacy & red‑teaming.
- **Build:** Guardrails + audits.
- **Assess:** Incident drills.

### Week 49
- **Targets:** Rollout plan.
- **Study:** Canary/shadow.
- **Build:** Deployment plan.
- **Assess:** Risk register.

### Week 50
- **Targets:** Docs & training.
- **Study:** Runbooks; playbooks.
- **Build:** Onboarding docs.
- **Assess:** Dry run handoff.

### Week 51
- **Targets:** Executive comms.
- **Study:** Briefing docs.
- **Build:** 1‑pager + deck.
- **Assess:** Stakeholder review.

### Week 52
- **Targets:** Reflection & next year.
- **Study:** Tech radar.
- **Build:** 12‑month roadmap.
- **Assess:** Postmortem & goals.
