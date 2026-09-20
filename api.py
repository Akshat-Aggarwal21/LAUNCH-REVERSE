"""
FastAPI Backend Layer for LAUNCH//REVERSE.
Provides REST API endpoints for launch artifacts, hypotheses, Launch DNA, and agent traces.
Parallels the backend architecture used in the candidate's API Deprecation Monitoring Platform and ARIS Agent.
"""

from typing import List, Dict, Any, Optional
from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from core.models import LaunchArtifact, LaunchDnaProfile, HypothesisRecord
from data.artifacts import RAW_ARTIFACTS, get_artifacts_by_case_study
from data.hypotheses import HYPOTHESES_DATA, PRESET_HYPOTHESES_SANDBOX
from data.launch_dna import LAUNCH_DNA_PROFILES
from data.agents_data import AGENTS_METADATA, SIMULATED_AGENT_TRACES
from core.engine import engine

app = FastAPI(
    title="LAUNCH//REVERSE API",
    description="Lightweight research terminal API layer for reverse-engineering product launches into testable hypotheses.",
    version="0.1.0"
)

# Enable CORS for local cross-origin prototyping
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChallengeRequest(BaseModel):
    category_or_query: str


@app.get("/")
def read_root():
    return {
        "project": "LAUNCH//REVERSE",
        "tagline": "Reverse-engineering how product launches become distribution.",
        "status": "PROTOTYPE_ONLINE",
        "epistemic_guarantee": "Strict distinction between OBSERVED, INFERRED, HYPOTHESIS, and SIMULATED data."
    }


@app.get("/api/case-studies")
def get_case_studies():
    """Returns available case studies."""
    return [
        {
            "id": "wispr-flow",
            "title": "Wispr Flow — Launch Analysis",
            "type": "Conceptual / public-artifact demo",
            "company": "Wispr Flow"
        },
        {
            "id": "gamma",
            "title": "Gamma — Launch Analysis",
            "type": "Conceptual / public-artifact demo",
            "company": "Gamma"
        },
        {
            "id": "example-ai",
            "title": "Example AI Startup — Synthetic Dataset",
            "type": "Simulated data",
            "company": "OmniContext AI"
        }
    ]


@app.get("/api/artifacts")
def get_artifacts(case_study_id: Optional[str] = Query(None)):
    """Fetch structured launch artifacts, optionally filtered by case study."""
    if case_study_id:
        return get_artifacts_by_case_study(case_study_id)
    return RAW_ARTIFACTS


@app.get("/api/dna/{case_study_id}")
def get_dna(case_study_id: str):
    """Retrieve 8-dimensional Launch DNA profile."""
    if case_study_id not in LAUNCH_DNA_PROFILES:
        raise HTTPException(status_code=404, detail="Case study not found")
    return LAUNCH_DNA_PROFILES[case_study_id]


@app.get("/api/hypotheses")
def get_hypotheses():
    """Retrieve evidence-grounded hypotheses and Skeptic counterarguments."""
    return HYPOTHESES_DATA


@app.get("/api/agents/traces/{case_study_id}")
def get_agent_traces(case_study_id: str, focus_topic: Optional[str] = Query("launch_sequence")):
    """Retrieve multi-agent execution traces for the 3 tool-using agents (Research, Pattern Hunter, Skeptic)."""
    from core.agent_orchestrator import run_agentic_research_pipeline
    return run_agentic_research_pipeline(case_study_id, focus_topic=focus_topic)



@app.post("/api/challenge")
def challenge_hypothesis(req: ChallengeRequest):
    """
    Skeptic Agent endpoint to challenge a hypothesis.
    Returns supporting evidence, counterevidence, assumptions, and confidence score.
    """
    return engine.challenge_hypothesis(req.category_or_query)
