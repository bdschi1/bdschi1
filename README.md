


_pm-to-ai:_ #Bridging the gap between **institutional finance** and **production‑grade AI**#
_Translating discretionary investment logic into reproducible, autonomous software agents and data engines_ 
_that generate training labels at scale._

***

## 🏛️ Core Applications — Buy‑Side Stack

_Tools designed to automate and augment the institutional investment process,_ from 
**idea debate** to **research scoring** to **factor validation**.

***

### 🔹 Long/Short Arena — *Deep Reasoning*

**Repository:**  
👉 https://github.com/bdschi1/llm-long-short-arena

An autonomous multi‑agent system where **Bull** and **Bear PMs** debate research documents, adjudicated by a **CIO agent**.

- **Alpha:** Forces mutually exclusive reasoning paths to mitigate confirmation bias and surface non‑obvious drivers.  
- **Focus:** Decision robustness under adversarial, institutional‑style reasoning on 10‑Ks, earnings calls, and sell‑side research.

**Tech:** Multi‑Agent Systems · Chain‑of‑Thought · Streamlit · OpenAI API

***

### 🔹 AI Investment Committee — *Qualitative*

**Repository:**  
👉 https://github.com/bdschi1/equity-research-scorer

An automated **Digital Portfolio Manager** that reads, grades, and validates investment research against a standardized rubric.

- **Alpha:** Quantifies the *variant view* embedded in unstructured text to detect consensus‑hugging and weak differentiation.  
- **Use Case:** First‑pass review of stock pitches and macro reports, with institutional scoring (variant view, bear case, pre‑mortem, mosaic strategy) and automatic fact‑checking against **SEC EDGAR** and **Yahoo Finance**.

**Tech:** Pydantic · OpenAI (GPT‑4o) · SEC & Yahoo Finance APIs

***

### 🔹 Backtest Factor Clinic — *Quantitative*

**Repository:**  
👉 https://github.com/bdschi1/backtest-factor-clinic[6]

A modular clinic for validating investment factors before they touch live capital.[6]

- **Alpha:** Stress‑tests signals across regimes, decay patterns, and transaction costs to expose fragile factors.  
- **Focus:** Overfitting prevention and factor hygiene via demonstrations of look‑ahead bias, survivorship bias, data leakage, and robust corrections (PIT data, purging/embargo, deflated Sharpe).[6]

**Tech:** Python (Pandas, NumPy, SciPy) · VectorBT · Statistical Analysis · Streamlit[6]


### 🔹 Financial RLHF Studio — *Data Engine*

**Repository:**  
👉 https://github.com/bdschi1/financial-rlhf-studio

A **human‑in‑the‑loop labeling interface** for capturing institutional expertise as structured training data.

- **Workflow:** RAG‑generated drafts vs. expert‑corrected outputs on 10‑Ks and research notes → diff tracking + error taxonomies → **DPO‑ready preference datasets**.  
- **Goal:** Encode institutional nuance beyond “generic finance” by tagging hallucinations, GAAP mixups, tone issues, and other domain‑specific errors.

**Focus:** Preference data generation and error‑taxonomy labeling for fine‑tuning financial LLMs.

***

### 🔹 Async Model Trainer — *Infrastructure*

**Repository:**  
👉 https://github.com/bdschi1/async-model-trainer

A production‑grade microservices architecture for scalable LLM fine‑tuning.

- **Architecture:** Decoupled **Control Plane (UI/API)** and **Compute Plane (GPU workers)** communicating via Redis, enabling non‑blocking, asynchronous training jobs with real‑time status.
- **Design:** Horizontally scalable, GPU‑aware Celery workers executing Unsloth / PyTorch fine‑tuning jobs, orchestrated via Docker Compose.

**Tech:** Celery · FastAPI · Pydantic · Unsloth (LLaMA‑3) · PyTorch · PEFT (LoRA) · Docker Compose · Streamlit

***

### 🔹 Dynamic Thesis Vetter — *Agentic RAG*

**Repository:**  
👉 https://github.com/bdschi1/dynamic-thesis-vetter

An **active interviewer** agent that interrogates investment memos instead of summarizing them.

- Identifies logical gaps, weak assumptions, and narrative fluff via a **Skeptic (CIO) agent**.  
- Generates probing questions and uses **RAG over the source PDF** to validate or refute claims via a **Validator (Research Associate) agent**, iterating until the thesis is stress‑tested.[4]

**Tech:** LangGraph · LangChain · Advanced RAG · OpenAI (GPT‑4o) · ChromaDB · Streamlit · Docker

***

### 🧬 AI Engineering & Ops — Model Stack

Infrastructure for creating, training, and vetting **financial‑domain models**, with a focus on **human‑in‑the‑loop supervision** and **asynchronous fine‑tuning**.

w.i.p.

***

## 🛠️ Technical Stack

| Category           | Tools                     |
| ------------------ | ------------------------- |
| **Languages**      | Python · SQL              |
| **AI & LLMs**      | OpenAI · LangChain · RLHF |
| **Data & Finance** | Pandas · VectorBT         |
| **Engineering**    | Git · Streamlit · Docker  |

---

## 📫 Connect

* **LinkedIn:** [https://www.linkedin.com/in/brad-schonhoft-cfa](https://www.linkedin.com/in/brad-schonhoft-cfa)
* **Email:** [mailto@protonmail.com](mailto:bdschi1@protonmail.com)
