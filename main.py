import streamlit as st

# ── Page config ────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FitSync · Main",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
  @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap');

  /* ── Reset & base ── */
  html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
  }
  .stApp {
    background: #080c14;
  }

  /* ── Hide Streamlit chrome ── */
  #MainMenu, footer, header { visibility: hidden; }
  .block-container {
    padding: 0 2.5rem 4rem 2.5rem;
    max-width: 1200px;
  }

  /* ── Typography helpers ── */
  .display-tag {
    font-family: 'Syne', sans-serif;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.25em;
    text-transform: uppercase;
    color: #00e5ff;
  }
  .hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.8rem, 6vw, 5rem);
    font-weight: 800;
    line-height: 1.05;
    color: #f0f6ff;
    margin: 0.4rem 0 1.2rem 0;
  }
  .hero-title span {
    background: linear-gradient(90deg, #00e5ff 0%, #00bcd4 60%, #7c4dff 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
  }
  .hero-sub {
    font-size: 1.15rem;
    font-weight: 300;
    color: #8fa8c8;
    line-height: 1.75;
    max-width: 580px;
  }

  /* ── Divider ── */
  .neon-divider {
    height: 2px;
    background: linear-gradient(90deg, #00e5ff33, #00e5ff, #7c4dff, #7c4dff33);
    border: none;
    margin: 0.5rem 0 2.5rem 0;
    border-radius: 2px;
  }

  /* ── Metric cards ── */
  .metric-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1rem;
    margin: 2rem 0 3rem 0;
  }
  .metric-card {
    background: linear-gradient(145deg, #0d1829 0%, #111c2f 100%);
    border: 1px solid #1c2e48;
    border-radius: 16px;
    padding: 1.4rem 1.2rem;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s ease, border-color 0.2s ease;
  }
  .metric-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 3px;
    background: var(--accent);
    border-radius: 16px 16px 0 0;
  }
  .metric-card:hover {
    transform: translateY(-4px);
    border-color: #2a3f5f;
  }
  .metric-icon {
    font-size: 1.7rem;
    margin-bottom: 0.65rem;
    display: block;
  }
  .metric-label {
    font-family: 'Syne', sans-serif;
    font-size: 0.75rem;
    font-weight: 600;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #4a6a8a;
    margin-bottom: 0.3rem;
  }
  .metric-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #d6eaff;
    margin-bottom: 0.4rem;
  }
  .metric-desc {
    font-size: 0.82rem;
    color: #5a7a9a;
    line-height: 1.55;
  }

  /* ── Benefits section ── */
  .section-title {
    font-family: 'Syne', sans-serif;
    font-size: 1.8rem;
    font-weight: 800;
    color: #f0f6ff;
    margin-bottom: 0.3rem;
  }
  .section-subtitle {
    font-size: 0.95rem;
    color: #607d9a;
    margin-bottom: 2rem;
  }
  .benefit-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 1.1rem;
  }
  .benefit-card {
    background: #0b1422;
    border: 1px solid #182236;
    border-radius: 14px;
    padding: 1.5rem 1.3rem;
    display: flex;
    gap: 1rem;
    align-items: flex-start;
    transition: background 0.2s ease;
  }
  .benefit-card:hover {
    background: #0f1a2e;
  }
  .benefit-icon-wrap {
    background: var(--icon-bg);
    border-radius: 10px;
    width: 42px;
    height: 42px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.2rem;
    flex-shrink: 0;
  }
  .benefit-body h4 {
    font-family: 'Syne', sans-serif;
    font-size: 0.92rem;
    font-weight: 700;
    color: #c8dff5;
    margin: 0 0 0.3rem 0;
  }
  .benefit-body p {
    font-size: 0.82rem;
    color: #4e6880;
    line-height: 1.6;
    margin: 0;
  }

  /* ── CTA banner ── */
  .cta-banner {
    background: linear-gradient(135deg, #0e1e35 0%, #0d1a30 50%, #12102a 100%);
    border: 1px solid #1e2e48;
    border-radius: 18px;
    padding: 2.5rem 3rem;
    display: flex;
    align-items: center;
    justify-content: space-between;
    margin-top: 3rem;
    gap: 2rem;
  }
  .cta-text h3 {
    font-family: 'Syne', sans-serif;
    font-size: 1.4rem;
    font-weight: 800;
    color: #f0f6ff;
    margin: 0 0 0.4rem 0;
  }
  .cta-text p {
    font-size: 0.9rem;
    color: #5a7a9a;
    margin: 0;
  }
  .cta-pills {
    display: flex;
    gap: 0.6rem;
    flex-wrap: wrap;
    justify-content: flex-end;
  }
  .pill {
    background: linear-gradient(90deg, #00b8d4 0%, #7c4dff 100%);
    color: #fff;
    font-family: 'Syne', sans-serif;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    padding: 0.45rem 1.1rem;
    border-radius: 100px;
    white-space: nowrap;
  }
  .pill.outline {
    background: transparent;
    border: 1px solid #1e3050;
    color: #4a7aaa;
  }

  /* ── Streamlit native dark overrides ── */

  /* Sidebar */
  [data-testid="stSidebar"] {
    background: #060a11 !important;
    border-right: 1px solid #111e33 !important;
  }
  [data-testid="stSidebar"] * {
    color: #7a9abf !important;
  }
  [data-testid="stSidebar"] a:hover,
  [data-testid="stSidebar"] [aria-selected="true"] {
    color: #00e5ff !important;
    background: #0d1829 !important;
  }
  [data-testid="stSidebarNav"] {
    background: transparent !important;
  }

  /* Top header bar */
  [data-testid="stHeader"] {
    background: #060a11 !important;
    border-bottom: 1px solid #111e33 !important;
  }

  /* Toolbar / top-right buttons */
  [data-testid="stToolbar"] {
    background: transparent !important;
  }

  /* Main content background */
  [data-testid="stAppViewContainer"] {
    background: #080c14 !important;
  }
  [data-testid="stMain"] {
    background: #080c14 !important;
  }

  /* Default text */
  p, li, span, label, div {
    color: #8fa8c8;
  }

  /* Streamlit markdown text */
  .stMarkdown p {
    color: #8fa8c8;
  }

  /* Buttons */
  .stButton > button {
    background: linear-gradient(90deg, #00b8d4 0%, #7c4dff 100%) !important;
    color: #fff !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 700 !important;
    letter-spacing: 0.06em !important;
    transition: opacity 0.2s ease !important;
  }
  .stButton > button:hover {
    opacity: 0.85 !important;
  }

  /* Select boxes, text inputs */
  .stSelectbox > div > div,
  .stTextInput > div > div > input,
  .stNumberInput > div > div > input,
  .stTextArea > div > div > textarea {
    background: #0d1829 !important;
    border: 1px solid #1c2e48 !important;
    color: #d6eaff !important;
    border-radius: 8px !important;
  }
  .stSelectbox > div > div:focus-within,
  .stTextInput > div > div > input:focus,
  .stTextArea > div > div > textarea:focus {
    border-color: #00e5ff !important;
    box-shadow: 0 0 0 2px #00e5ff22 !important;
  }

  /* Slider */
  .stSlider [data-baseweb="slider"] div[role="slider"] {
    background: #00e5ff !important;
  }
  .stSlider [data-baseweb="track"] div {
    background: #1c2e48 !important;
  }

  /* Checkbox & radio */
  .stCheckbox label span,
  .stRadio label span {
    color: #8fa8c8 !important;
  }

  /* Metric widgets */
  [data-testid="stMetric"] {
    background: #0d1829 !important;
    border: 1px solid #1c2e48 !important;
    border-radius: 12px !important;
    padding: 1rem !important;
  }
  [data-testid="stMetricValue"] {
    color: #00e5ff !important;
  }
  [data-testid="stMetricLabel"] {
    color: #4a6a8a !important;
  }
  [data-testid="stMetricDelta"] svg { fill: #69f0ae; }

  /* Dataframe / table */
  [data-testid="stDataFrame"] {
    background: #0d1829 !important;
    border: 1px solid #1c2e48 !important;
    border-radius: 10px !important;
    overflow: hidden;
  }
  .dvn-scroller { background: #0d1829 !important; }

  /* Expander */
  [data-testid="stExpander"] {
    background: #0d1829 !important;
    border: 1px solid #1c2e48 !important;
    border-radius: 10px !important;
  }
  [data-testid="stExpander"] summary {
    color: #8fa8c8 !important;
  }

  /* Alert / info boxes */
  [data-testid="stAlert"] {
    background: #0d1829 !important;
    border-left-color: #00e5ff !important;
    color: #8fa8c8 !important;
    border-radius: 8px !important;
  }

  /* Scrollbar */
  ::-webkit-scrollbar { width: 6px; height: 6px; }
  ::-webkit-scrollbar-track { background: #080c14; }
  ::-webkit-scrollbar-thumb {
    background: #1c2e48;
    border-radius: 10px;
  }
  ::-webkit-scrollbar-thumb:hover { background: #2a3f5f; }

  /* ── Responsive ── */
  @media (max-width: 900px) {
    .metric-grid { grid-template-columns: repeat(2, 1fr); }
    .benefit-grid { grid-template-columns: 1fr; }
    .cta-banner { flex-direction: column; }
    .cta-pills { justify-content: flex-start; }
  }
  @media (max-width: 520px) {
    .metric-grid { grid-template-columns: 1fr; }
  }
</style>
""", unsafe_allow_html=True)

# ── HERO ───────────────────────────────────────────────────────────────────────
st.markdown('<div class="display-tag">⚡ Health Analytics Platform</div>', unsafe_allow_html=True)
st.markdown("""
<h1 class="hero-title">
  Know Your Body.<br>
  <span>Own Your Data.</span>
</h1>
<p class="hero-sub">
  FitSync transforms raw biometric data — steps, heart rate, recovery — into
  clear, actionable insights so you can perform, recover, and live better every day.
</p>
""", unsafe_allow_html=True)

st.markdown('<hr class="neon-divider">', unsafe_allow_html=True)

# ── TRACKED METRICS ────────────────────────────────────────────────────────────
st.markdown('<div class="display-tag" style="margin-bottom:0.8rem;">What We Track</div>', unsafe_allow_html=True)

st.markdown("""
<div class="metric-grid">

  <div class="metric-card" style="--accent:#00e5ff;">
    <span class="metric-icon">👟</span>
    <div class="metric-label">Activity</div>
    <div class="metric-title">Daily Steps</div>
    <div class="metric-desc">Total steps, active minutes, distance traveled, and movement streaks over time.</div>
  </div>

  <div class="metric-card" style="--accent:#ff4081;">
    <span class="metric-icon">❤️</span>
    <div class="metric-label">Cardiovascular</div>
    <div class="metric-title">Heart Rate</div>
    <div class="metric-desc">Resting, active, and peak BPM trends — including heart rate variability (HRV).</div>
  </div>

  <div class="metric-card" style="--accent:#69f0ae;">
    <span class="metric-icon">🔋</span>
    <div class="metric-label">Restoration</div>
    <div class="metric-title">Recovery Rate</div>
    <div class="metric-desc">Post-workout recovery scores, sleep quality, and readiness metrics.</div>
  </div>

  <div class="metric-card" style="--accent:#ffd740;">
    <span class="metric-icon">📊</span>
    <div class="metric-label">Trends</div>
    <div class="metric-title">Performance Index</div>
    <div class="metric-desc">Weekly and monthly composites that reveal patterns invisible in daily snapshots.</div>
  </div>

</div>
""", unsafe_allow_html=True)

# ── BENEFITS SECTION ───────────────────────────────────────────────────────────
st.markdown("""
<div class="section-title">Why Track Your Health Data?</div>
<div class="section-subtitle">The numbers you collect today become the decisions that shape your tomorrow.</div>

<div class="benefit-grid">

  <div class="benefit-card">
    <div class="benefit-icon-wrap" style="--icon-bg:#00e5ff18;">🎯</div>
    <div class="benefit-body">
      <h4>Set Smarter Goals</h4>
      <p>Baseline data reveals where you actually are — not where you think you are — giving goals a realistic foundation.</p>
    </div>
  </div>

  <div class="benefit-card">
    <div class="benefit-icon-wrap" style="--icon-bg:#ff408118;">⚠️</div>
    <div class="benefit-body">
      <h4>Catch Patterns Early</h4>
      <p>Consistent monitoring can surface subtle warning signs — elevated resting HR, poor HRV — before symptoms appear.</p>
    </div>
  </div>

  <div class="benefit-card">
    <div class="benefit-icon-wrap" style="--icon-bg:#69f0ae18;">😴</div>
    <div class="benefit-body">
      <h4>Optimize Recovery</h4>
      <p>Understanding your recovery rate prevents overtraining and ensures each workout builds rather than breaks you down.</p>
    </div>
  </div>

  <div class="benefit-card">
    <div class="benefit-icon-wrap" style="--icon-bg:#ffd74018;">📈</div>
    <div class="benefit-body">
      <h4>Prove Your Progress</h4>
      <p>Objective data removes doubt. Watch your cardiovascular fitness improve in charts, not just in how you feel.</p>
    </div>
  </div>

  <div class="benefit-card">
    <div class="benefit-icon-wrap" style="--icon-bg:#7c4dff18;">🧠</div>
    <div class="benefit-body">
      <h4>Build Accountability</h4>
      <p>Seeing daily metrics logged creates a feedback loop that reinforces healthy habits and discourages regression.</p>
    </div>
  </div>

  <div class="benefit-card">
    <div class="benefit-icon-wrap" style="--icon-bg:#00bcd418;">💬</div>
    <div class="benefit-body">
      <h4>Informed Conversations</h4>
      <p>Bring structured data to your doctor or trainer — turning vague feelings into precise, actionable conversations.</p>
    </div>
  </div>

</div>
""", unsafe_allow_html=True)

# ── CTA BANNER ─────────────────────────────────────────────────────────────────
st.markdown("""
<div class="cta-banner">
  <div class="cta-text">
    <h3>Ready to explore your data?</h3>
    <p>Navigate to any module in the sidebar to dive into your metrics.</p>
  </div>
  <div class="cta-pills">
    <div class="pill">Steps Analysis</div>
    <div class="pill">Heart Rate</div>
    <div class="pill">Recovery</div>
    <div class="pill outline">+ More coming soon</div>
  </div>
</div>
""", unsafe_allow_html=True)