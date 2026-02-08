# pm-to-ai | Domain-Expert Evaluation Frameworks

## Bridging buy-side judgment and machine intelligence.


Expert-designed evaluation modules that test whether LLMs can reason correctly in high-stakes, non-stationary decision environments. Focus areas include: decision quality under uncertainty, risk classification and survivability, and detecting fluent but flawed reasoning.

---

## Core Problem

LLMs can sound correct while getting institutional-grade analysis wrong. Failure modes include:

- Misclassifying environmental tailwinds as company-specific alpha
- Overfitting narratives without regime-dependence checks
- Optimizing explanation quality instead of portfolio survivability / Verbosity and wordsmithing
- Producing incomplete or misleading risk decompositions

This repository encodes institutional judgment standards to detect those failures.

---

## Repository Structure 

### 1. fin-reasoning-eval — Inference Benchmark

Curated benchmark for evaluating LLM financial reasoning. 306 problems (and growing) across seven categories: earnings analysis, DCF valuation, fraud detection, catalyst identification, quant model auditing, financial statement analysis, and portfolio risk. Supports Claude, GPT-4, and open-source models with leaderboard and filtering by category and difficulty.

### 2. investment-workflow-evals — Strategic Scoring

Evaluation scenarios testing AI financial reasoning against institutional standards. Covers equity thesis construction, DCF valuation, portfolio construction, and risk attribution. Each scenario includes weighted rubrics, golden answers, and adversarial examples designed to expose common failure modes (e.g., alpha-beta confusion).

### 3. financial-rlhf-studio — Preference Data (DPO)

Direct Preference Optimization workflow where senior analysts correct AI-generated analysis of real documents (10-Ks, research notes). Includes RAG-enhanced generation, side-by-side annotation, visual diff tracking, and a categorized error taxonomy covering hallucinations, accounting standard confusion, and tone mismatches.

### 4. excel-model-eval — Forensic Graph Analysis

Forensic analysis of Excel-based financial models using graph theory. Converts workbooks into directed acyclic graphs to detect hard-coded overrides, circular references, accounting mismatches, and broken links. Optional LLM integration with explicit guardrails separating AI reasoning from execution control.

### 5. redflag_ex1_analyst — Compliance Engine

Rule-based red-teaming engine that scans analyst notes, research PDFs, and IC memos for MNPI, tipping, and regulatory arbitrage risks.

### 6. institutional-investor-casebook — LLM Evaluation for Institutional Finance

Evaluation framework that benchmarks LLM reasoning against institutional-grade financial analysis. Loads hedge fund case studies from JSONL, runs quantized Llama-3-8B inference with multi-GPU distribution and 4-bit NF4 quantization, and compares model outputs to expert golden answers. Purpose-built for constrained VRAM environments with aggressive memory offloading and deterministic sampling for analytical consistency.

---

## AI Training Lifecycle

These modules illustrate an end-to-end development lifecycle for specialized domains:

| Stage | Module | Function |
|---|---|---|
| **Benchmark** | fin-reasoning-eval | Quantify baseline performance across models |
| **Preference Data** | financial-rlhf-studio | Encode tacit domain knowledge into structured training artifacts |
| **Red-Teaming** | redflag_ex1_analyst, investment-workflow-evals | Identify where LLMs break and design tests exposing those failures |
| **Implementation** | excel-model-eval | Build auditable systems automating tasks previously requiring senior humans |

---

## Non-Goals

- General factual recall or trivia
- Simple signal discovery (e.g., sentiment classification)
- Spreadsheet mechanics or formula auditing

---

## Data and Compliance

- **No MNPI or employer-confidential data.** All scenarios are synthetic, auditable, and versioned.
- Built from personal experience and publicly available information.

---

## Contact
[LinkedIn](https://www.linkedin.com/in/brad-schonhoft-cfa)

pm-to-ai partners - **_"Curiosity compounds. Rigor endures."_**---
