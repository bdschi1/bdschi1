# Brad Schonhoft, CFA

Former institutional long/short portfolio manager building tools and evaluation frameworks that bring buy-side investment judgment to AI systems.

These projects exist because LLMs routinely fail at the things that matter most in professional investing: distinguishing alpha from environmental tailwinds, sizing risk correctly, and recognizing when a confident-sounding thesis is structurally fragile. Each repo attacks a different piece of that problem.

All projects are ongoing efforts.

---

## Projects

### [fin-reasoning-eval](https://github.com/bdschi1/fin-reasoning-eval)
Benchmark for evaluating LLM performance on financial reasoning tasks. 306 curated problems across seven categories — earnings analysis, DCF valuation, fraud detection, catalyst identification, quant model auditing, financial statement analysis, and portfolio risk. Supports Claude, GPT-4, and open-source models with a leaderboard and filtering by category and difficulty.

### [investment-workflow-evals](https://github.com/bdschi1/investment-workflow-evals)
Evaluation scenarios that test AI financial reasoning against institutional standards. Covers equity thesis construction, DCF valuation, portfolio construction, and risk attribution. Each scenario includes weighted rubrics, golden answers, and adversarial examples designed to expose common failure modes like confusing environmental tailwinds with company-specific alpha.

### [financial-rlhf-studio](https://github.com/bdschi1/financial-rlhf-studio)
Direct Preference Optimization workflow where financial analysts correct AI-generated analysis of real documents (10-Ks, research notes) to build training datasets. Includes RAG-enhanced generation, side-by-side annotation, visual diff tracking, and a categorized error taxonomy covering hallucinations, accounting standard confusion, and tone mismatches.

### [excel-model-eval](https://github.com/bdschi1/excel-model-eval)
Forensic analysis of Excel-based financial models using graph theory. Converts workbooks into directed acyclic graphs to detect hard-coded overrides, circular references, accounting mismatches, and broken links that manual review misses. Optional LLM integration with explicit guardrails keeping AI reasoning separate from execution control.

### [redflag_ex1_analyst](https://github.com/bdschi1/redflag_ex1_analyst)
Rule-based red-teaming engine that scans analyst notes, research PDFs, and IC memos for MNPI, tipping, and regulatory arbitrage risks.

---

**Contact:** [linkedin.com/in/brad-schonhoft-cfa](https://www.linkedin.com/in/brad-schonhoft-cfa)
