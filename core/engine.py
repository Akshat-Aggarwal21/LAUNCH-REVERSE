"""
Core analysis engine for LAUNCH//REVERSE using Pandas and NumPy.
Performs deterministic filtering, timeline aggregation, and metrics computation.
"""

from typing import List, Dict, Any, Optional
import pandas as pd
import numpy as np
from data.artifacts import RAW_ARTIFACTS, get_artifacts_df
from data.hypotheses import HYPOTHESES_DATA, PRESET_HYPOTHESES_SANDBOX
from data.launch_dna import LAUNCH_DNA_PROFILES
from data.agents_data import AGENTS_METADATA, SIMULATED_AGENT_TRACES


class LaunchAnalysisEngine:
    """
    Structured data analysis engine using Pandas/NumPy.
    """

    def __init__(self):
        self.df = get_artifacts_df()

    def get_case_study_artifacts(self, case_study_id: str) -> pd.DataFrame:
        """Filter artifacts by case study ID."""
        filtered = self.df[self.df["case_study_id"] == case_study_id].copy()
        filtered = filtered.sort_values(by=["day_offset", "engagement_interactions"], ascending=[True, False])
        return filtered

    def get_timeline_stats(self, case_study_id: str) -> Dict[str, Any]:
        """Compute aggregate statistics for the case study timeline."""
        sub_df = self.get_case_study_artifacts(case_study_id)
        if sub_df.empty:
            return {}

        total_artifacts = len(sub_df)
        total_views = int(sub_df["engagement_views"].sum())
        total_interactions = int(sub_df["engagement_interactions"].sum())
        interaction_rate = (total_interactions / total_views * 100) if total_views > 0 else 0

        author_counts = sub_df["author_type"].value_counts().to_dict()
        hook_counts = sub_df["hook_type"].value_counts().to_dict()
        phase_counts = sub_df["launch_phase"].value_counts().to_dict()

        return {
            "total_artifacts": total_artifacts,
            "total_views": total_views,
            "total_interactions": total_interactions,
            "interaction_rate": round(interaction_rate, 2),
            "author_counts": author_counts,
            "hook_counts": hook_counts,
            "phase_counts": phase_counts,
            "day_range": f"{sub_df['day_offset'].min()} to +{sub_df['day_offset'].max()}"
        }

    def get_dna_profile(self, case_study_id: str) -> Dict[str, Any]:
        """Retrieve Launch DNA profile."""
        return LAUNCH_DNA_PROFILES.get(case_study_id, LAUNCH_DNA_PROFILES["wispr-flow"])

    def get_agent_traces(self, case_study_id: str) -> List[Dict[str, Any]]:
        """Retrieve simulated ReAct agent execution trace."""
        return SIMULATED_AGENT_TRACES.get(case_study_id, SIMULATED_AGENT_TRACES["wispr-flow"])

    def challenge_hypothesis(self, category_or_query: str) -> Dict[str, Any]:
        """
        Deterministic hypothesis challenger matching the Skeptic Agent's logic.
        """
        # Match against preset categories
        for category, data in PRESET_HYPOTHESES_SANDBOX.items():
            if category.lower() in category_or_query.lower() or category_or_query.lower() in category.lower():
                return data

        # Default fallback challenge showing intellectual humility and bounds
        return {
            "title": f"Custom Hypothesis: '{category_or_query}'",
            "evidence": [
                f"Preliminary scan identified 2-3 public artifacts with topical relevance to '{category_or_query}'.",
                "Observed qualitative clustering in pre-launch discussions."
            ],
            "counterevidence": [
                "Dataset contains counterexamples with zero correlation between this variable and Day 0 conversion.",
                "High possibility of confounding from preexisting brand awareness."
            ],
            "mechanism": "Proposed mechanism assumes a direct causal link, but social engagement metrics reflect attention, not software adoption.",
            "confidence": "LOW",
            "assumptions": [
                "Engagement signals correlate with intent to purchase.",
                "Dataset is free of algorithmic platform delivery bias."
            ],
            "skeptic_verdict": "Insufficient evidence. This observation represents an unverified correlation that cannot be distinguished from background noise without larger sample sizes.",
            "next_data_required": "Telemetry linking specific user acquisition channels to 30-day active retention cohorts."
        }


# Global engine singleton
engine = LaunchAnalysisEngine()
