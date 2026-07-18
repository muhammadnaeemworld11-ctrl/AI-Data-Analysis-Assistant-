"""
Premium 3D Luxury Dark Theme for Streamlit
===========================================
Pure CSS injection via st.markdown(unsafe_allow_html=True).
No extra libraries. No JS. Works with Streamlit 1.28+.

Usage:
    from premium_theme import inject_premium_css, apply_chart_theme
    inject_premium_css()

    # When building Plotly figures:
    fig = px.bar(...)
    fig = apply_chart_theme(fig)
    st.plotly_chart(fig)
"""

import streamlit as st


# ---------------------------------------------------------------------------
# 1. CSS INJECTION
# ---------------------------------------------------------------------------

def inject_premium_css() -> None:
    """Inject the full premium 3D luxury dark theme via st.markdown."""

    st.markdown(
        """
        <style>
        /* ================================================================
           0. ANIMATED BACKGROUND — deep dark gradient with mesh overlay
           ================================================================ */
        @keyframes gradientShift {
            0%   { background-position: 0% 0%; }
            50%  { background-position: 100% 100%; }
            100% { background-position: 0% 0%; }
        }

        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #0a0a0f 0%, #111118 50%, #0d0d14 100%);
            background-size: 400% 400%;
            animation: gradientShift 20s ease infinite;
            position: relative;
        }

        /* Subtle radial mesh overlay on top of the gradient */
        [data-testid="stAppViewContainer"]::before {
            content: "";
            position: fixed;
            inset: 0;
            background:
                radial-gradient(ellipse 600px 600px at 20% 30%, rgba(212,175,55,0.04) 0%, transparent 70%),
                radial-gradient(ellipse 500px 500px at 80% 70%, rgba(232,180,184,0.03) 0%, transparent 70%),
                radial-gradient(ellipse 400px 400px at 50% 50%, rgba(212,175,55,0.02) 0%, transparent 70%);
            pointer-events: none;
            z-index: 0;
        }

        /* Ensure main content sits above the overlay */
        .main .block-container {
            position: relative;
            z-index: 1;
        }

        /* ================================================================
           1. HIDE DEFAULT STREAMLIT ELEMENTS
           ================================================================ */
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }

        [data-testid="stHeader"] {
            padding: 0px !important;
            background: rgba(0,0,0,0) !important;
        }

        /* ================================================================
           2. BASE TYPOGRAPHY
           ================================================================ */
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff !important;
            font-family: 'Segoe UI', 'Helvetica Neue', Arial, sans-serif;
        }

        p, span, label, div {
            color: #d0d0dd;
        }

        /* Primary headings — gold with shimmer */
        .main h1,
        .main [data-testid="stTitle"] {
            color: #d4af37 !important;
            text-shadow: 0 0 20px rgba(212,175,55,0.3);
            animation: shimmer 4s ease-in-out infinite;
        }

        .main h2, .main h3 {
            color: #d4af37 !important;
        }

        /* ================================================================
           3. ANIMATIONS
           ================================================================ */
        @keyframes float {
            0%, 100% { transform: translateY(0px); }
            50%      { transform: translateY(-8px); }
        }

        @keyframes shimmer {
            0%   { background-position: -200% center; }
            100% { background-position:  200% center; }
        }

        @keyframes borderRotate {
            0%   { --border-angle: 0deg; }
            100% { --border-angle: 360deg; }
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(12px); }
            to   { opacity: 1; transform: translateY(0); }
        }

        @keyframes glowPulse {
            0%, 100% { box-shadow: 0 0 5px rgba(212,175,55,0.2), inset 0 0 5px rgba(212,175,55,0.05); }
            50%      { box-shadow: 0 0 20px rgba(212,175,55,0.4), inset 0 0 10px rgba(212,175,55,0.1); }
        }

        @keyframes dashSpin {
            to { stroke-dashoffset: -40; }
        }

        @keyframes spinGold {
            0%   { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        /* Apply float to the title / logo area */
        .main [data-testid="stVerticalBlock"]:first-child {
            animation: float 6s ease-in-out infinite;
        }

        /* Fade-in for block sections */
        .main [data-testid="stVerticalBlock"] {
            animation: fadeIn 0.6s ease-out both;
        }
        .main [data-testid="stVerticalBlock"]:nth-child(2) { animation-delay: 0.1s; }
        .main [data-testid="stVerticalBlock"]:nth-child(3) { animation-delay: 0.2s; }
        .main [data-testid="stVerticalBlock"]:nth-child(4) { animation-delay: 0.3s; }
        .main [data-testid="stVerticalBlock"]:nth-child(5) { animation-delay: 0.4s; }
        .main [data-testid="stVerticalBlock"]:nth-child(6) { animation-delay: 0.5s; }

        /* Shimmer on headings via background-clip trick */
        .main h1,
        .main [data-testid="stTitle"] {
            background: linear-gradient(
                90deg,
                #d4af37 0%,
                #f5e6a3 25%,
                #d4af37 50%,
                #f5e6a3 75%,
                #d4af37 100%
            );
            background-size: 200% auto;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmer 4s linear infinite;
        }

        /* ================================================================
           4. CARD BACKGROUNDS — glass-like panels
           ================================================================ */
        .stDataFrame,
        .stDataframe,
        [data-testid="stDataFrame"] {
            background: rgba(255,255,255,0.03) !important;
            border: 1px solid rgba(212,175,55,0.15) !important;
            border-radius: 12px !important;
            overflow: hidden;
            transition: transform 0.4s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                        box-shadow 0.4s ease;
        }

        .stDataFrame:hover,
        .stDataframe:hover,
        [data-testid="stDataFrame"]:hover {
            transform: perspective(1000px) rotateX(2deg);
            box-shadow:
                0 10px 40px rgba(0,0,0,0.5),
                0 0 15px rgba(212,175,55,0.15),
                inset 0 1px 0 rgba(212,175,55,0.1);
        }

        /* Generic card wrapper for most Streamlit blocks */
        [data-testid="stVerticalBlock"],
        [data-testid="stHorizontalBlock"] {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(212,175,55,0.08);
            border-radius: 10px;
            padding: 4px 0;
        }

        /* ================================================================
           5. SIDEBAR — glassmorphism
           ================================================================ */
        [data-testid="stSidebar"] {
            background: rgba(10, 10, 18, 0.85) !important;
            backdrop-filter: blur(20px) !important;
            -webkit-backdrop-filter: blur(20px) !important;
            border-right: 1px solid rgba(212,175,55,0.25) !important;
            box-shadow: 4px 0 30px rgba(0,0,0,0.5);
            padding-top: 20px !important;
        }

        [data-testid="stSidebar"] [data-testid="stSidebarNav"] {
            padding: 0 8px;
        }

        /* Sidebar title */
        [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3 {
            color: #d4af37 !important;
            text-shadow: 0 0 12px rgba(212,175,55,0.2);
        }

        /* Sidebar paragraph / label text */
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] span {
            color: #a0a0b0 !important;
        }

        /* Sidebar radio buttons */
        [data-testid="stSidebar"] [data-testid="stRadio"] {
            background: rgba(255,255,255,0.03) !important;
            border: 1px solid rgba(212,175,55,0.1) !important;
            border-radius: 8px !important;
            padding: 4px 8px !important;
            margin-bottom: 6px !important;
        }

        [data-testid="stSidebar"] [data-testid="stRadio"] label {
            color: #c0c0cc !important;
            transition: color 0.3s ease, text-shadow 0.3s ease;
        }

        [data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
            color: #e8b4b8 !important;
        }

        /* Active radio item — gold glow pulse */
        [data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] {
            background: rgba(212,175,55,0.1) !important;
            border-radius: 6px;
            animation: glowPulse 3s ease-in-out infinite;
        }

        [data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] p {
            color: #d4af37 !important;
            font-weight: 600;
        }

        /* Sidebar divider */
        [data-testid="stSidebar"] hr,
        [data-testid="stSidebar"] [data-testid="stDivider"] {
            border: none;
            border-top: 1px solid rgba(212,175,55,0.15);
            margin: 16px 0;
        }

        /* Sidebar slider */
        [data-testid="stSidebar"] [data-testid="stSlider"] {
            background: rgba(255,255,255,0.03);
            border-radius: 8px;
            padding: 8px 4px;
        }

        /* ================================================================
           6. PLOTLY CHART CONTAINERS — 3D card lift on hover
           ================================================================ */
        [data-testid="stPlotlyChart"],
        .stPlotlyChart {
            border: 1px solid rgba(212,175,55,0.12) !important;
            border-radius: 12px !important;
            overflow: hidden;
            transition: transform 0.35s cubic-bezier(0.25, 0.46, 0.45, 0.94),
                        box-shadow 0.35s ease,
                        border-color 0.35s ease;
            box-shadow: 0 4px 20px rgba(0,0,0,0.3);
        }

        [data-testid="stPlotlyChart"]:hover,
        .stPlotlyChart:hover {
            transform: translateY(-4px);
            box-shadow:
                0 12px 40px rgba(0,0,0,0.5),
                0 0 20px rgba(212,175,55,0.12);
            border-color: rgba(212,175,55,0.3) !important;
        }

        /* ================================================================
           7. BUTTONS — gold gradient, 3D press
           ================================================================ */
        .stButton > button,
        [data-testid="stButton"] > button,
        [data-testid="stFormSubmitButton"] > button {
            background: linear-gradient(135deg, #d4af37 0%, #b8962e 50%, #9a7d24 100%) !important;
            color: #0a0a0f !important;
            font-weight: 700 !important;
            border: 1px solid rgba(245,230,163,0.3) !important;
            border-radius: 8px !important;
            padding: 10px 24px !important;
            text-shadow: 0 1px 2px rgba(255,255,255,0.2);
            box-shadow:
                0 4px 15px rgba(212,175,55,0.3),
                0 2px 4px rgba(0,0,0,0.4),
                inset 0 1px 0 rgba(255,255,255,0.2);
            transition: all 0.2s ease;
            cursor: pointer;
            position: relative;
            top: 0;
        }

        .stButton > button:hover,
        [data-testid="stButton"] > button:hover,
        [data-testid="stFormSubmitButton"] > button:hover {
            background: linear-gradient(135deg, #e8c84a 0%, #d4af37 50%, #b8962e 100%) !important;
            box-shadow:
                0 6px 25px rgba(212,175,55,0.45),
                0 3px 6px rgba(0,0,0,0.4),
                inset 0 1px 0 rgba(255,255,255,0.3);
            transform: translateY(-1px);
        }

        .stButton > button:active,
        [data-testid="stButton"] > button:active,
        [data-testid="stFormSubmitButton"] > button:active {
            transform: translateY(2px) !important;
            box-shadow:
                0 1px 5px rgba(212,175,55,0.2),
                0 0px 2px rgba(0,0,0,0.4),
                inset 0 2px 4px rgba(0,0,0,0.3);
            background: linear-gradient(135deg, #b8962e 0%, #9a7d24 100%) !important;
        }

        /* ================================================================
           8. FILE UPLOADER — animated gold dashed border
           ================================================================ */
        [data-testid="stFileUploader"] {
            position: relative;
        }

        [data-testid="stFileUploader"] section {
            background: rgba(255,255,255,0.02) !important;
            border: 2px dashed rgba(212,175,55,0.35) !important;
            border-radius: 12px !important;
            padding: 24px 16px !important;
            transition: all 0.3s ease;
            position: relative;
            overflow: hidden;
        }

        /* Animated rotating dash effect via SVG background */
        [data-testid="stFileUploader"] section::before {
            content: "";
            position: absolute;
            inset: -2px;
            border-radius: 14px;
            border: 2px dashed transparent;
            background:
                linear-gradient(var(--angle, 0deg), #d4af37, #e8b4b8, #d4af37) border-box;
            -webkit-mask:
                linear-gradient(#fff 0 0) padding-box,
                linear-gradient(#fff 0 0);
            mask:
                linear-gradient(#fff 0 0) padding-box,
                linear-gradient(#fff 0 0);
            -webkit-mask-composite: xor;
            mask-composite: exclude;
            animation: borderRotate 4s linear infinite;
            opacity: 0;
            transition: opacity 0.3s ease;
            pointer-events: none;
        }

        /* Fallback: use a simpler glow approach since --angle CSS custom
           property animation has limited browser support in Streamlit context.
           We use a pulsing gold border instead. */
        @keyframes borderGlow {
            0%, 100% { border-color: rgba(212,175,55,0.35); box-shadow: 0 0 10px rgba(212,175,55,0.05); }
            50%      { border-color: rgba(212,175,55,0.6);  box-shadow: 0 0 20px rgba(212,175,55,0.15); }
        }

        [data-testid="stFileUploader"] section {
            animation: borderGlow 3s ease-in-out infinite;
        }

        [data-testid="stFileUploader"] section:hover {
            border-color: rgba(212,175,55,0.6) !important;
            background: rgba(212,175,55,0.05) !important;
            box-shadow:
                0 0 30px rgba(212,175,55,0.15),
                inset 0 0 20px rgba(212,175,55,0.03);
        }

        [data-testid="stFileUploader"] label span {
            color: #a0a0b0 !important;
        }

        [data-testid="stFileUploader"] label span[data-baseweb="tooltip"] {
            color: #d4af37 !important;
        }

        /* ================================================================
           9. SELECTBOX / DROPDOWN
           ================================================================ */
        [data-testid="stSelectbox"] {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(212,175,55,0.15);
            border-radius: 8px;
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
        }

        [data-testid="stSelectbox"]:hover,
        [data-testid="stSelectbox"]:focus-within {
            border-color: rgba(212,175,55,0.4);
            box-shadow: 0 0 12px rgba(212,175,55,0.1);
        }

        [data-testid="stSelectbox"] label p {
            color: #d4af37 !important;
        }

        [data-testid="stSelectbox"] div[data-baseweb="select"] {
            background-color: rgba(10,10,18,0.8) !important;
            border: 1px solid rgba(212,175,55,0.1) !important;
            border-radius: 8px !important;
        }

        [data-testid="stSelectbox"] div[data-baseweb="select"] span {
            color: #e0e0ee !important;
        }

        /* Dropdown list items */
        [data-baseweb="popover"] {
            background-color: rgba(15,15,25,0.97) !important;
            border: 1px solid rgba(212,175,55,0.2) !important;
            border-radius: 8px !important;
            box-shadow: 0 8px 30px rgba(0,0,0,0.6), 0 0 15px rgba(212,175,55,0.08);
        }

        [data-baseweb="popover"] li {
            color: #c0c0cc !important;
            transition: background 0.2s ease, color 0.2s ease;
        }

        [data-baseweb="popover"] li:hover,
        [data-baseweb="popover"] li[aria-selected="true"] {
            background: rgba(212,175,55,0.15) !important;
            color: #d4af37 !important;
        }

        /* ================================================================
           10. SLIDERS
           ================================================================ */
        [data-testid="stSlider"] [role="slider"] {
            background: rgba(212,175,55,0.3) !important;
            border: 1px solid rgba(212,175,55,0.4) !important;
            box-shadow: 0 0 8px rgba(212,175,55,0.2);
        }

        [data-testid="stSlider"] [role="slider"]:hover {
            background: rgba(212,175,55,0.5) !important;
            box-shadow: 0 0 15px rgba(212,175,55,0.3);
        }

        [data-testid="stSlider"] [role="slider"]:focus {
            box-shadow: 0 0 0 3px rgba(212,175,55,0.3);
        }

        /* Slider track */
        [data-testid="stSlider"] div[style*="background-color: rgb(167, 167, 167)"],
        [data-testid="stSlider"] div[class*="Track"] {
            background: rgba(212,175,55,0.2) !important;
            border-radius: 4px;
        }

        [data-testid="stSlider"] div[class*="Tick"] {
            background: rgba(212,175,55,0.4) !important;
        }

        /* ================================================================
           11. TEXT AREA — dark glass, gold focus glow
           ================================================================ */
        [data-testid="stTextArea"] textarea {
            background: rgba(10,10,18,0.7) !important;
            border: 1px solid rgba(212,175,55,0.15) !important;
            border-radius: 10px !important;
            color: #e0e0ee !important;
            padding: 14px 16px !important;
            font-size: 15px !important;
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
            backdrop-filter: blur(8px);
        }

        [data-testid="stTextArea"] textarea::placeholder {
            color: #606070 !important;
        }

        [data-testid="stTextArea"] textarea:focus {
            border-color: rgba(212,175,55,0.5) !important;
            box-shadow: 0 0 20px rgba(212,175,55,0.12), inset 0 0 10px rgba(212,175,55,0.03) !important;
            outline: none !important;
        }

        [data-testid="stTextArea"] label p {
            color: #d4af37 !important;
        }

        /* ================================================================
           12. CHAT MESSAGES — glassmorphism bubbles
           ================================================================ */
        /* User message */
        [data-testid="stChatMessage"][data-testid*="user"],
        [data-testid="stChatMessage"]:has([data-testid="stChatInput"]) {
            /* won't match; user messages use role="user" attribute approach */
        }

        .stChatMessage {
            border-radius: 16px !important;
            padding: 14px 18px !important;
            margin: 6px 0 !important;
            backdrop-filter: blur(16px) !important;
            -webkit-backdrop-filter: blur(16px) !important;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        /* User chat bubble — dark gold tint */
        .stChatMessage:nth-child(odd),
        .stChatMessage[data-testid="stChatMessage-user"] {
            background: rgba(212,175,55,0.08) !important;
            border: 1px solid rgba(212,175,55,0.2) !important;
            box-shadow:
                0 4px 15px rgba(0,0,0,0.3),
                inset 0 1px 0 rgba(212,175,55,0.1);
            margin-left: 20px !important;
        }

        /* Assistant chat bubble — dark blue-gray tint */
        .stChatMessage:nth-child(even),
        .stChatMessage[data-testid="stChatMessage-assistant"] {
            background: rgba(30,35,55,0.6) !important;
            border: 1px solid rgba(100,120,180,0.15) !important;
            box-shadow:
                0 4px 15px rgba(0,0,0,0.3),
                inset 0 1px 0 rgba(100,120,180,0.08);
            margin-right: 20px !important;
        }

        .stChatMessage:hover {
            transform: translateY(-2px);
            box-shadow:
                0 6px 25px rgba(0,0,0,0.4),
                0 0 15px rgba(212,175,55,0.08);
        }

        .stChatMessage p, .stChatMessage span, .stChatMessage div {
            color: #e0e0ee !important;
        }

        /* Chat input */
        [data-testid="stChatInput"] {
            background: rgba(10,10,18,0.6) !important;
            border: 1px solid rgba(212,175,55,0.15) !important;
            border-radius: 12px !important;
            backdrop-filter: blur(12px);
        }

        [data-testid="stChatInput"] textarea {
            background: transparent !important;
            color: #e0e0ee !important;
        }

        [data-testid="stChatInput"] textarea::placeholder {
            color: #606070 !important;
        }

        /* ================================================================
           13. SPINNER — custom gold spinning animation
           ================================================================ */
        [data-testid="stSpinner"] > div {
            border-top-color: #d4af37 !important;
            border-right-color: rgba(212,175,55,0.3) !important;
            border-bottom-color: rgba(212,175,55,0.1) !important;
            border-left-color: rgba(212,175,55,0.6) !important;
            animation: spinGold 0.8s linear infinite !important;
        }

        /* Replace default spinner with a gold ring */
        @keyframes spinGold {
            0%   { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }

        /* ================================================================
           14. SUCCESS / WARNING / ERROR ALERTS
           ================================================================ */
        /* Success */
        [data-testid="stAlert"] [data-baseweb="notification"][role="alert"] {
            background: rgba(20,40,25,0.7) !important;
            border: 1px solid rgba(80,200,100,0.25) !important;
            border-left: 4px solid #4ade80 !important;
            border-radius: 10px !important;
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 20px rgba(0,0,0,0.3), 0 0 10px rgba(80,200,100,0.05);
        }

        [data-testid="stAlert"] [data-baseweb="notification"][role="alert"] p {
            color: #a0e8b0 !important;
        }

        /* Warning */
        .stAlert [data-baseweb="notification"],
        [data-testid="stAlert"] [data-baseweb="notification"][style*="amber"],
        [data-testid="stWarning"] {
            background: rgba(45,35,15,0.7) !important;
            border: 1px solid rgba(212,175,55,0.3) !important;
            border-left: 4px solid #d4af37 !important;
            border-radius: 10px !important;
            backdrop-filter: blur(12px);
            box-shadow: 0 4px 20px rgba(0,0,0,0.3), 0 0 10px rgba(212,175,55,0.08);
        }

        [data-testid="stAlert"] p,
        .stAlert p {
            color: #e0d0a0 !important;
        }

        /* Error */
        [data-testid="stAlert"] [data-baseweb="notification"][style*="red"] {
            background: rgba(50,15,15,0.7) !important;
            border: 1px solid rgba(220,80,80,0.3) !important;
            border-left: 4px solid #ef4444 !important;
            border-radius: 10px !important;
        }

        /* Info */
        [data-testid="stAlert"] [data-baseweb="notification"][style*="blue"] {
            background: rgba(15,20,45,0.7) !important;
            border: 1px solid rgba(100,140,220,0.25) !important;
            border-left: 4px solid #60a5fa !important;
            border-radius: 10px !important;
        }

        /* ================================================================
           15. MARKDOWN CONTENT IN MAIN AREA
           ================================================================ */
        .stMarkdown p, .stMarkdown li, .stMarkdown span {
            color: #c8c8d8 !important;
            line-height: 1.7;
        }

        .stMarkdown strong, .stMarkdown b {
            color: #e8e8f0 !important;
        }

        .stMarkdown a, .stMarkdown a:hover {
            color: #d4af37 !important;
            text-decoration: underline;
        }

        .stMarkdown code {
            background: rgba(212,175,55,0.08);
            border: 1px solid rgba(212,175,55,0.15);
            border-radius: 4px;
            padding: 2px 6px;
            color: #e8b4b8;
            font-size: 0.9em;
        }

        .stMarkdown pre {
            background: rgba(10,10,18,0.8) !important;
            border: 1px solid rgba(212,175,55,0.12) !important;
            border-radius: 8px !important;
            padding: 16px !important;
        }

        .stMarkdown pre code {
            background: transparent;
            border: none;
            color: #c8c8d8;
        }

        /* ================================================================
           16. COLUMNS — spacing
           ================================================================ */
        [data-testid="stHorizontalBlock"] {
            gap: 20px;
        }

        /* ================================================================
           17. IMAGES
           ================================================================ */
        .stImage > img {
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.4);
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        .stImage > img:hover {
            transform: scale(1.02);
            box-shadow: 0 8px 30px rgba(0,0,0,0.5), 0 0 15px rgba(212,175,55,0.1);
        }

        /* ================================================================
           18. METRICS / KPI CARDS
           ================================================================ */
        [data-testid="stMetric"] {
            background: rgba(255,255,255,0.03) !important;
            border: 1px solid rgba(212,175,55,0.12) !important;
            border-radius: 10px !important;
            padding: 16px !important;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }

        [data-testid="stMetric"]:hover {
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(0,0,0,0.3), 0 0 10px rgba(212,175,55,0.08);
        }

        [data-testid="stMetric"] label {
            color: #a0a0b0 !important;
        }

        [data-testid="stMetric"] [data-testid="stMetricValue"] {
            color: #d4af37 !important;
        }

        /* ================================================================
           19. EXPANDER / ACCORDION
           ================================================================ */
        .stExpander > div > div {
            background: rgba(255,255,255,0.02) !important;
            border: 1px solid rgba(212,175,55,0.1) !important;
            border-radius: 10px !important;
        }

        .stExpander [data-testid="stExpanderDetails"] {
            border-top: 1px solid rgba(212,175,55,0.1);
        }

        /* ================================================================
           20. TABS
           ================================================================ */
        .stTabs [data-baseweb="tab-list"] {
            gap: 4px;
            background: rgba(255,255,255,0.02);
            border-radius: 8px;
            padding: 4px;
        }

        .stTabs [data-baseweb="tab"] {
            border-radius: 6px !important;
            color: #a0a0b0 !important;
            transition: all 0.3s ease;
        }

        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: rgba(212,175,55,0.15) !important;
            color: #d4af37 !important;
            border-bottom: 2px solid #d4af37 !important;
        }

        .stTabs [data-baseweb="tab"]:hover {
            background: rgba(212,175,55,0.08) !important;
            color: #e8b4b8 !important;
        }

        /* ================================================================
           21. SCROLLBAR STYLING
           ================================================================ */
        ::-webkit-scrollbar {
            width: 8px;
            height: 8px;
        }

        ::-webkit-scrollbar-track {
            background: rgba(10,10,18,0.5);
        }

        ::-webkit-scrollbar-thumb {
            background: rgba(212,175,55,0.25);
            border-radius: 4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: rgba(212,175,55,0.45);
        }

        /* ================================================================
           22. RESPONSIVE TWEAKS
           ================================================================ */
        @media (max-width: 768px) {
            .main .block-container {
                padding-left: 16px !important;
                padding-right: 16px !important;
            }

            [data-testid="stSidebar"] {
                width: 280px !important;
            }

            .stChatMessage:nth-child(odd),
            .stChatMessage:nth-child(even) {
                margin-left: 4px !important;
                margin-right: 4px !important;
            }

            [data-testid="stDataFrame"]:hover {
                transform: none;  /* skip 3D tilt on small screens */
            }
        }

        @media (max-width: 480px) {
            .main h1 {
                font-size: 1.6rem !important;
            }

            .stButton > button {
                padding: 8px 16px !important;
                font-size: 14px !important;
            }
        }

        /* ================================================================
           23. SUBHEADER STYLING
           ================================================================ */
        .stSubheader {
            color: #d4af37 !important;
            border-bottom: 1px solid rgba(212,175,55,0.12);
            padding-bottom: 8px;
        }

        /* ================================================================
           24. DIVIDER
           ================================================================ */
        hr, [data-testid="stDivider"] {
            border: none;
            border-top: 1px solid rgba(212,175,55,0.12);
            margin: 20px 0;
        }

        /* ================================================================
           25. NUMBER INPUT / TEXT INPUT
           ================================================================ */
        [data-testid="stNumberInput"] input,
        [data-testid="stTextInput"] input {
            background: rgba(10,10,18,0.7) !important;
            border: 1px solid rgba(212,175,55,0.15) !important;
            border-radius: 8px !important;
            color: #e0e0ee !important;
            transition: border-color 0.3s ease, box-shadow 0.3s ease;
        }

        [data-testid="stNumberInput"] input:focus,
        [data-testid="stTextInput"] input:focus {
            border-color: rgba(212,175,55,0.5) !important;
            box-shadow: 0 0 15px rgba(212,175,55,0.1) !important;
            outline: none !important;
        }

        [data-testid="stNumberInput"] label p,
        [data-testid="stTextInput"] label p {
            color: #d4af37 !important;
        }

        /* ================================================================
           26. CHECKBOX
           ================================================================ */
        [data-testid="stCheckbox"] label span {
            color: #c0c0cc !important;
        }

        [data-testid="stCheckbox"] label:hover span {
            color: #e8b4b8 !important;
        }

        /* ================================================================
           27. TOOLTIP
           ================================================================ */
        [data-baseweb="tooltip"] {
            background: rgba(15,15,25,0.95) !important;
            border: 1px solid rgba(212,175,55,0.2) !important;
            border-radius: 6px !important;
            color: #e0e0ee !important;
            box-shadow: 0 4px 15px rgba(0,0,0,0.4);
        }

        /* ================================================================
           28. CODE BLOCKS (st.code / st.echo)
           ================================================================ */
        [data-testid="stCodeBlock"] {
            background: rgba(10,10,18,0.8) !important;
            border: 1px solid rgba(212,175,55,0.12) !important;
            border-radius: 10px !important;
        }

        [data-testid="stCodeBlock"] code,
        [data-testid="stCodeBlock"] pre {
            color: #c8c8d8 !important;
        }

        /* ================================================================
           29. PROGRESS BAR
           ================================================================ */
        [data-testid="stProgressBar"] > div > div > div {
            background: linear-gradient(90deg, #d4af37, #e8c84a) !important;
            border-radius: 4px !important;
            box-shadow: 0 0 10px rgba(212,175,55,0.3);
        }

        /* ================================================================
           30. FINAL BODY TEXT COLOR OVERRIDES
           ================================================================ */
        .main div, .main span, .main p, .main label {
            color: #c8c8d8;
        }

        .main a {
            color: #d4af37 !important;
        }

        .main a:hover {
            color: #e8b4b8 !important;
        }

        /* Ensure white for important headings */
        h1, h2, h3 {
            color: #ffffff !important;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# 2. PLOTLY THEME HELPERS
# ---------------------------------------------------------------------------

def style_plotly_charts() -> dict:
    """
    Return a Plotly layout template dict with the luxury dark theme.
    Merge this into any figure's layout or use it as a template.
    """
    return {
        "template": {
            "layout": {
                "paper_bgcolor": "rgba(0,0,0,0)",
                "plot_bgcolor": "#0a0a0f",
                "font": {
                    "family": "Segoe UI, Helvetica Neue, Arial, sans-serif",
                    "color": "#c8c8d8",
                    "size": 13,
                },
                "title": {
                    "font": {"color": "#d4af37", "size": 17},
                },
                "xaxis": {
                    "gridcolor": "rgba(212,175,55,0.1)",
                    "zerolinecolor": "rgba(212,175,55,0.2)",
                    "linecolor": "rgba(212,175,55,0.15)",
                    "tickfont": {"color": "#a0a0b0"},
                    "title": {"font": {"color": "#d4af37"}},
                },
                "yaxis": {
                    "gridcolor": "rgba(212,175,55,0.1)",
                    "zerolinecolor": "rgba(212,175,55,0.2)",
                    "linecolor": "rgba(212,175,55,0.15)",
                    "tickfont": {"color": "#a0a0b0"},
                    "title": {"font": {"color": "#d4af37"}},
                },
                "legend": {
                    "font": {"color": "#a0a0b0", "size": 12},
                    "bgcolor": "rgba(0,0,0,0)",
                    "bordercolor": "rgba(212,175,55,0.15)",
                    "borderwidth": 1,
                },
                "colorway": [
                    "#d4af37", "#e8b4b8", "#6ea8d9", "#7dd3a8",
                    "#d9a06e", "#b088d9", "#d96e8f", "#8ed9c4",
                    "#d9d06e", "#6e8fd9",
                ],
                "hoverlabel": {
                    "bgcolor": "#1a1a28",
                    "bordercolor": "rgba(212,175,55,0.3)",
                    "font": {"color": "#ffffff", "size": 13},
                },
                "modebar": {
                    "bgcolor": "transparent",
                    "color": "#a0a0b0",
                    "activecolor": "#d4af37",
                },
            }
        }
    }


def apply_chart_theme(fig) -> object:
    """
    Apply the luxury dark theme to a Plotly figure object.

    Parameters
    ----------
    fig : plotly.graph_objects.Figure
        The Plotly figure to style.

    Returns
    -------
    plotly.graph_objects.Figure
        The same figure with dark luxury styling applied.
    """
    theme = style_plotly_charts()

    # Apply template at the figure level
    fig.update_layout(template=theme["template"]["layout"])

    # Also set paper/plot bg directly as a safety net
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#0a0a0f",
    )

    # Style traces — gold hover highlight
    for trace in fig.data:
        trace.hoverinfo = "all"
        # If the trace supports marker, add hover styling
        if hasattr(trace, "marker"):
            trace.marker.line = dict(color="rgba(212,175,55,0.4)", width=1)
        if hasattr(trace, "line"):
            trace.line.width = 2

    return fig