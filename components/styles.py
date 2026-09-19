"""
Custom CSS and design system tokens for LAUNCH//REVERSE.
Theme: 'Research terminal meets modern product studio'
- Monospace accents (Fira Code, JetBrains Mono, SF Mono)
- High-contrast slate backgrounds (#090d16, #111827, #1f2937)
- Strict color-coded epistemic tags (OBSERVED, INFERRED, HYPOTHESIS, SIMULATED)
"""

TERMINAL_CSS = """
<style>
/* Global Streamlit overrides for research terminal aesthetic */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
}

.stApp {
    background-color: #0b0f19;
    color: #e2e8f0;
}

/* Monospace font for tags, code, headers */
.mono-font {
    font-family: 'JetBrains Mono', monospace;
}

/* Epistemic Badges */
.badge {
    display: inline-block;
    padding: 3px 8px;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
    text-transform: uppercase;
    margin-right: 6px;
    margin-bottom: 4px;
}

.badge-observed {
    background-color: rgba(34, 197, 94, 0.12);
    color: #4ade80;
    border: 1px solid rgba(34, 197, 94, 0.35);
}

.badge-inferred {
    background-color: rgba(56, 189, 248, 0.12);
    color: #38bdf8;
    border: 1px solid rgba(56, 189, 248, 0.35);
}

.badge-hypothesis {
    background-color: rgba(245, 158, 11, 0.12);
    color: #fbbf24;
    border: 1px solid rgba(245, 158, 11, 0.35);
}

.badge-simulated {
    background-color: rgba(168, 85, 247, 0.12);
    color: #c084fc;
    border: 1px solid rgba(168, 85, 247, 0.35);
}

.badge-counter {
    background-color: rgba(244, 63, 94, 0.12);
    color: #fb7185;
    border: 1px solid rgba(244, 63, 94, 0.35);
}

/* Research Terminal Cards */
.terminal-card {
    background: #111827;
    border: 1px solid #1f2937;
    border-radius: 6px;
    padding: 18px 20px;
    margin-bottom: 16px;
    transition: border-color 0.2s ease;
}

.terminal-card:hover {
    border-color: #374151;
}

.card-title {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.95rem;
    font-weight: 600;
    color: #f8fafc;
    letter-spacing: -0.01em;
    margin-bottom: 6px;
}

/* Metric Display Box */
.stat-box {
    background: #0f172a;
    border: 1px solid #1e293b;
    border-radius: 6px;
    padding: 12px 16px;
    text-align: left;
}

.stat-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    color: #94a3b8;
    text-transform: uppercase;
    letter-spacing: 0.05em;
}

.stat-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 1.35rem;
    font-weight: 700;
    color: #f1f5f9;
    margin-top: 4px;
}

/* Banner disclaimer */
.disclaimer-banner {
    background: rgba(15, 23, 42, 0.8);
    border-left: 3px solid #f59e0b;
    padding: 10px 14px;
    border-radius: 0 4px 4px 0;
    margin-bottom: 18px;
    font-size: 0.82rem;
    color: #cbd5e1;
    font-family: 'JetBrains Mono', monospace;
}

.hero-box {
    background: linear-gradient(180deg, #111827 0%, #0d121f 100%);
    border: 1px solid #1f2937;
    border-radius: 8px;
    padding: 24px 28px;
    margin-bottom: 24px;
}

/* Streamlit button custom styles */
div.stButton > button {
    background-color: #1e293b;
    color: #f1f5f9;
    border: 1px solid #334155;
    border-radius: 4px;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.85rem;
    padding: 8px 16px;
    transition: all 0.15s ease;
}

div.stButton > button:hover {
    background-color: #334155;
    border-color: #64748b;
    color: #ffffff;
}

/* Selectbox and Input styling */
div[data-baseweb="select"] {
    background-color: #111827 !important;
}

/* Custom divider */
.terminal-divider {
    border-top: 1px solid #1f2937;
    margin: 20px 0;
}
</style>
"""

def get_badge_html(tag_type: str, label: str) -> str:
    """Generate HTML string for epistemic badges."""
    type_map = {
        "OBSERVED": "badge-observed",
        "INFERRED": "badge-inferred",
        "HYPOTHESIS": "badge-hypothesis",
        "SIMULATED": "badge-simulated",
        "COUNTEREVIDENCE": "badge-counter",
        "CONCEPTUAL": "badge-inferred",
    }
    css_class = type_map.get(tag_type.upper(), "badge-observed")
    return f'<span class="badge {css_class}">{label}</span>'
