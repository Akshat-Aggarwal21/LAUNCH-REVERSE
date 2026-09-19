"""
The Skeptic Inspector component ('Why This Insight?').
Renders the strict epistemic audit breakdown:
- Supporting evidence
- Counterevidence exceptions
- Explicit assumptions
- Skeptic Agent verdict & confidence score
- Next data required to upgrade claim
"""

import streamlit as st
from typing import Dict, Any


def render_why_this_insight_card(hyp: Dict[str, Any]):
    """
    Renders the deep epistemic dissection card for a given hypothesis.
    """
    confidence_color = {
        "LOW": "#f43f5e",
        "MEDIUM": "#f59e0b",
        "HIGH": "#22c55e"
    }.get(hyp.get("confidence_level", "LOW"), "#94a3b8")

    st.markdown(
        f"""
        <div style="background: #0f172a; border: 1px solid #1e293b; border-radius: 8px; padding: 20px; margin-top: 10px; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 12px; margin-bottom: 16px;">
                <div>
                    <span style="font-family: 'JetBrains Mono'; font-size: 0.72rem; color: #94a3b8; text-transform: uppercase;">EPISTEMIC AUDIT // WHY THIS INSIGHT?</span>
                    <h3 style="font-family: 'JetBrains Mono'; font-size: 1.05rem; color: #f8fafc; margin: 4px 0 0 0;">{hyp['title']}</h3>
                </div>
                <div style="text-align: right;">
                    <span style="font-family: 'JetBrains Mono'; font-size: 0.7rem; color: #64748b; display: block;">CONFIDENCE</span>
                    <span style="font-family: 'JetBrains Mono'; font-weight: 700; font-size: 0.95rem; color: {confidence_color};">{hyp.get('confidence_level', 'LOW')}</span>
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                <!-- Column 1: Evidence vs Counterevidence -->
                <div>
                    <div style="margin-bottom: 16px;">
                        <span style="font-family: 'JetBrains Mono'; font-size: 0.78rem; font-weight: 600; color: #4ade80; text-transform: uppercase;">
                            ✓ Supporting Evidence
                        </span>
                        <div style="margin-top: 8px; font-family: 'JetBrains Mono'; font-size: 0.82rem; color: #cbd5e1; line-height: 1.6;">
                            <div>• <b>{hyp['supporting_artifacts_count']}</b> public artifacts in dataset</div>
                            <div>• <b>{hyp['supporting_launch_sequences']}</b> distinct launch sequences</div>
                            <div>• <b>{hyp['supporting_author_types']}</b> different author types (Founder, Core, Creator)</div>
                            <div style="margin-top: 6px; font-size: 0.8rem; color: #94a3b8; font-style: italic;">"{hyp['evidence_summary']}"</div>
                        </div>
                    </div>
                    
                    <div style="margin-bottom: 16px;">
                        <span style="font-family: 'JetBrains Mono'; font-size: 0.78rem; font-weight: 600; color: #fb7185; text-transform: uppercase;">
                            ⚠ Counterevidence & Exceptions
                        </span>
                        <div style="margin-top: 8px; font-family: 'JetBrains Mono'; font-size: 0.82rem; color: #cbd5e1; line-height: 1.5;">
                            <div>• <b>{hyp['counterevidence_exceptions_count']}</b> simulated launches did not follow this pattern.</div>
                            <div style="margin-top: 4px; font-size: 0.8rem; color: #fca5a5;">{hyp['counterevidence']}</div>
                        </div>
                    </div>
                </div>

                <!-- Column 2: Assumptions, Verdict, Next Investigation -->
                <div>
                    <div style="margin-bottom: 16px;">
                        <span style="font-family: 'JetBrains Mono'; font-size: 0.78rem; font-weight: 600; color: #fbbf24; text-transform: uppercase;">
                            • Explicit Assumptions
                        </span>
                        <ul style="margin-top: 8px; padding-left: 18px; font-size: 0.8rem; color: #94a3b8; line-height: 1.45;">
                            {"".join(f"<li>{a}</li>" for a in hyp['assumptions'])}
                        </ul>
                    </div>

                    <div style="background: rgba(244, 63, 94, 0.08); border-left: 3px solid #f43f5e; padding: 10px 12px; border-radius: 0 4px 4px 0; margin-bottom: 14px;">
                        <span style="font-family: 'JetBrains Mono'; font-size: 0.72rem; font-weight: 700; color: #f43f5e; text-transform: uppercase;">
                            Skeptic Agent Verdict:
                        </span>
                        <div style="font-size: 0.8rem; color: #cbd5e1; margin-top: 4px; line-height: 1.4;">
                            {hyp['skeptic_critique']}
                        </div>
                    </div>

                    <div style="border-top: 1px dashed #334155; padding-top: 10px;">
                        <span style="font-family: 'JetBrains Mono'; font-size: 0.72rem; color: #38bdf8; text-transform: uppercase; font-weight: 600;">
                            Next Data Required to Validate:
                        </span>
                        <div style="font-size: 0.8rem; color: #cbd5e1; margin-top: 4px;">
                            {hyp['next_data_required']}
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )
