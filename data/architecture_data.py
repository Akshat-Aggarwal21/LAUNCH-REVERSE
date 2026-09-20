"""
Production architecture specifications and resume connections for LAUNCH//REVERSE.
Maps prototype components to production systems and real candidate experience.
"""

from typing import List, Dict, Any

PIPELINE_STAGES = [
    {
        "stage": "1. PUBLIC SOURCES",
        "description": "Publicly observable web footprint (X posts, videos, changelogs, forum threads).",
        "prototype": "Curated 25+ public-artifact analyses and synthetic reference records.",
        "production": "Permitted REST APIs (X API v2, Product Hunt GraphQL, YouTube Data v3) & RSS feeds."
    },
    {
        "stage": "2. INGESTION",
        "description": "Raw payload ingestion with provenance metadata (source URL, author handle, platform timestamp).",
        "prototype": "In-memory Python dictionaries and Pandas DataFrames with source provenance.",
        "production": "Asynchronous REST ingestion endpoints with deduplication and SHA-256 provenance hashing."
    },
    {
        "stage": "3. NORMALIZATION",
        "description": "Normalize heterogeneous platform payloads into standard Pydantic models with relative day offsets (Day -7 → +3).",
        "prototype": "LaunchArtifact Pydantic model with day offsets and engagement fields.",
        "production": "FastAPI normalization service writing to MongoDB document collections with strict schema validation."
    },
    {
        "stage": "4. RESEARCH AGENT",
        "description": "Gathers and structures evidence using constrained retrieval tools.",
        "prototype": "Tool-equipped agent using get_artifact(), filter_artifacts(), get_launch_timeline(), search_artifacts().",
        "production": "Tool-augmented agent querying MongoDB document collections and chronological indexes."
    },
    {
        "stage": "5. PATTERN HUNTER",
        "description": "Detects recurring temporal sequences, author handoffs, and format distributions.",
        "prototype": "Tool-equipped agent using count_by(), compare_launches(), find_sequences(), calculate_statistics().",
        "production": "Statistical sequence mining across normalized cohort graphs."
    },
    {
        "stage": "6. SKEPTIC AGENT",
        "description": "Actively seeks counterexamples, tests confounders, and enforces epistemic bounds.",
        "prototype": "Adversarial agent using find_counterexamples(), inspect_artifacts(), compare_groups().",
        "production": "Automated adversarial verification evaluating against null hypotheses and penalizing missing conversion telemetry."
    },
    {
        "stage": "7. HUMAN REVIEW",
        "description": "Interactive researcher interrogation with 'Why This Insight?' audits and counterexample inspection.",
        "prototype": "Streamlit research terminal with epistemic badges and interactive Skeptic Sandbox.",
        "production": "Executive research console with verifiable citation links and provenance audit trails."
    },
    {
        "stage": "8. INSIGHT DOSSIER",
        "description": "Epistemically calibrated intelligence report separating surviving patterns from data gaps.",
        "prototype": "'What Did We Actually Learn?' report separating patterns, counterevidence, and missing telemetry.",
        "production": "Automated research dossiers exported to Markdown/JSON with calibrated confidence ratings."
    }
]



RESUME_CONNECTIONS = [
    {
        "component": "AI Agents & Tool Use (ReAct Loop)",
        "tech": "Python, Tool-augmented LLM orchestration",
        "resume_project": "ARIS Agent (Autonomous Research & Intelligence System)",
        "connection_detail": "Directly parallels the ARIS agent architecture: giving specialized LLM agents dedicated tool interfaces (MongoDB document retrieval, Python code execution, schema validation) rather than relying on unstructured chat prompts."
    },
    {
        "component": "Two-Stage Ingestion & Classification",
        "tech": "FastAPI, REST APIs, RSS Feeds, Heuristic + LLM Pipeline",
        "resume_project": "API Deprecation Monitoring Platform",
        "connection_detail": "Adapts the two-stage monitoring workflow: using cheap deterministic filtering and regex to discard noise at the ingestion layer before passing high-signal candidates to LLMs for deep semantic classification, drastically saving compute and API costs."
    },
    {
        "component": "Structured Artifact Storage & Results Cache",
        "tech": "MongoDB & PyMongo / Motor",
        "resume_project": "ARIS Agent Database Layer",
        "connection_detail": "Uses MongoDB flexible schema documents to store raw polymorphic social artifacts alongside versioned agent execution traces and confidence scores."
    },
    {
        "component": "Adversarial Verification & Epistemic Bounds",
        "tech": "Python, Pandas, NumPy, Automated Evaluation Harnesses",
        "resume_project": "Python-Based Evaluation Work",
        "connection_detail": "Brings rigorous evaluation discipline to launch analysis: building a dedicated 'Skeptic Agent' that treats claims as unverified hypotheses until counterevidence has been systematically queried, avoiding AI hallucination."
    }
]


