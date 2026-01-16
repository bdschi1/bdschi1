# pm-to-ai | Domain Expert for AI Evaluation (Equity L/S, Healthcare)

**Former institutional PM translating buy-side judgment into machine-readable structured criteria for LLM training, evaluation, and adversarial testing.**

---

## Background

| Credential | Detail |
|------------|--------|
| **Investment** | PM / Equity Analyst / Hedge Fund launch, capital raising experience (1998–2023); 14 yrs as PM; ~$750M AUM peak |
| **Platforms** | Sigma Capital (now part of Point72), ~10 yrs; Balyasny; Forstmann; others |
| **CFA** | Chartered 2001 |
| **MS Data Science** | Northwestern (2022) — ML/Deep Learning specialization 
| **Domain** | Global Healthcare (GICS 3510/3520; Americas/Europe/India); cross-sector generalist L/S |

pm-to-ai is founder-led today for speed and accountability. As scope warrants, additional domain experts (buy-side, technical) are coordinated under a single rubric and QA process.

---

## Evaluation Standards

LLM outputs are graded the way an institutional PM reviews analyst work:

| Dimension | What Matters |
|-----------|--------------|
| **GenAI does not generate institutional level investment judgement** | Domain experts validate whether an idea makes sense |
| **Outcome only focus fails in process assessment** | Expert evals evaluate process quality, utility |
| **Assessment of Investment Process** | Logic, Efficiency, Scalability, Communication |
| **Variant view quality** | Specific, testable, differentiated edge — not consensus paraphrase |
| **Bear-case rigor** | Disconfirming evidence, downside path completeness, what breaks the thesis |
| **Evidence hygiene** | Clear separation of facts vs inference vs speculation; unsupported assertions penalized |
| **Decision realism** | Constraints (liquidity, position limits), timing, second-order portfolio effects |
| **Conviction updates** | Correct updating under conflicting or partial data |
| **Cost-of-error focus** | Whether failures would drive material decision-quality degradation |
| **Sizing focus** | Dynamic position sizing based on conviction and volatility / Kelly criterion |
| **Thematic Trade builds**  | multi-instrument thesis evaluations |
| **Cross-corpus pattern detection** | Hidden correlation surfacing |
| **Portfolio Risk Management rigor** | 'Bench' portfolios; risk metric design, implementation, and monitoring |
| **Volatility has exploitable structure** | Domain knowledge required to model |
| **Thesis Risk Decomposition focus** | Scoring based on material risks - fundamental and stat/market |

### Healthcare / Biotech Specifics
- Trial design logic (endpoints, power, populations, comparators)
- Readout interpretation and uncertainty handling
- Regulatory pathway realism (FDA, EMA)
- Mechanism plausibility vs narrative-only reasoning
- Portfolio modifications and risk management evaluations around major events (e.g. Phase 3 clinical trial results; macro risks )

### Short-Selling Expertise
Experience is weighted toward **alpha-generating short positions** — fundamental shorts with differentiated variant views and quant/stat-based shorts. This informs evaluation of:
- Short thesis construction and catalyst identification
- Downside scenario completeness
- Borrow/locate realism and squeeze risk awareness
- Asymmetry assessment (e.g. short interest return profile)
- Volatility assessments (e.g. low vol anomalies; compression considerations)
- Derivatives/Synthetics strategies
- Portfolio risk metrics implications and mitigation approaches

---

## Adversarial Testing - Red Teaming

Constructing and evaluating inputs designed to expose model failures that matter in real decision contexts. Generic benchmarks miss domain-specific failure modes; domain-expert adversarial testing increase probability of identifying them. Conviction testing designed to discern actionable information from new but insignificant within event path.

**Examples of adversarial scenarios used in evaluation:**

| Scenario | What It Tests |
|----------|---------------|
| Event driven trade | Explore less obvious failure modes |
| Provide thesis with well defined event path| Stale data detection, legal or FOIA info misses|
| Present conflicting sell-side estimates | Conviction updating under uncertainty |
| Include a recent stock split or dividend not reflected in price history | Corporate action awareness |
| LLM GARP thesis | Factor decomposition, estimates dispersion, volatility sizing considerations |
| Describe a Phase 2 trial with underpowered secondary endpoint | Clinical reasoning rigor |
| Describe Phase 3 trial that hit primary endpoint, stock up |  manufacturing, label, or approval timing remain key risks |
| Thesis event path | Exit strategy and latent relationships |
| Ask for bear case on consensus long | Disconfirming evidence generation vs generic "competition risk" |
| Request thesis on company with material GAAP/non-GAAP divergence | Accounting quality sensitivity |
| Present regime-dependent logic (ZIRP vs inflation environment) | Regime shift recognition |
| Merger Arb thesis clearly modeled | Why spread exists |
| Portfolio impact focus| Carry cost, volatility impact |

The goal: identify where models fail in ways that would degrade decision quality or generate losses in a real portfolio context.

---

## Sample Repositories

