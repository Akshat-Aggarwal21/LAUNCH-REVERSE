"""
Agent Execution Terminal for LAUNCH//REVERSE.
Renders the genuine 3-agent tool-using research workflow:
1. Research Agent (Tools: filter_artifacts, get_launch_timeline, search_artifacts)
2. Pattern Hunter Agent (Tools: find_sequences, count_by, calculate_statistics, compare_launches)
3. Skeptic Agent (Tools: find_counterexamples, compare_groups, inspect_artifacts)
Plus Synthesis step.
Uses textwrap.dedent to ensure pristine HTML rendering without raw tag leakage.
"""

import streamlit as st
import textwrap
import json
from typing import List, Dict, Any
from components.styles import render_html


def render_agentic_workflow_trace(pipeline_result: Dict[str, Any]):
    """
    Renders the live agent execution trace, tool invocations, and structured outputs.
    Uses render_html to guarantee error-free, uncorrupted HTML rendering.
    """
    steps = pipeline_result.get("steps", [])
    synthesis = pipeline_result.get("synthesis", {})

    header_html = """
<div style="background: #0f172a; border: 1px solid #1e293b; border-radius: 8px; padding: 18px 20px; margin-bottom: 20px;">
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <div>
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #38bdf8; text-transform: uppercase;">
                MULTI-AGENT RE-ACT WORKFLOW // 3 SPECIALIZED AGENTS + TOOLS
            </span>
            <h3 style="font-family: 'JetBrains Mono', monospace; font-size: 1.1rem; color: #f8fafc; margin: 4px 0 0 0;">
                Evidence-Grounded Research Pipeline
            </h3>
        </div>
        <div style="background: rgba(34, 197, 94, 0.1); border: 1px solid rgba(34, 197, 94, 0.3); padding: 4px 10px; border-radius: 4px;">
            <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #4ade80;">TOOL-AUGMENTED WORKFLOW</span>
        </div>
    </div>
    <p style="font-size: 0.84rem; color: #94a3b8; margin: 8px 0 0 0;">
        Agents communicate through constrained tools and structured records rather than raw text passing.
    </p>
</div>
"""
    render_html(header_html)

    # -------------------------------------------------------------------------
    # Quick High-Level Trace View (Instruction 19)
    # -------------------------------------------------------------------------
    st.markdown("#### ⚡ HIGH-LEVEL AGENT TRACE")

    col_t1, col_t2, col_t3 = st.columns(3)

    agent_colors = ["#38bdf8", "#a855f7", "#f43f5e"]
    for idx, (col, step) in enumerate(zip([col_t1, col_t2, col_t3], steps)):
        with col:
            color = agent_colors[idx % len(agent_colors)]
            bullets = "".join([f"<div style='margin-top: 4px;'>→ {b}</div>" for b in step.get("trace_bullets", [])])
            box_html = f"""
<div style="background: #111827; border: 1px solid #1f2937; border-radius: 6px; padding: 14px; min-height: 180px;">
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.82rem; font-weight: 700; color: {color};">
        {step['agent_name']}
    </div>
    <div style="font-size: 0.72rem; color: #64748b; text-transform: uppercase; margin-bottom: 8px;">
        {step['role']}
    </div>
    <div style="font-family: 'JetBrains Mono', monospace; font-size: 0.76rem; color: #cbd5e1; line-height: 1.45;">
        {bullets}
    </div>
</div>
"""
            render_html(box_html)

    render_html("<div style='margin-top: 20px;'></div>")

    # -------------------------------------------------------------------------
    # Detailed Agent Tool Call Inspector
    # -------------------------------------------------------------------------
    st.markdown("#### 🔍 DETAILED AGENT EXECUTION & TOOL CALLS")

    tab_titles = [s["agent_name"] for s in steps] + ["Final Synthesis"]
    agent_tabs = st.tabs(tab_titles)

    for idx, step in enumerate(steps):
        with agent_tabs[idx]:
            color = agent_colors[idx % len(agent_colors)]
            detail_html = f"""
<div style="background: #111827; border: 1px solid #1f2937; border-radius: 6px; padding: 16px; margin-bottom: 14px;">
    <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid #1f2937; padding-bottom: 8px; margin-bottom: 12px;">
        <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.85rem; font-weight: 700; color: {color};">
            {step['agent_name']} — {step['role']}
        </span>
        <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.72rem; color: #94a3b8;">
            {len(step['tool_invocations'])} TOOL CALLS EXECUTED
        </span>
    </div>
    <div style="font-size: 0.83rem; color: #cbd5e1; line-height: 1.5; margin-bottom: 12px;">
        <b>Agent Reasoning:</b> {step['reasoning']}
    </div>
</div>
"""
            render_html(detail_html)

            # Tool Calls Section
            st.markdown("**Tool Calls Executed by this Agent:**")
            for t_idx, t_call in enumerate(step.get("tool_invocations", []), start=1):
                with st.expander(f"Tool Call #{t_idx}: `{t_call['tool']}()` — {t_call['summary']}", expanded=False):
                    st.markdown(f"**Tool Parameters:**")
                    st.code(json.dumps(t_call["parameters"], indent=2), language="json")
                    st.markdown(f"**Result Data:**")
                    st.json(t_call["raw_result"])

            # Structured Output
            with st.expander("Structured Agent Output (Pydantic / JSON)", expanded=False):
                st.json(step.get("structured_output", {}))

    # Synthesis Tab
    with agent_tabs[-1]:
        synth_html = f"""
<div style="background: #0f172a; border: 1px solid #1e293b; border-radius: 6px; padding: 18px; margin-bottom: 14px;">
    <span style="font-family: 'JetBrains Mono', monospace; font-size: 0.75rem; color: #4ade80; text-transform: uppercase; font-weight: 700;">
        AGENT 04 // SYNTHESIS & BOUNDED DOSSIER
    </span>
    <h4 style="font-family: 'JetBrains Mono', monospace; font-size: 1.05rem; color: #f8fafc; margin: 6px 0 12px 0;">
        {synthesis.get('headline_insight', 'Research synthesis complete.')}
    </h4>
    <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 16px; font-size: 0.82rem; margin-top: 10px;">
        <div style="background: #111827; padding: 12px; border-radius: 4px; border-left: 3px solid #4ade80;">
            <span style="color: #4ade80; font-weight: 600; font-family: 'JetBrains Mono', monospace;">[OBSERVED]:</span>
            <div style="color: #cbd5e1; margin-top: 4px;">{synthesis.get('epistemic_summary', {}).get('OBSERVED', '')}</div>
        </div>
        <div style="background: #111827; padding: 12px; border-radius: 4px; border-left: 3px solid #38bdf8;">
            <span style="color: #38bdf8; font-weight: 600; font-family: 'JetBrains Mono', monospace;">[INFERRED]:</span>
            <div style="color: #cbd5e1; margin-top: 4px;">{synthesis.get('epistemic_summary', {}).get('INFERRED', '')}</div>
        </div>
        <div style="background: #111827; padding: 12px; border-radius: 4px; border-left: 3px solid #fbbf24;">
            <span style="color: #fbbf24; font-weight: 600; font-family: 'JetBrains Mono', monospace;">[HYPOTHESIS]:</span>
            <div style="color: #cbd5e1; margin-top: 4px;">{synthesis.get('epistemic_summary', {}).get('HYPOTHESIS', '')}</div>
        </div>
        <div style="background: #111827; padding: 12px; border-radius: 4px; border-left: 3px solid #f43f5e;">
            <span style="color: #fb7185; font-weight: 600; font-family: 'JetBrains Mono', monospace;">[SKEPTIC BOUNDS]:</span>
            <div style="color: #cbd5e1; margin-top: 4px;">{synthesis.get('epistemic_summary', {}).get('BOUNDS', '')}</div>
        </div>
    </div>
    <div style="border-top: 1px dashed #334155; padding-top: 10px; margin-top: 14px; font-family: 'JetBrains Mono', monospace; font-size: 0.78rem; color: #94a3b8;">
        <b>CALIBRATED CONFIDENCE:</b> <span style="color: #fbbf24;">{synthesis.get('calibrated_confidence', 'MEDIUM')}</span> | 
        <b>NEXT DATA REQUIRED:</b> <span style="color: #7dd3fc;">{synthesis.get('next_data_required', '')}</span>
    </div>
</div>
"""
        render_html(synth_html)

