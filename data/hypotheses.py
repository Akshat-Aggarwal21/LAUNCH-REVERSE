"""
Hypotheses dataset and Skeptic Agent counterevidence repository for LAUNCH//REVERSE.
Implements the core 'Evidence vs Hypothesis' pipeline and 'Why This Insight?' inspector data.
"""

from typing import List, Dict, Any

HYPOTHESES_DATA: List[Dict[str, Any]] = [
    {
        "id": "HYP-01",
        "title": "Early Founder Narrative Contextualizes Later Product Distribution",
        "category": "Founder-led narrative",
        "observation": "Founder-led posts appear early in 4 of 6 simulated launch sequences (Day -7 to Day -5) prior to official product announcements.",
        "supporting_artifacts_count": 7,
        "supporting_launch_sequences": 4,
        "supporting_author_types": 3,
        "evidence_summary": "In both Wispr Flow and Gamma sequences, high-engagement posts by founders appeared 5 to 7 days before the launch day, focusing on the fundamental problem ('Typing is unnatural', 'PowerPoint is cognitive waste') rather than product feature lists.",
        "hypothesis_mechanism": "Founder participation may establish emotional and philosophical narrative tension before technical or product-focused distribution. This prepares the audience's mental model so that the subsequent product release feels like an inevitable answer to an acknowledged problem.",
        "counterevidence": "2 simulated launches did not use founder-led posts prior to launch; they relied exclusively on anonymous corporate handles and immediate demo clips without prior narrative build-up.",
        "counterevidence_exceptions_count": 2,
        "assumptions": [
            "Public social posts reflect intentional pre-launch strategy rather than random ad-hoc musings.",
            "Engagement on founder posts was organic rather than boosted through paid influencer syndication.",
            "Audience overlap exists between early thread readers and Day 0 adopters."
        ],
        "skeptic_critique": "Correlation is not causation. We have no access to private conversion funnel data to prove that users who engaged with Day -7 founder threads actually converted on Day 0. The founder posts may simply reflect high personal follower counts rather than an effective distribution mechanic.",
        "confidence_level": "MEDIUM",
        "status": "Needs more data",
        "next_data_required": "Attribution telemetry or UTM-tagged links linking pre-launch readers to Day 0 signups, plus comparative cohorts of launches without founder posts.",
        "tags": ["Founder Distribution", "Pre-launch", "Narrative Framing"]
    },
    {
        "id": "HYP-02",
        "title": "Creator Amplification Drives Volume, But Depends on Prior Product Proof",
        "category": "Creator amplification",
        "observation": "High-reach creator posts cluster tightly on Day 0 and Day +1, generating over 60% of total recorded public view impressions.",
        "supporting_artifacts_count": 8,
        "supporting_launch_sequences": 3,
        "supporting_author_types": 2,
        "evidence_summary": "Creator posts (e.g. Sam Parr, Rowan Cheung, Ali Abdaal) recorded massive engagement (400k-800k views each) immediately following the launch announcement.",
        "hypothesis_mechanism": "Third-party creators act as top-of-funnel velocity multipliers by translating technical product claims into relatable, consumer-friendly use cases ('Drafted 1,500 words in 6 minutes walking').",
        "counterevidence": "Multiple high-performing artifacts occurred BEFORE creator involvement. Furthermore, some creator posts yielded superficial video views with minimal demonstrable downstream retention or product usage.",
        "counterevidence_exceptions_count": 3,
        "assumptions": [
            "View count on social platforms corresponds to meaningful brand consideration.",
            "Creator endorsements were interpreted as authentic rather than dismissed as paid sponsorships.",
            "The product was already stable enough to absorb sudden traffic spikes without high churn."
        ],
        "skeptic_critique": "Insufficient evidence to claim creator amplification is the primary driver of product success. Creator reach creates vanity impression spikes, but without retention data, we cannot establish whether creator distribution builds sustainable user bases or temporary noise.",
        "confidence_level": "LOW",
        "status": "Plausible but unverified",
        "next_data_required": "Day 7 and Day 30 user retention cohorts segmented by acquisition source (Founder referral vs Creator video vs Product Hunt direct).",
        "tags": ["Creator Economy", "Amplification", "Top of Funnel"]
    },
    {
        "id": "HYP-03",
        "title": "High-Velocity Video Demos Outperform Static Screenshots in Pre-Launch Teasers",
        "category": "Product demonstration",
        "observation": "Screencast video demos under 30 seconds average 3.2x higher interaction-to-view ratios compared to static UI screenshots during the teaser phase (Day -5 to Day -1).",
        "supporting_artifacts_count": 6,
        "supporting_launch_sequences": 3,
        "supporting_author_types": 2,
        "evidence_summary": "Wispr Flow's 200ms latency split-screen and Gamma's 28-second prompt-to-deck screencast each crossed 200k-400k views with high bookmark rates prior to public availability.",
        "hypothesis_mechanism": "In an AI market flooded with marketing promises, short continuous-take videos provide verifiable 'product proof' that collapses skepticism and triggers waitlist FOMO.",
        "counterevidence": "OmniContext AI's static graph screenshot achieved comparable engagement with significantly lower production cost, suggesting the novelty of the visual graph itself drove curiosity regardless of animation.",
        "counterevidence_exceptions_count": 1,
        "assumptions": [
            "Video content was not boosted by platform algorithm bias favoring video formats over images.",
            "Viewers watched the entire 30-second demonstration rather than scrolling past on autoplay."
        ],
        "skeptic_critique": "Platform algorithms on X and LinkedIn heavily prioritize native video in their recommendation feeds. The 3.2x interaction ratio may be an artifact of algorithmic delivery preferences rather than user demand for video proof.",
        "confidence_level": "MEDIUM",
        "status": "Needs more data",
        "next_data_required": "A/B testing of static vs video assets within identical audience segments, controlling for algorithmic feed weighting.",
        "tags": ["Product Proof", "Video Demos", "Visual Distribution"]
    },
    {
        "id": "HYP-04",
        "title": "Contrarian Problem-First Hooks Generate Higher Retweet/Share Quotients",
        "category": "Contrarian hook",
        "observation": "Artifacts employing contrarian hooks ('Typing is unnatural', 'PowerPoint is broken') generate 48% more shares/retweets than feature-descriptive hooks.",
        "supporting_artifacts_count": 5,
        "supporting_launch_sequences": 3,
        "supporting_author_types": 3,
        "evidence_summary": "Opening statements attacking legacy habits create debate in comments, turning readers into active participants who quote-tweet to express their own stance.",
        "hypothesis_mechanism": "Contrarian framing creates social currency: sharing an attack on an outdated tool (like PowerPoint or typing) signals modern technological sophistication for the sharer.",
        "counterevidence": "Contrarian framing can attract polarized backlash that distorts engagement metrics without converting into product advocates. Negative comments inflate engagement count identically to positive interest.",
        "counterevidence_exceptions_count": 2,
        "assumptions": [
            "High share volume indicates brand resonance rather than outrage-baiting.",
            "Users who share ideological opinions about typing/slides are prospective software buyers."
        ],
        "skeptic_critique": "Outrage and debate on social media generate high interaction counts that rarely correlate with software buying intent. Equating quote-tweet debates with launch traction is an elementary attribution error.",
        "confidence_level": "LOW",
        "status": "Needs more data",
        "next_data_required": "Sentiment analysis separating positive endorsement from critical debate, paired with down-funnel product activation rates.",
        "tags": ["Contrarian Hook", "Social Currency", "Narrative Tension"]
    }
]