| Repo | Purpose |
|------|---------|
| **[backtest-factor-clinic](https://github.com/bdschi1/backtest-factor-clinic)** | Diagnostic suite for detecting financial hallucinations in quant code. Statistical checks (Point-in-Time, Deflated Sharpe) to eliminate biases. |
| **[financial-rlhf-studio](https://github.com/bdschi1/financial-rlhf-studio)** | DPO workflow for transforming domain expertise into structured training data. Corrects AI hallucinations on financial reasoning. |
| **[equity-research-scorer](https://github.com/bdschi1/equity-research-scorer)** | Automated benchmarking of investment theses against institutional standards. |
| **[llm-long-short-arena](https://github.com/bdschi1/llm-long-short-arena)** | Evaluation harness for L/S reasoning quality. |
| **[dynamic-thesis-vetter](https://github.com/bdschi1/dynamic-thesis-vetter)** | Tests conviction updating when new information arrives. |
| **[async-model-trainer](https://github.com/bdschi1/async-model-trainer)** | Production-grade async training pipeline (FastAPI, Redis, Celery, auto-hardware detection). |

---

## Deliverables

**For AI labs and evaluation platforms:**

1. **Rubrics & scoring guides** — Institutional standards with explicit pass/fail thresholds; failure taxonomies tied to cost-of-error
2. **Expert-labeled datasets** — Labeled examples with rationales; counterexamples and adversarial variants
3. **Adversarial test suites** — Scenarios designed to expose consequential failure modes; stress tests where errors compound
4. **Evaluation task design** — Scenario construction, prompt sets, acceptance criteria, scoring plans
5. **RLHF/DPO feedback** — High-quality preference data grounded in institutional judgment

**Failure modes typically caught:**
- Stale data (metrics from outdated filings, price data integrity/adjustments)
- Corporate actions missed (splits, spinoffs, M&A)
- Survivorship / look-ahead bias
- Regime shift blindness | Failure to see correlation changes
- Decomposing realized P&L into fewer than these components: selection process, sizing, and timing
- Sizing on conviction score and target without considering idiosyncratic risk
- Event risk mishandling (especially biotech catalysts)
- Shallow or generic bear cases
- New datapoints / analyses that don’t change risk/reward
- Factor exposure mistakenly identified as alpha 

---

## Engagement

For contract inquiries, include:
- **Workflow** (e.g., trial readout reasoning, thesis memo quality, catalyst mapping, portfolio sizing, short thesis robustness)
- **Output format** (free text vs structured JSON; schema constraints; rubric/grader requirements)
- **Failure modes of interest** (hallucinations, evidence gaps, shallow bear case, endpoint mistakes)
- **Volume & cadence** (items per week; sprint length; review cycle)

**Contact:** [LinkedIn](https://www.linkedin.com/in/brad-schonhoft-cfa)

---

## Technical Environment

| Component | Setup |
|-----------|-------|
| **Compute** | Lambda GPU workstation (Ubuntu/Windows/CUDA); Apple silicon (M4, 128GB unified memory) |
| **LLM APIs** | Claude (Sonnet/Opus), GPT-4o, Gemini 1.5 Pro, open-source models |
| **Evaluation stack** | Python, Pydantic schemas, W&B observability |
| **Secure workflows** | Air-gapped auditing patterns available when required |

---

## Recent Certifications or near completion (2025-2026)

- CFA Institute — Data Science for Investment Professionals
- DeepLearning.AI — Building Evaluations for LLMs
- DeepLearning.AI - LangChain for LLM Application Development
- Anthropic — Prompt Engineering Interactive Tutorial
- Weights & Biases — LLM Monitoring and Observability
- GitLab — Remote Foundations

---

## Data Hygiene

- No MNPI. No employer-confidential process leakage.
- Public releases use synthetic scenarios and/or public information only.
- Client work under NDA with clear boundaries.
- Evals designed to be auditable, reproducible, and versioned.

---

## Career Detail

**Investment & leadership:**
- Long/short equity PM, buy-side analyst, DOR, CCO (1998–2025); 14 years as PM
- Sigma Capital (~10 years) — SAC pod, now part of Point72; no down years
- Balyasny Asset Management; Forstmann; other multi-strat and long-biased platforms
- Invested through multiple regimes: dot-com aftermath, post-9/11, GFC, EU debt crisis, COVID, 2022 inflation

**Domain depth:**
- Global healthcare specialization + cross-sector generalist L/S
- FDA pathway fluency; active FOIA user
- Emphasis on alpha-generating shorts (fundamental, catalyst-driven) vs mechanical hedging

**Teaching & talent development:**
- TA and Lecturer for MolBio at Ohio State (1990s) | Taught valuation internally at SAC (2000s)
- Track record hiring and developing analyst teams in high-accountability environments; no analyst turnover.

**Education:**
- MS Data Science (Northwestern, 2022)
- MBA (Rollins College) | BA Biology (Miami University) | Molecular Genetics PhD student (2.5 years FT, ABD) — The Ohio State University

---

## Repository Structure (Intended)

```
/datasets/   — task definitions, scenarios, ground-truth annotations
/rubrics/    — scoring criteria, failure taxonomies, labeling guidelines
/scorers/    — deterministic evaluators (schema + grading logic)
/runs/       — configs, manifests, example outputs, comparison reports
/docs/       — methodology notes, limitations, contribution standards
```


