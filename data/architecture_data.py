"""
Production architecture specifications and resume connections for LAUNCH//REVERSE.
Maps prototype components to production systems and real candidate experience.
"""

from typing import List, Dict, Any

PIPELINE_STAGES = [
    {
        "stage": "PUBLIC ARTIFACTS",
        "description": "Unstructured public web footprint (posts, videos, changelogs, forum threads).",
        "prototype": "Curated 25+ synthetic and public-inspired records.",
        "production": "Permitted REST APIs (X API v2, Product Hunt GraphQL, YouTube Data v3) & RSS/Atom feeds."
    },
    {
        "stage": "COLLECT",
        "description": "Continuous ingestion with deduplication and provenance hashing.",
        "prototype": "In-memory Python dictionaries and Pandas DataFrames.",
        "production": "Distributed Celery/Redis ingestion queue with two-stage deterministic filtering (as built in candidate's API Deprecation Monitoring Platform)."
    },
    {
        "stage": "STRUCTURE",
        "description": "Normalize heterogeneous platform payloads into standard Pydantic document models.",
        "prototype": "LaunchArtifact Pydantic model with day offsets and engagement fields.",
        "production": "FastAPI ingestion endpoints writing to MongoDB document collections with schema validation."
    },
    {
        "stage": "CLASSIFY",
        "description": "Classify narrative theme, author archetype, hook type, and CTA intent.",
        "prototype": "Deterministic keyword mapping and pre-labeled illustrative tags.",
        "production": "Two-stage classifier: fast regex/heuristic pre-filtering followed by structured LLM JSON outputs (JSON mode / Pydantic schema enforcement)."
    },
    {
        "stage": "CONNECT",
        "description": "Build temporal graph relating founder, creator, post, narrative, and launch phase.",
        "prototype": "Chronological timeline index with author-type clustering.",
        "production": "Graph representation in NetworkX/Neo4j linking narrative threads across platforms and measuring network diffusion velocity."
    },
    {
        "stage": "GENERATE HYPOTHESES",
        "description": "Pattern Hunter agent surfaces recurring sequences and correlation clusters.",
        "prototype": "Pre-computed pattern clusters and interactive sandbox query mapper.",
        "production": "ReAct-style Pattern Hunter agent equipped with SQL/Pandas tools to query statistical distribution anomalies."
    },
    {
        "stage": "CHALLENGE HYPOTHESES",
        "description": "Skeptic agent actively seeks counterexamples and tests for confounding variables.",
        "prototype": "Deterministic counterevidence retrieval showing exceptions and confidence caps.",
        "production": "Adversarial Skeptic agent that formulates null hypotheses, searches for counterexamples, and penalizes claims lacking attribution data."
    },
    {
        "stage": "GENERATE INSIGHTS",
        "description": "Synthesize epistemically bounded intelligence report for human strategic review.",
        "prototype": "Interactive insight cards with 'Why This Insight?' breakdown.",
        "production": "Human-in-the-loop executive research console with exportable Markdown/PDF dossiers and verifiable citation links."
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
