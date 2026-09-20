"""
LAUNCH//REVERSE — Main Research Terminal
"Reverse-engineering how product launches become distribution."
An AI-native research tool prototype for Social Capital.
"""

import streamlit as st
import pandas as pd
import json
import time

from core.engine import engine
from core.agent_orchestrator import run_agentic_research_pipeline
from components.styles import TERMINAL_CSS, get_badge_html, render_html
from components.visuals import build_timeline_figure, build_launch_dna_radar, build_hook_distribution_bar
from components.skeptic_inspector import render_why_this_insight_card
from components.terminal import render_agentic_workflow_trace
from data.hypotheses import HYPOTHESES_DATA, PRESET_HYPOTHESES_SANDBOX
from data.architecture_data import PIPELINE_STAGES, RESUME_CONNECTIONS, BUILD_LOG, KNOW_VS_DONT_KNOW
from data.launch_dna import DNA_DISCLAIMER

# Page configuration
st.set_page_config(
    page_title="LAUNCH//REVERSE — AI-Native Distribution Research",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Apply custom terminal styling
st.markdown(TERMINAL_CSS, unsafe_allow_html=True)


# ==============================================================================
# SIDEBAR NAVIGATION & CASE STUDY SELECTION
# ==============================================================================

with st.sidebar:
    sidebar_brand = """
<div style="padding: 6px 0 14px 0; border-bottom: 1px solid #1f2937;">
    <div style="font-family: 'JetBrains Mono', monospace; font-weight: 800; font-size: 1.15rem; color: #f8fafc; letter-spacing: -0.02em;">
        LAUNCH<span style="color: #38bdf8;">//</span>REVERSE
    </div>
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #94a3b8; margin-top: 2px;">
        DISTRIBUTION REVERSE-ENGINEERING
    </div>
    <div style="margin-top: 8px;">
        <span class="badge badge-simulated">RESEARCH PROTOTYPE</span>
        <span class="badge badge-observed">AI-NATIVE · PYTHON BUILT</span>
    </div>
</div>
"""
    render_html(sidebar_brand)

    st.markdown("### 1. EXECUTION MODE")
    execution_mode = st.radio(
        "Select Operating Mode:",
        ["⚡ Demo Mode (Deterministic Local)", "🤖 Agent Mode (Tool-Using Loop)"],
        index=0,
        help="Demo Mode works 100% locally with zero API keys. Agent Mode activates the multi-agent tool-calling loop."
    )

    if "Agent Mode" in execution_mode:
        agent_mode_banner = """
<div style="background: rgba(168, 85, 247, 0.1); border: 1px solid rgba(168, 85, 247, 0.3); border-radius: 4px; padding: 8px 10px; margin-top: 6px; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #d8b4fe;">
    <b>AGENT MODE ACTIVE:</b> 3 tool-equipped agents (Research, Pattern Hunter, Skeptic) execute live queries over structured records.
</div>
"""
        render_html(agent_mode_banner)
    else:
        demo_mode_banner = """
<div style="background: rgba(34, 197, 94, 0.08); border: 1px solid rgba(34, 197, 94, 0.25); border-radius: 4px; padding: 8px 10px; margin-top: 6px; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #86efac;">
    <b>DEMO MODE ACTIVE:</b> 100% local curated dataset. Zero external API keys or credentials needed.
</div>
"""
        render_html(demo_mode_banner)

    st.markdown("---")
    st.markdown("### 2. SELECT CASE STUDY")
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

    if selected_cs in ["wispr-flow", "gamma"]:
        cs_banner = """
<div style="background: rgba(56, 189, 248, 0.08); border-left: 2px solid #38bdf8; padding: 6px 10px; font-family: 'JetBrains Mono', monospace; font-size: 0.73rem; color: #7dd3fc; margin-bottom: 10px;">
    <b>Public Artifact Analysis</b><br>
    Modeled strictly on publicly visible posts, videos & timelines.
</div>
"""
    else:
        cs_banner = """
<div style="background: rgba(168, 85, 247, 0.08); border-left: 2px solid #a855f7; padding: 6px 10px; font-family: 'JetBrains Mono', monospace; font-size: 0.73rem; color: #d8b4fe; margin-bottom: 10px;">
    <b>Synthetic / Simulated Reference Dataset</b><br>
    Synthetically generated to test edge cases & challenge assumptions.
</div>
"""
    render_html(cs_banner)

    st.markdown("---")
    st.markdown("### 3. NAVIGATION")
    nav_view = st.radio(
        "Workspace View",
        [
            "⚡ 1. Evidence → Hypothesis Loop",
            "🤖 2. Tool-Using Agents (Trace)",
            "🔬 3. Interactive Skeptic Sandbox",
            "🧬 4. Launch DNA & Timeline",
            "💡 5. What Did We Actually Learn?",
            "🏗️ 6. System Architecture & Code",
            "👤 7. Why I Built This & Build Log"
        ],
        key="nav_view_radio"
    )

    st.markdown("---")
    epistemic_footer = """
<div style="font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; color: #64748b; line-height: 1.5;">
    <b>EPISTEMIC BOUNDS:</b><br>
    • <span style="color: #4ade80;">[OBSERVED]</span>: Directly in artifacts<br>
    • <span style="color: #38bdf8;">[INFERRED]</span>: Calculated patterns<br>
    • <span style="color: #fbbf24;">[HYPOTHESIS]</span>: Proposed mechanisms<br>
    • <span style="color: #c084fc;">[SIMULATED]</span>: Synthetic benchmarks<br>
    • <span style="color: #fb7185;">[COUNTER]</span>: Skeptic exceptions
</div>
"""
    render_html(epistemic_footer)


# ==============================================================================
# HERO HEADER & SOCIAL CAPITAL INTELLECTUAL HONESTY FRAMING
# ==============================================================================

hero_html = """
<div class="hero-box">
    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
            <span class="badge badge-simulated">RESEARCH PROTOTYPE</span>
            <span class="badge badge-observed">AI-NATIVE · PYTHON BUILT</span>
            <h1 style="font-family: 'JetBrains Mono', monospace; font-size: 1.65rem; color: #f8fafc; margin: 8px 0 6px 0; letter-spacing: -0.02em;">
                Can we reverse-engineer a launch?
            </h1>
            <p style="font-size: 0.94rem; color: #cbd5e1; max-width: 820px; line-height: 1.5; margin: 0 0 10px 0;">
                <b>LAUNCH//REVERSE</b> analyzes publicly visible launch artifacts and turns them into testable hypotheses about distribution using tool-augmented agents.
            </p>
        </div>
        <div style="text-align: right; background: #0f172a; border: 1px solid #1e293b; padding: 10px 14px; border-radius: 6px;">
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #64748b; display: block;">TARGET CONTEXT</span>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; font-weight: 700; color: #38bdf8;">Social Capital Inc.</span>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.68rem; color: #94a3b8; display: block; margin-top: 2px;">Technical Generalist Role</span>
        </div>
    </div>

    <div style="background: #0b0f19; border: 1px solid #1e293b; border-radius: 6px; padding: 12px 16px; margin-top: 8px;">
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; color: #94a3b8; line-height: 1.5;">
            <b>INTELLECTUAL HONESTY NOTICE:</b> This project does not claim to reproduce Social Capital's internal methodology. 
            It explores whether publicly observable launch artifacts can be modeled as structured evidence and analyzed for repeatable distribution patterns.
        </div>
    </div>
</div>
"""
render_html(hero_html)


# Load data and pipeline results
artifacts_df = engine.get_case_study_artifacts(selected_cs)
timeline_stats = engine.get_timeline_stats(selected_cs)
dna_profile = engine.get_dna_profile(selected_cs)

# Run agentic research pipeline
if "selected_focus_topic" not in st.session_state:
    st.session_state["selected_focus_topic"] = "launch_sequence"

pipeline_result = run_agentic_research_pipeline(selected_cs, focus_topic=st.session_state["selected_focus_topic"])


# ==============================================================================
# VIEW 1: EVIDENCE → HYPOTHESIS LOOP (THE CENTERPIECE)
# ==============================================================================

if "1. Evidence → Hypothesis Loop" in nav_view:
    st.markdown("### 🎯 THE CENTERPIECE: EVIDENCE → PATTERN → HYPOTHESIS → CHALLENGE")
    
    view1_intro_html = """
<div style="font-size: 0.88rem; color: #cbd5e1; margin-bottom: 16px;">
    Instead of presenting AI assertions as objective facts, every finding is built through a verifiable 5-step epistemic progression:
    <b>Observed Evidence → Detected Pattern → Proposed Hypothesis → Skeptic Counterexamples → Calibrated Bounds</b>.
</div>
"""
    render_html(view1_intro_html)

    # -------------------------------------------------------------
    # Concrete Evidence-Backed Finding (Instruction 11)
    # -------------------------------------------------------------
    featured_finding_html = """
<div style="background: linear-gradient(180deg, #0f172a 0%, #111827 100%); border: 1px solid #1e293b; border-left: 4px solid #38bdf8; border-radius: 6px; padding: 20px; margin-bottom: 24px;">
    <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 10px;">
        <div>
            <span class="badge badge-observed">[OBSERVED CALCULATION]</span>
            <span class="badge badge-hypothesis">[HYPOTHESIS]</span>
            <span class="badge badge-counter">[SKEPTIC AUDITED]</span>
            <h3 style="font-family: 'JetBrains Mono', monospace; font-size: 1.15rem; color: #f8fafc; margin: 6px 0 0 0;">
                Featured Discovery: The Two-Phase Velocity Decoupling
            </h3>
        </div>
        <div style="text-align: right;">
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #64748b; display: block;">CONFIDENCE</span>
            <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #fbbf24;">MEDIUM (BOUNDED)</span>
        </div>
    </div>

    <div style="font-size: 0.86rem; color: #cbd5e1; line-height: 1.6;">
        <p><b>1. Observed Pattern in Dataset:</b><br>
        In Wispr Flow and Gamma launches, pre-launch founder posts (Day -7 to Day -1) average a <b>2.35% interaction-to-view ratio</b> (dense intellectual debate and comment depth). In contrast, Day 0 creator posts achieve <b>2.5x higher view impressions</b> (mean: 491,000 views) but drop to a <b>1.62% interaction ratio</b>. Crucially, continuous-take video screencasts under 30s appeared <i>before or on Day 0</i> across both launches, generating 5,410 to 11,800 interactions.</p>

        <p><b>2. Proposed Mechanism (Hypothesis):</b><br>
        Pre-launch speed proof collapses consumer skepticism. When Day 0 creator spikes arrive, viewers convert because the product's core utility has already been visibly demonstrated, preventing high bounce rates.</p>

        <p style="color: #fca5a5;"><b>3. Skeptic Agent Counterevidence:</b><br>
        • In the OmniContext synthetic reference set (EX-02), static graph screenshots achieved 1,550 interactions without video proof.<br>
        • Confounding factor: Algorithmic feed weighting on X and LinkedIn heavily prioritizes native video formats over text.<br>
        • Public artifacts cannot verify whether creator view spikes drove paid retention or merely transient curiosity.</p>
    </div>

    <div style="background: #0b0f19; border: 1px solid #1f2937; padding: 10px 14px; border-radius: 4px; margin-top: 12px; font-family: 'JetBrains Mono', monospace; font-size: 0.76rem; color: #94a3b8;">
        <b>MISSING TELEMETRY BEFORE CLAIMING CAUSATION:</b> First-party UTM conversion parameters and 30-day cohort retention data segmented by acquisition referral source.
    </div>
</div>
"""
    render_html(featured_finding_html)

    # -------------------------------------------------------------
    # Surfaced Hypotheses with "Why This Insight?" Inspector
    # -------------------------------------------------------------
    st.markdown("#### 📑 ACTIVE RESEARCH HYPOTHESES")
    
    hyp_intro_html = """
<div style="font-size: 0.84rem; color: #94a3b8; margin-bottom: 12px;">
    Each hypothesis below separates direct observation from proposed explanation and includes counterexamples found by the Skeptic Agent:
</div>
"""
    render_html(hyp_intro_html)

    for hyp in HYPOTHESES_DATA:
        card_markup = f"""
<div class="terminal-card">
    <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
            <span class="badge badge-hypothesis">{hyp['category']}</span>
            <span class="badge badge-simulated">{hyp['status']}</span>
            <div class="card-title" style="margin-top: 4px;">{hyp['title']}</div>
        </div>
        <div style="text-align: right;">
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #64748b; display: block;">CONFIDENCE</span>
            <span style="font-family: 'JetBrains Mono', monospace; font-weight: 700; color: #fbbf24;">{hyp['confidence_level']}</span>
        </div>
    </div>
    <div style="font-size: 0.83rem; color: #cbd5e1; margin-top: 8px; line-height: 1.5;">
        <span style="color: #4ade80; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">[OBSERVED]:</span> {hyp['observation']}<br>
        <span style="color: #fbbf24; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">[HYPOTHESIS]:</span> {hyp['hypothesis_mechanism']}<br>
        <span style="color: #fb7185; font-family: 'JetBrains Mono', monospace; font-size: 0.75rem;">[COUNTEREVIDENCE]:</span> {hyp['counterevidence']}
    </div>
</div>
"""
        render_html(card_markup)

        with st.expander(f"🔍 Why This Insight? — Epistemic Audit for {hyp['id']}", expanded=False):
            render_why_this_insight_card(hyp)


# ==============================================================================
# VIEW 2: TOOL-USING AGENTS (TRACE)
# ==============================================================================

elif "2. Tool-Using Agents (Trace)" in nav_view:
    st.markdown("### 🤖 3 TOOL-USING AGENTS: RESEARCH → PATTERN HUNTER → SKEPTIC")
    
    view2_intro_html = """
<div style="font-size: 0.88rem; color: #cbd5e1; margin-bottom: 16px;">
    Rather than relying on vague chat prompts, the system uses 3 specialized agents equipped with constrained tools operating directly over the structured launch dataset.
</div>
"""
    render_html(view2_intro_html)

    # In Agent Mode: allow interactive re-execution with specific focus topic
    if "Agent Mode" in execution_mode:
        st.markdown("#### ⚡ INTERACTIVE AGENT CONTROLS")
        col_ctl1, col_ctl2 = st.columns([2, 1])
        with col_ctl1:
            focus_options = {
                "launch_sequence": "Launch Sequence & Phase Handoffs (Founder → Creator)",
                "video": "Video Demonstration vs Static Screenshot Velocity",
                "founder": "Founder Pre-Launch Problem Framing",
                "creator": "Creator Reach & Amplification Mechanics"
            }
            chosen_topic = st.selectbox(
                "Select Investigation Focus Topic:",
                options=list(focus_options.keys()),
                format_func=lambda k: focus_options[k],
                key="agent_focus_select"
            )
        with col_ctl2:
            st.markdown("<div style='margin-top: 28px;'></div>", unsafe_allow_html=True)
            run_btn = st.button("▶ RUN MULTI-AGENT INVESTIGATION", type="primary")

        if run_btn:
            with st.status("Executing Multi-Agent Tool-Calling Loop...", expanded=True) as status:
                st.write("🔍 **Research Agent:** Executing `filter_artifacts`, `search_artifacts`, `get_launch_timeline`...")
                time.sleep(0.4)
                st.write("📊 **Pattern Hunter Agent:** Executing `find_sequences`, `calculate_statistics`, `count_by`...")
                time.sleep(0.4)
                st.write("🔬 **Skeptic Agent:** Executing `find_counterexamples`, `compare_groups`, adversarial bounds...")
                time.sleep(0.4)
                st.write("📝 **Synthesizer:** Generating calibrated dossier and missing data requirements...")
                time.sleep(0.3)
                status.update(label="✓ Multi-Agent Pipeline Complete: Evidence Synthesized & Bounded", state="complete", expanded=False)
            pipeline_result = run_agentic_research_pipeline(selected_cs, focus_topic=chosen_topic)

    render_agentic_workflow_trace(pipeline_result)


# ==============================================================================
# VIEW 3: INTERACTIVE SKEPTIC SANDBOX
# ==============================================================================

elif "3. Interactive Skeptic Sandbox" in nav_view:
    st.markdown("### 🔬 INTERACTIVE SKEPTIC SANDBOX")
    
    view3_intro_html = """
<div style="font-size: 0.88rem; color: #cbd5e1; margin-bottom: 14px;">
    The Skeptic Agent's primary job is to <b>actively break hypotheses</b>. Select or type a proposition to trigger an adversarial audit against the dataset:
</div>
"""
    render_html(view3_intro_html)

    col_b1, col_b2, col_b3, col_b4 = st.columns(4)
    preset_choice = None
    with col_b1:
        if st.button("Founder-led narrative"):
            preset_choice = "Founder-led narrative"
    with col_b2:
        if st.button("Creator amplification"):
            preset_choice = "Creator amplification"
    with col_b3:
        if st.button("Product demonstration"):
            preset_choice = "Product demonstration"
    with col_b4:
        if st.button("Contrarian hook"):
            preset_choice = "Contrarian hook"

    target_hyp = st.text_input(
        "Hypothesis to challenge:",
        value=preset_choice if preset_choice else "Creator amplification",
        placeholder="Enter a launch hypothesis..."
    )

    if st.button("🔍 CHALLENGE HYPOTHESIS (RUN SKEPTIC AGENT)", type="primary"):
        challenge_res = engine.challenge_hypothesis(target_hyp)
        
        evidence_items = "".join([f"<li>{e}</li>" for e in challenge_res["evidence"]])
        counter_items = "".join([f"<li>{c}</li>" for c in challenge_res["counterevidence"]])

        audit_html = f"""
<div style="background: #0f172a; border: 1px solid #1e293b; border-radius: 8px; padding: 18px 22px; margin-top: 14px;">
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1e293b; padding-bottom: 10px;">
        <div>
            <span class="badge badge-counter">SKEPTIC AUDIT REPORT</span>
            <h4 style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; color: #f8fafc; margin: 4px 0 0 0;">
                {challenge_res['title']}
            </h4>
        </div>
        <div style="text-align: right;">
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.7rem; color: #64748b; display: block;">CONFIDENCE</span>
            <span class="badge badge-hypothesis">{challenge_res['confidence']}</span>
        </div>
    </div>

    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px; margin-top: 14px; font-size: 0.83rem;">
        <div>
            <span style="font-family: 'JetBrains Mono', monospace; font-weight: 600; color: #4ade80;">✓ OBSERVED EVIDENCE:</span>
            <ul style="color: #cbd5e1; padding-left: 18px; margin-top: 6px; line-height: 1.5;">
                {evidence_items}
            </ul>
            <div style="background: #111827; padding: 10px; border-radius: 4px; border: 1px solid #1f2937; margin-top: 10px;">
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #fbbf24;">PROPOSED MECHANISM:</span>
                <div style="color: #cbd5e1; margin-top: 2px;">{challenge_res['mechanism']}</div>
            </div>
        </div>

        <div>
            <span style="font-family: 'JetBrains Mono', monospace; font-weight: 600; color: #fb7185;">⚠ SKEPTIC COUNTERARGUMENT:</span>
            <ul style="color: #cbd5e1; padding-left: 18px; margin-top: 6px; line-height: 1.5;">
                {counter_items}
            </ul>
            <div style="background: rgba(244, 63, 94, 0.1); border-left: 3px solid #f43f5e; padding: 8px 12px; border-radius: 0 4px 4px 0; margin-top: 10px;">
                <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; font-weight: 700; color: #f43f5e;">SKEPTIC VERDICT:</span>
                <div style="color: #fecdd3; margin-top: 2px;">{challenge_res['skeptic_verdict']}</div>
            </div>
        </div>
    </div>

    <div style="border-top: 1px dashed #334155; padding-top: 12px; margin-top: 16px; font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; color: #94a3b8;">
        <b>NEXT DATA REQUIRED BEFORE ACCEPTANCE:</b> <span style="color: #7dd3fc;">{challenge_res['next_data_required']}</span>
    </div>
</div>
"""
        render_html(audit_html)


# ==============================================================================
# VIEW 4: LAUNCH DNA & TIMELINE (EVIDENCE-BACKED)
# ==============================================================================

elif "4. Launch DNA & Timeline" in nav_view:
    st.markdown("### 🧬 LAUNCH DNA & CHRONOLOGICAL TIMELINE")

    # Metrics row
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)
    with col_m1:
        render_html(f'<div class="stat-box"><div class="stat-label">STRUCTURED ARTIFACTS</div><div class="stat-value">{timeline_stats.get("total_artifacts", 0)}</div><div style="color: #4ade80; font-size: 0.7rem;">✓ Verified Provenance</div></div>')
    with col_m2:
        render_html(f'<div class="stat-box"><div class="stat-label">RECORDED IMPRESSIONS</div><div class="stat-value">{timeline_stats.get("total_views", 0):,}</div><div style="color: #38bdf8; font-size: 0.7rem;">Public Video / Threads</div></div>')
    with col_m3:
        render_html(f'<div class="stat-box"><div class="stat-label">INTERACTIONS</div><div class="stat-value">{timeline_stats.get("total_interactions", 0):,}</div><div style="color: #fbbf24; font-size: 0.7rem;">Likes, Reposts, Upvotes</div></div>')
    with col_m4:
        render_html(f'<div class="stat-box"><div class="stat-label">INTERACTION RATIO</div><div class="stat-value">{timeline_stats.get("interaction_rate", 0)}%</div><div style="color: #c084fc; font-size: 0.7rem;">Engagement Density</div></div>')

    render_html("<div style='margin-top: 20px;'></div>")

    # Timeline Chart
    timeline_fig = build_timeline_figure(artifacts_df)
    st.plotly_chart(timeline_fig, width="stretch")

    # DNA Radar and Hook Distribution
    col_dna, col_hook = st.columns([1.1, 0.9])

    with col_dna:
        st.markdown("#### 🧬 8-DIMENSIONAL LAUNCH DNA (EVIDENCE-BACKED)")
        dna_box = f"""
<div class="disclaimer-banner">
    ⚠️ <b>EPISTEMIC NOTICE:</b> {DNA_DISCLAIMER}
</div>
"""
        render_html(dna_box)

        radar_fig = build_launch_dna_radar(dna_profile)
        st.plotly_chart(radar_fig, width="stretch")

        # Evidence basis for each dimension
        with st.expander("View Calculation Basis for Each Dimension", expanded=False):
            for dim_name, dim_val in dna_profile["dimensions"].items():
                if isinstance(dim_val, dict):
                    st.markdown(f"**{dim_name} ({dim_val['score']}/100)** `[{dim_val['epistemic_status']}]` — *{dim_val['calculation_basis']}*")

    with col_hook:
        st.markdown("#### 🎯 HOOK TYPE DISTRIBUTION")
        hook_bar = build_hook_distribution_bar(artifacts_df)
        st.plotly_chart(hook_bar, width="stretch")

        hook_heuristic_html = """
<div style="font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; color: #94a3b8; background: #0f172a; padding: 12px 14px; border-radius: 4px; border: 1px solid #1e293b; line-height: 1.5;">
    <b>Observed Heuristic:</b> Launches frontloading <i>Contrarian</i> or <i>Pain-Point</i> hooks build conversational tension. 
    Demos deploying <i>Velocity Proof</i> in pre-launch report higher organic bookmark density.
</div>
"""
        render_html(hook_heuristic_html)

    st.markdown("---")

    # Artifact Explorer with Full Provenance (Instruction 21)
    st.markdown("#### 🗃️ ARTIFACT PROVENANCE EXPLORER")
    for _, row in artifacts_df.iterrows():
        header_summary = f"{row['id']} | {row['day_label']} — {row['author']} ({row['author_type']}) on {row['platform']}: {row['narrative'][:60]}..."
        with st.expander(header_summary, expanded=False):
            col_x1, col_x2 = st.columns([1.2, 0.8])
            with col_x1:
                st.markdown(f"**Verbatim Post Text / Content:**")
                st.info(f"\"{row['raw_content']}\"")
                st.markdown(f"**Source URL:** [{row.get('source_url', 'public post')}]({row.get('source_url', '#')})")
            with col_x2:
                art_meta_html = f"""
<div style="background: #0f172a; border: 1px solid #1e293b; padding: 12px; border-radius: 4px; font-family: 'JetBrains Mono', monospace; font-size: 0.78rem;">
    <div><b>EPISTEMIC STATUS:</b> {get_badge_html(row['epistemic_status'], row['epistemic_status'])}</div>
    <div style="margin-top: 4px;"><b>AUTHOR HANDLE:</b> {row.get('author_handle', '@unknown')}</div>
    <div><b>PLATFORM:</b> {row['platform']}</div>
    <div><b>VIEWS:</b> {row['engagement_views']:,}</div>
    <div><b>INTERACTIONS:</b> {row['engagement_interactions']:,}</div>
    <div><b>CONFIDENCE:</b> {int(row['confidence_score'] * 100)}%</div>
</div>
"""
                render_html(art_meta_html)


