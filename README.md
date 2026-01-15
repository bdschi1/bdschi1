
# pm-to-ai | Domain Expert Evaluation for LLMs (Equity L/S, Healthcare)

pm-to-ai is a founder-led effort with a single objective: deliver high-quality
contract work as a domain expert for AI model training, evaluation, and
adversarial testing—then scale the capability over time. pm-to-ai was founded 12/2025.

The focus is institutional equity long/short decision-making, with an initial
emphasis on global healthcare and risk management frameworks. The operating principle is “cost of error”:
evaluate and train models on the failures that matter in real workflows—where
mistakes compound across evidence, conviction, portfolio construction, and risk.

This repository is the public portfolio: rubrics, datasets, scorers, and run
artifacts that demonstrate how discretionary buy-side judgment can be translated
into machine-readable ground truth and reproducible evaluation.


## Engagement

For contracting inquiries, it is most efficient to include:

- Workflow (examples: trial readout reasoning, FDA/regulatory pathway logic,
  healthcare thesis memo quality, catalyst mapping, portfolio hedging and sizing,
  short thesis robustness)
- Output format (free text vs structured JSON; schema constraints; rubric/grader
  requirements)
- Failure modes (hallucination, evidence gaps, shallow bear case, consensus-
  hugging, endpoint mistakes, poor uncertainty handling)
- Volume, cadence, and timeline (items per week; sprint length; review cycle)

Contact:
- LinkedIn: https://www.linkedin.com/in/brad-schonhoft-cfa


## Operating model

pm-to-ai is founder-led today for speed, accountability, and consistency of
standards.

For larger scopes or multi-vertical coverage, I can bring in vetted domain
partners (buy-side and technical) from a long-standing network under a single
rubric and QA process, once scope and acceptance criteria are defined.


## What I deliver

I am most valuable where you need domain-expert ground truth that is realistic,
auditable, and usable by an evaluation team.

Typical deliverables:

- **Rubrics and scoring guides**
  - Institutional standards with explicit pass/fail thresholds
  - Failure taxonomies tied to “cost of error”
  - Clear separation of known facts vs inference vs speculation

- **Expert-labeled datasets**
  - Labeled examples with rationales and “what would change my mind”
  - Counterexamples, edge cases, and adversarial variants
  - Consistent terminology and definitions for downstream annotators

- **Adversarial test suites**
  - Scenarios designed to expose consequential failure modes
  - Stress tests where errors compound across multi-step workflows
  - Regression sets suitable for model iteration cycles

- **Evaluation task design**
  - Scenario construction, prompt sets, acceptance criteria, and scoring plans
  - Stateful decision chains when portfolio realism matters

- **Scoring harness direction (as needed)**
  - Structured-output contracts and schema validation
  - Deterministic grading logic and reproducibility discipline
  - Versioned datasets/prompts and regression-oriented run configs


## Evaluation standards

The evaluation lens is how a PM reviews work product in a real decision process:

- **Variant view quality:** specific, testable, and differentiated edge
- **Bear-case rigor:** disconfirming evidence, downside path completeness, and
  clarity on what breaks the thesis
- **Evidence hygiene:** transparent separation of facts, inference, and
  uncertainty
- **Decision realism:** constraints, timing, and second-order portfolio effects
- **Conviction updates:** correct updating under conflicting or partial data
- **Cost-of-error focus:** whether failures would drive material PnL or decision
  quality degradation


## Featured frameworks in this repo

This repo is organized around three evaluation families. Each will include
datasets, rubrics, scoring guidance, and run artifacts as it is published.

### 1) Healthcare PM LLM Evals

Focus: biotech/clinical reasoning and FDA/regulatory pathways.

Targets:
- Trial design logic (endpoints, power, populations, comparators)
- Readout interpretation and uncertainty handling
- Regulatory constraints and pathway realism
- Mechanism plausibility vs narrative-only reasoning

### 2) Equity Research Scorer

Focus: institutional-quality investment memos.

Targets:
- Variant view clarity and falsifiability
- Bear-case depth and scenario thinking
- Mosaic integration (how evidence supports conviction)
- Differentiated insight vs consensus paraphrase

### 3) Thematic Unitization Lab

Focus: “trade packages” as a single synthetic risk unit (longs/shorts/hedges,
options/ETFs/baskets), rather than isolated tickers.

Targets:
- Coherence of multi-leg intent (what is being hedged and why)
- Portfolio realism and exposure management
- Decision updates as new information arrives (conviction and sizing)


## Reproducibility and instrumentation (proof over claims)

This work is structured so an eval lead can audit and rerun results:

- Versioned datasets and prompts (changes tracked explicitly)
- Deterministic scoring where possible (schema-first outputs; repeatable graders)
- Run manifests capturing the evaluation configuration (dataset version, prompt
  version, scorer version, and environment)
- Regression sets that preserve discovered failure modes across model iterations

As the repo matures, example run artifacts will live in `/runs/` and include:
- Configs (what was tested)
- Outputs (what the model produced)
- Scores (how it was graded)
- Notes (what failed and why)


## Infrastructure and execution environment

Infrastructure is not the product; it supports reliable delivery. Current
capacity enables controlled benchmarking and local-first workflows:

- Local compute includes a **Lambda GPU workstation** (Ubuntu/Windows/CUDA) for
  secure workflows and repeatable evaluation runs.
- Apple silicon workflows (MacBook Pro M4-class machines; **128GB unified
  memory configurations**) for local experimentation and agentic tooling.
- Support for secure / air-gapped auditing patterns when required by a client,
  implemented via client-approved procedures.


## Data hygiene and confidentiality

- No MNPI. No employer-confidential process leakage.
- Public releases use synthetic scenarios and/or public information only.
- Client work can be performed under NDA with clear boundaries.
- Evals are designed to be auditable, reproducible, and versioned.


## Background (compressed)

Brad Schonhoft, CFA (chartered 2001)

- Long/short equity PM and buy-side analyst >20 years; 14 years as Senior PM;
  managed up to ~$750M AUM (peak).
- Institutional platforms include Sigma Capital (Point72; ~10 years), Balyasny,
  and other hedge fund environments.
- Deep global healthcare specialization plus cross-sector generalist L/S
  experience. 
- Regulatory and primary research orientation (FDA pathway fluency; active FOIA
  usage).
- MS Data Science (Northwestern, 2022); modern ML/LLM evaluation tooling literacy and python/R.
- Additional education: MBA (Rollins); BA Biology (Miami University); Molecular
  Genetics PhD program - all coursework (2 years FT; ABD).


## Repository structure (intended)

- /datasets/  — task definitions, scenarios, and ground-truth annotations
- /rubrics/   — scoring criteria, failure taxonomies, and labeling guidelines
- /scorers/   — deterministic evaluators (schema + grading logic)
- /runs/      — configs, manifests, example outputs, and comparison reports
- /docs/      — methodology notes, limitations, and contribution standards


## Roadmap (only insofar as it supports delivery)

Near-term (2026):
- Publish healthcare eval rubrics plus labeled examples and adversarial variants
- Expand portfolio/risk tasks (sizing, hedging, factor exposure awareness)
- Add regression suites capturing failure modes discovered through contract work

Longer-term (2h2026-2027)
- Adjacent workflows where cost of error is high (REIT/real estate frameworks,
  investment committee multi-step logic, sell-side to PM distillation)


## Contact

LinkedIn: https://www.linkedin.com/in/brad-schonhoft-cfa
```
