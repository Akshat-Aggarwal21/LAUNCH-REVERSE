"""
Interactive Agent Terminal for LAUNCH//REVERSE.
Visualizes multi-agent orchestration across:
- AGENT 01: ARCHIVIST ("What happened?")
- AGENT 02: PATTERN HUNTER ("What appears repeatedly?")
- AGENT 03: SKEPTIC ("Could this pattern be coincidence?")
- AGENT 04: FIRST-PRINCIPLES ANALYST ("What mechanism explains this?")
- AGENT 05: SYNTHESIZER ("What can we responsibly say?")
"""

import streamlit as st
import json
from typing import List, Dict, Any
from data.agents_data import AGENTS_METADATA


def render_agent_orchestrator(traces: List[Dict[str, Any]]):
    """
    Renders the interactive 5-agent execution workflow.
    """
    st.markdown(
        """
        <div style="background: #0f172a; border: 1px solid #1e293b; border-radius: 8px; padding: 18px 20px; margin-bottom: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center;">
                <div>
                    <span style="font-family: 'JetBrains Mono'; font-size: 0.72rem; color: #38bdf8; text-transform: uppercase;">
                        AGENT ORCHESTRATION CONSOLE // 5 RE-ACT WORKFLOWS
                    </span>
                    <h3 style="font-family: 'JetBrains Mono'; font-size: 1.1rem; color: #f8fafc; margin: 4px 0 0 0;">
                        Autonomous Investigative Pipeline
                    </h3>
                </div>
                <div style="background: rgba(56, 189, 248, 0.1); border: 1px solid rgba(56, 189, 248, 0.3); padding: 4px 10px; border-radius: 4px;">
                    <span style="font-family: 'JetBrains Mono'; font-size: 0.75rem; color: #38bdf8;">SIMULATED LOCAL EXECUTION</span>
                </div>
            </div>
            <p style="font-size: 0.84rem; color: #94a3b8; margin: 8px 0 0 0;">
                Demonstrates how specialized AI agents use structured tools and epistemic bounds to investigate launch distribution without blind chat prompt hallucination.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Agent selection pills or step tabs
    agent_names = [f"{a['name'].split('—')[1].strip()} ({a['question']})" for a in AGENTS_METADATA]
    selected_idx = st.radio(
        "Select Agent Inspection View:",
        range(len(AGENTS_METADATA)),
        format_func=lambda i: agent_names[i],
        horizontal=True,
        key="agent_radio_select"
    )

    agent_meta = AGENTS_METADATA[selected_idx]
    trace = traces[selected_idx] if selected_idx < len(traces) else {}

    st.markdown(
        f"""
        <div style="background: #111827; border: 1px solid #1f2937; border-radius: 8px; padding: 20px; margin-top: 14px;">
            <!-- Agent Header -->
            <div style="display: flex; justify-content: space-between; align-items: flex-start; border-bottom: 1px solid #1f2937; padding-bottom: 14px; margin-bottom: 16px;">
                <div>
                    <span style="font-family: 'JetBrains Mono'; font-size: 0.75rem; color: {agent_meta['color']}; font-weight: 700;">
                        {agent_meta['name']}
                    </span>
                    <h4 style="font-family: 'JetBrains Mono'; font-size: 1.05rem; color: #f8fafc; margin: 4px 0 2px 0;">
                        Core Question: "{agent_meta['question']}"
                    </h4>
                    <span style="font-size: 0.82rem; color: #94a3b8;">{agent_meta['purpose']}</span>
                </div>
                <div style="text-align: right;">
                    <span style="font-family: 'JetBrains Mono'; font-size: 0.7rem; color: #64748b; display: block;">EPISTEMIC BOUND</span>
                    <span style="font-family: 'JetBrains Mono'; font-size: 0.8rem; font-weight: 700; color: {agent_meta['color']};">{agent_meta['epistemic_tag']}</span>
                </div>
            </div>

            <!-- Tools Bound to Agent -->
            <div style="margin-bottom: 18px;">
                <span style="font-family: 'JetBrains Mono'; font-size: 0.72rem; color: #64748b; text-transform: uppercase;">
                    Bound Tools (Parallels ARIS Agent Architecture):
                </span>
                <div style="margin-top: 6px;">
                    {" ".join([f"<code style='background: #1e293b; color: #cbd5e1; padding: 2px 6px; border-radius: 3px; font-size: 0.75rem; margin-right: 6px;'>{t}()</code>" for t in agent_meta['tools']])}
                </div>
            </div>

            <!-- ReAct Cycle Box -->
            <div style="display: flex; flex-direction: column; gap: 12px; font-family: 'JetBrains Mono'; font-size: 0.83rem;">
                <div style="background: #0f172a; border-left: 3px solid #38bdf8; padding: 10px 14px; border-radius: 0 4px 4px 0;">
                    <span style="color: #38bdf8; font-weight: 600; text-transform: uppercase; font-size: 0.72rem;">Thought:</span>
                    <div style="color: #e2e8f0; margin-top: 4px;">{trace.get('thought', 'Analyzing input parameters...')}</div>
                </div>

                <div style="background: #0f172a; border-left: 3px solid #a855f7; padding: 10px 14px; border-radius: 0 4px 4px 0;">
                    <span style="color: #a855f7; font-weight: 600; text-transform: uppercase; font-size: 0.72rem;">Action:</span>
                    <div style="color: #e2e8f0; margin-top: 4px;"><code>{trace.get('action', 'inspect()')}</code></div>
                </div>

                <div style="background: #0f172a; border-left: 3px solid #22c55e; padding: 10px 14px; border-radius: 0 4px 4px 0;">
                    <span style="color: #22c55e; font-weight: 600; text-transform: uppercase; font-size: 0.72rem;">Observation:</span>
                    <div style="color: #e2e8f0; margin-top: 4px;">{trace.get('observation', 'Completed query execution.')}</div>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Structured JSON output toggle
    with st.expander(f"View Structured JSON Output from {agent_meta['name']}", expanded=True):
        st.json(trace.get("structured_output", {}))