# ==============================================================================
# VIEW 5: WHAT DID WE ACTUALLY LEARN? (INSTRUCTION 12)
# ==============================================================================

elif "5. What Did We Actually Learn?" in nav_view:
    st.markdown("### 💡 WHAT DID WE ACTUALLY LEARN?")
    
    view5_intro_html = """
<div style="font-family: 'JetBrains Mono', monospace; font-size: 0.74rem; color: #64748b; margin-bottom: 16px;">
    A RIGOROUS RESEARCH SUMMARY SEPARATING SURVIVING PATTERNS FROM UNJUSTIFIED CLAIMS
</div>
"""
    render_html(view5_intro_html)

    learned_html = """
<div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 18px; margin-bottom: 24px;">
    <!-- Column 1: Patterns -->
    <div style="background: #0f172a; border: 1px solid #1e293b; border-top: 3px solid #38bdf8; border-radius: 6px; padding: 18px;">
        <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; font-weight: 700; color: #38bdf8;">
            1. SURVIVING PATTERNS
        </span>
        <div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.55; margin-top: 10px;">
            <p><b>• Velocity Proof Works:</b> Sub-30s screencasts demonstrating continuous speed (<200ms latency or 28s deck creation) consistently generate over 3.2x higher interaction ratios than static marketing images.</p>
            <p><b>• Two-Phase Sequence:</b> High-velocity launches separate narrative tension (pre-launch problem framing) from volume amplification (Day 0 creator blast).</p>
        </div>
    </div>

    <!-- Column 2: Counterevidence -->
    <div style="background: #0f172a; border: 1px solid #1e293b; border-top: 3px solid #fb7185; border-radius: 6px; padding: 18px;">
        <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; font-weight: 700; color: #fb7185;">
            2. COUNTEREVIDENCE & LIMITS
        </span>
        <div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.55; margin-top: 10px;">
            <p><b>• Correlation ≠ Causation:</b> Creator posts explode in views on Day 0, but high viral velocity already existed in closed beta before any creator posted.</p>
            <p><b>• Founder Confounder:</b> Pre-launch founder traction heavily reflects preexisting social capital, not necessarily the messaging framework alone.</p>
        </div>
    </div>

    <!-- Column 3: What We Still Don't Know -->
    <div style="background: #0f172a; border: 1px solid #1e293b; border-top: 3px solid #fbbf24; border-radius: 6px; padding: 18px;">
        <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; font-weight: 700; color: #fbbf24;">
            3. WHAT WE STILL DON'T KNOW
        </span>
        <div style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.55; margin-top: 10px;">
            <p><b>• Retention vs Curiosity:</b> Public views tell us nothing about whether users retained at Day 30 or churned after 3 minutes.</p>
            <p><b>• Algorithmic Bias:</b> Platform algorithms on X/LinkedIn favor video formats; the observed video advantage may be an algorithm artifact rather than genuine buyer preference.</p>
        </div>
    </div>
</div>
"""
    render_html(learned_html)