# Lookup dictionary for the interactive "Test a Hypothesis" sandbox
PRESET_HYPOTHESES_SANDBOX = {
    "Founder-led narrative": {
        "title": "Founder-led narrative drives higher Day 0 conversion than corporate handle posts",
        "evidence": [
            "4 of 6 simulated launches contain founder-led narrative posts before the main announcement.",
            "Founder posts average 2.4x higher comment engagement than brand account announcements.",
            "Founders who articulate personal pain points generate stronger emotional resonance in early beta circles."
        ],
        "counterevidence": [
            "2 simulated launches achieved top-tier product status using purely corporate channels and creator partnerships.",
            "Founder visibility without strong underlying product utility results in high churn post-launch.",
            "Founder brand value does not scale automatically to non-technical or enterprise buyers."
        ],
        "mechanism": "Founder participation establishes human credibility and narrative context before commercial intent is declared, reducing cognitive resistance to marketing.",
        "confidence": "MEDIUM",
        "assumptions": [
            "Audience perceives founder as authentic rather than PR-coached.",
            "Founder already has an active or receptive baseline follower network."
        ],
        "skeptic_verdict": "Plausible contextual factor, but unsupported as an absolute rule. Confounding factor: Many founders already possess high preexisting social capital.",
        "next_data_required": "Controlled comparison of founder-led vs brand-led launches across companies with identical initial follower counts."
    },
    "Creator amplification": {
        "title": "Creator amplification is the single decisive catalyst for launch day reach",
        "evidence": [
            "Creator posts contribute over 60% of total viral impression peaks on Day 0 and Day +1.",
            "Creator video demonstrations show higher completion rates than generic software ad trailers.",
            "Creators introduce the product to adjacent non-early-adopter audiences."
        ],
        "counterevidence": [
            "Significant user signups and viral momentum existed in closed beta before any creator posted.",
            "Creator reach often produces short-lived curiosity spikes rather than lasting retained users.",
            "Correlation with reach does not equate to correlation with active weekly users."
        ],
        "mechanism": "Creators serve as trusted curators who lower the evaluation threshold for new software by showing real-world workflows.",
        "confidence": "LOW",
        "assumptions": [
            "Views reported by platforms represent actual human impressions.",
            "Creator audiences match the ideal customer profile for the product."
        ],
        "skeptic_verdict": "Insufficient evidence. Creator amplification accelerates distribution of an already-sticky product, but cannot create product-market fit independently.",
        "next_data_required": "Attribution modeling tracking user retention at 14 and 30 days based on specific creator referral parameters."
    },
    "Product demonstration": {
        "title": "Continuous-take video demonstrations are mandatory to overcome AI skepticism",
        "evidence": [
            "Video demonstrations achieve 3.2x higher bookmark rates than static product UI screenshots.",
            "Screen recordings with visible cursor and typing speed validate latency claims transparently.",
            "Viewers share demonstrations that show end-to-end execution of complex tasks in seconds."
        ],
        "counterevidence": [
            "High-concept static architectural diagrams and knowledge graphs also achieved viral reach in technical communities.",
            "Video editing and AI generation are increasingly suspected of fabrication unless audited."
        ],
        "mechanism": "Tangible visual proof lowers skepticism by demonstrating software responsiveness in an era of vaporware marketing.",
        "confidence": "MEDIUM",
        "assumptions": [
            "Audiences believe video captures are genuine, unedited real-time recordings.",
            "The demonstrated feature represents typical rather than edge-case performance."
        ],
        "skeptic_verdict": "Strong empirical correlation with immediate user attention, but algorithmic feed bias toward video formats accounts for a large portion of the metric differential.",
        "next_data_required": "Log-file audits of user session recording duration compared with the specific video features they viewed."
    },
    "Contrarian hook": {
        "title": "Contrarian framing creates sustainable competitive differentiation",
        "evidence": [
            "Attacking incumbent conventions ('Typing is obsolete', 'Slides are dead') generates 48% higher quote-tweet rates.",
            "Debate in comments increases social algorithmic distribution by triggering replies."
        ],
        "counterevidence": [
            "Outrage engagement frequently produces negative brand sentiment and attracting adversarial scrutiny.",
            "Many software buyers prefer boring, reliable tools over ideological manifestos."
        ],
        "mechanism": "Positioning against a widely acknowledged friction point allows a new product to define itself by opposition rather than feature checklists.",
        "confidence": "LOW",
        "assumptions": [
            "Negative or contentious replies represent productive brand awareness.",
            "The product can fulfill the bold contrarian claim without disappointing users."
        ],
        "skeptic_verdict": "High risk of false-positive evaluation. High engagement from internet arguments does not translate into qualified commercial adoption.",
        "next_data_required": "Sentiment-stratified conversion analysis measuring actual signups originating from debate threads."
    }
}
