"""
Plotly data visualization components for LAUNCH//REVERSE.
Includes:
- Launch Timeline track (Day -7 to Day +3 with author-type coloring and engagement bubbles)
- Launch DNA 8-dimensional Radar Chart
- Hook & Phase Distribution Bar Charts
"""

from typing import Dict, Any, List
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px


# Color palette for terminal charts
SLATE_THEME = {
    "bg_color": "#0b0f19",
    "paper_color": "#111827",
    "grid_color": "#1f2937",
    "text_color": "#94a3b8",
    "accent_cyan": "#38bdf8",
    "accent_emerald": "#22c55e",
    "accent_amber": "#f59e0b",
    "accent_purple": "#a855f7",
    "accent_rose": "#f43f5e"
}

AUTHOR_COLORS = {
    "Founder": "#38bdf8",         # Cyan
    "Core Team": "#818cf8",       # Indigo
    "Creator": "#f59e0b",         # Amber
    "Tech Influencer": "#a855f7", # Purple
    "Early Adopter": "#22c55e"    # Emerald
}


def build_timeline_figure(df: pd.DataFrame) -> go.Figure:
    """
    Creates an interactive chronological timeline track from Day -7 to Day +3.
    """
    fig = go.Figure()

    # Base line across days
    min_day = df["day_offset"].min()
    max_day = df["day_offset"].max()
    fig.add_shape(
        type="line",
        x0=min_day - 0.5,
        y0=0,
        x1=max_day + 0.5,
        y1=0,
        line=dict(color="#334155", width=2, dash="dot")
    )

    # Launch Day (Day 0) milestone vertical marker
    fig.add_shape(
        type="line",
        x0=0,
        y0=-1.5,
        x1=0,
        y1=2.5,
        line=dict(color="#f59e0b", width=1.5, dash="dash")
    )
    fig.add_annotation(
        x=0,
        y=2.6,
        text="LAUNCH DAY (DAY 0)",
        showarrow=False,
        font=dict(family="JetBrains Mono", size=10, color="#fbbf24")
    )

    # Plot events by author type
    for author_type, color in AUTHOR_COLORS.items():
        sub = df[df["author_type"] == author_type]
        if sub.empty:
            continue

        # Jitter y slightly based on launch phase for visual clarity
        y_offsets = []
        phase_map = {
            "Pre-launch": -0.6,
            "Teaser": -0.2,
            "Launch Day": 1.2,
            "Post-launch Amplification": 0.6,
            "Proof & Defense": -0.4
        }
        for _, row in sub.iterrows():
            y_offsets.append(phase_map.get(row["launch_phase"], 0.2))

        # Bubble size scaled to interaction count (min 14, max 32)
        sizes = [max(12, min(32, int(val / 350) + 12)) for val in sub["engagement_interactions"]]

        hover_texts = []
        for _, r in sub.iterrows():
            txt = (
                f"<b>{r['id']} — {r['author']}</b> ({r['author_type']})<br>"
                f"<b>Day:</b> {r['day_label']} | <b>Platform:</b> {r['platform']}<br>"
                f"<b>Hook:</b> {r['hook_type']}<br>"
                f"<b>Narrative:</b> {r['narrative'][:60]}...<br>"
                f"<b>Interactions:</b> {r['engagement_interactions']:,} | <b>Views:</b> {r['engagement_views']:,}<br>"
                f"<b>Status:</b> {r['epistemic_status']}"
            )
            hover_texts.append(txt)

        fig.add_trace(go.Scatter(
            x=sub["day_offset"],
            y=y_offsets,
            mode="markers+text",
            name=author_type,
            marker=dict(
                size=sizes,
                color=color,
                opacity=0.88,
                line=dict(width=1.5, color="#ffffff")
            ),
            text=sub["id"],
            textposition="top center",
            textfont=dict(family="JetBrains Mono", size=9, color="#cbd5e1"),
            hoverinfo="text",
            hovertext=hover_texts
        ))

    fig.update_layout(
        title=dict(
            text="CHRONOLOGICAL LAUNCH SEQUENCE (DAY -7 TO DAY +3)",
            font=dict(family="JetBrains Mono", size=13, color="#f1f5f9")
        ),
        xaxis=dict(
            title="Launch Timeline Days",
            tickmode="linear",
            tick0=min_day,
            dtick=1,
            gridcolor=SLATE_THEME["grid_color"],
            zerolinecolor=SLATE_THEME["grid_color"],
            color=SLATE_THEME["text_color"],
            tickfont=dict(family="JetBrains Mono", size=10)
        ),
        yaxis=dict(
            showgrid=False,
            zeroline=False,
            showticklabels=False,
            range=[-1.8, 3.0]
        ),
        paper_bgcolor=SLATE_THEME["paper_color"],
        plot_bgcolor=SLATE_THEME["paper_color"],
        height=320,
        margin=dict(l=20, r=20, t=50, b=30),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(family="JetBrains Mono", size=10, color="#94a3b8")
        )
    )

    return fig