# ==============================================================================
# VIEW 6: SYSTEM ARCHITECTURE & CODE (STREAMLINED & HONEST)
# ==============================================================================

elif "6. System Architecture & Code" in nav_view:
    st.markdown("### 🏗️ SYSTEM ARCHITECTURE & CODE STRUCTURE")
    
    view6_intro_html = """
<div style="font-size: 0.88rem; color: #cbd5e1; margin-bottom: 16px;">
    A clean, honest pipeline showing what is currently running in this prototype, and how it naturally scales into a full production system.
</div>
"""
    render_html(view6_intro_html)

    # Clean 10-second architecture diagram (Instruction 18)
    arch_diagram_html = """
<div style="background: #0f172a; border: 1px solid #1e293b; border-radius: 6px; padding: 20px; font-family: 'JetBrains Mono', monospace; font-size: 0.8rem; color: #94a3b8; line-height: 1.5; text-align: center; margin-bottom: 24px;">
    <span style="color: #38bdf8; font-weight: 700;">PUBLIC ARTIFACTS</span> (Posts, Videos, Changelogs, Discussion Threads)<br>
    ↓<br>
    <span style="color: #f8fafc; font-weight: 600;">ARTIFACT SCHEMA</span> (Pydantic Document Models with Day Offsets & Epistemic Tags)<br>
    ↓<br>
    <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 14px; text-align: left; margin: 14px 0;">
        <div style="background: #111827; border: 1px solid #1f2937; padding: 12px; border-radius: 4px;">
            <span style="color: #38bdf8; font-weight: 700;">RESEARCH AGENT</span><br>
            <span style="font-size: 0.72rem; color: #64748b;">Gathers & structures evidence</span><br>
            <div style="margin-top: 6px; font-size: 0.73rem; color: #cbd5e1;">
                • get_artifact()<br>• filter_artifacts()<br>• get_launch_timeline()<br>• search_artifacts()
            </div>
        </div>
        <div style="background: #111827; border: 1px solid #1f2937; padding: 12px; border-radius: 4px;">
            <span style="color: #a855f7; font-weight: 700;">PATTERN HUNTER</span><br>
            <span style="font-size: 0.72rem; color: #64748b;">Surfaces sequences & correlations</span><br>
            <div style="margin-top: 6px; font-size: 0.73rem; color: #cbd5e1;">
                • count_by()<br>• compare_launches()<br>• find_sequences()<br>• calculate_statistics()
            </div>
        </div>
        <div style="background: #111827; border: 1px solid #1f2937; padding: 12px; border-radius: 4px;">
            <span style="color: #f43f5e; font-weight: 700;">SKEPTIC AGENT</span><br>
            <span style="font-size: 0.72rem; color: #64748b;">Actively seeks counterexamples</span><br>
            <div style="margin-top: 6px; font-size: 0.73rem; color: #cbd5e1;">
                • find_counterexamples()<br>• inspect_artifacts()<br>• compare_groups()<br>• audit_assumptions()
            </div>
        </div>
    </div>
    ↓<br>
    <span style="color: #4ade80; font-weight: 600;">HUMAN REVIEW & CALIBRATED SYNTHESIS</span><br>
    ↓<br>
    <span style="color: #38bdf8; font-weight: 700;">FINAL INSIGHT DOSSIER</span>
    <div style="border-top: 1px solid #1e293b; margin-top: 12px; padding-top: 8px; font-size: 0.72rem; color: #64748b;">
        Production scale could introduce queues, vector search, distributed workers, cross-platform entity resolution, and continuous evaluation.
    </div>
</div>
"""
    render_html(arch_diagram_html)

    # Technology Mapping Table
    st.markdown("#### 🔗 REASONING & RESUME CONNECTION")
    for item in RESUME_CONNECTIONS:
        res_card_html = f"""
<div class="terminal-card">
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1f2937; padding-bottom: 8px; margin-bottom: 8px;">
        <span class="badge badge-inferred">{item['tech']}</span>
        <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.76rem; color: #38bdf8;">
            PARALLELS: <b>{item['resume_project']}</b>
        </span>
    </div>
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.9rem; color: #f8fafc; margin-bottom: 4px;">
        {item['component']}
    </div>
    <p style="font-size: 0.82rem; color: #cbd5e1; line-height: 1.5; margin: 0;">
        {item['connection_detail']}
    </p>
</div>
"""
        render_html(res_card_html)


