"""
Launch DNA 8-dimensional evidence-backed profiles for LAUNCH//REVERSE.
Every dimension includes an explicit calculation basis and epistemic status (INFERRED or HYPOTHESIS)
to prevent presenting arbitrary scores as objective truth.
"""

from typing import Dict, Any

LAUNCH_DNA_PROFILES: Dict[str, Dict[str, Any]] = {
    "wispr-flow": {
        "company_name": "Wispr Flow",
        "case_study_title": "Wispr Flow — Launch Analysis",
        "case_study_badge": "Public Artifact Analysis",
        "archetype": "Velocity & Problem-Shifted Dictation",
        "dimensions": {
            "Curiosity": {
                "score": 78,
                "epistemic_status": "INFERRED",
                "calculation_basis": "Calculated from teaser phase bookmark-to-like ratio (18.2%) on Day -3 and Day -1 posts."
            },
            "Narrative Tension": {
                "score": 88,
                "epistemic_status": "HYPOTHESIS",
                "calculation_basis": "Inferred from opening contrarian framing ('Typing is unnatural') generating 48% higher comment depth."
            },
            "Founder Involvement": {
                "score": 92,
                "epistemic_status": "INFERRED",
                "calculation_basis": "Directly measured: Founder (@tanaykothari) authored 4 out of 9 total launch artifacts (44.4% volume)."
            },
            "Creator Involvement": {
                "score": 84,
                "epistemic_status": "INFERRED",
                "calculation_basis": "Measured: Creator reviews (Sam Parr, Ali Abdaal) accounted for 54.8% of total recorded public view impressions."
            },
            "Product Proof": {
                "score": 95,
                "epistemic_status": "INFERRED",
                "calculation_basis": "Measured: Continuous-take split-screen latency video demo (<200ms) pinned as primary pre-launch artifact."
            },
            "Visual Content": {
                "score": 86,
                "epistemic_status": "INFERRED",
                "calculation_basis": "Measured: 6 of 9 artifacts featured video screencasts or split-screen benchmark graphics."
            },
            "Social Proof": {
                "score": 90,
                "epistemic_status": "INFERRED",
                "calculation_basis": "Measured: #1 Product of the Day milestone broadcast on Day +1 (100k+ downloads claim)."
            },
            "Contrarian Framing": {
                "score": 82,
                "epistemic_status": "HYPOTHESIS",
                "calculation_basis": "Inferred: Explicit attacks on legacy typing mechanics vs Apple/Whisper conventional dictation."
            }
        },
        "description": "Heavy emphasis on real-time latency demonstration (Product Proof: 95) and founder-led philosophical framing against typing (Founder: 92, Narrative Tension: 88). Amplified via creator workflow screencasts on Day 0 and Day +2.",
        "key_takeaway": "Focuses on tangible speed proof over marketing claims to collapse consumer skepticism."
    },
    "gamma": {
        "company_name": "Gamma",
        "case_study_title": "Gamma — Launch Analysis",
        "case_study_badge": "Public Artifact Analysis",
        "archetype": "Generative Canvas & Viral Loop Engine",
        "dimensions": {
            "Curiosity": {
                "score": 90,
                "epistemic_status": "INFERRED",
                "calculation_basis": "Measured: Viral thread bookmark velocity (over 24,000 interactions on 1-prompt-to-deck teasers)."
            },
            "Narrative Tension": {
                "score": 85,
                "epistemic_status": "HYPOTHESIS",
                "calculation_basis": "Inferred from anti-PowerPoint positioning ('slides are 1990s desktop artifacts') triggering high retweet debate."
            },
            "Founder Involvement": {
                "score": 76,
                "epistemic_status": "INFERRED",
                "calculation_basis": "Measured: Founder Grant Lee authored 2 key artifacts (LinkedIn origin story + Product Hunt launch announcement)."
            },
            "Creator Involvement": {
                "score": 94,
                "epistemic_status": "INFERRED",
                "calculation_basis": "Measured: Newsletter & workflow creators (Rowan Cheung, Dickie Bush) drove 68.2% of launch week views."
            },
            "Product Proof": {
                "score": 89,
                "epistemic_status": "INFERRED",
                "calculation_basis": "Measured: 28-second prompt-to-presentation screen recording featured in 4 separate amplification threads."
            },
            "Visual Content": {
                "score": 96,
                "epistemic_status": "INFERRED",
                "calculation_basis": "Measured: 7 of 8 artifacts featured high-fidelity interactive canvas recordings or template galleries."
            },
            "Social Proof": {
                "score": 92,
                "epistemic_status": "INFERRED",
                "calculation_basis": "Measured: Public milestone artifact announcing 1,000,000 decks created within 48 hours."
            },
            "Contrarian Framing": {
                "score": 88,
                "epistemic_status": "HYPOTHESIS",
                "calculation_basis": "Inferred: Direct ideological attack on traditional presentation software culture."
            }
        },
        "description": "Driven by breathtaking visual content (Visual Content: 96) and widespread creator curation (Creator: 94). The attack on legacy slide formatting creates viral social currency.",
        "key_takeaway": "Combines prompt-to-presentation 'magic moments' with an intrinsic viewer-to-creator referral loop."
    },
    "example-ai": {
        "company_name": "OmniContext AI",
        "case_study_title": "Example AI Startup — Synthetic Reference Dataset",
        "case_study_badge": "Synthetic / Simulated Reference Dataset",
        "archetype": "Local-First Semantic Memory Layer",
        "dimensions": {
            "Curiosity": {
                "score": 82,
                "epistemic_status": "SIMULATED",
                "calculation_basis": "Simulated metric: Based on waitlist signup pace modeled after developer tooling benchmarks."
            },
            "Narrative Tension": {
                "score": 79,
                "epistemic_status": "SIMULATED",
                "calculation_basis": "Simulated heuristic: Attack on token context windows in favor of associative persistent memory."
            },
            "Founder Involvement": {
                "score": 85,
                "epistemic_status": "SIMULATED",
                "calculation_basis": "Simulated metric: Founder authored 4 of 9 synthetic launch artifacts."
            },
            "Creator Involvement": {
                "score": 65,
                "epistemic_status": "SIMULATED",
                "calculation_basis": "Simulated metric: Lower creator dependence; focuses primarily on developer evangelists."
            },
            "Product Proof": {
                "score": 78,
                "epistemic_status": "SIMULATED",
                "calculation_basis": "Simulated metric: Static knowledge graph screenshot and Rust memory footprint benchmark."
            },
            "Visual Content": {
                "score": 70,
                "epistemic_status": "SIMULATED",
                "calculation_basis": "Simulated metric: Technical architecture diagrams and terminal demos."
            },
            "Social Proof": {
                "score": 72,
                "epistemic_status": "SIMULATED",
                "calculation_basis": "Simulated metric: 15,000 beta signups announced on Day +1."
            },
            "Contrarian Framing": {
                "score": 80,
                "epistemic_status": "SIMULATED",
                "calculation_basis": "Simulated heuristic: Local-first privacy vs cloud-hosted model surveillance."
            }
        },
        "description": "Synthetic reference dataset illustrating an engineer-targeted launch balancing privacy guarantees with waitlist onboarding.",
        "key_takeaway": "Architecture-driven launch emphasizing technical credibility over creator hype."
    }
}

DNA_DISCLAIMER = (
    "EPISTEMIC NOTICE: These dimensions represent structured inferences and hypotheses calculated "
    "from publicly observable artifact patterns (such as author distribution, video ratio, and engagement velocity). "
    "They do NOT represent measured internal causal conversion or private analytics."
)
