_pm-to-ai_

# Institutional AI Evaluation & Investment Workflows

**20+ years as a portfolio manager and equity analyst at elite global hedge funds (Point72/SAC, Balyasny), managing $500MM–$750MM portfolios and building/leading research teams. MS in Data Science (ML/Deep Learning, Northwestern) | MBA (Finance, Rollins) | CFA Charterholder.**

Now specializing in evaluation frameworks and quality assurance for AI systems in institutional finance—translating buy-side quality standards into reproducible test suites, rubrics, and validation workflows.
---

## 🎯 Core Competency: LLM Evaluation for Finance

Designing evaluation frameworks that stress-test AI outputs against institutional quality bars—GAAP accuracy, variant view strength, numerical reasoning, and factual grounding.

**Focus Areas:**
- Evaluation rubric design for investment research and financial analysis
- Ground truth validation against regulatory filings (SEC EDGAR) and market data
- Error taxonomy development (hallucinations, GAAP mixups, consensus-hugging)
- Human-in-the-loop labeling workflows for preference data generation
- Statistical validation of model outputs (A/B testing, significance testing)

---

## 📂 Evaluation Projects

### 🔹 AI Investment Committee — Automated Research Scoring

**Repository:** https://github.com/bdschi1/equity-research-scorer

An evaluation framework that grades investment research against institutional rubrics.

**Evaluation Design:**
- Standardized scoring criteria: variant view strength, bear case quality, mosaic strategy, pre-mortem analysis
- Automated fact-checking against SEC EDGAR and Yahoo Finance APIs
- Error detection: consensus-hugging, weak differentiation, unsupported claims

**Value Proposition:** Quantifies research quality and detects low-conviction pitches that institutional investors would reject.

**Tech:** Pydantic · OpenAI (GPT-4o) · SEC & Yahoo Finance APIs

---

### 🔹 Financial RLHF Studio — Evaluation Data Engine

**Repository:** https://github.com/bdschi1/financial-rlhf-studio

A human-in-the-loop labeling interface for capturing institutional expertise as evaluation datasets.

**Workflow:**
- RAG-generated drafts vs expert-corrected outputs on 10-Ks and research notes
- Diff tracking with error taxonomies (hallucinations, GAAP errors, tone issues, numerical mistakes)
- Generates DPO-ready preference datasets and golden answer test suites

**Value Proposition:** Encodes domain-specific quality standards beyond generic finance benchmarks.

**Tech:** LangChain · OpenAI · ChromaDB · Streamlit · Docker

---

### 🔹 Dynamic Thesis Vetter — Adversarial Evaluation Agent

**Repository:** https://github.com/bdschi1/dynamic-thesis-vetter

An agentic evaluation system that stress-tests investment memos through adversarial interrogation.

**Evaluation Approach:**
- **Skeptic Agent (CIO):** Identifies logical gaps, weak assumptions, and narrative fluff
- **Validator Agent (Research Associate):** Uses RAG over source PDFs to verify or refute claims
- Iterative questioning until thesis is rigorously challenged

**Value Proposition:** Detects confirmation bias and tests robustness of investment logic before capital deployment.

**Tech:** LangGraph · LangChain · Advanced RAG · OpenAI (GPT-4o) · ChromaDB · Streamlit · Docker

---

### 🔹 Long/Short Arena — Multi-Agent Evaluation Testbed

**Repository:** https://github.com/bdschi1/llm-long-short-arena

An adversarial debate system where Bull and Bear PMs argue opposing sides of an investment case, adjudicated by a CIO agent.

**Evaluation Use Case:**
- Forces mutually exclusive reasoning paths to surface non-obvious risk factors
- Tests model consistency under adversarial prompting
- Validates decision robustness on 10-Ks, earnings calls, and sell-side research

**Value Proposition:** Detects confirmation bias and one-sided analysis that would fail institutional scrutiny.

**Tech:** Multi-Agent Systems · Chain-of-Thought · Streamlit · OpenAI API

---

### 🔹 Backtest Factor Clinic — Quantitative Validation Framework

**Repository:** https://github.com/bdschi1/backtest-factor-clinic

A validation clinic for stress-testing investment factors before live deployment.

**Quality Assurance Focus:**
- Overfitting detection and regime stability testing
- Bias correction: look-ahead bias, survivorship bias, data leakage
- Robust validation techniques: point-in-time data, purging/embargo, deflated Sharpe ratios

**Value Proposition:** Prevents fragile factors from reaching production by enforcing statistical rigor.

**Tech:** Python (Pandas, NumPy, SciPy) · VectorBT · Statistical Analysis · Streamlit

---

## 🎓 AI & Investment Certifications (Q4 2025 – Jan 2026)

- CFA Institute – "Data Science for Investment Professionals"
- DeepLearning.AI – "Building Evaluations for LLMs"
- Anthropic – "Prompt Engineering Interactive Tutorial"
- Weights & Biases – "LLM Monitoring and Observability"
- Google – "Machine Learning Crash Course"
- Coursera – "Inferential Statistics" (Duke University)

---

## 🛠️ Technical Stack

| Category              | Tools                                      |
| --------------------- | ------------------------------------------ |
| **Evaluation & QA**   | Pytest · Statistical Analysis · RLHF       |
| **AI & LLMs**         | OpenAI · Anthropic · LangChain · LangGraph |
| **Data & Finance**    | Bloomberg Terminal (PORT/PRTU) · AlphaSense · Visible Alpha · Pandas · NumPy · VectorBT · SEC EDGAR API  |
| **Development**       | Python · Git · Docker · Streamlit          |
---

## 📫 Connect

- **LinkedIn:** https://www.linkedin.com/in/brad-schonhoft-cfa
- **Email:** bdschi1@protonmail.com

---

**Focus:** Translating institutional quality standards into reproducible AI evaluation frameworks. Available for consulting on LLM evaluation design, domain-specific test suite development, and validation workflow implementation.