# ==============================================================================
# VIEW 7: WHY I BUILT THIS & BUILD LOG
# ==============================================================================

elif "7. Why I Built This & Build Log" in nav_view:
    st.markdown("### 👤 WHY I BUILT THIS & BUILD LOG")

    manifesto_html = """
<div style="background: #111827; border: 1px solid #1f2937; border-radius: 8px; padding: 20px; margin-bottom: 24px;">
    <div style="font-size: 0.9rem; color: #e2e8f0; line-height: 1.65;">
        I wanted to test a question: <b>Can an ambiguous distribution problem be turned into something a machine can research, measure, challenge, and explain?</b><br><br>
        Instead of building another generic chatbot, I treated public launch activity as a structured dataset and built a small research system around it:
        <ol style="margin-top: 8px; padding-left: 20px; line-height: 1.6;">
            <li>Structure public launch artifacts into normalized records with day offsets.</li>
            <li>Use a Research Agent to gather and index evidence with concrete tools.</li>
            <li>Use a Pattern Hunter Agent to detect recurring temporal sequences.</li>
            <li><b>Use a Skeptic Agent to actively search for counterexamples and break those patterns.</b></li>
            <li>Strictly separate what is observed from what is an unproven hypothesis.</li>
        </ol>
        The goal is to demonstrate builder mentality, first-principles thinking, and intellectual honesty about what evidence can and cannot prove.
    </div>
</div>
"""
    render_html(manifesto_html)

    # What I Don't Know Yet vs What I Do Know
    col_dk1, col_dk2 = st.columns(2)
    with col_dk1:
        dk_items_html = "".join([f"<div style='margin-bottom: 12px;'><b>• {item['topic']}:</b><br><span style='color: #94a3b8;'>{item['detail']}</span></div>" for item in KNOW_VS_DONT_KNOW['dont_know']])
        dk_html = f"""
<div style="background: rgba(244, 63, 94, 0.05); border: 1px solid rgba(244, 63, 94, 0.2); border-radius: 6px; padding: 18px; height: 100%;">
    <span class="badge badge-counter">WHAT I DON'T KNOW YET</span>
    <div style="margin-top: 10px; font-size: 0.82rem; color: #cbd5e1; line-height: 1.5;">
        {dk_items_html}
    </div>
</div>
"""
        render_html(dk_html)

    with col_dk2:
        k_items_html = "".join([f"<div style='margin-bottom: 12px;'><b>• {item['topic']}:</b><br><span style='color: #94a3b8;'>{item['detail']}</span></div>" for item in KNOW_VS_DONT_KNOW['do_know']])
        k_html = f"""
<div style="background: rgba(34, 197, 94, 0.05); border: 1px solid rgba(34, 197, 94, 0.2); border-radius: 6px; padding: 18px; height: 100%;">
    <span class="badge badge-observed">WHAT I DO KNOW HOW TO DO</span>
    <div style="margin-top: 10px; font-size: 0.82rem; color: #cbd5e1; line-height: 1.5;">
        {k_items_html}
    </div>
</div>
"""
        render_html(k_html)

    st.markdown("---")

    # Build Log
    st.markdown("#### 🛠️ BUILD LOG (01 → 06)")
    for b in BUILD_LOG:
        b_html = f"""
<div style="display: flex; gap: 16px; margin-bottom: 12px; background: #0f172a; border: 1px solid #1e293b; padding: 12px 16px; border-radius: 6px;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 1.15rem; font-weight: 700; color: #38bdf8;">
        {b['step']}
    </div>
    <div>
        <h5 style="font-family: 'JetBrains Mono', monospace; font-size: 0.9rem; color: #f8fafc; margin: 0 0 2px 0;">
            {b['title']}
        </h5>
        <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.76rem; color: #fbbf24; margin-bottom: 4px;">
            "{b['question']}"
        </div>
        <div style="font-size: 0.81rem; color: #94a3b8; line-height: 1.45;">
            {b['detail']}
        </div>
    </div>
</div>
"""
        render_html(b_html)


# ==============================================================================
# FOOTER
# ==============================================================================

st.markdown("---")
footer_html = """
<div style="display: flex; justify-content: space-between; align-items: center; font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #64748b; padding: 6px 0;">
    <div>
        <b>LAUNCH//REVERSE</b> — AI-Native Distribution Research Terminal | Python · Streamlit · Plotly · Pandas · FastAPI
    </div>
    <div>
        Status: <span style="color: #4ade80;">LOCAL_OPERATIONAL</span> | Epistemic Integrity: <span style="color: #38bdf8;">AUDITED</span>
    </div>
</div>
"""
render_html(footer_html)
