# LAUNCH//REVERSE

> *"Reverse-engineering how product launches become distribution."*  
> A conceptual AI-native research tool prototype for Social Capital Inc.

---

## 1. Why I Built This

I didn't want to build another generic AI chatbot or wrap an LLM around a simple prompt.

Social Capital's public focus on product launches, distribution channels, creators, content systems, and go-to-market mechanics sparked a core question:

> **If distribution is an engineered system, can publicly visible launch artifacts be analyzed as structured data to uncover how launches actually build reach?**

Most post-launch analysis starts too late and looks only at vanity metrics: *What happened? How many views? How many likes?*

I wanted to ask a different set of questions:
- What was the chronological structure of the launch?
- Which narratives and pain points were seeded first?
- Who amplified them (Founders, Core Team, Creators, Tech Influencers)?
- What formats (continuous video proof vs contrarian threads) converted attention?
- **Crucially: Which observations are genuinely backed by evidence versus speculative correlation?**

This prototype was built to demonstrate my builder mentality, how I break down ambiguous problems into clean systems, and how I use AI agents with rigorous epistemic skepticism.

---

## 2. What the Prototype Demonstrates

1. **Structured Research Pipelines**: Deconstructing messy, unstructured social posts into normalized schema records (`LaunchArtifact`) with day offsets (`Day -7` to `Day +3`), hook classifications, and engagement metrics.
2. **Multi-Agent ReAct Orchestration**: Visualizing 5 specialized agents with distinct roles:
   - **Agent 01 (Archivist)**: *"What happened?"* — Ingestion & normalization.
   - **Agent 02 (Pattern Hunter)**: *"What appears repeatedly?"* — Structural & temporal clustering.
   - **Agent 03 (Skeptic)**: *"Could this pattern be coincidence?"* — Counterexample search, confounding variable detection, and confidence caps.
   - **Agent 04 (First-Principles Analyst)**: *"What mechanism explains this?"* — Cognitive friction and incentive modeling.
   - **Agent 05 (Synthesizer)**: *"What can we responsibly say?"* — Bounded intelligence dossier.
3. **Strict Epistemic Boundaries**: Distinguishing between four explicit epistemic categories on every card and chart:
   - `[OBSERVED]` — Directly recorded in artifact text or timestamps.
   - `[INFERRED]` — Derived through classification or relational mapping.
   - `[HYPOTHESIS]` — Mechanistic propositions requiring testing.
   - `[SIMULATED]` — Synthetic reference data created for framework demonstration.
4. **The Skeptic Agent & "Why This Insight?" Inspector**: Rather than accepting AI assertions at face value, every insight provides a full audit: supporting artifact counts, counterevidence exceptions, explicit assumptions, skeptic verdicts, and next data required.
5. **Interactive Hypothesis Sandbox**: A live tool allowing users to pick or type a distribution hypothesis (e.g. *Founder-led narrative*, *Creator amplification*, *Product proof*) and trigger an immediate adversarial critique.
6. **Launch DNA Profiling**: An 8-dimensional visual radar (Curiosity, Narrative Tension, Founder Involvement, Creator Involvement, Product Proof, Visual Content, Social Proof, Contrarian Framing) explicitly labeled as an *illustrative framework demonstration*.

---

## 3. Technology Stack & Direct Resume Alignment

The prototype is built with a lightweight, dependable Python stack that connects directly to projects already on my resume:

| Technology | Layer | Resume Project Alignment | Why It Fits This Prototype |
| :--- | :--- | :--- | :--- |
| **Python** | Core Language | Python-based evaluation work | Rapid prototyping, clean data processing, and rich ecosystem |
| **Streamlit** | Research UI | Internal research tools | Fast, high-density, interactive terminal interface without frontend bloat |
| **Plotly** | Visualization | Evaluation metrics dashboards | Interactive timeline Gantt tracks, distributions, and 8-D Launch DNA radar |
| **Pandas & NumPy** | Data Engine | Data pipeline & evaluation benchmarks | Fast in-memory filtering, timeline aggregations, and metric distributions |
| **FastAPI** | Backend / API Layer | **API Deprecation Monitoring Platform** | Lightweight REST service layer (`/api/artifacts`, `/api/hypotheses`, `/api/challenge`) |
| **MongoDB (Schemas)** | Document Model | **ARIS Agent Database** | Flexible JSON-document schemas for storing polymorphic social artifacts |
| **ReAct Tool Agents** | Agent Workflow | **ARIS Agent** | Tool-augmented ReAct reasoning loops replacing monolithic chat prompts |
| **Adversarial Checks** | Skeptic Agent | **Two-stage analysis & eval work** | Deterministic sanity checks and falsification testing before making claims |

