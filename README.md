# pm-to-ai | Domain Expert Evaluation Frameworks

Former institutional long/short PM translating **buy-side investment judgment** into **machine-readable evaluation artifacts** for AI model training, assessment, and red-teaming.

---

## What This Repo Is

A portfolio of **expert-designed evaluation modules** that test whether LLMs can reason correctly in **high-stakes, non-stationary decision environments**.

Focus:

* Decision quality under uncertainty
* Risk classification and survivability
* Avoiding fluent but dangerous reasoning

Not focused on:

* Factual recall
* Signal discovery
* Spreadsheet mechanics

---

## Core Problem Addressed

LLMs often:

* Sound correct while misclassifying **environmental effects as alpha**
* Overfit narratives
* Ignore regime dependence and fragility
* Optimize explanations instead of survivability

This repo encodes **institutional judgment standards** to detect those failures.

---

## Repository Structure (6 Evaluation Modules)

1. **Equity Thesis Evaluation**
   Variant views, evidence hygiene, bear cases, conviction updates, optionality.

2. **DCF & Valuation Judgment**
   Assumption discipline, terminal value risk, normalization vs uncertainty.

3. **Portfolio Construction**
   Risk-based sizing, hedging vs intentional exposure, correlation instability.

4. **Earnings & Event Interpretation**
   Signal vs noise, information decay, post-event second-order risks.

5. **Risk Attribution**
   Factor vs idiosyncratic outcomes, hypothesis falsification, process vs P&L.

6. **Spurious Correlation & Fragility**
   Classification and management of predictive but non-causal relationships.
   Tests whether a model can **use correlations without believing them**.

---

## Evaluation Methodology

All modules share a common rubric.

**Universal scoring axes (0–3):**

1. Correct classification (alpha vs environment vs regime)
2. Fragility and regime awareness
3. Explicit risk treatment (sizing, hedging, decay)
4. **Critical failure avoidance**
   → Misclassified environmental or spurious correlation as durable alpha

Each scenario includes:

* Clear task prompt
* Explicit grading rubric
* Anchor answers (strong / acceptable / failing)
* Adversarial variants that sound intelligent but are wrong

---

## Domain Focus

Healthcare equity (biotech, pharma, medtech, tools, services).

Chosen because it naturally embeds:

* Binary outcomes
* Skew and convexity
* Reflexivity and crowding
* Regulatory and policy risk

---

## Intended Use

* Model evaluation and benchmarking
* RLHF / preference-learning datasets
* Red-teaming financial reasoning
* Human-in-the-loop training workflows

Demonstrates ability to:

* Convert tacit expert judgment into evaluable structure
* Design high-signal failure-mode tests
* Evaluate reasoning, not just answers

---

## Data & Compliance

* No MNPI
* No employer-confidential processes
* Synthetic, auditable, versioned scenarios

---

**Contact:** [www.linkedin.com/in/brad-schonhoft-cfa](http://www.linkedin.com/in/brad-schonhoft-cfa)
**License:** MIT
