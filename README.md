# pm-to-ai | Domain Expert for AI Evaluation 
**_"Curiosity compounds. Rigor endures"_**

**Former institutional PM translating buy-side judgment into machine-readable structured criteria for LLM training, evaluation, and adversarial testing.**

---

## Background

| Credential | Detail |
|------------|--------|
| **Investment** | PM / Equity Analyst / Hedge Fund launch, capital raising experience (2011–2019); 14 yrs as PM; ~$750M AUM peak |
| **Platforms** | Sigma Capital (now part of Point72), ~10 yrs; Balyasny; Forstmann; others |
| **CFA** | Chartered 2001 |
| **MS Data Science** | Northwestern (2022) — ML/Deep Learning specialization |
| **Domain** | Global Healthcare (GICS 3510/3520; Americas/Europe/India); cross-sector generalist L/S; ETFs |

pm-to-ai is founder-led today for speed and accountability. As scope warrants, additional domain experts (buy-side, sell-side, finance, strategy, technical, scientific/medcial) are coordinated under a single rubric and QA process.

## Evaluation Standards

LLM outputs are graded the way an institutional PM reviews analyst work or how portfolio (pod) risk is assessed at the CIO level.  Dimensions are categorized by institutional philosophy, thesis construction, advanced dynamics, and risk management.

| Dimension | What Matters |
|-----------|--------------|
| **Investment Process** | Consistency and Actionability evals|
| **Project Managing real-time Paper Portfolio** | 20+ years domain expertise for training, evals/rubrics, adversarial testing. 
| **Institutional Judgment** | GenAI does not generate institutional level investment judgment; domain experts validate whether an idea makes sense. |
| **Process Quality Assessment** | Outcome-only focus fails in process assessment; expert evals evaluate logic, efficiency, scalability, and conviction communication. Idea template assessments|
| **Counterfactual Reasoning** | Separating decision quality from outcome quality; process evaluation independent of P&L. |
| **Decision Realism** | Constraints (liquidity, position limits), timing, and second-order portfolio effects. |
| **Thesis Construction & Evidence** | Evaluate how conviction can change |
| **Variant View Quality** | Specific, testable, differentiated edge—not consensus paraphrase. |
| **Bear-case Rigor** | Disconfirming evidence, downside path completeness, and what breaks the thesis. |
| **Evidence Hygiene** | Clear separation of facts vs. inference vs. speculation; unsupported assertions penalized. |
| **Information Decay Rate** | Recognizing different information half-lives; identifying where stale data creates negative expected value. |
| **Reflexivity Recognition** | Understanding that investment actions change market dynamics; thesis validity decays as capital crowds in.|
| **Value-chain-driven thesis Evaluations** | Mapping to upstream, downstream, competitive value-chain exposures. |
| **Optionality Asymmetry** | Distinguishing symmetric vs. asymmetric payoff structures; embedded convexity in equity positions. |
| **Volatility Structure** | Domain knowledge required to model exploitable structure in volatility. |
| **Pattern Detection** | Hidden correlation surfacing and latent relationships across cross-corpus data. |
| **Portfolio Risk Rigor** | 'bullpen' portfolios; risk metric design, implementation, and monitoring. |
| **Thesis Risk Decomposition** | Scoring based on material risks—fundamental, statistical, and market. |
| **Sizing Focus** | Dynamic position sizing based on conviction and volatility (Kelly criterion). |
| **Conviction Updates** | Correct updating under conflicting or partial data. Does new information change conviction? |
| **Cost-of-Error Focus** | Whether failures would drive material decision-quality degradation. |
| **Thematic Trade Builds** | Multi-instrument thesis evaluations. |

### Healthcare Sector Specifics
- Modeling evals of all subsectors.
- Clinical trial design logic (endpoints, power, populations, comparators).
- Event interpretation and uncertainty handling.
- Regulatory pathway realism (FDA, EMA).
- Portfolio modifications and risk management evaluations around major events (e.g., Phase 3 results; macro risks).

### Short-Selling Expertise
Experience is weighted toward **alpha-generating short positions** as well as porfolio hedging. This informs evaluation of:
- Short thesis construction and catalyst identification.
- Downside scenario completeness.
- Borrow/locate realism and squeeze risk awareness.
- Asymmetry assessment (e.g., short interest return profile).
- Volatility assessments (e.g., low vol anomalies; compression considerations).
- Derivatives/Synthetics strategies and portfolio risk metrics implications.

---

## Adversarial Testing - Red Teaming

Constructing and evaluating inputs designed to expose model failures that matter in real decision contexts.

