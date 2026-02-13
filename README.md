# Domain Expert — Finance × LLM Evaluation & Alignment × Healthcare Sector PM

* **>20 years institutional buy-side experience** (SAC Capital/Sigma/Point72, BAM, WRC).
* **MS Analytics & Modeling** (ML/Deep Learning), Northwestern 2022; **MBA Finance | CFA® Charterholder**
* **Scientific Foundation:** PhD (ABD) Research (Molecular Genetics), The Ohio State University; BA Biology/pre-med.

---

### Current Focus
Evaluating and improving LLM performance on financial reasoning tasks — building the rubrics, adversarial tests, preference data, and multi-agent systems to evaluate if AI models can meet institutional-grade investment standards.

---

## Institutional Foundation

### Investment Pedigree & Leadership
* **Experience:** 10 years at SAC Capital/Sigma (Point72) as Senior PM; >20 years buy-side total (BAM, WRC).
* **Track Record:** Built and led high-performance analyst teams with zero turnover.
* **AUM & Strategy:** Peak AUM $750M; concentrated L/S equity with factor-aware risk management and alpha/beta/noise decomposition.
* **Instruments:** Single-name L/S; ETFs, futures, statistical baskets, and options for hedging and alpha expression.

### Scientific & Technical Depth
* **AI/ML:** Capstone: "Predicting Biotech Stock Prices with LSTM Architectures" — sequence-based deep learning applied to volatile healthcare equities.
* **Hard Science:** Research focus: **Topology of DNA**. TA in Genetics and Physics.

### Healthcare Sector Specialization
* **Domain Literacy:** Full-lifecycle expertise across the GICS universe: Biotech, Large/Specialty Pharma, Life Science Tools, Diagnostics, HCIT, Providers/Payors, and API/CMO supply chains.
* **Due Diligence:** 1,000+ corporate 1×1s, investor conferences, site visits, and medical meetings across the US, Europe, and India.
* **Multi-Sector Coverage:** Additional generalist experience in Technology, Industrials, and Real Estate.

### Failure Pattern Recognition

Anchoring on stale consensus; asymmetric risk framing; false precision; backtest survivorship bias. Reflexivity errors (sentiment vs. catalysts); narrative fallacy (story vs. data); footnote blindness (unaudited headline metrics); tail-risk/convexity bias. Mapping decades of analyst oversight experience to modern LLM evaluation rubrics.

---

## II. Applied AI Evaluation & Alignment

### Evaluation Methodology
* **Methods:** RLHF preference data; adversarial red teaming; guardrail/safety taxonomy testing.
* **Infrastructure:** Scoring rubrics; golden answer authoring; domain-specific fine-tuning (SFT).
* **Architecture:** Multi-agent orchestration; prompt engineering; role-integrity testing.
* **Benchmarking:** 306-problem finance reasoning benchmark (valuation, accounting, credit, portfolio math) with difficulty grading and multi-model leaderboard; institutional workflow evals covering thesis → catalysts → sizing → risk → monitoring → post-mortem.
* **Model Audit:** Graph-based structural auditing of LLM-generated Excel models — dependency tracing, circular reference detection, balance sheet consistency checks, complexity scoring.

### RLHF & Preference Data
* **Signal:** Authoring preference pairs where domain-expertise signal outweighs stylistic polish.
* **Criteria:** Transparency of assumptions; quantitative precision; intellectual honesty regarding uncertainty.
* **Calibration:** Expert-led alignment to distinguish appropriate hedging from evasive output.
* **Pipeline:** Section-aware document ingestion (10-K/10-Q structure detection); boilerplate filtering reclaiming 13–22% of tokens; K-ranking annotation mode extracting up to 36 pairwise comparisons per session; multi-provider generation (Claude, GPT-4o, Gemini).

