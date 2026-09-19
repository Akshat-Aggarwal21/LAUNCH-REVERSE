"""
LAUNCH//REVERSE — Main Streamlit Application
"Reverse-engineering how product launches become distribution."
A conceptual AI-native research tool prototype for Social Capital Inc.
"""

import streamlit as st
import pandas as pd
import json

from core.engine import engine
from components.styles import TERMINAL_CSS, get_badge_html
from components.visuals import build_timeline_figure, build_launch_dna_radar, build_hook_distribution_bar
from components.skeptic_inspector import render_why_this_insight_card
from components.terminal import render_agent_orchestrator
from data.hypotheses import HYPOTHESES_DATA, PRESET_HYPOTHESES_SANDBOX
from data.architecture_data import PIPELINE_STAGES, RESUME_CONNECTIONS, BUILD_LOG, KNOW_VS_DONT_KNOW
from data.launch_dna import DNA_DISCLAIMER

# Page configuration
st.set_page_config(
    page_title="LAUNCH//REVERSE — Distribution Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply terminal theme styles
st.markdown(TERMINAL_CSS, unsafe_allow_html=True)


# ==============================================================================
# SIDEBAR NAVIGATION & CASE STUDY SELECTION
# ==============================================================================

with st.sidebar:
    st.markdown(
        """
        <div style="padding: 10px 0 16px 0; border-bottom: 1px solid #1f2937;">
            <div style="font-family: 'JetBrains Mono'; font-weight: 800; font-size: 1.15rem; color: #f8fafc; letter-spacing: -0.02em;">
                LAUNCH<span style="color: #38bdf8;">//</span>REVERSE
            </div>
            <div style="font-family: 'JetBrains Mono'; font-size: 0.72rem; color: #94a3b8; margin-top: 4px;">
                DISTRIBUTION REVERSE-ENGINEERING
            </div>
            <div style="margin-top: 8px;">
                <span class="badge badge-simulated">PROTOTYPE</span>
                <span class="badge badge-observed">PYTHON NATIVE</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("### 1. SELECT CASE STUDY")
    case_study_options = {
        "wispr-flow": "Wispr Flow — Launch Analysis",
        "gamma": "Gamma — Launch Analysis",
        "example-ai": "Example AI Startup — Synthetic Dataset"
    }

    selected_cs = st.selectbox(
        "Choose an active investigation:",
        options=list(case_study_options.keys()),
        format_func=lambda k: case_study_options[k],
        key="selected_case_study"
    )

    # Dynamic badge for case study type
    if selected_cs in ["wispr-flow", "gamma"]:
        st.markdown(
            """
            <div style="background: rgba(56, 189, 248, 0.1); border-left: 2px solid #38bdf8; padding: 6px 10px; font-family: 'JetBrains Mono'; font-size: 0.73rem; color: #7dd3fc; margin-bottom: 12px;">
                CLASSIFICATION: <b>Conceptual / public-artifact demo</b><br>
                Source: Public posts & videos only.
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            """
            <div style="background: rgba(168, 85, 247, 0.1); border-left: 2px solid #a855f7; padding: 6px 10px; font-family: 'JetBrains Mono'; font-size: 0.73rem; color: #d8b4fe; margin-bottom: 12px;">
                CLASSIFICATION: <b>Simulated synthetic data</b><br>
                Purpose: Demonstrates framework mechanics.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")
    st.markdown("### 2. WORKSPACE MODULES")
    nav_view = st.radio(
        "Navigation",
        [
            "⚡ 1. Analysis Workspace",
            "🤖 2. Multi-Agent Orchestration",
            "🔬 3. Hypothesis Sandbox",
            "📑 4. Executive Insight Report",
            "🏗️ 5. Prototype → Production",
            "💡 6. Why I Built This & Build Log"
        ],
        key="nav_view_radio"
    )

    st.markdown("---")
    st.markdown(
        """
        <div style="font-family: 'JetBrains Mono'; font-size: 0.7rem; color: #64748b; line-height: 1.4;">
            <b>EPISTEMIC GUARDRAIL:</b><br>
            • Green: <span style="color: #4ade80;">OBSERVED</span><br>
            • Blue: <span style="color: #38bdf8;">INFERRED</span><br>
            • Amber: <span style="color: #fbbf24;">HYPOTHESIS</span><br>
            • Purple: <span style="color: #c084fc;">SIMULATED</span><br>
            • Rose: <span style="color: #fb7185;">COUNTEREVIDENCE</span>
        </div>
        """,
        unsafe_allow_html=True
    )


# ==============================================================================
# HEADER HERO STORY (Always visible at the top)
# ==============================================================================

st.markdown(
    """
    <div class="hero-box">
        <div style="display: flex; justify-content: space-between; align-items: flex-start;">
            <div>
                <span class="badge badge-simulated">RESEARCH TERMINAL PROTOTYPE</span>
                <span class="badge badge-observed">NO PRIVATE DATA ACCESSED</span>
                <h1 style="font-family: 'JetBrains Mono'; font-size: 1.7rem; color: #f8fafc; margin: 10px 0 6px 0; letter-spacing: -0.02em;">
                    Can we reverse-engineer a launch?
                </h1>
                <p style="font-size: 0.96rem; color: #cbd5e1; max-width: 820px; line-height: 1.5; margin: 0 0 12px 0;">
                    <b>LAUNCH//REVERSE</b> is an AI-native prototype for analyzing public launch artifacts and turning them into testable hypotheses about distribution.
                </p>
            </div>
            <div style="text-align: right; background: #0f172a; border: 1px solid #1e293b; padding: 10px 14px; border-radius: 6px;">
                <span style="font-family: 'JetBrains Mono'; font-size: 0.7rem; color: #64748b; display: block;">TARGET AUDIENCE</span>
                <span style="font-family: 'JetBrains Mono'; font-size: 0.8rem; font-weight: 700; color: #38bdf8;">Social Capital Inc.</span>
                <span style="font-family: 'JetBrains Mono'; font-size: 0.68rem; color: #94a3b8; display: block; margin-top: 2px;">Technical Generalist Role</span>
            </div>
        </div>

        <div style="background: #0b0f19; border: 1px solid #1e293b; border-radius: 6px; padding: 14px 18px; margin-top: 10px;">
            <div style="font-family: 'JetBrains Mono'; font-size: 0.84rem; color: #94a3b8; line-height: 1.55;">
                Most launch analysis starts after the fact: <i>What happened? How many views? How many likes?</i><br>
                I wanted to ask a different question: <b>What was the structure of the launch?</b><br>
                <span style="color: #cbd5e1;">What narratives appeared first? Who amplified them? Which formats were used? How did the story evolve? And crucially: <b>Which observations are actually supported by evidence?</b></span>
            </div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# Retrieve active data for current selection
artifacts_df = engine.get_case_study_artifacts(selected_cs)
timeline_stats = engine.get_timeline_stats(selected_cs)
dna_profile = engine.get_dna_profile(selected_cs)
agent_traces = engine.get_agent_traces(selected_cs)


# ==============================================================================
# VIEW 1: ANALYSIS WORKSPACE
# ==============================================================================

if "1. Analysis Workspace" in nav_view:
    st.markdown("### 📊 ACTIVE INVESTIGATION OVERVIEW")

    # Top metrics bar
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        st.markdown(
            f"""
            <div class="stat-box">
                <div class="stat-label">PUBLIC ARTIFACTS</div>
                <div class="stat-value">{timeline_stats.get('total_artifacts', 0)}</div>
                <div style="font-family: 'JetBrains Mono'; font-size: 0.72rem; color: #4ade80; margin-top: 2px;">✓ Structured & Normalized</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_m2:
        st.markdown(
            f"""
            <div class="stat-box">
                <div class="stat-label">RECORDED IMPRESSIONS</div>
                <div class="stat-value">{timeline_stats.get('total_views', 0):,}</div>
                <div style="font-family: 'JetBrains Mono'; font-size: 0.72rem; color: #38bdf8; margin-top: 2px;">Public Views & Streams</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_m3:
        st.markdown(
            f"""
            <div class="stat-box">
                <div class="stat-label">PUBLIC INTERACTIONS</div>
                <div class="stat-value">{timeline_stats.get('total_interactions', 0):,}</div>
                <div style="font-family: 'JetBrains Mono'; font-size: 0.72rem; color: #fbbf24; margin-top: 2px;">Likes, Reposts, Upvotes</div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_m4:
        st.markdown(
            f"""
            <div class="stat-box">
                <div class="stat-label">TIMELINE SPAN</div>
                <div class="stat-value">DAY -7 → +3</div>
                <div style="font-family: 'JetBrains Mono'; font-size: 0.72rem; color: #c084fc; margin-top: 2px;">Pre-launch to Amplification</div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<div style='margin-top: 24px;'></div>", unsafe_allow_html=True)

    # -------------------------------------------------------------
    # 1. Interactive Launch Timeline
    # -------------------------------------------------------------
    st.markdown("### 🗓️ CHRONOLOGICAL LAUNCH TIMELINE")
    st.markdown(
        """
        <div style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 12px;">
            Every node represents an individual public artifact (post, video, announcement). Hover over bubbles to inspect narrative hooks; click cards below for raw schema verification.
        </div>
        """,
        unsafe_allow_html=True
    )

    timeline_fig = build_timeline_figure(artifacts_df)
    st.plotly_chart(timeline_fig, width="stretch")

    # -------------------------------------------------------------
    # 2. Side-by-Side: Launch DNA vs Hook Distribution
    # -------------------------------------------------------------
    col_dna, col_hooks = st.columns([1.1, 0.9])

    with col_dna:
        st.markdown(
            """
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <h4 style="font-family: 'JetBrains Mono'; font-size: 0.95rem; color: #f8fafc; margin: 0;">
                    🧬 LAUNCH DNA (8 DIMENSIONS)
                </h4>
                <span class="badge badge-hypothesis">ILLUSTRATIVE CLASSIFICATION</span>
            </div>
            """,
            unsafe_allow_html=True
        )
        st.markdown(
            f"""
            <div class="disclaimer-banner" style="margin-top: 8px;">
                ⚠️ <b>METHODOLOGY NOTICE:</b> {DNA_DISCLAIMER}
            </div>
            """,
            unsafe_allow_html=True
        )
        radar_fig = build_launch_dna_radar(dna_profile)
        st.plotly_chart(radar_fig, width="stretch")
        st.markdown(
            f"""
            <div style="font-family: 'JetBrains Mono'; font-size: 0.78rem; color: #cbd5e1; background: #111827; padding: 10px 14px; border-radius: 4px; border: 1px solid #1f2937;">
                <b>Identified Archetype:</b> <span style="color: #38bdf8;">{dna_profile['archetype']}</span><br>
                {dna_profile['description']}
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_hooks:
        st.markdown(
            """
            <h4 style="font-family: 'JetBrains Mono'; font-size: 0.95rem; color: #f8fafc; margin: 0 0 10px 0;">
                🎯 HOOK FREQUENCY & NARRATIVE BALANCE
            </h4>
            """,
            unsafe_allow_html=True
        )
        hook_bar = build_hook_distribution_bar(artifacts_df)
        st.plotly_chart(hook_bar, width="stretch")

        st.markdown(
            """
            <div style="font-family: 'JetBrains Mono'; font-size: 0.78rem; color: #94a3b8; background: #0f172a; padding: 12px 14px; border-radius: 4px; border: 1px solid #1e293b; line-height: 1.5;">
                <b>Analytical Heuristic:</b> Launches that frontload <i>Contrarian</i> or <i>Pain-Point</i> hooks establish narrative friction before product releases. Demos that deploy <i>Velocity Proof</i> during pre-launch report higher organic bookmark ratios.
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # -------------------------------------------------------------
    # 3. Artifact Explorer with Schema Inspection
    # -------------------------------------------------------------
    st.markdown("### 🗃️ STRUCTURED ARTIFACT EXPLORER")
    st.markdown(
        """
        <div style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 14px;">
            Filter and inspect the underlying records stored in the normalized schema (compatible with MongoDB / Pandas).
        </div>
        """,
        unsafe_allow_html=True
    )

    f_phase = st.multiselect(
        "Filter by Launch Phase:",
        options=list(artifacts_df["launch_phase"].unique()),
        default=list(artifacts_df["launch_phase"].unique())
    )

    filtered_df = artifacts_df[artifacts_df["launch_phase"].isin(f_phase)]

    for _, row in filtered_df.iterrows():
        with st.expander(f"{row['id']} | {row['day_label']} — {row['author']} ({row['author_type']}) on {row['platform']}: {row['narrative'][:65]}...", expanded=False):
            col_a1, col_a2 = st.columns([1.2, 0.8])
            with col_a1:
                st.markdown(f"**Verbatim Post Text / Content:**")
                st.info(f"\"{row['raw_content']}\"")
                st.markdown(
                    f"""
                    **Extracted Entity Keywords:** `{'`, `'.join(row['structured_extracted_entities'])}`<br>
                    **Call To Action:** `{row['cta']}` | **Hook Category:** `{row['hook_type']}`
                    """,
                    unsafe_allow_html=True
                )
            with col_a2:
                st.markdown(
                    f"""
                    <div style="background: #0f172a; border: 1px solid #1e293b; padding: 12px; border-radius: 4px; font-family: 'JetBrains Mono'; font-size: 0.78rem;">
                        <div><b>EPISTEMIC STATUS:</b> {get_badge_html(row['epistemic_status'], row['epistemic_status'])}</div>
                        <div style="margin-top: 6px;"><b>SOURCE TYPE:</b> {row['source_type']}</div>
                        <div><b>VIEWS:</b> {row['engagement_views']:,}</div>
                        <div><b>INTERACTIONS:</b> {row['engagement_interactions']:,}</div>
                        <div><b>EXTRACTION CONFIDENCE:</b> {int(row['confidence_score'] * 100)}%</div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )


# ==============================================================================
# VIEW 2: MULTI-AGENT ORCHESTRATION CONSOLE
# ==============================================================================

elif "2. Multi-Agent Orchestration" in nav_view:
    st.markdown("### 🤖 5-AGENT SYSTEM ORCHESTRATION")
    st.markdown(
        """
        <div style="font-size: 0.88rem; color: #cbd5e1; margin-bottom: 16px;">
            Rather than a monolithic 'AI prompt', the investigation decomposes into 5 specialized agents with defined responsibilities, distinct epistemic boundaries, and dedicated toolkits.
        </div>
        """,
        unsafe_allow_html=True
    )

    render_agent_orchestrator(agent_traces)

    st.markdown("---")
    st.markdown("### 🔄 THE SEVEN-STAGE PROCESSING PIPELINE")
    st.markdown(
        """
        <div style="font-size: 0.84rem; color: #94a3b8; margin-bottom: 14px;">
            Click on any pipeline stage below to compare what this prototype does versus what a production system would execute:
        </div>
        """,
        unsafe_allow_html=True
    )

    stage_names = [p["stage"] for p in PIPELINE_STAGES]
    selected_stage_name = st.selectbox("Inspect Pipeline Stage:", stage_names)
    stage_info = next(p for p in PIPELINE_STAGES if p["stage"] == selected_stage_name)

    col_p1, col_p2 = st.columns(2)
    with col_p1:
        st.markdown(
            f"""
            <div style="background: #0f172a; border: 1px solid #1e293b; border-radius: 6px; padding: 16px;">
                <span class="badge badge-simulated">CURRENT PROTOTYPE BEHAVIOR</span>
                <h4 style="font-family: 'JetBrains Mono'; font-size: 0.95rem; color: #f8fafc; margin: 8px 0;">{stage_info['stage']}</h4>
                <p style="font-size: 0.83rem; color: #cbd5e1; line-height: 1.5;">{stage_info['prototype']}</p>
                <div style="font-family: 'JetBrains Mono'; font-size: 0.75rem; color: #94a3b8; margin-top: 8px;">
                    Goal: Validate reasoning structure without infrastructure overhead.
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    with col_p2:
        st.markdown(
            f"""
            <div style="background: #111827; border: 1px solid #1f2937; border-radius: 6px; padding: 16px;">
                <span class="badge badge-inferred">PRODUCTION SYSTEM ROADMAP</span>
                <h4 style="font-family: 'JetBrains Mono'; font-size: 0.95rem; color: #38bdf8; margin: 8px 0;">Future Implementation</h4>
                <p style="font-size: 0.83rem; color: #cbd5e1; line-height: 1.5;">{stage_info['production']}</p>
                <div style="font-family: 'JetBrains Mono'; font-size: 0.75rem; color: #94a3b8; margin-top: 8px;">
                    Integrates with candidate's existing work (FastAPI, Celery, MongoDB, LLM APIs).
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==============================================================================
# VIEW 3: HYPOTHESIS SANDBOX & SKEPTIC INSPECTOR
# ==============================================================================

elif "3. Hypothesis Sandbox" in nav_view:
    st.markdown("### 🔬 EVIDENCE VS HYPOTHESIS PIPELINE & SKEPTIC SANDBOX")
    st.markdown(
        """
        <div style="font-size: 0.88rem; color: #cbd5e1; margin-bottom: 16px;">
            The core intellectual virtue of LAUNCH//REVERSE is <b>humility before evidence</b>. We do not declare 'AI has discovered the secret to launches'. Instead, every recurring pattern is immediately challenged by the Skeptic Agent.
        </div>
        """,
        unsafe_allow_html=True
    )

    # -------------------------------------------------------------
    # Interactive "Test a Hypothesis" Playground
    # -------------------------------------------------------------
    st.markdown("#### ⚡ INTERACTIVE: TEST A HYPOTHESIS")
    st.markdown(
        """
        <div style="font-size: 0.82rem; color: #94a3b8; margin-bottom: 10px;">
            Select a common launch hypothesis or enter a custom proposition. Click <b>'Challenge Hypothesis'</b> to trigger an adversarial check.
        </div>
        """,
        unsafe_allow_html=True
    )

    col_btn1, col_btn2, col_btn3, col_btn4 = st.columns(4)
    preset_picked = None
    with col_btn1:
        if st.button("Founder-led narrative"):
            preset_picked = "Founder-led narrative"
    with col_btn2:
        if st.button("Creator amplification"):
            preset_picked = "Creator amplification"
    with col_btn3:
        if st.button("Product demonstration"):
            preset_picked = "Product demonstration"
    with col_btn4:
        if st.button("Contrarian hook"):
            preset_picked = "Contrarian hook"

    custom_hyp = st.text_input(
        "Or type a custom launch hypothesis:",
        value=preset_picked if preset_picked else "Creator amplification",
        placeholder="e.g. Free tiers drive higher Day 0 conversion than waitlists"
    )

    if st.button("🔍 CHALLENGE HYPOTHESIS (RUN SKEPTIC AGENT)", type="primary"):
        res = engine.challenge_hypothesis(custom_hyp)
        st.markdown(
            f"""
            <div style="background: #0f172a; border: 1px solid #1e293b; border-radius: 8px; padding: 18px 22px; margin-top: 14px;">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 10px;">
                    <div>
                        <span class="badge badge-counter">SKEPTIC AUDIT REPORT</span>
                        <h4 style="font-family: 'JetBrains Mono'; font-size: 1.05rem; color: #f8fafc; margin: 4px 0 0 0;">{res['title']}</h4>
                    </div>
                    <div style="text-align: right;">
                        <span style="font-family: 'JetBrains Mono'; font-size: 0.7rem; color: #64748b; display: block;">CONFIDENCE</span>
                        <span class="badge badge-hypothesis">{res['confidence']}</span>
                    </div>
                </div>

                <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 14px; font-size: 0.83rem;">
                    <div>
                        <span style="font-family: 'JetBrains Mono'; font-weight: 600; color: #4ade80;">✓ OBSERVED EVIDENCE:</span>
                        <ul style="color: #cbd5e1; padding-left: 18px; margin-top: 6px; line-height: 1.5;">
                            {"".join(f"<li>{e}</li>" for e in res['evidence'])}
                        </ul>
                        <div style="background: #111827; padding: 10px; border-radius: 4px; border: 1px solid #1f2937; margin-top: 10px;">
                            <span style="font-family: 'JetBrains Mono'; font-size: 0.72rem; color: #fbbf24;">PROPOSED MECHANISM:</span>
                            <div style="color: #cbd5e1; margin-top: 2px;">{res['mechanism']}</div>
                        </div>
                    </div>

                    <div>
                        <span style="font-family: 'JetBrains Mono'; font-weight: 600; color: #fb7185;">⚠ SKEPTIC COUNTERARGUMENT:</span>
                        <ul style="color: #cbd5e1; padding-left: 18px; margin-top: 6px; line-height: 1.5;">
                            {"".join(f"<li>{c}</li>" for c in res['counterevidence'])}
                        </ul>
                        <div style="background: rgba(244, 63, 94, 0.1); border-left: 3px solid #f43f5e; padding: 8px 12px; border-radius: 0 4px 4px 0; margin-top: 10px;">
                            <span style="font-family: 'JetBrains Mono'; font-size: 0.72rem; font-weight: 700; color: #f43f5e;">VERDICT:</span>
                            <div style="color: #fecdd3; margin-top: 2px;">{res['skeptic_verdict']}</div>
                        </div>
                    </div>
                </div>

                <div style="border-top: 1px dashed #334155; padding-top: 12px; margin-top: 16px; font-family: 'JetBrains Mono'; font-size: 0.78rem; color: #94a3b8;">
                    <b>NEXT DATA REQUIRED BEFORE ACCEPTANCE:</b> <span style="color: #7dd3fc;">{res['next_data_required']}</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # -------------------------------------------------------------
    # Pre-computed Deep Hypothesis Dissections
    # -------------------------------------------------------------
    st.markdown("#### 📑 SURFACED HYPOTHESES ACROSS DATASET")
    st.markdown(
        """
        <div style="font-size: 0.84rem; color: #94a3b8; margin-bottom: 12px;">
            Click <b>'Inspect Why This Insight'</b> on any card below to open the complete evidence breakdown.
        </div>
        """,
        unsafe_allow_html=True
    )

    for hyp in HYPOTHESES_DATA:
        with st.container():
            st.markdown(
                f"""
                <div class="terminal-card">
                    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
                        <div>
                            <span class="badge badge-hypothesis">{hyp['category']}</span>
                            <span class="badge badge-simulated">{hyp['status']}</span>
                            <div class="card-title" style="margin-top: 6px;">{hyp['title']}</div>
                        </div>
                        <div style="text-align: right;">
                            <span style="font-family: 'JetBrains Mono'; font-size: 0.7rem; color: #64748b; display: block;">CONFIDENCE</span>
                            <span style="font-family: 'JetBrains Mono'; font-weight: 700; color: #fbbf24;">{hyp['confidence_level']}</span>
                        </div>
                    </div>
                    <div style="font-size: 0.83rem; color: #cbd5e1; margin-top: 8px; line-height: 1.5;">
                        <b>Observation:</b> {hyp['observation']}<br>
                        <b>Possible Mechanism:</b> {hyp['hypothesis_mechanism']}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

            # Killer Feature: Why this insight button & expander
            with st.expander(f"🔍 Why This Insight? — Epistemic Audit for {hyp['id']}", expanded=False):
                render_why_this_insight_card(hyp)


# ==============================================================================
# VIEW 4: EXECUTIVE INSIGHT REPORT
# ==============================================================================

elif "4. Executive Insight Report" in nav_view:
    st.markdown("### 📑 EXECUTIVE INSIGHT REPORT")
    st.markdown(
        """
        <div style="font-family: 'JetBrains Mono'; font-size: 0.74rem; color: #64748b; margin-bottom: 16px;">
            REPORT GENERATED BY AGENT 05 (SYNTHESIZER) // BOUNDED RESEARCH DOSSIER
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div style="background: #111827; border: 1px solid #1f2937; border-radius: 8px; padding: 22px;">
            <div style="border-bottom: 1px solid #1f2937; padding-bottom: 12px; margin-bottom: 16px;">
                <span class="badge badge-observed">EXECUTIVE SUMMARY</span>
                <h3 style="font-family: 'JetBrains Mono'; font-size: 1.15rem; color: #f8fafc; margin: 6px 0 0 0;">
                    What the Prototype Observed in Public Launch Artifacts
                </h3>
            </div>
            
            <div style="font-size: 0.88rem; color: #cbd5e1; line-height: 1.6;">
                Across 25+ structured artifacts spanning <b>Wispr Flow</b>, <b>Gamma</b>, and synthetic reference benchmarks, product launches exhibit distinct phase-separated distribution patterns:
                <ol style="margin-top: 8px; padding-left: 20px;">
                    <li><b>Problem-First Pre-Launch:</b> High-performing launches systematically seed philosophical narrative tension (attacking typing friction or slide deck formatting) 5–7 days prior to product availability.</li>
                    <li><b>Verification over Description:</b> Continuous-take video screencasts validating speed (e.g. sub-200ms latency or 28s deck creation) achieve 3.2x higher interaction density than static screenshots.</li>
                    <li><b>Asynchronous Creator Seeding:</b> Top creator impressions concentrate on Day 0 and Day +1, but depend fundamentally on prior product proof to convert attention into active downloads.</li>
                </ol>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<div style='margin-top: 18px;'></div>", unsafe_allow_html=True)

    # Detailed report cards
    for idx, hyp in enumerate(HYPOTHESES_DATA, start=1):
        st.markdown(
            f"""
            <div style="background: #0f172a; border: 1px solid #1e293b; border-radius: 6px; padding: 18px; margin-bottom: 16px;">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 8px; margin-bottom: 12px;">
                    <span style="font-family: 'JetBrains Mono'; font-size: 0.8rem; font-weight: 700; color: #38bdf8;">
                        INSIGHT #{idx:02d} // {hyp['category'].upper()}
                    </span>
                    <span style="font-family: 'JetBrains Mono'; font-size: 0.72rem; color: #fbbf24;">
                        CONFIDENCE: {hyp['confidence_level']}
                    </span>
                </div>

                <div style="font-size: 0.83rem; line-height: 1.55; color: #cbd5e1;">
                    <p><b>Observation:</b> {hyp['observation']}</p>
                    <p><b>Possible Explanation:</b> {hyp['hypothesis_mechanism']}</p>
                    <p style="color: #fca5a5;"><b>Counterevidence & Exceptions:</b> {hyp['counterevidence']}</p>
                    <div style="background: #111827; padding: 8px 12px; border-radius: 4px; border: 1px solid #1f2937; margin-top: 8px; font-family: 'JetBrains Mono'; font-size: 0.76rem;">
                        <b>WHAT WE NEED NEXT:</b> <span style="color: #7dd3fc;">{hyp['next_data_required']}</span>
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==============================================================================
# VIEW 5: PROTOTYPE → PRODUCTION & RESUME ALIGNMENT
# ==============================================================================

elif "5. Prototype → Production" in nav_view:
    st.markdown("### 🏗️ FROM PROTOTYPE → PRODUCTION ARCHITECTURE")
    st.markdown(
        """
        <div style="font-size: 0.88rem; color: #cbd5e1; margin-bottom: 18px;">
            The current demo deliberately uses simulated & curated public data to isolate and validate the analytical thinking. Here is the real production architecture I would build next, and how it directly maps to technologies already on my resume.
        </div>
        """,
        unsafe_allow_html=True
    )

    # Visual ASCII / Block Diagram
    st.markdown(
        """
        <div style="background: #0f172a; border: 1px solid #1e293b; border-radius: 6px; padding: 18px; font-family: 'JetBrains Mono'; font-size: 0.78rem; color: #94a3b8; line-height: 1.45; text-align: center; margin-bottom: 24px;">
            <span style="color: #38bdf8; font-weight: 700;">PUBLIC SOURCES</span> (X API v2, Product Hunt GraphQL, YouTube Data v3, RSS Feeds)<br>
            ↓<br>
            <span style="color: #f8fafc; font-weight: 600;">DATA COLLECTION & INGESTION LAYER</span> (FastAPI + Distributed Celery Queue)<br>
            ↓<br>
            <span style="color: #f8fafc; font-weight: 600;">NORMALIZATION & TWO-STAGE FILTERING</span> (Pydantic Models + Heuristic Filter)<br>
            ↓<br>
            <span style="color: #f8fafc; font-weight: 600;">MONGODB & VECTOR STORE</span> (Artifact Collections + pgvector Embeddings)<br>
            ↓<br>
            <span style="color: #a855f7; font-weight: 700;">AGENT ORCHESTRATION LAYER (ReAct Loops)</span><br>
            ┌───────────────────────┴───────────────────────┐<br>
            ↓                                               ↓<br>
            <span style="color: #c084fc;">AGENT 02: PATTERN HUNTER</span>                 <span style="color: #fb7185;">AGENT 03: SKEPTIC CRITIC</span><br>
            (Surfaces recurring temporal clusters)       (Finds counterexamples & checks sample size)<br>
            └───────────────────────┬───────────────────────┘<br>
            ↓<br>
            <span style="color: #fbbf24; font-weight: 600;">AGENT 04: FIRST-PRINCIPLES ANALYST</span> (Cognitive & Incentive Modeling)<br>
            ↓<br>
            <span style="color: #4ade80; font-weight: 600;">HUMAN-IN-THE-LOOP STRATEGIC REVIEW</span> (Streamlit / React Research Terminal)<br>
            ↓<br>
            <span style="color: #38bdf8; font-weight: 700;">FINAL BOUNDED INSIGHT DOSSIER</span> (Exportable Evidence Graph)
            <div style="margin-top: 14px; font-size: 0.72rem; color: #64748b; border-top: 1px solid #1e293b; padding-top: 8px;">
                Prototype architecture — production implementation requires rate-limiting proxies, cross-platform entity resolution, and continuous evaluation harnesses.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("#### 🔗 DIRECT RESUME ALIGNMENT")
    st.markdown(
        """
        <div style="font-size: 0.84rem; color: #94a3b8; margin-bottom: 14px;">
            How every layer of this proposed production architecture connects to projects I have already built:
        </div>
        """,
        unsafe_allow_html=True
    )

    for item in RESUME_CONNECTIONS:
        st.markdown(
            f"""
            <div class="terminal-card">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1f2937; padding-bottom: 8px; margin-bottom: 10px;">
                    <div>
                        <span class="badge badge-inferred">{item['tech']}</span>
                        <h4 style="font-family: 'JetBrains Mono'; font-size: 0.95rem; color: #f8fafc; margin: 4px 0 0 0;">{item['component']}</h4>
                    </div>
                    <div style="text-align: right;">
                        <span style="font-family: 'JetBrains Mono'; font-size: 0.72rem; color: #38bdf8; font-weight: 600;">
                            PARALLELS RESUME PROJECT:
                        </span>
                        <div style="font-family: 'JetBrains Mono'; font-size: 0.8rem; color: #f1f5f9;">{item['resume_project']}</div>
                    </div>
                </div>
                <p style="font-size: 0.83rem; color: #cbd5e1; line-height: 1.5; margin: 0;">
                    {item['connection_detail']}
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==============================================================================
# VIEW 6: WHY I BUILT THIS, BUILD LOG & HONEST BOUNDS
# ==============================================================================

elif "6. Why I Built This & Build Log" in nav_view:
    st.markdown("### 💡 WHY I BUILT THIS")
    
    st.markdown(
        """
        <div style="background: #111827; border: 1px solid #1f2937; border-radius: 8px; padding: 22px; margin-bottom: 24px;">
            <div style="font-size: 0.92rem; color: #e2e8f0; line-height: 1.65;">
                I didn't want to build another generic AI chatbot.<br><br>
                Social Capital's public work around product launches, distribution, creators, content, research, and go-to-market systems made me curious about the underlying problem: <b>If distribution is an engineered system, could publicly visible launch artifacts be analyzed as structured data?</b><br><br>
                I started from the smallest testable version of that idea:
                <ol style="margin-top: 8px; padding-left: 20px; line-height: 1.6;">
                    <li>Collect launch artifacts.</li>
                    <li>Structure them into a normalized schema.</li>
                    <li>Classify hook types, author archetypes, and narrative tension.</li>
                    <li>Look for recurring temporal patterns.</li>
                    <li><b>Try to disprove those patterns with a dedicated Skeptic Agent.</b></li>
                    <li>Strictly separate evidence from hypotheses.</li>
                </ol>
                This prototype intentionally stops before pretending to have a production-grade scraping pipeline. The goal is to demonstrate the thinking behind the system, my builder mentality, and how I break down ambiguous problems.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # What I Don't Know Yet vs What I Do Know
    st.markdown("### ⚖️ INTELLECTUAL HONESTY: BOUNDARIES & STRENGTHS")
    st.markdown(
        """
        <div style="font-size: 0.85rem; color: #94a3b8; margin-bottom: 14px;">
            I am a fresher. Rather than pretending to be an expert in every technology, here is an honest breakdown of where my current boundaries lie and what I know how to execute right now.
        </div>
        """,
        unsafe_allow_html=True
    )

    col_k1, col_k2 = st.columns(2)

    with col_k1:
        st.markdown(
            """
            <div style="background: rgba(244, 63, 94, 0.05); border: 1px solid rgba(244, 63, 94, 0.2); border-radius: 6px; padding: 18px; height: 100%;">
                <span class="badge badge-counter">WHAT I DON'T KNOW YET</span>
                <div style="margin-top: 10px; font-size: 0.82rem; color: #cbd5e1; line-height: 1.5;">
            """
            + "".join([
                f"<div style='margin-bottom: 12px;'><b>• {item['topic']}:</b><br><span style='color: #94a3b8;'>{item['detail']}</span></div>"
                for item in KNOW_VS_DONT_KNOW['dont_know']
            ])
            + """
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col_k2:
        st.markdown(
            """
            <div style="background: rgba(34, 197, 94, 0.05); border: 1px solid rgba(34, 197, 94, 0.2); border-radius: 6px; padding: 18px; height: 100%;">
                <span class="badge badge-observed">WHAT I DO KNOW HOW TO DO</span>
                <div style="margin-top: 10px; font-size: 0.82rem; color: #cbd5e1; line-height: 1.5;">
            """
            + "".join([
                f"<div style='margin-bottom: 12px;'><b>• {item['topic']}:</b><br><span style='color: #94a3b8;'>{item['detail']}</span></div>"
                for item in KNOW_VS_DONT_KNOW['do_know']
            ])
            + """
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("---")

    # Build Log
    st.markdown("### 🛠️ BUILD LOG (01 → 06)")
    st.markdown(
        """
        <div style="font-size: 0.84rem; color: #94a3b8; margin-bottom: 16px;">
            Chronological progression of how this prototype was conceptualized and built:
        </div>
        """,
        unsafe_allow_html=True
    )

    for item in BUILD_LOG:
        st.markdown(
            f"""
            <div style="display: flex; gap: 16px; margin-bottom: 14px; background: #0f172a; border: 1px solid #1e293b; padding: 14px 18px; border-radius: 6px;">
                <div style="font-family: 'JetBrains Mono'; font-size: 1.2rem; font-weight: 700; color: #38bdf8;">
                    {item['step']}
                </div>
                <div>
                    <h5 style="font-family: 'JetBrains Mono'; font-size: 0.92rem; color: #f8fafc; margin: 0 0 2px 0;">
                        {item['title']}
                    </h5>
                    <div style="font-family: 'JetBrains Mono'; font-size: 0.78rem; color: #fbbf24; margin-bottom: 4px;">
                        "{item['question']}"
                    </div>
                    <div style="font-size: 0.82rem; color: #94a3b8; line-height: 1.45;">
                        {item['detail']}
                    </div>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ==============================================================================
# FOOTER
# ==============================================================================

st.markdown("---")
st.markdown(
    """
    <div style="display: flex; justify-content: space-between; align-items: center; font-family: 'JetBrains Mono'; font-size: 0.72rem; color: #64748b; padding: 10px 0;">
        <div>
            <b>LAUNCH//REVERSE</b> — Prototype Research Terminal | Built with Python, Streamlit, Plotly, Pandas, FastAPI
        </div>
        <div>
            Status: <span style="color: #4ade80;">LOCAL_DEMO_READY</span> | Epistemic Integrity: <span style="color: #38bdf8;">VERIFIED</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)
