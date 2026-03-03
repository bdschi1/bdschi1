## An open and evolving collection of repos exploring how AI, fundamental, and quantitative methods apply to institutional investment research. 

Ideas come from experience managing long/short institutional equity portfolios, academic research we are fortunate to have access to, and the open-source community. Each repo is both a working tool and a learning exercise — built to educate and be educated by. Input and perspectives are welcome. 

Created and maintained by a former long/short equity portfolio manager with 20+ years of institutional buy-side experience.

*Curiosity compounds. Rigor endures.*

---

## Current Focus
Evaluating and improving LLM performance on financial reasoning tasks — building the rubrics, adversarial tests, preference data, and multi-agent systems to evaluate if AI models can meet institutional-grade investment standards.

---

## Sample Repositories

### Evaluation Frameworks

**[investment-workflow-evals](https://github.com/bdschi1/investment-workflow-evals)** — Scoring rubrics for the full institutional workflow (thesis → catalysts → sizing → risk → monitoring → post-mortem). Adversarial variants target specific LLM failure modes: regime-blind extrapolation, confident nonsense on illiquid names, circular reasoning between price targets and multiples.

**[fin-reasoning-eval](https://github.com/bdschi1/fin-reasoning-eval)** — 306 finance reasoning problems (valuation, accounting, credit, portfolio math) with difficulty grading and worked solutions. Tests quantitative rigor, not financial vocabulary.

### Red Teaming & Compliance

**[redflag-ex1-analyst](https://github.com/bdschi1/redflag-ex1-analyst)** — Rule-based red-flag detection for analyst research notes. Identifies buried assumptions, one-sided risk presentation, stale comps, missing sensitivity analysis, and filler content. PDF/DOCX ingestion with section-aware parsing. Same adversarial mindset applied to LLM-generated financial content.

### Multi-Agent Systems

**[multi-agent-investment-committee](https://github.com/bdschi1/multi-agent-investment-committee)** — Five-agent investment committee (sector analyst, short analyst, risk manager, macro analyst, portfolio manager) on LangGraph. Parallel assessments, structured debate, committee memo with position sizing. 6-dimension eval harness, Shapley attribution, 6 portfolio optimizers. Multi-provider LLM support. Bloomberg and IBKR adapters available.

### Backtesting

**[backtest-lab](https://github.com/bdschi1/backtest-lab)** — Event-driven backtesting with realistic execution (spread, market impact, slippage, commission, borrow costs). Regime detection (threshold + HMM). Statistical inference (PSR, MinTRL, FDR corrections). Bias guards for lookahead leakage, walk-forward degradation, and overfitting. Bridges to MAIC, ls-portfolio-lab, redflag, and fund-tracker-13f.

### Portfolio Analytics

**[ls-portfolio-lab](https://github.com/bdschi1/ls-portfolio-lab)** — L/S portfolio construction and risk analysis. Performance attribution, drawdown decomposition, rebalancing, trade impact modeling. Gross/net exposure, factor concentration, rolling Sharpe, max drawdown duration. Yahoo, Bloomberg, and IB data providers. Streamlit dashboard.

---

## How the Repos Relate

![Tier 1 Repository Ecosystem](tier1_repo_ecosystem.png)

---

## Applied AI Evaluation & Alignment

#### Evaluation Methodology
* **Methods:** RLHF preference data; adversarial red teaming; guardrail/safety taxonomy testing.
* **Infrastructure:** Scoring rubrics; golden answer authoring; domain-specific fine-tuning (SFT).
* **Architecture:** Multi-agent orchestration; prompt engineering; role-integrity testing.
* **Benchmarking:** 306-problem finance reasoning benchmark (valuation, accounting, credit, portfolio math) with difficulty grading and multi-model leaderboard; institutional workflow evals covering thesis → catalysts → sizing → risk → monitoring → post-mortem.
* **Model Audit:** Graph-based structural auditing of LLM-generated Excel models — dependency tracing, circular reference detection, balance sheet consistency checks, complexity scoring.

#### RLHF & Preference Data
* **Signal:** Authoring preference pairs where domain-expertise signal outweighs stylistic polish.
* **Criteria:** Transparency of assumptions; quantitative precision; intellectual honesty regarding uncertainty.
* **Calibration:** Expert-led alignment to distinguish appropriate hedging from evasive output.
* **Pipeline:** Section-aware document ingestion (10-K/10-Q structure detection); boilerplate filtering reclaiming 13–22% of tokens; K-ranking annotation mode extracting up to 36 pairwise comparisons per session; multi-provider generation (Claude, GPT-4o, Gemini).

#### Multi-Agent Systems
* **Investment Committee Simulation:** Five-agent system (long analyst, short analyst, risk manager, macro analyst, PM) with structured debate rounds and configurable parameters.
* **Reasoning Traces:** THINK → PLAN → ACT → REFLECT loop with full trace visibility for evaluation and debugging.
* **Output Signal:** Directional T-signal (direction × entropy-adjusted confidence) designed as RL input for downstream portfolio systems.

---

## AI Safety & Strategic Risk

* **Red Teaming:** Multi-turn escalation sequences and persona-based probes testing safety beyond first-refusal holds. Hypothesis-driven with full conversation path reproducibility.
* **Guardrails:** Evaluating deterministic filters, semantic classifiers, and system prompt constraints — distinguishing systemic vulnerabilities from superficial keyword-trigger failures.
* **Purple Teaming:** Translating red team findings into refined safety taxonomies, training data, and targeted SFT/RLHF updates.
* **Dual-Use Risk:** Calibrating harm severity in financial contexts — distinguishing legitimate analysis from manipulation facilitation, minimizing both over-blocking and leakage.

---

## Background

Over 20 years institutional buy-side experience (PM/Analyst | L/S equity | SAC/Point72, WRC). MBA Finance. MS Analytics & Modeling (ML/Deep Learning). Northwestern. CFA® Charterholder.


---

#### Technical Stack

Python · PyTorch · Hugging Face (transformers, datasets, evaluate) · Weights & Biases · Braintrust · Promptfoo · LangGraph · Streamlit · pandas · SQL · Git

Local inference on Mac M4 Max (128GB RAM). Lambda Cloud dual-GPU (2× NVIDIA) for larger workloads.

---

#### AI Platform

Claude (Anthropic) is the preferred model across all LLM-integrated repos. Multi-agent, evaluation, and generation modules are built around Claude where applicable.

The maintainer strongly supports Anthropic's leadership and their commitment to treating AI safety and moral responsibility with the same rigor as capability.

---

### <u>References</u>

#### Quantitative Finance & Market Theory
* **Bailey, David H., and Marcos López de Prado.** 2014. "The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality." *Journal of Portfolio Management*. [SSRN 2460551](https://ssrn.com/abstract=2460551).
* **CHSOFT AG.** 2022. *Practical Performance Calculation*. v4.0.
* **Darmanin, Adam.** n.d. "Language Model Guided Reinforcement Learning in Quantitative Trading." University of Malta.
* **López de Prado, Marcos.** 2018. *Advances in Financial Machine Learning*. Hoboken, NJ: Wiley.
* **López de Prado, Marcos.** 2020. *Machine Learning for Asset Managers*. Cambridge: Cambridge University Press.
* **López de Prado, Marcos.** 2023. *Causal Factor Investing: Can Factor Investing Become Scientific?* Cambridge: Cambridge University Press.
* **Paleologo, Giuseppe A.** 2021. *Advanced Portfolio Management: A Quant's Guide for Fundamental Investors*. Hoboken, NJ: Wiley. <small>(Focus: Chapters 6–8)</small>
* **Paleologo, Giuseppe A.** 2024. *The Elements of Quantitative Investing*. Hoboken, NJ: Wiley. <small>(Focus: Sections 3.5, 3.6, 4.4, 4.5, and Chapter 7)</small>

---

#### Machine Learning & Artificial Intelligence
* **Ahmed, Nisha Arya.** 2022. "Vanishing/Exploding Gradients in Deep Neural Networks." *Heartbeat*. [Link](https://medium.com/fritzheartbeat/vanishing-exploding-gradients-in-deep-neural-networks).
* **Brownlee, Jason.** n.d. *Machine Learning Mastery*. [https://machinelearningmastery.com/](https://machinelearningmastery.com/).
* **Chollet, François.** 2021. *Deep Learning with Python*. 2nd ed. Manning Publications.
* **Gao, Hanyao, and Gang Kou, et al.** 2022. "Machine Learning in Business and Finance: A Literature Review and Research Opportunities." *Financial Innovation*. [DOI: 10.1186/s40854-022-00353-8](https://doi.org/10.1186/s40854-022-00353-8).
* **Géron, Aurélien.** 2022. *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. 3rd ed. O'Reilly Media.
* **Géron, Aurélien.** 2023. *Hands-On Machine Learning with Scikit-Learn and PyTorch: Concepts, Tools, and Techniques to Build Intelligent Systems*. 1st ed. Sebastopol, CA: O'Reilly Media.
* **Ha, Vi Q.** n.d. "Building an RLHF Pipeline for LLMs: A Beginner-Friendly Tutorial."

---

#### Mental Models & Philosophy
* **Chivers, Tom.** 2024. *Everything Is Predictable: How Bayesian Statistics Explain Our World*.
* **Cromwell, David.** n.d. *Richard Feynman's Mental Models*.
* **Dylan, Bob.** *Thematic evolution and narrative complexity.*
* **Weir, Bob.** *Improvisational theory and structural interplay.*

---

#### Contact:   [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/brad-schonhoft-cfa)