---

## 4. What is Simulated (Honesty & Limitations)

- **Simulated & Illustrative Data**: Contains 25+ curated launch artifacts across three case studies:
  1. *Wispr Flow — Launch Analysis* (`Conceptual / public-artifact demo`)
  2. *Gamma — Launch Analysis* (`Conceptual / public-artifact demo`)
  3. *Example AI Startup — Synthetic Dataset* (`Simulated data`)
- **No Private Data**: No private Social Capital data, internal client records, or proprietary systems were accessed or used.
- **No Live Scraping**: The demo operates locally without scraping live websites or risking platform terms-of-service violations.
- **No Causal Proof**: Social media engagement metrics (likes, views, reposts) reflect public attention and platform feed algorithms, **not** private revenue, product conversion, or retention.

---

## 5. What a Production Version Would Require

```
                PUBLIC SOURCES (X API v2, Product Hunt GraphQL, YouTube Data v3, RSS)
                                      ↓
                DATA COLLECTION & INGESTION LAYER (FastAPI + Distributed Celery Queue)
                                      ↓
                NORMALIZATION & TWO-STAGE FILTERING (Pydantic Models + Heuristic Filter)
                                      ↓
                MONGODB & VECTOR STORE (Document Artifacts + pgvector Embeddings)
                                      ↓
                AGENT ORCHESTRATION LAYER (ReAct Loops with Tool Invocation)
                    ┌─────────────────┴─────────────────┐
                    ↓                                   ↓
            AGENT 02: PATTERN HUNTER            AGENT 03: SKEPTIC CRITIC
          (Recurring temporal clusters)       (Counterexamples & Confounders)
                    └─────────────────┬─────────────────┘
                                      ↓
            AGENT 04: FIRST-PRINCIPLES ANALYST (Cognitive & Incentive Modeling)
                                      ↓
            HUMAN-IN-THE-LOOP STRATEGIC REVIEW (Streamlit / React Research Terminal)
                                      ↓
            FINAL BOUNDED INSIGHT DOSSIER (Exportable Evidence Graph)
```

1. **Permitted API Ingestion**: Official API partnerships, rate-limiting queue workers, and webhook listeners.
2. **Cross-Platform Entity Resolution**: Disambiguating founder handles and brand accounts across X, LinkedIn, Product Hunt, and YouTube.
3. **Attribution Telemetry**: Integrating private analytics (UTM links, cohort retention) to bridge the gap between social views and actual product adoption.
4. **Continuous Agent Evaluation**: Automated benchmark test harnesses to evaluate extraction accuracy and catch non-deterministic hallucinations.

---

## 6. What I Don't Know Yet vs. What I Do Know

### What I Don't Know Yet
- How to reliably run large-scale web crawling across hostile anti-bot platforms at 100k+ posts/day without breaking terms of service.
- How to isolate true product conversion from opaque social algorithm recommendation weighting.
- How to handle cross-platform entity resolution when handles and usernames diverge completely.
- Production-scale LLM evaluation pipelines for non-deterministic multi-agent consensus loops.

### What I Do Know How To Do
- Break ambiguous, messy problems down into concrete, testable architectures.
- Prototype fast, high-fidelity tools in Python using Streamlit, FastAPI, and Pandas.
- Design structured schemas that transform unstructured text into actionable data models.
- Build multi-agent workflows with specialized roles, bounded tools, and ReAct-style reasoning.
- Enforce intellectual humility: treating patterns as unverified hypotheses until counterevidence has been evaluated.

---

## 7. Quickstart Guide

### Prerequisites
- Python 3.10+
- Installed packages: `streamlit`, `plotly`, `pandas`, `fastapi`, `uvicorn`, `pydantic`

### Run the Interactive Terminal (Streamlit)
```bash
streamlit run app.py
```
Open your browser at `http://localhost:8501`.

### Run the REST API Layer (FastAPI)
```bash
uvicorn api:app --reload --port 8000
```
View the interactive Swagger API docs at `http://localhost:8000/docs`.

---

## 8. Final Product Principle

> *"I don't need to know every implementation detail before I start building.  
> I can take an ambiguous problem,  
> define a smaller version,  
> make the assumptions explicit,  
> prototype the system,  
> test the reasoning,  
> identify what I don't know,  
> and design the next iteration."*
