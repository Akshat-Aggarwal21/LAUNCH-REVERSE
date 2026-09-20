"""
Agent system definitions and legacy simulated execution traces for LAUNCH//REVERSE (unused by the live pipeline — kept for reference only).
Showcases multi-agent orchestration across 5 specialized agents.
"""

from typing import List, Dict, Any

AGENTS_METADATA = [
    {
        "id": "agent-01",
        "name": "AGENT 01 — ARCHIVIST",
        "role": "Ingestion & Normalization",
        "question": "What happened?",
        "purpose": "Collect and organize launch artifacts from public sources into structured schema records.",
        "tools": ["rest_api_ingest", "rss_feed_parser", "schema_normalizer", "mongo_document_writer"],
        "color": "#38bdf8",  # sky
        "epistemic_tag": "OBSERVED"
    },
    {
        "id": "agent-02",
        "name": "AGENT 02 — PATTERN HUNTER",
        "role": "Structural Analysis",
        "question": "What appears repeatedly?",
        "purpose": "Identify recurring temporal sequences, hook structures, and author-network configurations.",
        "tools": ["temporal_aligner", "hook_clusterer", "graph_relational_mapper", "frequency_analyzer"],
        "color": "#a855f7",  # purple
        "epistemic_tag": "INFERRED"
    },
    {
        "id": "agent-03",
        "name": "AGENT 03 — SKEPTIC",
        "role": "Epistemic Audit & Falsification",
        "question": "Could this pattern be coincidence?",
        "purpose": "Actively search for counterexamples, small sample size artifacts, and correlation-causation fallacies.",
        "tools": ["counterexample_search", "confounding_detector", "sample_size_auditor", "falsification_tester"],
        "color": "#f43f5e",  # rose
        "epistemic_tag": "COUNTEREVIDENCE"
    },
    {
        "id": "agent-04",
        "name": "AGENT 04 — FIRST-PRINCIPLES ANALYST",
        "role": "Causal Mechanism Modeling",
        "question": "What mechanism might explain this?",
        "purpose": "Deconstruct surviving patterns into underlying human psychology and network incentives.",
        "tools": ["cognitive_load_model", "incentive_mapper", "k_factor_estimator", "mental_model_tracer"],
        "color": "#f59e0b",  # amber
        "epistemic_tag": "HYPOTHESIS"
    },
    {
        "id": "agent-05",
        "name": "AGENT 05 — SYNTHESIZER",
        "role": "Intelligence Briefing",
        "question": "What can we responsibly say?",
        "purpose": "Compile observations, hypotheses, skeptic bounds, and next data requirements into an executive report.",
        "tools": ["epistemic_guardrail_check", "confidence_calibrator", "report_formatter", "gap_identifier"],
        "color": "#22c55e",  # emerald
        "epistemic_tag": "SYNTHESIS"
    }
]