BUILD_LOG = [
    {
        "step": "01",
        "title": "Framing the Problem",
        "question": "Can launch distribution be represented as structured data rather than marketing lore?",
        "detail": "Started by decomposing viral launches into atomic events: who posted, when relative to launch day, with what hook, and what narrative tension."
    },
    {
        "step": "02",
        "title": "Designing the Artifact Schema",
        "question": "What minimal schema captures launch anatomy without platform-specific lock-in?",
        "detail": "Designed the LaunchArtifact schema with day offsets (Day -7 to Day +3), author archetypes, hook categories, and explicit epistemic tags (OBSERVED, INFERRED, HYPOTHESIS, SIMULATED)."
    },
    {
        "step": "03",
        "title": "Separating Observations from Hypotheses",
        "question": "How do we prevent AI from presenting correlation as objective fact?",
        "detail": "Established the strict rule: an observation is only what is recorded in the data; any claim about why it worked or whether it drove conversion is explicitly labeled a HYPOTHESIS."
    },
    {
        "step": "04",
        "title": "Adding the Skeptic Agent",
        "question": "What happens when pattern detection creates false-positive conclusions?",
        "detail": "Pattern recognition without skepticism generates marketing fluff. Added Agent 03 (Skeptic) specifically tasked with finding counterexamples, pointing out confounding variables (e.g. founder preexisting follower counts), and capping confidence scores."
    },
    {
        "step": "05",
        "title": "Designing the Production Architecture",
        "question": "How does this prototype scale into an enterprise intelligence system?",
        "detail": "Designed the full production roadmap (FastAPI, MongoDB, vector indexing, ReAct tool agents) without building unnecessary infrastructure into this lightweight client-side demo."
    },
    {
        "step": "06",
        "title": "Building the Interactive Terminal",
        "question": "How do we make the thinking transparent in under 60 seconds?",
        "detail": "Built the complete interactive Streamlit research terminal with Plotly Gantt/Timeline, Launch DNA radar, ReAct agent trace runner, and the signature 'Why This Insight?' inspector."
    }
]


KNOW_VS_DONT_KNOW = {
    "dont_know": [
        {
            "topic": "Reliable Large-Scale Public Data Collection",
            "detail": "Managing anti-scraping safeguards, distributed proxies, and platform TOS compliance at 100k+ posts/day scale."
        },
        {
            "topic": "Platform API Volatility & Rate Limiting",
            "detail": "Handling sudden X API v2 pricing shifts, rate quotas, and undocumented GraphQL schema mutations across multiple social networks."
        },
        {
            "topic": "Cross-Platform Entity Resolution",
            "detail": "Disambiguating whether '@tanay' on X is the same individual as 'Tanay Kothari' on LinkedIn, Substack, or Product Hunt without manual ground truth."
        },
        {
            "topic": "Causal Inference from Biased Social Metrics",
            "detail": "Separating true product conversion from algorithmic platform bias (e.g. video boosts, outrage virality) without access to private internal analytics."
        },
        {
            "topic": "Production Agent Evaluation at Scale",
            "detail": "Building automated CI/CD benchmark suites to detect drift and hallucination across non-deterministic multi-agent consensus loops."
        }
    ],
    "do_know": [
        {
            "topic": "Decompose Ambiguous Problems",
            "detail": "Transforming a nebulous question ('Why did this launch blow up?') into testable, structured data pipelines."
        },
        {
            "topic": "Build Fast, Functional Prototypes",
            "detail": "Shipping clean, high-density interactive tools that validate user workflows before writing thousands of lines of backend glue."
        },
        {
            "topic": "Structure Messy Information",
            "detail": "Designing clean Pydantic and MongoDB document schemas that turn polymorphic social posts into normalized research artifacts."
        },
        {
            "topic": "Multi-Agent ReAct Orchestration",
            "detail": "Structuring agent workflows with explicit roles, specialized tool interfaces, and ReAct-style thought-action-observation cycles."
        },
        {
            "topic": "Intellectual Humility & Skepticism",
            "detail": "Enforcing strict epistemic boundaries between what is observed, what is inferred, and what remains an unverified hypothesis."
        },
        {
            "topic": "Rapid Builder Iteration",
            "detail": "Tying new problem spaces directly back to established technical foundations (Python, FastAPI, Streamlit, Pandas, MongoDB) to deliver working software quickly."
        }
    ]
}