### Multi-Agent Systems
* **Investment Committee Simulation:** Four-agent system (analyst, devil's advocate, risk manager, PM) with structured debate rounds and configurable parameters.
* **Reasoning Traces:** THINK → PLAN → ACT → REFLECT loop with full trace visibility for evaluation and debugging.
* **Output Signal:** Directional T-signal (direction × entropy-adjusted confidence) designed as RL input for downstream portfolio systems.

---

## III. AI Safety & Strategic Risk

### Adversarial Testing & Red Teaming
* **Strategy:** Design of multi-turn escalation sequences and persona-based probes targeting safety degradation.
* **Logic:** Probing beyond first-refusal holds to test deep-layer safety mechanisms.
* **Traceability:** Hypothesis-driven testing with full conversation path reproducibility.

### Guardrails & Defense Layers
* **Security Stack:** Evaluation of deterministic filtering, semantic classifiers, and system prompt constraints.
* **Dynamics:** Assessing dependencies between RLHF safety tuning and real-time output scanning.
* **Precision:** Surfacing systemic vulnerabilities versus superficial keyword-trigger failures.

### Purple Teaming & Remediation
* **Feedback Loops:** Translating red team vulnerabilities into refined safety taxonomies and training data.
* **Remediation:** Improving system prompt constraints and targeted SFT/RLHF updates based on eval artifacts.

### Dual-Use & Communication
* **Risk Management:** Distinguishing legitimate financial analysis from market manipulation facilitation.
* **Sensitivity:** Calibrating harm severity to prevent over-blocking (refusals) or under-blocking (leakage).
* **Reporting:** Mapping complex technical failures to actionable risk reports for non-technical leadership and investment committees.

---

## Sample Repositories

### Evaluation Frameworks

**[investment-workflow-evals](https://github.com/bdschi1/investment-workflow-evals)** — Evaluation suite mapping the institutional investment workflow into machine-readable scoring rubrics. Each stage (thesis → catalysts → sizing → risk → monitoring → post-mortem) has structured criteria, anchor examples for each score level, and adversarial variants designed to trigger specific LLM failure modes: regime-blind extrapolation, confident nonsense on illiquid names, circular reasoning between price targets and valuation multiples.

**[fin-reasoning-eval](https://github.com/bdschi1/fin-reasoning-eval)** — 306 finance reasoning problems covering valuation, accounting, credit, and portfolio math. Tests quantitative rigor rather than financial vocabulary — unit economics, share dilution arithmetic, EBITDA-to-FCF bridges, NOL carryforward mechanics, convertible bond math. Each problem has structured metadata, difficulty grading, and golden answers with worked solutions.

**[excel-model-eval](https://github.com/bdschi1/excel-model-eval)** — Framework for evaluating LLM-generated Excel financial models against institutional standards. Checks internal consistency (does the balance sheet balance? does the cash flow statement tie to the income statement?), formula correctness, edge case handling (negative working capital, deferred revenue, circular references in interest expense), and whether outputs are defensible enough to size a position around.

### Red Teaming & RLHF

**[redflag_ex1_analyst](https://github.com/bdschi1/redflag_ex1_analyst)** — Red-flag detection engine for analyst research notes. Rule-based + heuristic system that identifies the patterns experienced PMs look for in junior work: buried or missing assumptions, one-sided risk presentation, stale comparable sets, earnings estimates without sensitivity analysis, and boilerplate filler inflating page count without adding information content. Supports PDF and DOCX ingestion with section-aware parsing and boilerplate filtering. Full CI pipeline with pytest. The approach transfers directly to AI safety red teaming — the same adversarial mindset applied to LLM-generated financial content rather than human analyst work.

**[financial-rlhf-studio](https://github.com/bdschi1/financial-rlhf-studio)** — RLHF preference data pipeline for financial domain tuning. Generates paired completions (preferred vs. rejected) with structured annotations capturing the specific dimensions of investment judgment: analytical depth, assumption transparency, risk acknowledgment, quantitative precision, and intellectual honesty about uncertainty. Streamlit interface for human annotation. The goal is preference data where the signal comes from domain expertise, not stylistic polish.

### Multi-Agent Systems

**[multi-agent-investment-committee](https://github.com/bdschi1/multi-agent-investment-committee)** — Multi-agent system simulating a buy-side investment committee with distinct roles: presenting analyst, devil's advocate, risk manager, and portfolio manager. Agents debate through structured rounds with configurable parameters (debate depth, token budgets, temperature). Extracts sentiment, confidence signals, and a directional T-signal from PM output for downstream analysis. Supports multiple LLM providers (Anthropic, OpenAI, Google, Hugging Face, Ollama). HITL review mode enabled by default.

### Portfolio Analytics

**[ls-portfolio-lab](https://github.com/bdschi1/ls-portfolio-lab)** — Long/short portfolio construction and analysis toolkit. Performance attribution, drawdown decomposition, rebalancing logic, trade impact modeling, and the risk metrics institutional allocators actually ask about: gross/net exposure, factor concentration, rolling Sharpe, max drawdown duration. Data providers for Yahoo Finance, Bloomberg, and Interactive Brokers. Streamlit dashboard with chart gallery and PM scorecard.

---

### Technical Stack

Python · PyTorch · Hugging Face (transformers, datasets, evaluate) · Weights & Biases · Braintrust · Promptfoo · LangGraph · Streamlit · pandas · SQL · Git

Local inference on Mac M4 Max (128GB RAM). Lambda Cloud dual-GPU (2× NVIDIA) for larger workloads.

---

### Contact:   [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://linkedin.com/in/brad-schonhoft-cfa)

---

### <u>References & Bibliography</u>

### Quantitative Finance & Market Theory
* **Bailey, David H., and Marcos López de Prado.** 2014. "The Deflated Sharpe Ratio: Correcting for Selection Bias, Backtest Overfitting and Non-Normality." *Journal of Portfolio Management*. [SSRN 2460551](https://ssrn.com/abstract=2460551).
* **CHSOFT AG.** 2022. *Practical Performance Calculation*. v4.0.
* **Darmanin, Adam.** n.d. "Language Model Guided Reinforcement Learning in Quantitative Trading." University of Malta.
* **López de Prado, Marcos.** 2018. *Advances in Financial Machine Learning*. Hoboken, NJ: Wiley.
* **López de Prado, Marcos.** 2020. *Machine Learning for Asset Managers*. Cambridge: Cambridge University Press.
* **López de Prado, Marcos.** 2023. *Causal Factor Investing: Can Factor Investing Become Scientific?* Cambridge: Cambridge University Press.
* **Paleologo, Giuseppe A.** 2021. *Advanced Portfolio Management: A Quant's Guide for Fundamental Investors*. Hoboken, NJ: Wiley. <small>(Focus: Chapters 6–8)</small>
* **Paleologo, Giuseppe A.** 2024. *The Elements of Quantitative Investing*. Hoboken, NJ: Wiley. <small>(Focus: Sections 3.5, 3.6, 4.4, 4.5, and Chapter 7)</small>

---

### Machine Learning & Artificial Intelligence
* **Ahmed, Nisha Arya.** 2022. "Vanishing/Exploding Gradients in Deep Neural Networks." *Heartbeat*. [Link](https://medium.com/fritzheartbeat/vanishing-exploding-gradients-in-deep-neural-networks).
* **Brownlee, Jason.** n.d. *Machine Learning Mastery*. [https://machinelearningmastery.com/](https://machinelearningmastery.com/).
* **Chollet, François.** 2021. *Deep Learning with Python*. 2nd ed. Manning Publications.
* **Gao, Hanyao, and Gang Kou, et al.** 2022. "Machine Learning in Business and Finance: A Literature Review and Research Opportunities." *Financial Innovation*. [DOI: 10.1186/s40854-022-00353-8](https://doi.org/10.1186/s40854-022-00353-8).
* **Géron, Aurélien.** 2022. *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. 3rd ed. O'Reilly Media.
* **Géron, Aurélien.** 2023. *Hands-On Machine Learning with Scikit-Learn and PyTorch: Concepts, Tools, and Techniques to Build Intelligent Systems*. 1st ed. Sebastopol, CA: O'Reilly Media.
* **Ha, Vi Q.** n.d. "Building an RLHF Pipeline for LLMs: A Beginner-Friendly Tutorial."

---

### Mental Models & Philosophy
* **Chivers, Tom.** 2024. *Everything Is Predictable: How Bayesian Statistics Explain Our World*.
* **Cromwell, David.** n.d. *Richard Feynman's Mental Models*.
* **Feuerstein, Georg.** 2013. *The Psychology of Yoga: Integrating Eastern and Western Approaches for Understanding the Mind*.
* **Fraenkel, Ernst.** 1941. *The Dual State: A Contribution to the Theory of Dictatorship*. Oxford University Press.
* **Dylan, Bob.** *Thematic evolution and narrative complexity.*
* **Weir, Bob.** *Improvisational theory and structural interplay.*

---

<small>**Note:** This bibliography tracks the theoretical foundations of the most projects in this repo, most notably Portfolio Lab and Institutional Eval frameworks.</small>
