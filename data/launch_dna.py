"""
Launch DNA 8-dimensional profiles for LAUNCH//REVERSE.
Explicitly marked as ILLUSTRATIVE CLASSIFICATION.
"""

from typing import Dict, Any

LAUNCH_DNA_PROFILES: Dict[str, Dict[str, Any]] = {
    "wispr-flow": {
        "company_name": "Wispr Flow",
        "case_study_title": "Wispr Flow — Launch Analysis",
        "badge_type": "Conceptual / public-artifact demo",
        "archetype": "Velocity & Problem-Shifted Dictation",
        "dimensions": {
            "Curiosity": 78,
            "Narrative Tension": 88,
            "Founder Involvement": 92,
            "Creator Involvement": 84,
            "Product Proof": 95,
            "Visual Content": 86,
            "Social Proof": 90,
            "Contrarian Framing": 82
        },
        "description": "Heavy emphasis on real-time latency demonstration (Product Proof 95%) and founder-led philosophical framing against typing (Founder Involvement 92%, Narrative Tension 88%). Amplified via creator workflow screencasts on Day 0 and Day +2.",
        "key_takeaway": "Focuses on tangible speed proof over marketing fluff to collapse skepticism."
    },
    "gamma": {
        "company_name": "Gamma",
        "case_study_title": "Gamma — Launch Analysis",
        "badge_type": "Conceptual / public-artifact demo",
        "archetype": "Generative Canvas & Viral Loop Engine",
        "dimensions": {
            "Curiosity": 90,
            "Narrative Tension": 85,
            "Founder Involvement": 76,
            "Creator Involvement": 94,
            "Product Proof": 89,
            "Visual Content": 96,
            "Social Proof": 92,
            "Contrarian Framing": 88
        },
        "description": "Driven by breathtaking visual content (Visual Content 96%) and widespread creator curation (Creator Involvement 94%). Attack on legacy slide formatting creates viral social currency.",
        "key_takeaway": "Combines prompt-to-presentation 'magic moments' with an intrinsic viewer-to-creator referral loop."
    },
    "example-ai": {
        "company_name": "OmniContext AI",
        "case_study_title": "Example AI Startup — Synthetic Dataset",
        "badge_type": "Simulated data",
        "archetype": "Local-First Semantic Memory Layer",
        "dimensions": {
            "Curiosity": 82,
            "Narrative Tension": 79,
            "Founder Involvement": 85,
            "Creator Involvement": 65,
            "Product Proof": 78,
            "Visual Content": 70,
            "Social Proof": 72,
            "Contrarian Framing": 80
        },
        "description": "Synthetic dataset illustrating a technical founder challenging context-window limitations in favor of on-device semantic memory. Relies more on technical architecture posts than creator hype.",
        "key_takeaway": "Architecture-driven launch balancing privacy guarantees with early waitlist onboarding."
    }
}

DNA_DISCLAIMER = (
    "ILLUSTRATIVE CLASSIFICATION: These scores demonstrate the proposed analytical framework, "
    "not measured causal effects or scientifically validated performance metrics."
)