SIMULATED_AGENT_TRACES: Dict[str, List[Dict[str, Any]]] = {
    "wispr-flow": [
        {
            "agent_id": "agent-01",
            "agent_name": "AGENT 01 — ARCHIVIST",
            "thought": "Ingesting public launch artifacts from X timeline, Product Hunt post, and YouTube reviews for Wispr Flow.",
            "action": "mongo_document_writer.insert_batch()",
            "observation": "Successfully extracted and normalized 9 artifacts spanning Day -7 to Day +3. Timestamps aligned to launch origin: 2024-09-10 09:00:00 PST.",
            "structured_output": {
                "total_artifacts": 9,
                "platforms_covered": ["X", "ProductHunt", "YouTube"],
                "author_types_found": ["Founder", "Core Team", "Tech Influencer", "Creator"],
                "status": "RAW_STORED_IN_MONGO"
            }
        },
        {
            "agent_id": "agent-02",
            "agent_name": "AGENT 02 — PATTERN HUNTER",
            "thought": "Scanning chronological sequence for recurring hook clusters and author transition points.",
            "action": "temporal_aligner.detect_phase_transitions()",
            "observation": "Detected a 3-phase progression: (1) Philosophical framing at Day -7 by Founder, (2) Tangible split-screen latency video at Day -5, (3) Clustered creator reviews on Day 0 and Day +2.",
            "structured_output": {
                "detected_pattern": "Problem-first founder hook -> Latency proof -> Creator amplification",
                "cluster_strength": 0.88,
                "repetition_across_dataset": "Consistent with 4 out of 6 examined launches"
            }
        },
        {
            "agent_id": "agent-03",
            "agent_name": "AGENT 03 — SKEPTIC",
            "thought": "Challenging the detected pattern. Could high day-0 traction be explained by factors outside this sequence?",
            "action": "falsification_tester.check_confounders()",
            "observation": "Warning: High engagement on Day -7 founder post may reflect preexisting founder follower network, not the messaging strategy itself. Also, creator endorsements were partially sponsored/seeded.",
            "structured_output": {
                "skeptic_verdict": "Plausible but unproven",
                "counterexamples_found": 2,
                "epistemic_risk": "High risk of confusing founder audience size with launch formula efficacy",
                "confidence_score": 0.58
            }
        },
        {
            "agent_id": "agent-04",
            "agent_name": "AGENT 04 — FIRST-PRINCIPLES ANALYST",
            "thought": "Deconstructing why sub-200ms latency proof worked psychologically.",
            "action": "cognitive_load_model.evaluate_friction()",
            "observation": "AI dictation has suffered a 10-year reputation of sluggish transcription. A continuous-take split-screen video provides immediate refutation of user skepticism without verbal persuasion.",
            "structured_output": {
                "causal_mechanism": "Tangible speed proof dissolves the primary historical objection before product signup",
                "incentive_loop": "Beta users gain social status by sharing miraculous screencasts of effortless typing"
            }
        },
        {
            "agent_id": "agent-05",
            "agent_name": "AGENT 05 — SYNTHESIZER",
            "thought": "Synthesizing surviving findings under strict epistemic bounds. Excluding unverified causal claims.",
            "action": "epistemic_guardrail_check.enforce()",
            "observation": "All observations clearly separated from hypotheses. Skeptic counterarguments preserved in final dossier.",
            "structured_output": {
                "primary_claim": "Wispr Flow utilized a problem-first founder narrative followed by split-screen latency proof.",
                "skeptic_caveat": "Cannot conclude this strategy alone caused 100k+ downloads without paid attribution data.",
                "recommended_investigation": "Run cohort analysis isolating referral tags from founder vs creator vs direct organic."
            }
        }
    ],
    "gamma": [
        {
            "agent_id": "agent-01",
            "agent_name": "AGENT 01 — ARCHIVIST",
            "thought": "Harvesting public launch records for Gamma 2.0 launch across X threads, Product Hunt, LinkedIn, and Substack deep dives.",
            "action": "schema_normalizer.parse_timeline()",
            "observation": "8 structured artifacts stored. Identified 3 high-impact creator threads and 1 technical origin story.",
            "structured_output": {
                "total_artifacts": 8,
                "dominant_media": "Short video screencasts (prompt-to-deck)",
                "status": "NORMALIZED"
            }
        },
        {
            "agent_id": "agent-02",
            "agent_name": "AGENT 02 — PATTERN HUNTER",
            "thought": "Analyzing viral distribution mechanics.",
            "action": "graph_relational_mapper.map_k_factor()",
            "observation": "Artifacts exhibit a dual loop: (1) Top-of-funnel creator video teasers showing 30s generation, (2) User-generated shared presentations containing 'Made with Gamma' viral watermark.",
            "structured_output": {
                "loop_type": "Prompt demonstration + Watermarked presentation viewer-to-creator loop",
                "frequency": "Present across all post-launch amplification artifacts"
            }
        },
        {
            "agent_id": "agent-03",
            "agent_name": "AGENT 03 — SKEPTIC",
            "thought": "Auditing creator volume claim. Did creator tweets cause the 1M presentations or merely report on them?",
            "action": "sample_size_auditor.test_correlation()",
            "observation": "Skeptic flag: Rowan Cheung and newsletter curators posted 12 hours after Product Hunt launched. Correlation is high, but the product was already #1 before their tweets published.",
            "structured_output": {
                "skeptic_verdict": "Creator amplification accelerated an already-winning launch rather than igniting it from zero.",
                "confidence_score": 0.62
            }
        },
        {
            "agent_id": "agent-04",
            "agent_name": "AGENT 04 — FIRST-PRINCIPLES ANALYST",
            "thought": "Examining the anti-PowerPoint positioning.",
            "action": "incentive_mapper.analyze_pain_points()",
            "observation": "Slide formatting represents high cognitive friction for low status gain. Providing an automated aesthetic baseline relieves acute workplace anxiety.",
            "structured_output": {
                "causal_mechanism": "Relieving formatting anxiety turns knowledge workers into aggressive organic evangelists."
            }
        },
        {
            "agent_id": "agent-05",
            "agent_name": "AGENT 05 — SYNTHESIZER",
            "thought": "Assembling the balanced Gamma research brief.",
            "action": "report_formatter.build_summary()",
            "observation": "Clear bounded intelligence brief prepared with clear labeling of speculative claims.",
            "structured_output": {
                "observed": "Generative prompt-to-deck screencasts generated 1.5M+ combined impressions.",
                "hypothesis": "Embedded viewer watermark represents the primary retention & growth driver.",
                "counterevidence": "Public artifacts cannot quantify the exact percentage of signups attributable to watermark vs direct creator links."
            }
        }
    ],
    "example-ai": [
        {
            "agent_id": "agent-01",
            "agent_name": "AGENT 01 — ARCHIVIST",
            "thought": "Ingesting synthetic dataset for OmniContext AI (simulated prototype launch sequence).",
            "action": "mongo_document_writer.insert_simulated()",
            "observation": "9 synthetic artifacts mapped across Day -7 to Day +3.",
            "structured_output": {
                "dataset_type": "SIMULATED SYNTHETIC",
                "total_records": 9
            }
        },
        {
            "agent_id": "agent-02",
            "agent_name": "AGENT 02 — PATTERN HUNTER",
            "thought": "Mapping architectural framing strategy in synthetic sequence.",
            "action": "hook_clusterer.group_hooks()",
            "observation": "Found high proportion of 'Mechanism Reveal' and 'Technical Architecture' content types compared to creator reactions.",
            "structured_output": {
                "classification": "Engineer-targeted / Privacy-first positioning"
            }
        },
        {
            "agent_id": "agent-03",
            "agent_name": "AGENT 03 — SKEPTIC",
            "thought": "Interrogating synthetic assumptions.",
            "action": "falsification_tester.check_synthetic_biases()",
            "observation": "Synthetic dataset inherently reflects author's preconceived mental model of ideal launch stages. Must not be conflated with real market behavior.",
            "structured_output": {
                "skeptic_verdict": "Valid for structural framework demonstration only. No empirical truth claims allowed.",
                "confidence_score": 0.45
            }
        },
        {
            "agent_id": "agent-04",
            "agent_name": "AGENT 04 — FIRST-PRINCIPLES ANALYST",
            "thought": "Synthesizing theoretical mechanism for local-first software adoption.",
            "action": "mental_model_tracer.trace()",
            "observation": "In privacy-sensitive domains (personal memory, meeting notes), technical transparency (Rust engine, local vector index) acts as the trust prerequisite for adoption.",
            "structured_output": {
                "mechanism": "Technical transparency reduces adoption risk for invasive AI tooling."
            }
        },
        {
            "agent_id": "agent-05",
            "agent_name": "AGENT 05 — SYNTHESIZER",
            "thought": "Generating final synthetic research dossier.",
            "action": "report_formatter.build_summary()",
            "observation": "Report completed with prominent SIMULATED watermark.",
            "structured_output": {
                "status": "SIMULATED_DEMO_READY"
            }
        }
    ]
}
