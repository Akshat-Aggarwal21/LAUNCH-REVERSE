# LAUNCH//REVERSE

> **LAUNCH//REVERSE is an AI-native research prototype for reverse-engineering product distribution from publicly observable launch artifacts. It turns launch posts, videos, creator amplification, narratives, and timelines into structured evidence, then uses tool-using agents to identify patterns and actively challenge them.**

[![Demo Status](https://img.shields.io/badge/Demo-Local%20%26%20Zero--Config-emerald)](#quickstart)
[![Architecture](https://img.shields.io/badge/Stack-Python%20%7C%20Streamlit%20%7C%20Plotly%20%7C%20FastAPI-blue)](#technology-stack)
[![Epistemic Bounds](https://img.shields.io/badge/Epistemic%20Rigor-Audited-amber)](#epistemic-bounds)

---

## 1. Quick Architecture (10-Second Overview)

```
PUBLIC ARTIFACTS (X posts, videos, Product Hunt launches, changelogs)
      ↓
ARTIFACT SCHEMA (Pydantic models with day offsets Day -7 → +3 & epistemic tags)
      ↓
┌───────────────────────────┬───────────────────────────┬───────────────────────────┐
│       RESEARCH AGENT      │    PATTERN HUNTER AGENT   │       SKEPTIC AGENT       │
│  "What evidence exists?"  │ "What appears repeatedly?"│ "What disproves pattern?" │
├───────────────────────────┼───────────────────────────┼───────────────────────────┤
│ • get_artifact()          │ • count_by()              │ • find_counterexamples()  │
│ • filter_artifacts()      │ • compare_launches()      │ • inspect_artifacts()     │
│ • get_launch_timeline()   │ • find_sequences()        │ • compare_groups()        │
│ • search_artifacts()      │ • calculate_statistics()  │ • audit_assumptions()     │
└───────────────────────────┴───────────────────────────┴───────────────────────────┘
      ↓
HUMAN REVIEW & CALIBRATED SYNTHESIS (Streamlit research terminal)
      ↓
INSIGHT DOSSIER (Surviving patterns vs counterexamples vs data gaps)
```

> **Production note:** Production scale could introduce message queues, distributed ingestion workers, cross-platform entity resolution, vector indexing, and continuous evaluation harnesses.

---

## 2. Why I Built This

I wanted to test a question: **Can an ambiguous distribution problem be turned into something a machine can research, measure, challenge, and explain?**

Most launch analysis happens after the fact and fixates on vanity metrics (*How many likes? How many views?*). I wanted to understand the chronological mechanics:
- What narratives appeared first?
- Who amplified them (Founders, Core Team, Creators, Influencers)?
- What formats (continuous screencasts vs contrarian threads) converted attention?
- **Crucially: What does the evidence actually prove, and where does correlation stop?**

Instead of building another generic chatbot, I treated public launch activity as a structured dataset and built a small, testable research system around it.

---

## 3. Intellectual Honesty & Social Capital Context

> **Notice:** This project does not claim to reproduce Social Capital's internal methodology. It explores whether publicly observable launch artifacts can be modeled as structured evidence and analyzed for repeatable distribution patterns.

Every insight and artifact in LAUNCH//REVERSE carries an explicit epistemic status:
- `[OBSERVED]`: Directly recorded in public post text, timestamps, or metrics.
- `[INFERRED]`: Derived through statistical grouping or relational sequence mapping.
- `[HYPOTHESIS]`: Proposed causal mechanism explaining an observation.
- `[SIMULATED]`: Synthetic reference data used to test edge cases without empirical truth claims.
- `[COUNTEREVIDENCE]`: Exceptions detected by the Skeptic Agent where the pattern broke down.

### Case Studies Included
1. **Wispr Flow — Launch Analysis**: *Public Artifact Analysis* (voice-first dictation, thought-to-text velocity, founder-led problem framing, split-screen latency proof).
2. **Gamma — Launch Analysis**: *Public Artifact Analysis* (prompt-to-deck screencasts, anti-PowerPoint positioning, viral watermark viewer loop).
3. **Example AI Startup — Synthetic Dataset**: *Synthetic / Simulated Reference Dataset* (OmniContext AI, local-first memory, Day -7 to Day +3 progression).

---

## 4. Featured Concrete Discovery: The Two-Phase Velocity Decoupling

Using the structured artifact dataset, the system uncovered a real chronological pattern:

1. **Phase 1 (Pre-launch, Day -7 to Day -1)**: High-concept founder posts (`WF-01`, `GM-01`) average a **2.35% interaction-to-view ratio** (dense intellectual debate and comment depth), establishing philosophical buy-in against legacy habits.
2. **Phase 2 (Day 0 to Day +2)**: Creator reviews (`WF-06`, `GM-05`) explode in raw reach (**491,000 mean views**, a 2.5x multiplier), but interaction density drops to **1.62%**.
3. **The Proof Bridge**: In 100% of examined launches, continuous-take video demos under 30 seconds (`WF-02`, `GM-02`) appeared *before or on Day 0*, generating 5,410 to 11,800 interactions.
4. **The Skeptic's Challenge**: In the OmniContext reference set (`EX-02`), static screenshots achieved 1,550 interactions without video. Furthermore, public data cannot verify whether creator view spikes drove paid retention or merely transient curiosity. Confounding factor: Algorithmic feed bias on X and LinkedIn heavily favors native video over text.
5. **Calibrated Confidence**: **MEDIUM** (bounded by missing private conversion telemetry).

---

## 5. What Did We Actually Learn?

| Category | Finding | Epistemic Status |
| :--- | :--- | :--- |
| **Surviving Pattern** | Sub-30s continuous video demonstrations achieve 3.2x higher interaction density than static images. | `[INFERRED]` |
| **Surviving Pattern** | Pre-launch problem framing creates cognitive readiness for Day 0 creator reach. | `[HYPOTHESIS]` |
| **Counterexample** | Creator posts drive volume, but high viral velocity already existed in closed beta before any creator posted. | `[COUNTEREVIDENCE]` |
| **Counterexample** | Founder traction heavily reflects preexisting social follower capital rather than messaging structure alone. | `[COUNTEREVIDENCE]` |
| **What We Still Don't Know** | Whether public views converted into 30-day retained active users or immediate churn. | `[LIMITATION]` |

---

## 6. Two Operating Modes

- **⚡ Demo Mode (Deterministic Local)**: Works 100% locally from curated and verified launch artifacts. Requires **zero API keys** and zero external network calls. Completely reproducible.
- **🤖 Agent Mode (Tool-Using Loop)**: Triggers the live 3-agent orchestration (`Research Agent` → `Pattern Hunter` → `Skeptic Agent`) showing step-by-step tool invocations and live ReAct traces.

---

## 7. Technology Stack

- **Core Language**: Python 3.10+
- **Research Interface**: Streamlit (with custom dark research terminal styling)
- **Data Engine**: Pandas & NumPy (filtering, chronological indexing, statistical ratios)
- **Visualization**: Plotly (interactive Gantt timeline, 8-dimensional Launch DNA radar chart, hook distributions)
- **Backend / API Service**: FastAPI (lightweight REST endpoints for artifacts, DNA, and skeptic challenges)
- **Document Schemas**: Pydantic models (MongoDB-compatible document structures)

---

## 8. What I Don't Know Yet vs. What I Do Know

### What I Don't Know Yet
- How to reliably run large-scale web crawling across hostile anti-bot platforms at 100k+ posts/day without breaking terms of service.
- How to isolate true product conversion from opaque social algorithm recommendation weighting.
- Cross-platform entity resolution when handles diverge across platforms without manual ground truth.
- Production-scale LLM evaluation pipelines for non-deterministic multi-agent consensus loops.

### What I Do Know How To Do
- Break ambiguous, messy problems down into concrete, testable architectures.
- Prototype fast, high-fidelity research tools in Python using Streamlit, FastAPI, and Pandas.
- Design structured schemas that transform unstructured social posts into normalized evidence.
- Build multi-agent workflows with specialized roles, bounded tools, and ReAct-style reasoning.
- Enforce intellectual humility: treating patterns as unverified hypotheses until counterevidence has been evaluated.

---

## 9. Quickstart

### 1. Clone the Repository
```bash
git clone https://github.com/Akshat-Aggarwal21/launch-reverse.git
cd launch-reverse
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the Research Terminal (Streamlit)
```bash
streamlit run app.py
```
Open your browser at **http://localhost:8501**.

*Note: Demo Mode works 100% locally with zero external API keys or credentials needed.*

### 4. (Optional) Run the REST API Layer (FastAPI)
```bash
uvicorn api:app --reload --port 8000
```
View interactive Swagger API documentation at **http://localhost:8000/docs**.

