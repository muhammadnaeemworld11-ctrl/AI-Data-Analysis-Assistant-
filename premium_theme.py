"""
Premium 3D Luxury Dark Theme for Streamlit — DRAMATIC EDITION
===============================================================
Pure CSS injection via st.markdown(unsafe_allow_html=True).
No extra libraries. No JS. Works with Streamlit 1.28+.

Usage — add ONLY 2 lines to main.py, touch NOTHING else:

    from premium_theme import inject_premium_css
    inject_premium_css()          # put right after st.set_page_config(...)

That's it. Done. Your visualization.py stays 100% untouched.
The CSS handles everything — containers, sidebar, buttons, charts, etc.

Optional (only if you ALSO want Plotly internals dark, not just the container):
    from premium_theme import inject_premium_css, apply_chart_theme
    fig = apply_chart_theme(fig)  # before st.plotly_chart(fig)
"""

import streamlit as st


def inject_premium_css() -> None:
    """Inject the full premium 3D luxury dark theme via st.markdown."""

    st.markdown(
        """
        <style>
        /*================================================================
          ★  ANIMATED BACKGROUND — living, breathing dark canvas
          =================================================================*/
        @keyframes bgDrift {
            0%,100%{background-position:0% 50%}
            25%{background-position:100% 0%}
            50%{background-position:100% 100%}
            75%{background-position:0% 100%}
        }
        @keyframes meshPulse1 {
            0%,100%{opacity:.35;transform:scale(1)}
            50%{opacity:.65;transform:scale(1.08)}
        }
        @keyframes meshPulse2 {
            0%,100%{opacity:.25;transform:scale(1.05)}
            50%{opacity:.5;transform:scale(0.95)}
        }
        @keyframes meshPulse3 {
            0%,100%{opacity:.3;transform:translate(0,0)}
            50%{opacity:.55;transform:translate(10px,-10px)}
        }

        [data-testid="stAppViewContainer"] {
            background: linear-gradient(-45deg,
                #06060c, #0a0a14, #0e0b16, #0b0f18, #08080e, #0d0a12);
            background-size: 600% 600% !important;
            animation: bgDrift 25s ease infinite !important;
            min-height: 100vh;
        }

        /* Animated radial glow orbs floating on the background */
        [data-testid="stAppViewContainer"]::before {
            content:"";
            position:fixed; inset:0;
            pointer-events:none; z-index:0;
            background:
                radial-gradient(ellipse 700px 700px at 15% 25%,
                    rgba(212,175,55,0.07) 0%, transparent 60%),
                radial-gradient(ellipse 500px 500px at 85% 75%,
                    rgba(232,180,184,0.05) 0%, transparent 55%),
                radial-gradient(ellipse 600px 600px at 50% 10%,
                    rgba(212,175,55,0.04) 0%, transparent 50%);
            animation: meshPulse1 8s ease-in-out infinite;
        }
        [data-testid="stAppViewContainer"]::after {
            content:"";
            position:fixed; inset:0;
            pointer-events:none; z-index:0;
            background:
                radial-gradient(ellipse 400px 400px at 70% 20%,
                    rgba(140,120,220,0.04) 0%, transparent 55%),
                radial-gradient(ellipse 450px 450px at 25% 80%,
                    rgba(212,175,55,0.05) 0%, transparent 50%);
            animation: meshPulse2 10s ease-in-out infinite;
        }

        .main .block-container { position:relative; z-index:1; }

        /*================================================================
          ★  HIDE DEFAULT STREAMLIT CHROME
          =================================================================*/
        #MainMenu{visibility:hidden}
        footer{visibility:hidden}
        [data-testid="stHeader"]{
            padding:0!important;
            background:rgba(0,0,0,0)!important;
        }

        /*================================================================
          ★  KEYFRAME LIBRARY
          =================================================================*/
        @keyframes float {
            0%,100%{transform:translateY(0)}
            50%{transform:translateY(-10px)}
        }
        @keyframes shimmer {
            0%{background-position:-300% center}
            100%{background-position:300% center}
        }
        @keyframes fadeInUp {
            from{opacity:0;transform:translateY(24px) scale(0.98)}
            to{opacity:1;transform:translateY(0) scale(1)}
        }
        @keyframes glowPulse {
            0%,100%{box-shadow:0 0 8px rgba(212,175,55,0.15),
                0 0 2px rgba(212,175,55,0.1), inset 0 0 4px rgba(212,175,55,0.03)}
            50%{box-shadow:0 0 25px rgba(212,175,55,0.4),
                0 0 8px rgba(212,175,55,0.2), inset 0 0 12px rgba(212,175,55,0.08)}
        }
        @keyframes borderGlow {
            0%,100%{border-color:rgba(212,175,55,0.25);
                box-shadow:0 0 8px rgba(212,175,55,0.05)}
            50%{border-color:rgba(212,175,55,0.7);
                box-shadow:0 0 28px rgba(212,175,55,0.15),
                inset 0 0 15px rgba(212,175,55,0.04)}
        }
        @keyframes spinGold {
            0%{transform:rotate(0deg)}
            100%{transform:rotate(360deg)}
        }
        @keyframes textGlow {
            0%,100%{text-shadow:0 0 8px rgba(212,175,55,0.3),
                0 0 2px rgba(212,175,55,0.15)}
            50%{text-shadow:0 0 20px rgba(212,175,55,0.6),
                0 0 6px rgba(212,175,55,0.3),
                0 0 40px rgba(212,175,55,0.15)}
        }
        @keyframes slideInLeft {
            from{opacity:0;transform:translateX(-30px)}
            to{opacity:1;transform:translateX(0)}
        }
        @keyframes breathe {
            0%,100%{transform:scale(1);opacity:0.8}
            50%{transform:scale(1.02);opacity:1}
        }
        @keyframes scanline {
            0%{top:-5%}
            100%{top:105%}
        }
        @keyframes borderDash {
            to{stroke-dashoffset:-80}
        }

        /*================================================================
          ★  TITLE — floating gold shimmer
          =================================================================*/
        .main [data-testid="stVerticalBlock"]:first-child {
            animation: float 5s ease-in-out infinite;
        }

        .main h1,
        .main [data-testid="stTitle"],
        [data-testid="stHeadingWithActionIcon"] h1 {
            background: linear-gradient(90deg,
                #d4af37 0%, #f5e6a3 15%, #fff8e1 30%,
                #d4af37 45%, #e8b4b8 60%, #d4af37 75%,
                #f5e6a3 90%, #d4af37 100%);
            background-size: 300% 100% !important;
            -webkit-background-clip:text !important;
            -webkit-text-fill-color:transparent !important;
            background-clip:text !important;
            animation: shimmer 5s linear infinite !important;
            filter: drop-shadow(0 0 12px rgba(212,175,55,0.35));
            font-weight:800 !important;
            letter-spacing:0.5px;
        }

        .main h2, .main h3 {
            color:#d4af37 !important;
            animation: textGlow 4s ease-in-out infinite;
            font-weight:700 !important;
        }

        .main h4, .main h5 {
            color:#e8d5a0 !important;
        }

        /*================================================================
          ★  FADE-IN ANIMATIONS ON SECTIONS
          =================================================================*/
        .main [data-testid="stVerticalBlock"] {
            animation: fadeInUp 0.7s cubic-bezier(0.22,1,0.36,1) both;
        }
        .main [data-testid="stVerticalBlock"]:nth-child(1){animation-delay:0s}
        .main [data-testid="stVerticalBlock"]:nth-child(2){animation-delay:.08s}
        .main [data-testid="stVerticalBlock"]:nth-child(3){animation-delay:.16s}
        .main [data-testid="stVerticalBlock"]:nth-child(4){animation-delay:.24s}
        .main [data-testid="stVerticalBlock"]:nth-child(5){animation-delay:.32s}
        .main [data-testid="stVerticalBlock"]:nth-child(6){animation-delay:.40s}
        .main [data-testid="stVerticalBlock"]:nth-child(7){animation-delay:.48s}
        .main [data-testid="stVerticalBlock"]:nth-child(8){animation-delay:.56s}
        .main [data-testid="stVerticalBlock"]:nth-child(9){animation-delay:.64s}
        .main [data-testid="stVerticalBlock"]:nth-child(10){animation-delay:.72s}

        /*================================================================
          ★  SIDEBAR — luxury glassmorphism with animated gold border
          =================================================================*/
        @keyframes sidebarGlow {
            0%,100%{border-right-color:rgba(212,175,55,0.2);
                box-shadow:4px 0 30px rgba(0,0,0,0.5),
                inset -1px 0 0 rgba(212,175,55,0.05)}
            50%{border-right-color:rgba(212,175,55,0.45);
                box-shadow:4px 0 30px rgba(0,0,0,0.5),
                4px 0 40px rgba(212,175,55,0.06),
                inset -1px 0 0 rgba(212,175,55,0.12)}
        }

        [data-testid="stSidebar"] {
            background: linear-gradient(180deg,
                rgba(8,8,16,0.92) 0%,
                rgba(12,12,22,0.88) 50%,
                rgba(10,10,18,0.92) 100%) !important;
            backdrop-filter:blur(24px) saturate(1.2) !important;
            -webkit-backdrop-filter:blur(24px) saturate(1.2) !important;
            border-right:2px solid rgba(212,175,55,0.25) !important;
            animation:sidebarGlow 5s ease-in-out infinite;
        }

        [data-testid="stSidebar"]::before {
            content:"";
            position:absolute; top:0; left:0; right:0; bottom:0;
            background:
                linear-gradient(180deg,
                    rgba(212,175,55,0.06) 0%,
                    transparent 30%,
                    transparent 70%,
                    rgba(212,175,55,0.04) 100%);
            pointer-events:none;
        }

        [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
            color:#d4af37 !important;
            text-shadow:0 0 15px rgba(212,175,55,0.3);
            animation:textGlow 5s ease-in-out infinite;
        }

        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] span {
            color:#a8a8b8 !important;
            transition:color .3s ease;
        }

        [data-testid="stSidebar"] p:hover,
        [data-testid="stSidebar"] label:hover {
            color:#e8b4b8 !important;
        }

        /* Sidebar radio — luxury card style */
        [data-testid="stSidebar"] [data-testid="stRadio"] {
            background:rgba(255,255,255,0.025) !important;
            border:1px solid rgba(212,175,55,0.08) !important;
            border-radius:10px !important;
            padding:6px 10px !important;
            margin-bottom:8px !important;
            transition:all .35s ease !important;
        }

        [data-testid="stSidebar"] [data-testid="stRadio"]:hover {
            border-color:rgba(232,180,184,0.25) !important;
            background:rgba(255,255,255,0.04) !important;
        }

        /* Active sidebar radio — GOLD GLOW PULSE */
        [data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] {
            background:rgba(212,175,55,0.1) !important;
            border-radius:8px;
            animation:glowPulse 3s ease-in-out infinite !important;
        }

        [data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] p,
        [data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] span {
            color:#d4af37 !important;
            font-weight:700 !important;
            text-shadow:0 0 8px rgba(212,175,55,0.3);
        }

        /* Sidebar divider */
        [data-testid="stSidebar"] hr,
        [data-testid="stSidebar"] [data-testid="stDivider"] {
            border:none;
            height:1px;
            background:linear-gradient(90deg,
                transparent, rgba(212,175,55,0.3), transparent);
            margin:20px 0 !important;
        }

        /* Sidebar slider track */
        [data-testid="stSidebar"] [data-testid="stSlider"] {
            background:rgba(255,255,255,0.02);
            border-radius:10px;
            padding:10px 6px;
            border:1px solid rgba(212,175,55,0.06);
        }

        /* Sidebar section entrance */
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
            animation:slideInLeft 0.5s ease-out both;
        }
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"]:nth-child(2){animation-delay:.1s}
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"]:nth-child(3){animation-delay:.2s}
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"]:nth-child(4){animation-delay:.3s}
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"]:nth-child(5){animation-delay:.4s}
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"]:nth-child(6){animation-delay:.5s}

        /*================================================================
          ★  BUTTONS — bold gold gradient + dramatic 3D press
          =================================================================*/
        .stButton > button,
        [data-testid="stButton"] > button,
        [data-testid="stFormSubmitButton"] > button {
            background:linear-gradient(135deg,
                #c9a227 0%, #f0d060 20%, #d4af37 40%,
                #e8c84a 60%, #b8962e 80%, #d4af37 100%) !important;
            background-size:200% 200% !important;
            animation:breathe 4s ease-in-out infinite;
            color:#0a0a0f !important;
            font-weight:800 !important;
            font-size:15px !important;
            letter-spacing:0.6px;
            border:none !important;
            border-radius:10px !important;
            padding:12px 32px !important;
            text-shadow:0 1px 2px rgba(255,255,255,0.25);
            box-shadow:
                0 6px 25px rgba(212,175,55,0.35),
                0 3px 8px rgba(0,0,0,0.5),
                inset 0 1px 0 rgba(255,255,255,0.35),
                inset 0 -2px 4px rgba(0,0,0,0.15);
            transition:all .25s cubic-bezier(0.34,1.56,0.64,1) !important;
            cursor:pointer;
            position:relative;
            top:0;
            text-transform:uppercase;
        }

        .stButton > button:hover,
        [data-testid="stButton"] > button:hover,
        [data-testid="stFormSubmitButton"] > button:hover {
            transform:translateY(-3px) scale(1.02) !important;
            box-shadow:
                0 10px 40px rgba(212,175,55,0.5),
                0 5px 15px rgba(0,0,0,0.5),
                inset 0 1px 0 rgba(255,255,255,0.4),
                0 0 60px rgba(212,175,55,0.15);
            background-position:100% 100% !important;
        }

        .stButton > button:active,
        [data-testid="stButton"] > button:active,
        [data-testid="stFormSubmitButton"] > button:active {
            transform:translateY(2px) scale(0.98) !important;
            box-shadow:
                0 1px 5px rgba(212,175,55,0.2),
                0 0px 1px rgba(0,0,0,0.5),
                inset 0 3px 8px rgba(0,0,0,0.35);
            transition-duration:0.1s !important;
        }

        /* Secondary / outline feel for file uploader button area */
        [data-testid="stFileUploader"] button {
            background:rgba(212,175,55,0.12) !important;
            border:1px solid rgba(212,175,55,0.3) !important;
            color:#d4af37 !important;
            border-radius:8px !important;
            transition:all .3s ease;
        }
        [data-testid="stFileUploader"] button:hover {
            background:rgba(212,175,55,0.2) !important;
            box-shadow:0 0 20px rgba(212,175,55,0.15);
        }

        /*================================================================
          ★  FILE UPLOADER — animated pulsing gold border
          =================================================================*/
        [data-testid="stFileUploader"] section {
            background:rgba(255,255,255,0.015) !important;
            border:2px dashed rgba(212,175,55,0.3) !important;
            border-radius:14px !important;
            padding:28px 20px !important;
            animation:borderGlow 3s ease-in-out infinite !important;
            transition:all .35s ease;
            position:relative;
            overflow:hidden;
        }

        /* Scanline sweep effect on hover */
        [data-testid="stFileUploader"] section::after {
            content:"";
            position:absolute;
            left:0; right:0;
            height:40px;
            background:linear-gradient(180deg,
                transparent, rgba(212,175,55,0.08), transparent);
            animation:scanline 4s linear infinite;
            pointer-events:none;
        }

        [data-testid="stFileUploader"] section:hover {
            border-color:rgba(212,175,55,0.7) !important;
            background:rgba(212,175,55,0.04) !important;
            box-shadow:
                0 0 40px rgba(212,175,55,0.12),
                inset 0 0 30px rgba(212,175,55,0.03),
                0 0 80px rgba(212,175,55,0.06);
            transform:scale(1.01);
        }

        [data-testid="stFileUploader"] label p,
        [data-testid="stFileUploader"] label span {
            color:#a0a0b0 !important;
            transition:color .3s ease;
        }

        [data-testid="stFileUploader"]:hover label p {
            color:#d4af37 !important;
        }

        /*================================================================
          ★  DATAFRAMES — dramatic 3D tilt on hover
          =================================================================*/
        .stDataFrame,
        .stDataframe,
        [data-testid="stDataFrame"] {
            background:rgba(255,255,255,0.025) !important;
            border:1px solid rgba(212,175,55,0.12) !important;
            border-radius:14px !important;
            overflow:hidden;
            transition:transform .45s cubic-bezier(0.25,0.46,0.45,0.94),
                        box-shadow .45s ease,
                        border-color .35s ease !important;
            box-shadow:0 2px 12px rgba(0,0,0,0.3);
            transform-style:preserve-3d;
        }

        .stDataFrame:hover,
        .stDataframe:hover,
        [data-testid="stDataFrame"]:hover {
            transform:perspective(1200px) rotateX(2deg) rotateY(-1deg) translateY(-4px) !important;
            box-shadow:
                0 20px 60px rgba(0,0,0,0.5),
                0 0 30px rgba(212,175,55,0.1),
                0 8px 20px rgba(0,0,0,0.3),
                inset 0 1px 0 rgba(212,175,55,0.12);
            border-color:rgba(212,175,55,0.35) !important;
        }

        /*================================================================
          ★  PLOTLY CHART CONTAINERS — 3D lift with gold glow
          =================================================================*/
        [data-testid="stPlotlyChart"],
        .stPlotlyChart {
            border:1px solid rgba(212,175,55,0.1) !important;
            border-radius:14px !important;
            overflow:hidden;
            box-shadow:
                0 4px 20px rgba(0,0,0,0.3),
                0 0 1px rgba(212,175,55,0.1);
            transition:
                transform .4s cubic-bezier(0.25,0.46,0.45,0.94),
                box-shadow .4s ease,
                border-color .4s ease;
            transform-style:preserve-3d;
        }

        [data-testid="stPlotlyChart"]:hover,
        .stPlotlyChart:hover {
            transform:perspective(1000px) translateY(-6px) rotateX(1deg) !important;
            box-shadow:
                0 20px 50px rgba(0,0,0,0.5),
                0 0 35px rgba(212,175,55,0.12),
                0 0 80px rgba(212,175,55,0.04);
            border-color:rgba(212,175,55,0.35) !important;
        }

        /* Force transparent background on Plotly iframe */
        [data-testid="stPlotlyChart"] iframe,
        .stPlotlyChart iframe {
            background:transparent !important;
        }

        /*================================================================
          ★  SELECTBOX / DROPDOWN — dark luxury with gold highlight
          =================================================================*/
        [data-testid="stSelectbox"] {
            background:rgba(255,255,255,0.02);
            border:1px solid rgba(212,175,55,0.12);
            border-radius:10px;
            transition:border-color .3s ease, box-shadow .3s ease, background .3s ease;
        }

        [data-testid="stSelectbox"]:hover,
        [data-testid="stSelectbox"]:focus-within {
            border-color:rgba(212,175,55,0.4);
            box-shadow:0 0 20px rgba(212,175,55,0.08);
            background:rgba(255,255,255,0.03);
        }

        [data-testid="stSelectbox"] label p {
            color:#d4af37 !important;
            font-weight:600;
        }

        [data-testid="stSelectbox"] div[data-baseweb="select"] {
            background-color:rgba(10,10,18,0.85) !important;
            border:1px solid rgba(212,175,55,0.1) !important;
            border-radius:10px !important;
            transition:all .3s ease;
        }

        [data-testid="stSelectbox"] div[data-baseweb="select"]:hover {
            border-color:rgba(212,175,55,0.3) !important;
        }

        [data-testid="stSelectbox"] div[data-baseweb="select"] span {
            color:#e0e0ee !important;
        }

        /* Dropdown popover */
        [data-baseweb="popover"] {
            background:rgba(12,12,22,0.97) !important;
            border:1px solid rgba(212,175,55,0.2) !important;
            border-radius:10px !important;
            box-shadow:0 12px 40px rgba(0,0,0,0.7), 0 0 20px rgba(212,175,55,0.06);
            backdrop-filter:blur(20px);
        }

        [data-baseweb="popover"] li {
            color:#b0b0c0 !important;
            transition:all .2s ease;
            border-radius:6px;
            margin:2px 4px;
        }

        [data-baseweb="popover"] li:hover {
            background:rgba(212,175,55,0.12) !important;
            color:#d4af37 !important;
            padding-left:12px;
        }

        [data-baseweb="popover"] li[aria-selected="true"] {
            background:rgba(212,175,55,0.18) !important;
            color:#d4af37 !important;
            font-weight:600;
        }

        /*================================================================
          ★  SLIDERS — gold track and thumb
          =================================================================*/
        [data-testid="stSlider"] [role="slider"] {
            background:linear-gradient(135deg, #d4af37, #e8c84a) !important;
            border:2px solid rgba(255,255,255,0.2) !important;
            box-shadow:0 0 12px rgba(212,175,55,0.3), 0 2px 6px rgba(0,0,0,0.4);
            transition:all .2s ease;
            width:22px !important;
            height:22px !important;
        }

        [data-testid="stSlider"] [role="slider"]:hover {
            transform:scale(1.2);
            box-shadow:0 0 20px rgba(212,175,55,0.5), 0 2px 8px rgba(0,0,0,0.5);
        }

        [data-testid="stSlider"] [role="slider"]:focus {
            box-shadow:0 0 0 4px rgba(212,175,55,0.2), 0 0 15px rgba(212,175,55,0.3);
        }

        /* Slider active track (filled portion) */
        [data-testid="stSlider"] div[class*="Track-active"],
        [data-testid="stSlider"] div[style*="background-color"] {
            background:linear-gradient(90deg, rgba(212,175,55,0.4), rgba(212,175,55,0.6)) !important;
            border-radius:4px;
        }

        /*================================================================
          ★  TEXT AREA — dark glass with gold focus burst
          =================================================================*/
        [data-testid="stTextArea"] textarea {
            background:rgba(8,8,16,0.75) !important;
            border:1px solid rgba(212,175,55,0.12) !important;
            border-radius:12px !important;
            color:#e0e0ee !important;
            padding:16px 18px !important;
            font-size:15px !important;
            line-height:1.6;
            transition:all .35s ease !important;
            backdrop-filter:blur(12px);
            box-shadow:inset 0 2px 8px rgba(0,0,0,0.3);
        }

        [data-testid="stTextArea"] textarea::placeholder {
            color:#505068 !important;
            font-style:italic;
        }

        [data-testid="stTextArea"] textarea:focus {
            border-color:rgba(212,175,55,0.5) !important;
            box-shadow:
                0 0 30px rgba(212,175,55,0.1),
                inset 0 0 15px rgba(212,175,55,0.02),
                0 0 60px rgba(212,175,55,0.05) !important;
            outline:none !important;
            background:rgba(12,12,22,0.85) !important;
        }

        [data-testid="stTextArea"] label p {
            color:#d4af37 !important;
            font-weight:600;
        }

        /*================================================================
          ★  CHAT MESSAGES — glassmorphism bubbles with depth
          =================================================================*/
        .stChatMessage {
            border-radius:18px !important;
            padding:16px 20px !important;
            margin:8px 0 !important;
            backdrop-filter:blur(20px) !important;
            -webkit-backdrop-filter:blur(20px) !important;
            transition:all .3s cubic-bezier(0.25,0.46,0.45,0.94) !important;
            position:relative;
            overflow:hidden;
        }

        /* Shine sweep on chat bubbles */
        .stChatMessage::before {
            content:"";
            position:absolute;
            top:0; left:-100%; width:60%; height:100%;
            background:linear-gradient(90deg, transparent, rgba(255,255,255,0.03), transparent);
            transition:left .6s ease;
            pointer-events:none;
        }
        .stChatMessage:hover::before {
            left:120%;
        }

        /* User — warm gold tint */
        .stChatMessage:nth-child(odd),
        .stChatMessage[data-testid="stChatMessage-user"] {
            background:rgba(212,175,55,0.06) !important;
            border:1px solid rgba(212,175,55,0.18) !important;
            box-shadow:
                0 6px 25px rgba(0,0,0,0.35),
                0 0 15px rgba(212,175,55,0.05),
                inset 0 1px 0 rgba(212,175,55,0.08);
            margin-left:24px !important;
            animation:fadeInUp 0.4s ease-out both;
        }

        /* Assistant — cool blue-gray tint */
        .stChatMessage:nth-child(even),
        .stChatMessage[data-testid="stChatMessage-assistant"] {
            background:rgba(25,30,50,0.6) !important;
            border:1px solid rgba(90,110,170,0.15) !important;
            box-shadow:
                0 6px 25px rgba(0,0,0,0.35),
                0 0 15px rgba(90,110,170,0.04),
                inset 0 1px 0 rgba(90,110,170,0.06);
            margin-right:24px !important;
            animation:fadeInUp 0.4s ease-out both;
        }

        .stChatMessage:hover {
            transform:translateY(-3px) scale(1.005);
            box-shadow:
                0 10px 35px rgba(0,0,0,0.45),
                0 0 25px rgba(212,175,55,0.06);
        }

        .stChatMessage p, .stChatMessage span, .stChatMessage div {
            color:#e0e0ee !important;
            line-height:1.65;
        }

        /* Chat input */
        [data-testid="stChatInput"] {
            background:rgba(10,10,18,0.65) !important;
            border:1px solid rgba(212,175,55,0.12) !important;
            border-radius:14px !important;
            backdrop-filter:blur(16px);
            box-shadow:0 4px 15px rgba(0,0,0,0.3);
            transition:border-color .3s ease, box-shadow .3s ease;
        }

        [data-testid="stChatInput"]:focus-within {
            border-color:rgba(212,175,55,0.35) !important;
            box-shadow:0 0 25px rgba(212,175,55,0.08);
        }

        [data-testid="stChatInput"] textarea {
            background:transparent !important;
            color:#e0e0ee !important;
        }

        [data-testid="stChatInput"] textarea::placeholder {
            color:#505068 !important;
        }

        /*================================================================
          ★  SPINNER — bold gold ring
          =================================================================*/
        [data-testid="stSpinner"] > div {
            border:3px solid rgba(212,175,55,0.15) !important;
            border-top-color:#d4af37 !important;
            border-right-color:rgba(245,230,163,0.5) !important;
            border-bottom-color:rgba(212,175,55,0.3) !important;
            border-left-color:rgba(232,180,184,0.4) !important;
            animation:spinGold 0.7s cubic-bezier(0.4,0,0.2,1) infinite !important;
            box-shadow:0 0 15px rgba(212,175,55,0.2);
        }

        /*================================================================
          ★  ALERTS — success/warning/error/info all restyled
          =================================================================*/
        [data-testid="stAlert"] [data-baseweb="notification"] {
            backdrop-filter:blur(16px);
            border-radius:12px !important;
            padding:14px 18px !important;
            box-shadow:0 6px 25px rgba(0,0,0,0.3);
            animation:fadeInUp 0.4s ease-out both;
            border-left:4px solid !important;
        }

        /* Success — emerald gold */
        [data-testid="stSuccess"] [data-baseweb="notification"],
        [data-testid="stAlert"] [data-baseweb="notification"][style*="green"] {
            background:rgba(16,40,22,0.75) !important;
            border-color:rgba(80,200,100,0.3) !important;
            border-left-color:#4ade80 !important;
            box-shadow:0 6px 25px rgba(0,0,0,0.3), 0 0 15px rgba(80,200,100,0.06);
        }

        /* Warning — amber gold */
        [data-testid="stWarning"] [data-baseweb="notification"],
        [data-testid="stAlert"] [data-baseweb="notification"][style*="amber"] {
            background:rgba(45,35,12,0.75) !important;
            border-color:rgba(212,175,55,0.3) !important;
            border-left-color:#d4af37 !important;
            box-shadow:0 6px 25px rgba(0,0,0,0.3), 0 0 15px rgba(212,175,55,0.08);
        }

        /* Error — deep red */
        [data-testid="stError"] [data-baseweb="notification"],
        [data-testid="stAlert"] [data-baseweb="notification"][style*="red"] {
            background:rgba(50,12,12,0.75) !important;
            border-color:rgba(220,80,80,0.3) !important;
            border-left-color:#ef4444 !important;
        }

        /* Info — soft blue */
        [data-testid="stInfo"] [data-baseweb="notification"],
        [data-testid="stAlert"] [data-baseweb="notification"][style*="blue"] {
            background:rgba(12,18,45,0.75) !important;
            border-color:rgba(100,140,220,0.25) !important;
            border-left-color:#60a5fa !important;
        }

        [data-testid="stAlert"] p {
            color:#e0e0ee !important;
            line-height:1.6;
        }

        /*================================================================
          ★  MARKDOWN CONTENT
          =================================================================*/
        .stMarkdown p, .stMarkdown li, .stMarkdown span {
            color:#c8c8d8 !important;
            line-height:1.75;
        }

        .stMarkdown strong, .stMarkdown b {
            color:#f0f0f8 !important;
        }

        .stMarkdown a {
            color:#d4af37 !important;
            text-decoration:none;
            border-bottom:1px solid rgba(212,175,55,0.3);
            transition:all .2s ease;
        }

        .stMarkdown a:hover {
            color:#e8b4b8 !important;
            border-bottom-color:rgba(232,180,184,0.4);
        }

        .stMarkdown code {
            background:rgba(212,175,55,0.06);
            border:1px solid rgba(212,175,55,0.12);
            border-radius:5px;
            padding:2px 7px;
            color:#e8b4b8;
            font-size:0.9em;
        }

        .stMarkdown pre {
            background:rgba(6,6,12,0.85) !important;
            border:1px solid rgba(212,175,55,0.1) !important;
            border-radius:10px !important;
            padding:18px !important;
            box-shadow:inset 0 2px 10px rgba(0,0,0,0.3);
        }

        .stMarkdown pre code {
            background:transparent;
            border:none;
            color:#c8c8d8;
        }

        /*================================================================
          ★  IMAGES — elegant frame with hover zoom
          =================================================================*/
        .stImage > img, .stImage img {
            border-radius:14px !important;
            box-shadow:0 6px 25px rgba(0,0,0,0.45);
            border:1px solid rgba(212,175,55,0.1);
            transition:all .4s cubic-bezier(0.25,0.46,0.45,0.94);
        }

        .stImage > img:hover, .stImage img:hover {
            transform:scale(1.03);
            box-shadow:0 12px 40px rgba(0,0,0,0.5), 0 0 25px rgba(212,175,55,0.08);
        }

        /*================================================================
          ★  SUBHEADERS
          =================================================================*/
        .stSubheader {
            color:#d4af37 !important;
            border-bottom:1px solid rgba(212,175,55,0.1);
            padding-bottom:10px !important;
            text-shadow:0 0 10px rgba(212,175,55,0.15);
        }

        /*================================================================
          ★  DIVIDERS
          =================================================================*/
        hr, [data-testid="stDivider"] {
            border:none !important;
            height:1px !important;
            background:linear-gradient(90deg,
                transparent 0%,
                rgba(212,175,55,0.25) 20%,
                rgba(212,175,55,0.4) 50%,
                rgba(212,175,55,0.25) 80%,
                transparent 100%) !important;
            margin:24px 0 !important;
        }

        /*================================================================
          ★  METRICS
          =================================================================*/
        [data-testid="stMetric"] {
            background:rgba(255,255,255,0.025) !important;
            border:1px solid rgba(212,175,55,0.1) !important;
            border-radius:12px !important;
            padding:18px !important;
            transition:all .3s ease;
        }

        [data-testid="stMetric"]:hover {
            transform:translateY(-3px);
            box-shadow:0 8px 25px rgba(0,0,0,0.35), 0 0 15px rgba(212,175,55,0.06);
            border-color:rgba(212,175,55,0.25);
        }

        [data-testid="stMetric"] label {
            color:#a0a0b0 !important;
        }

        [data-testid="stMetric"] [data-testid="stMetricValue"] {
            color:#d4af37 !important;
            font-weight:700;
        }

        /*================================================================
          ★  EXPANDERS
          =================================================================*/
        .stExpander > div > div {
            background:rgba(255,255,255,0.02) !important;
            border:1px solid rgba(212,175,55,0.08) !important;
            border-radius:12px !important;
            transition:all .3s ease;
        }

        .stExpander > div > div:hover {
            border-color:rgba(212,175,55,0.2);
        }

        /*================================================================
          ★  TABS
          =================================================================*/
        .stTabs [data-baseweb="tab-list"] {
            gap:4px;
            background:rgba(255,255,255,0.02);
            border-radius:10px;
            padding:5px;
            border:1px solid rgba(212,175,55,0.08);
        }

        .stTabs [data-baseweb="tab"] {
            border-radius:8px !important;
            color:#8080a0 !important;
            transition:all .3s ease;
            padding:8px 16px !important;
        }

        .stTabs [data-baseweb="tab"]:hover {
            background:rgba(212,175,55,0.08) !important;
            color:#e8b4b8 !important;
        }

        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background:rgba(212,175,55,0.15) !important;
            color:#d4af37 !important;
            font-weight:700;
            box-shadow:0 0 12px rgba(212,175,55,0.1);
        }

        /*================================================================
          ★  PROGRESS BAR
          =================================================================*/
        [data-testid="stProgressBar"] > div > div > div {
            background:linear-gradient(90deg, #d4af37, #f5e6a3, #d4af37) !important;
            background-size:200% 100% !important;
            animation:shimmer 2s linear infinite !important;
            border-radius:6px !important;
            box-shadow:0 0 12px rgba(212,175,55,0.4);
        }

        /*================================================================
          ★  NUMBER INPUT / TEXT INPUT
          =================================================================*/
        [data-testid="stNumberInput"] input,
        [data-testid="stTextInput"] input {
            background:rgba(8,8,16,0.75) !important;
            border:1px solid rgba(212,175,55,0.12) !important;
            border-radius:10px !important;
            color:#e0e0ee !important;
            padding:10px 14px !important;
            transition:all .3s ease;
            backdrop-filter:blur(8px);
        }

        [data-testid="stNumberInput"] input:focus,
        [data-testid="stTextInput"] input:focus {
            border-color:rgba(212,175,55,0.45) !important;
            box-shadow:0 0 20px rgba(212,175,55,0.1), inset 0 0 8px rgba(212,175,55,0.02) !important;
            outline:none !important;
        }

        [data-testid="stNumberInput"] label p,
        [data-testid="stTextInput"] label p {
            color:#d4af37 !important;
        }

        /*================================================================
          ★  CHECKBOX
          =================================================================*/
        [data-testid="stCheckbox"] label {
            color:#b0b0c0 !important;
            transition:color .2s ease;
        }

        [data-testid="stCheckbox"] label:hover {
            color:#e8b4b8 !important;
        }

        /*================================================================
          ★  SCROLLBARS — gold accent
          =================================================================*/
        ::-webkit-scrollbar {
            width:8px;
            height:8px;
        }

        ::-webkit-scrollbar-track {
            background:rgba(10,10,18,0.5);
        }

        ::-webkit-scrollbar-thumb {
            background:linear-gradient(180deg, rgba(212,175,55,0.3), rgba(212,175,55,0.15));
            border-radius:4px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background:linear-gradient(180deg, rgba(212,175,55,0.5), rgba(212,175,55,0.25));
        }

        /*================================================================
          ★  RESPONSIVE
          =================================================================*/
        @media (max-width:768px) {
            .main .block-container {
                padding-left:16px !important;
                padding-right:16px !important;
            }
            [data-testid="stSidebar"] {
                width:280px !important;
            }
            .stChatMessage {
                margin-left:4px !important;
                margin-right:4px !important;
            }
            [data-testid="stDataFrame"]:hover {
                transform:none !important;
            }
            .main h1 {
                font-size:1.5rem !important;
            }
        }

        @media (max-width:480px) {
            .main h1 { font-size:1.3rem !important; }
            .stButton > button {
                padding:10px 18px !important;
                font-size:13px !important;
            }
        }

        /*================================================================
          ★  GLOBAL TEXT COLOR
          =================================================================*/
        .main div, .main span, .main p, .main label {
            color:#c0c0d0;
        }

        .main a { color:#d4af37 !important; }
        .main a:hover { color:#e8b4b8 !important; }

        /*================================================================
          ★  TOOLTIP
          =================================================================*/
        [data-baseweb="tooltip"] {
            background:rgba(12,12,22,0.95) !important;
            border:1px solid rgba(212,175,55,0.2) !important;
            border-radius:8px !important;
            color:#e0e0ee !important;
            box-shadow:0 6px 20px rgba(0,0,0,0.5);
        }

        /*================================================================
          ★  CODE BLOCKS
          =================================================================*/
        [data-testid="stCodeBlock"] {
            background:rgba(6,6,12,0.85) !important;
            border:1px solid rgba(212,175,55,0.1) !important;
            border-radius:12px !important;
            box-shadow:inset 0 2px 10px rgba(0,0,0,0.3);
        }

        [data-testid="stCodeBlock"] code,
        [data-testid="stCodeBlock"] pre {
            color:#c8c8d8 !important;
        }

        /*================================================================
          ★  WRAPPER CARDS — subtle depth on all blocks
          =================================================================*/
        [data-testid="stVerticalBlock"] {
            background:rgba(255,255,255,0.015);
            border:1px solid rgba(255,255,255,0.02);
            border-radius:12px;
            padding:2px 0;
        }

        [data-testid="stHorizontalBlock"] {
            gap:20px;
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


# ---------------------------------------------------------------------------
# PLOTLY THEME HELPERS (OPTIONAL — only if you want chart internals dark)
# ---------------------------------------------------------------------------

def style_plotly_charts() -> dict:
    """
    Return a Plotly layout template dict with the luxury dark theme.
    This is OPTIONAL. The CSS already handles chart containers.
    Only use this if you also want Plotly's internal axes/gridlines/text dark.
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
                    "gridcolor": "rgba(212,175,55,0.08)",
                    "zerolinecolor": "rgba(212,175,55,0.15)",
                    "linecolor": "rgba(212,175,55,0.12)",
                    "tickfont": {"color": "#888898"},
                    "title": {"font": {"color": "#d4af37"}},
                },
                "yaxis": {
                    "gridcolor": "rgba(212,175,55,0.08)",
                    "zerolinecolor": "rgba(212,175,55,0.15)",
                    "linecolor": "rgba(212,175,55,0.12)",
                    "tickfont": {"color": "#888898"},
                    "title": {"font": {"color": "#d4af37"}},
                },
                "legend": {
                    "font": {"color": "#a0a0b0", "size": 12},
                    "bgcolor": "rgba(0,0,0,0)",
                    "bordercolor": "rgba(212,175,55,0.12)",
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
    OPTIONAL — CSS already makes containers look premium.
    Only call this if you ALSO want the chart internals (axes, gridlines, text) dark.
    """
    theme = style_plotly_charts()
    fig.update_layout(template=theme["template"]["layout"])
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="#0a0a0f",
    )
    for trace in fig.data:
        trace.hoverinfo = "all"
        if hasattr(trace, "marker"):
            trace.marker.line = dict(color="rgba(212,175,55,0.4)", width=1)
        if hasattr(trace, "line"):
            trace.line.width = 2
    return fig