def build_launch_dna_radar(dna_profile: Dict[str, Any]) -> go.Figure:
    """
    Renders the 8-dimensional Launch DNA Radar chart.
    """
    dims = dna_profile["dimensions"]
    categories = list(dims.keys())
    values = [v["score"] if isinstance(v, dict) else v for v in dims.values()]
    statuses = [v.get("epistemic_status", "INFERRED") if isinstance(v, dict) else "INFERRED" for v in dims.values()]
    bases = [v.get("calculation_basis", "") if isinstance(v, dict) else "" for v in dims.values()]

    # Close the radar loop
    categories.append(categories[0])
    values.append(values[0])
    statuses.append(statuses[0])
    bases.append(bases[0])

    hover_texts = [
        f"<b>{c}</b>: {val}/100 [{st}]<br><i>Basis:</i> {b}"
        for c, val, st, b in zip(categories, values, statuses, bases)
    ]

    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill="toself",
        fillcolor="rgba(56, 189, 248, 0.20)",
        line=dict(color="#38bdf8", width=2),
        marker=dict(size=6, color="#38bdf8"),
        name=dna_profile["company_name"],
        hoverinfo="text",
        hovertext=hover_texts
    ))

    fig.update_layout(
        polar=dict(
            bgcolor="#0f172a",
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                tickfont=dict(family="JetBrains Mono", size=9, color="#64748b"),
                gridcolor="#1e293b",
                linecolor="#1e293b"
            ),
            angularaxis=dict(
                tickfont=dict(family="JetBrains Mono", size=10, color="#cbd5e1"),
                gridcolor="#1e293b",
                linecolor="#1e293b"
            )
        ),
        paper_bgcolor=SLATE_THEME["paper_color"],
        height=340,
        margin=dict(l=35, r=35, t=30, b=30),
        showlegend=False
    )

    return fig


def build_hook_distribution_bar(df: pd.DataFrame) -> go.Figure:
    """
    Bar chart of hook types distribution across the launch artifacts.
    """
    counts = df["hook_type"].value_counts().reset_index()
    counts.columns = ["hook_type", "count"]

    fig = px.bar(
        counts,
        x="hook_type",
        y="count",
        text="count",
        color="hook_type",
        color_discrete_sequence=["#38bdf8", "#818cf8", "#f59e0b", "#22c55e", "#a855f7"]
    )

    fig.update_traces(
        textfont=dict(family="JetBrains Mono", size=11, color="#ffffff"),
        textposition="outside"
    )

    fig.update_layout(
        title=dict(
            text="HOOK TYPE FREQUENCY IN ARTIFACTS",
            font=dict(family="JetBrains Mono", size=12, color="#f1f5f9")
        ),
        xaxis=dict(
            title="",
            gridcolor=SLATE_THEME["grid_color"],
            color=SLATE_THEME["text_color"],
            tickfont=dict(family="JetBrains Mono", size=9)
        ),
        yaxis=dict(
            title="Artifact Count",
            gridcolor=SLATE_THEME["grid_color"],
            color=SLATE_THEME["text_color"],
            tickfont=dict(family="JetBrains Mono", size=9)
        ),
        paper_bgcolor=SLATE_THEME["paper_color"],
        plot_bgcolor=SLATE_THEME["paper_color"],
        height=240,
        margin=dict(l=20, r=20, t=40, b=20),
        showlegend=False
    )

    return fig