| Scenario | What It Tests |
|----------|---------------|
| **"Negative EV" Biotech** | **Optionality asymmetry awareness:** Present a biotech company trading at/below net cash with an upcoming Phase 2 readout. Test if model identifies embedded convexity (limited downside vs. high-velocity upside). |
| **"High-Freq Macro" Conflict** | **Information decay rate calibration:** Provide a 3-day-old high-impact macro data point (e.g., CPI) vs. a fresh but low-significance sell-side "check." Test if model incorrectly prioritizes "new" data over decaying data. |
| **"Gating" Liquidity Event** | **Liquidity regime contingency:** Request sizing for a small-cap position during a simulated VIX spike (VIX > 35). Test if model recognizes liquidity is regime-dependent. |
| **"Right Process/Wrong Outcome"** | **Counterfactual reasoning integrity:** Present a logical investment memo for a trade that lost 20% due to an unpredictable "black swan." Evaluate if LLM penalizes process based on P&L (outcome bias). |
| **Event-driven trade** | Explore less obvious failure modes in time-sensitive contexts. |
| **Stale event path** | Provide thesis with well-defined event path to test for stale data or legal/FOIA info misses. |
| **Conflicting estimates** | Present conflicting sell-side estimates to test conviction updating under uncertainty. |
| **Corporate Action Awareness** | Include a recent stock split or dividend not reflected in price history. |
| **LLM GARP thesis** | Factor decomposition, estimates dispersion, and volatility sizing considerations. |
| **Underpowered Trial** | Describe a Phase 2 trial with underpowered secondary endpoints to test clinical reasoning rigor. |
| **Post-Catalyst Drift** | Describe Phase 3 trial that hit primary endpoint with stock up; test if manufacturing/label risks are identified. |
| **Consensus Bear Case** | Ask for a bear case on consensus long to test for disconfirming evidence vs. generic "competition risk." |
| **Portfolio Impact** | Focus on carry cost, volatility impact, and event path matching within a broader portfolio. |
| **Conviction assessments** | Evaluate if new information/datapoints change thesis conviction. |

---

## Sample Repositories / WIPs

| Repo | Purpose |
|------|---------|
| **[backtest-factor-clinic](https://github.com/bdschi1/backtest-factor-clinic)** | Diagnostic suite for detecting financial hallucinations in quant code. |
| **[financial-rlhf-studio](https://github.com/bdschi1/financial-rlhf-studio)** | DPO workflow for transforming domain expertise into structured training data. |
| **[equity-research-scorer](https://github.com/bdschi1/equity-research-scorer)** | Automated benchmarking of investment theses against institutional standards. |
| **[llm-long-short-arena](https://github.com/bdschi1/llm-long-short-arena)** | Evaluation harness for L/S reasoning quality. |
| **[dynamic-thesis-vetter](https://github.com/bdschi1/dynamic-thesis-vetter)** | Tests conviction updating when new information arrives. |
| **[async-model-trainer](https://github.com/bdschi1/async-model-trainer)** | Production-grade async training pipeline (FastAPI, Redis, Celery). |

---

## Deliverables

**For AI labs and evaluation platforms:**
1. **Rubrics & scoring guides** — Institutional standards with failure taxonomies tied to cost-of-error.
2. **Expert-labeled datasets** — Examples with rationales, counterexamples, and adversarial variants.
3. **Adversarial test suites** — Scenarios designed to expose consequential failure modes.
4. **Evaluation task design** — Scenario construction, prompt sets, and acceptance criteria.
5. **RLHF/DPO feedback** — High-quality preference data grounded in institutional judgment.


## Career Detail

**Investment & leadership:**
- Long/short equity PM, analyst, DOR, CCO (1998–2025); 14 years as PM.
- Sigma Capital (~10 years global hc long/short pm) — SAC pod; no down years.
- Balyasny; Forstmann; long-biased platforms.
- Invested through dot-com aftermath, 9/11, GFC, COVID, and 2022 inflation.

**Education & Certifications:**
- MS Data Science (Northwestern, 2022).
- MBA (Rollins) | BA Biology (Miami) | Molecular Genetics PhD student (ABD) — The OSU.
- Certifications (2025-2026) in-process or completed: DeepLearning.AI – Langchain Apps; Agent Skills with Anthropic
- Google Cloud - RL from Human Feedback
- Weights & Biases – LLM Monitoring and Observability
- Coursera – Machine Learning Engineer certification (IBM); Harnessing LLMs: Strategy, Fine-Tuning & Evaluation
  
## Data Hygiene
- No MNPI. No employer-confidential process leakage.
- pm-to-ai internal process documentation, compliance/standards manual
- Client work under NDA with clear boundaries.
- Evals designed to be auditable, reproducible, and versioned.

## Disclosures
- No personal trading activity — available for conflict-free engagements for certain projects
- NDA-protected work involving proprietary investment workflows accepted
- Public repositories contain original samples only — no proprietary or client data

## Contact
www.linkedin.com/in/brad-schonhoft-cfa

## Repositories
```
├── 📐 EVALUATION & RUBRICS
│   ├── investment-workflow-evals        # Institutional workflow evaluation frameworks
│   ├── llm-long-short-arena             # Adversarial test suites for equity LLM outputs
│   └── equity-research-scorer           # Automated sell-side/buy-side research grading
│
├── 🛠️ TOOLING
│   ├── dynamic-thesis-vetter            # Real-time investment thesis validation
│   ├── financial-rlhf-studio            # RLHF dataset generation for finance domain
│   └── backtest-factor-clinic           # Factor attribution and backtest diagnostics
│
└── 🧪 IN DEVELOPMENT
    ├── biotech-catalyst-evals           # Binary event evaluation (PDUFA, trials)
    └── short-thesis-stress-tests        # Squeeze risk and short-specific failure modes


