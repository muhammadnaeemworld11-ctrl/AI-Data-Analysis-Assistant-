"""
MotionSites-Inspired ULTIMATE 3D Animated Luxury Theme for Streamlit
=====================================================================
Reverse-engineered from https://motionsites.ai/ design system.
Pure CSS injection — no JS, no extra libraries.

Design DNA extracted from MotionSites.ai:
  - Background: #171717 | Cards: #292929 | Borders: rgba(255,255,255,0.1)
  - Card hover: translateY(-4px) + spring physics cubic-bezier(0,0,0.2,1)
  - Buttons: pill shape (9999px), gradient CTA purple-pink-orange
  - Animations: gradient-shift, shimmer, marquee, pulse
  - Transitions: 0.15s snappy for micro, 0.3s spring for cards

USAGE — add 2 lines to main.py, NOTHING else changes:

    from premium_theme import inject_premium_css
    inject_premium_css()   # right after st.set_page_config(...)
"""

import streamlit as st


def inject_premium_css() -> None:
    st.markdown(
        """
        <style>
        /*================================================================
          MOTIONSITES DNA — COLOR SYSTEM
          =================================================================*/
        :root {
            --bg-deep: #171717;
            --bg-card: #292929;
            --bg-elevated: #202020;
            --bg-subtle: #303030;
            --border-subtle: rgba(255,255,255,0.1);
            --border-glow: rgba(255,255,255,0.15);
            --text-primary: #f5f5f5;
            --text-muted: #ababab;
            --text-dim: rgba(255,255,255,0.5);
            --accent-purple: #a855f7;
            --accent-pink: #f472b6;
            --accent-orange: #fdba74;
            --accent-blue: #60a5fa;
            --spring: cubic-bezier(0, 0, 0.2, 1);
            --spring-bounce: cubic-bezier(0.34, 1.56, 0.64, 1);
            --snappy: cubic-bezier(0.4, 0, 0.2, 1);
        }

        /*================================================================
          HIDE DEFAULT STREAMLIT CHROME
          =================================================================*/
        #MainMenu{visibility:hidden}
        footer{visibility:hidden}
        [data-testid="stHeader"]{padding:0!important;background:transparent!important}

        /*================================================================
          ★ ANIMATED BACKGROUND — gradient-shift inspired by motionsites
          =================================================================*/
        @keyframes gradientShiftMotion {
            0%   {background-position: 0% 50%}
            25%  {background-position: 50% 0%}
            50%  {background-position: 100% 50%}
            75%  {background-position: 50% 100%}
            100% {background-position: 0% 50%}
        }
        @keyframes orbFloat1 {
            0%,100%{transform:translate(0,0) scale(1);opacity:.3}
            33%{transform:translate(30px,-20px) scale(1.1);opacity:.5}
            66%{transform:translate(-15px,15px) scale(.95);opacity:.35}
        }
        @keyframes orbFloat2 {
            0%,100%{transform:translate(0,0) scale(1);opacity:.2}
            50%{transform:translate(-25px,-30px) scale(1.15);opacity:.4}
        }
        @keyframes orbFloat3 {
            0%,100%{transform:translate(0,0);opacity:.25}
            40%{transform:translate(20px,25px);opacity:.45}
            80%{transform:translate(-10px,-15px);opacity:.2}
        }
        @keyframes gridPulse {
            0%,100%{opacity:.03}
            50%{opacity:.07}
        }

        [data-testid="stAppViewContainer"] {
            background: #171717 !important;
            background-image:
                radial-gradient(ellipse 900px 600px at 15% 20%, rgba(168,85,247,0.06) 0%, transparent 70%),
                radial-gradient(ellipse 700px 500px at 85% 80%, rgba(244,114,182,0.05) 0%, transparent 70%),
                radial-gradient(ellipse 500px 500px at 50% 50%, rgba(96,165,250,0.03) 0%, transparent 60%);
            background-size: 200% 200% !important;
            animation: gradientShiftMotion 18s ease infinite !important;
            min-height:100vh;
            overflow-x:hidden;
        }

        /* Floating gradient orbs — 3D depth feel */
        [data-testid="stAppViewContainer"]::before {
            content:"";
            position:fixed; inset:0;
            pointer-events:none; z-index:0;
            background:
                radial-gradient(circle 500px at 20% 30%, rgba(168,85,247,0.07), transparent),
                radial-gradient(circle 400px at 75% 65%, rgba(244,114,182,0.06), transparent),
                radial-gradient(circle 300px at 60% 15%, rgba(253,186,116,0.04), transparent);
            animation: orbFloat1 12s ease-in-out infinite;
        }
        [data-testid="stAppViewContainer"]::after {
            content:"";
            position:fixed; inset:0;
            pointer-events:none; z-index:0;
            background:
                radial-gradient(circle 450px at 80% 20%, rgba(96,165,250,0.05), transparent),
                radial-gradient(circle 350px at 10% 85%, rgba(168,85,247,0.04), transparent);
            animation: orbFloat2 15s ease-in-out infinite;
        }

        /* Subtle animated grid pattern overlay */
        .main .block-container::before {
            content:"";
            position:fixed; inset:0;
            pointer-events:none; z-index:0;
            background-image:
                linear-gradient(rgba(255,255,255,0.02) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.02) 1px, transparent 1px);
            background-size:60px 60px;
            animation: gridPulse 8s ease-in-out infinite;
        }

        .main .block-container { position:relative; z-index:1; }

        /*================================================================
          ★ KEYFRAME LIBRARY — all animations
          =================================================================*/
        @keyframes float3D {
            0%,100%{transform:translateY(0) rotateX(0deg) rotateY(0deg)}
            25%{transform:translateY(-8px) rotateX(1deg) rotateY(-0.5deg)}
            50%{transform:translateY(-12px) rotateX(0deg) rotateY(0.5deg)}
            75%{transform:translateY(-6px) rotateX(-1deg) rotateY(-0.3deg)}
        }
        @keyframes shimmerMotion {
            0%{background-position:-300% center}
            100%{background-position:300% center}
        }
        @keyframes fadeInUp3D {
            from{opacity:0;transform:translateY(30px) translateZ(-20px) rotateX(3deg) scale(0.97)}
            to{opacity:1;transform:translateY(0) translateZ(0) rotateX(0) scale(1)}
        }
        @keyframes slideInRight {
            from{opacity:0;transform:translateX(40px) perspective(800px) rotateY(-5deg)}
            to{opacity:1;transform:translateX(0) perspective(800px) rotateY(0)}
        }
        @keyframes slideInLeft {
            from{opacity:0;transform:translateX(-40px) perspective(800px) rotateY(5deg)}
            to{opacity:1;transform:translateX(0) perspective(800px) rotateY(0)}
        }
        @keyframes glowPulse3D {
            0%,100%{box-shadow:0 0 0 rgba(168,85,247,0), 0 0 0 rgba(168,85,247,0);border-color:rgba(255,255,255,0.1)}
            50%{box-shadow:0 0 20px rgba(168,85,247,0.15), 0 0 40px rgba(168,85,247,0.05);border-color:rgba(255,255,255,0.18)}
        }
        @keyframes borderGlowPulse {
            0%,100%{border-color:rgba(255,255,255,0.1);box-shadow:inset 0 0 0 rgba(168,85,247,0)}
            50%{border-color:rgba(168,85,247,0.4);box-shadow:inset 0 0 20px rgba(168,85,247,0.05),0 0 15px rgba(168,85,247,0.08)}
        }
        @keyframes spinGradient {
            0%{--angle:0deg}
            100%{--angle:360deg}
        }
        @keyframes breathe {
            0%,100%{transform:scale(1);opacity:.85}
            50%{transform:scale(1.02);opacity:1}
        }
        @keyframes textReveal {
            from{clip-path:inset(0 100% 0 0)}
            to{clip-path:inset(0 0% 0 0)}
        }
        @keyframes scanlineMove {
            0%{top:-10%}
            100%{top:110%}
        }
        @keyframes marqueeGradient {
            0%{background-position:0% 50%}
            50%{background-position:100% 50%}
            100%{background-position:0% 50%}
        }
        @keyframes tilt3D {
            0%,100%{transform:perspective(1000px) rotateX(0) rotateY(0) scale(1)}
            25%{transform:perspective(1000px) rotateX(1.5deg) rotateY(-1deg) scale(1.01)}
            50%{transform:perspective(1000px) rotateX(0) rotateY(1.5deg) scale(1.02)}
            75%{transform:perspective(1000px) rotateX(-1deg) rotateY(0) scale(1.01)}
        }
        @keyframes cardEnter {
            from{opacity:0;transform:perspective(800px) translateZ(-30px) translateY(20px) scale(0.95)}
            to{opacity:1;transform:perspective(800px) translateZ(0) translateY(0) scale(1)}
        }

        /*================================================================
          ★ TITLE — 3D floating gradient text (motionsites hero style)
          =================================================================*/
        .main [data-testid="stVerticalBlock"]:first-child {
            animation: float3D 7s ease-in-out infinite;
            transform-style:preserve-3d;
        }

        .main h1,
        .main [data-testid="stTitle"] {
            background: linear-gradient(90deg,
                #f5f5f5 0%, #a855f7 15%, #f472b6 30%,
                #f5f5f5 45%, #fdba74 60%, #60a5fa 75%,
                #f5f5f5 90%, #a855f7 100%);
            background-size: 400% 100% !important;
            -webkit-background-clip:text !important;
            -webkit-text-fill-color:transparent !important;
            background-clip:text !important;
            animation: shimmerMotion 6s linear infinite !important;
            filter: drop-shadow(0 0 30px rgba(168,85,247,0.2))
                    drop-shadow(0 4px 8px rgba(0,0,0,0.4));
            font-weight:800 !important;
            letter-spacing:-0.02em;
            transform-style:preserve-3d;
        }

        .main h2, .main h3 {
            color:#f5f5f5 !important;
            font-weight:700 !important;
            position:relative;
        }

        .main h2::after, .main h3::after {
            content:"";
            position:absolute;
            bottom:-6px; left:0;
            width:40px; height:3px;
            background:linear-gradient(90deg, #a855f7, #f472b6, #fdba74);
            border-radius:2px;
            animation: breathe 4s ease-in-out infinite;
        }

        .main h4 { color:#e5e5e5 !important; }

        /*================================================================
          ★ SECTION ANIMATIONS — 3D fade-in with stagger
          =================================================================*/
        .main [data-testid="stVerticalBlock"] {
            animation: cardEnter 0.6s var(--spring, cubic-bezier(0,0,0.2,1)) both;
            transform-style:preserve-3d;
        }
        .main [data-testid="stVerticalBlock"]:nth-child(1){animation-delay:0s}
        .main [data-testid="stVerticalBlock"]:nth-child(2){animation-delay:.06s}
        .main [data-testid="stVerticalBlock"]:nth-child(3){animation-delay:.12s}
        .main [data-testid="stVerticalBlock"]:nth-child(4){animation-delay:.18s}
        .main [data-testid="stVerticalBlock"]:nth-child(5){animation-delay:.24s}
        .main [data-testid="stVerticalBlock"]:nth-child(6){animation-delay:.30s}
        .main [data-testid="stVerticalBlock"]:nth-child(7){animation-delay:.36s}
        .main [data-testid="stVerticalBlock"]:nth-child(8){animation-delay:.42s}
        .main [data-testid="stVerticalBlock"]:nth-child(9){animation-delay:.48s}
        .main [data-testid="stVerticalBlock"]:nth-child(10){animation-delay:.54s}

        /*================================================================
          ★ SIDEBAR — motionsites card + glassmorphism
          =================================================================*/
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg,
                rgba(23,23,23,0.95) 0%,
                rgba(25,25,25,0.92) 50%,
                rgba(23,23,23,0.95) 100%) !important;
            backdrop-filter:blur(24px) saturate(1.3) !important;
            -webkit-backdrop-filter:blur(24px) saturate(1.3) !important;
            border-right:1px solid var(--border-subtle) !important;
            box-shadow:4px 0 40px rgba(0,0,0,0.4);
        }

        /* Subtle gradient line on sidebar left edge */
        [data-testid="stSidebar"]::before {
            content:"";
            position:absolute;
            top:0; bottom:0; left:0; width:2px;
            background:linear-gradient(180deg,
                transparent 0%,
                #a855f7 20%,
                #f472b6 50%,
                #fdba74 80%,
                transparent 100%);
            opacity:.4;
            animation:marqueeGradient 8s ease infinite;
            background-size:200% 200%;
        }

        [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
            color:#f5f5f5 !important;
            background:none !important;
            -webkit-text-fill-color:#f5f5f5 !important;
        }

        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] span {
            color:var(--text-muted) !important;
            transition:color .15s var(--snappy);
        }

        [data-testid="stSidebar"] p:hover,
        [data-testid="stSidebar"] label:hover {
            color:#f5f5f5 !important;
        }

        /* Sidebar radio — card style like motionsites */
        [data-testid="stSidebar"] [data-testid="stRadio"] {
            background:var(--bg-card) !important;
            border:1px solid var(--border-subtle) !important;
            border-radius:16px !important;
            padding:6px 14px !important;
            margin-bottom:6px !important;
            transition:all .3s var(--spring) !important;
        }

        [data-testid="stSidebar"] [data-testid="stRadio"]:hover {
            background:var(--bg-elevated) !important;
            border-color:var(--border-glow) !important;
            transform:translateX(4px);
        }

        /* Active radio — 3D glow pulse */
        [data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] {
            background:rgba(168,85,247,0.12) !important;
            border-color:rgba(168,85,247,0.3) !important;
            border-radius:12px;
            animation: glowPulse3D 4s ease-in-out infinite !important;
        }

        [data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] p,
        [data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] span {
            color:#f5f5f5 !important;
            font-weight:600;
        }

        /* Sidebar divider */
        [data-testid="stSidebar"] hr,
        [data-testid="stSidebar"] [data-testid="stDivider"] {
            border:none !important;
            height:1px !important;
            background:linear-gradient(90deg, transparent, rgba(168,85,247,0.2), transparent) !important;
            margin:18px 0 !important;
        }

        /* Sidebar sections slide in */
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
            animation: slideInLeft 0.5s var(--spring) both;
        }
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"]:nth-child(2){animation-delay:.08s}
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"]:nth-child(3){animation-delay:.16s}
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"]:nth-child(4){animation-delay:.24s}
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"]:nth-child(5){animation-delay:.32s}

        /*================================================================
          ★ BUTTONS — pill shape + gradient CTA (motionsites style)
          =================================================================*/
        /* Primary buttons — white CTA like motionsites */
        .stButton > button,
        [data-testid="stButton"] > button,
        [data-testid="stFormSubmitButton"] > button {
            background:linear-gradient(135deg, #a855f7 0%, #f472b6 40%, #fdba74 100%) !important;
            background-size:200% 200% !important;
            color:#f5f5f5 !important;
            font-weight:600 !important;
            font-size:14px !important;
            letter-spacing:0.01em;
            border:none !important;
            border-radius:9999px !important;
            padding:10px 28px !important;
            box-shadow:
                0 4px 15px rgba(168,85,247,0.3),
                0 2px 4px rgba(0,0,0,0.3);
            transition:all .3s var(--spring-bounce) !important;
            cursor:pointer;
            position:relative;
            top:0;
            animation:breathe 5s ease-in-out infinite;
            transform-style:preserve-3d;
            text-shadow:0 1px 3px rgba(0,0,0,0.3);
        }

        .stButton > button:hover,
        [data-testid="stButton"] > button:hover,
        [data-testid="stFormSubmitButton"] > button:hover {
            transform:translateY(-4px) scale(1.03) !important;
            box-shadow:
                0 12px 35px rgba(168,85,247,0.4),
                0 6px 12px rgba(0,0,0,0.3),
                0 0 50px rgba(168,85,247,0.1);
            background-position:100% 0% !important;
        }

        .stButton > button:active,
        [data-testid="stButton"] > button:active,
        [data-testid="stFormSubmitButton"] > button:active {
            transform:translateY(2px) scale(0.98) !important;
            box-shadow:0 1px 4px rgba(168,85,247,0.2), 0 0 1px rgba(0,0,0,0.3);
            transition-duration:.1s !important;
        }

        /* File uploader button — secondary style */
        [data-testid="stFileUploader"] button {
            background:var(--bg-elevated) !important;
            border:1px solid var(--border-subtle) !important;
            color:var(--text-primary) !important;
            border-radius:9999px !important;
            padding:8px 20px !important;
            transition:all .15s var(--snappy);
        }
        [data-testid="stFileUploader"] button:hover {
            background:var(--bg-subtle) !important;
            border-color:var(--border-glow) !important;
            box-shadow:0 0 15px rgba(168,85,247,0.1);
        }

        /*================================================================
          ★ FILE UPLOADER — animated border
          =================================================================*/
        [data-testid="stFileUploader"] section {
            background:rgba(41,41,41,0.5) !important;
            border:1.5px dashed var(--border-subtle) !important;
            border-radius:20px !important;
            padding:28px 20px !important;
            animation:borderGlowPulse 4s ease-in-out infinite !important;
            transition:all .3s var(--spring) !important;
            position:relative;
            overflow:hidden;
        }

        /* Scanline sweep */
        [data-testid="stFileUploader"] section::after {
            content:"";
            position:absolute;
            left:0; right:0;
            height:50px;
            background:linear-gradient(180deg,
                transparent, rgba(168,85,247,0.06), transparent);
            animation:scanlineMove 5s linear infinite;
            pointer-events:none;
        }

        [data-testid="stFileUploader"] section:hover {
            border-color:rgba(168,85,247,0.4) !important;
            background:rgba(41,41,41,0.7) !important;
            box-shadow:0 0 40px rgba(168,85,247,0.08), inset 0 0 30px rgba(168,85,247,0.03);
            transform:scale(1.005);
        }

        [data-testid="stFileUploader"] label p,
        [data-testid="stFileUploader"] label span {
            color:var(--text-muted) !important;
            transition:color .15s var(--snappy);
        }
        [data-testid="stFileUploader"]:hover label p { color:#f5f5f5 !important; }

        /*================================================================
          ★ DATAFRAMES — motionsites .card-hover 3D
          =================================================================*/
        .stDataFrame, .stDataframe, [data-testid="stDataFrame"] {
            background:var(--bg-card) !important;
            border:1px solid var(--border-subtle) !important;
            border-radius:20px !important;
            overflow:hidden;
            box-shadow:none;
            transition:all .3s var(--spring) !important;
            transform-style:preserve-3d;
        }

        .stDataFrame:hover, .stDataframe:hover, [data-testid="stDataFrame"]:hover {
            transform:perspective(1000px) translateY(-6px) rotateX(2deg) rotateY(-1deg) scale(1.005) !important;
            box-shadow:
                0 25px 50px -12px rgba(0,0,0,0.5),
                0 0 30px rgba(168,85,247,0.06);
            border-color:rgba(168,85,247,0.2) !important;
        }

        /*================================================================
          ★ PLOTLY CHARTS — 3D card lift (motionsites card-hover)
          =================================================================*/
        [data-testid="stPlotlyChart"], .stPlotlyChart {
            border:1px solid var(--border-subtle) !important;
            border-radius:20px !important;
            overflow:hidden;
            box-shadow:none;
            transition:all .3s var(--spring) !important;
            transform-style:preserve-3d;
        }

        [data-testid="stPlotlyChart"]:hover, .stPlotlyChart:hover {
            transform:perspective(1000px) translateY(-6px) rotateX(1.5deg) rotateY(-0.5deg) !important;
            box-shadow:
                0 20px 40px -8px rgba(0,0,0,0.5),
                0 0 30px rgba(168,85,247,0.05);
            border-color:rgba(168,85,247,0.2) !important;
        }

        [data-testid="stPlotlyChart"] iframe,
        .stPlotlyChart iframe {
            background:transparent !important;
        }

        /*================================================================
          ★ SELECTBOX — pill container (motionsites filter button style)
          =================================================================*/
        [data-testid="stSelectbox"] {
            background:transparent;
            border-radius:12px;
            transition:all .15s var(--snappy);
        }

        [data-testid="stSelectbox"]:hover,
        [data-testid="stSelectbox"]:focus-within {
            background:rgba(255,255,255,0.02);
        }

        [data-testid="stSelectbox"] label p {
            color:var(--text-muted) !important;
            font-weight:500;
        }

        [data-testid="stSelectbox"] div[data-baseweb="select"] {
            background-color:var(--bg-elevated) !important;
            border:1px solid var(--border-subtle) !important;
            border-radius:12px !important;
            transition:all .15s var(--snappy);
        }

        [data-testid="stSelectbox"] div[data-baseweb="select"]:hover {
            border-color:var(--border-glow) !important;
        }

        [data-testid="stSelectbox"] div[data-baseweb="select"] span {
            color:#f5f5f5 !important;
        }

        /* Dropdown popover */
        [data-baseweb="popover"] {
            background:rgba(23,23,23,0.98) !important;
            border:1px solid var(--border-subtle) !important;
            border-radius:14px !important;
            box-shadow:0 20px 50px rgba(0,0,0,0.6), 0 0 1px rgba(255,255,255,0.1);
            backdrop-filter:blur(24px);
        }

        [data-baseweb="popover"] li {
            color:var(--text-muted) !important;
            transition:all .15s var(--snappy);
            border-radius:10px;
            margin:2px 6px;
        }

        [data-baseweb="popover"] li:hover {
            background:rgba(168,85,247,0.12) !important;
            color:#f5f5f5 !important;
            padding-left:16px;
        }

        [data-baseweb="popover"] li[aria-selected="true"] {
            background:rgba(168,85,247,0.18) !important;
            color:#f5f5f5 !important;
            font-weight:600;
        }

        /*================================================================
          ★ SLIDERS — accent colored
          =================================================================*/
        [data-testid="stSlider"] [role="slider"] {
            background:linear-gradient(135deg, #a855f7, #f472b6) !important;
            border:2px solid rgba(255,255,255,0.15) !important;
            box-shadow:0 0 10px rgba(168,85,247,0.25), 0 2px 6px rgba(0,0,0,0.4);
            transition:all .15s var(--snappy);
            width:20px !important; height:20px !important;
        }

        [data-testid="stSlider"] [role="slider"]:hover {
            transform:scale(1.25);
            box-shadow:0 0 20px rgba(168,85,247,0.4), 0 2px 8px rgba(0,0,0,0.5);
        }

        [data-testid="stSlider"] [role="slider"]:focus {
            box-shadow:0 0 0 4px rgba(168,85,247,0.15), 0 0 15px rgba(168,85,247,0.25);
        }

        [data-testid="stSlider"] div[class*="Track-active"] {
            background:linear-gradient(90deg, rgba(168,85,247,0.5), rgba(244,114,182,0.5)) !important;
            border-radius:4px;
        }

        /*================================================================
          ★ TEXT AREA — elevated dark card
          =================================================================*/
        [data-testid="stTextArea"] textarea {
            background:var(--bg-card) !important;
            border:1px solid var(--border-subtle) !important;
            border-radius:16px !important;
            color:#f5f5f5 !important;
            padding:16px 18px !important;
            font-size:15px !important;
            line-height:1.65;
            transition:all .3s var(--spring) !important;
            box-shadow:inset 0 2px 8px rgba(0,0,0,0.3);
        }

        [data-testid="stTextArea"] textarea::placeholder {
            color:var(--text-dim) !important;
        }

        [data-testid="stTextArea"] textarea:focus {
            border-color:rgba(168,85,247,0.4) !important;
            box-shadow:
                0 0 0 3px rgba(168,85,247,0.08),
                0 0 30px rgba(168,85,247,0.06),
                inset 0 0 10px rgba(168,85,247,0.02) !important;
            outline:none !important;
            background:var(--bg-elevated) !important;
        }

        [data-testid="stTextArea"] label p {
            color:var(--text-muted) !important;
            font-weight:500;
        }

        /*================================================================
          ★ CHAT MESSAGES — 3D glass bubbles
          =================================================================*/
        .stChatMessage {
            border-radius:20px !important;
            padding:16px 20px !important;
            margin:8px 0 !important;
            backdrop-filter:blur(20px) saturate(1.2) !important;
            -webkit-backdrop-filter:blur(20px) saturate(1.2) !important;
            transition:all .3s var(--spring) !important;
            transform-style:preserve-3d;
            position:relative;
            overflow:hidden;
            box-shadow:0 4px 20px rgba(0,0,0,0.2);
        }

        /* Shine sweep */
        .stChatMessage::before {
            content:"";
            position:absolute;
            top:0; left:-100%; width:60%; height:100%;
            background:linear-gradient(90deg, transparent, rgba(255,255,255,0.04), transparent);
            transition:left .6s ease;
            pointer-events:none;
        }
        .stChatMessage:hover::before { left:140%; }

        /* User — purple/pink tint */
        .stChatMessage:nth-child(odd),
        .stChatMessage[data-testid="stChatMessage-user"] {
            background:rgba(168,85,247,0.08) !important;
            border:1px solid rgba(168,85,247,0.15) !important;
            margin-left:24px !important;
            animation:slideInRight 0.4s var(--spring) both;
        }

        /* Assistant — blue tint */
        .stChatMessage:nth-child(even),
        .stChatMessage[data-testid="stChatMessage-assistant"] {
            background:rgba(96,165,250,0.06) !important;
            border:1px solid rgba(96,165,250,0.1) !important;
            margin-right:24px !important;
            animation:slideInLeft 0.4s var(--spring) both;
        }

        .stChatMessage:hover {
            transform:perspective(600px) translateY(-3px) rotateX(1.5deg) scale(1.005) !important;
            box-shadow:0 12px 35px rgba(0,0,0,0.35), 0 0 20px rgba(168,85,247,0.05);
        }

        .stChatMessage p, .stChatMessage span, .stChatMessage div {
            color:#e5e5e5 !important;
            line-height:1.65;
        }

        /* Chat input */
        [data-testid="stChatInput"] {
            background:var(--bg-card) !important;
            border:1px solid var(--border-subtle) !important;
            border-radius:16px !important;
            box-shadow:0 4px 15px rgba(0,0,0,0.25);
            transition:all .3s var(--spring);
        }

        [data-testid="stChatInput"]:focus-within {
            border-color:rgba(168,85,247,0.3) !important;
            box-shadow:0 0 25px rgba(168,85,247,0.08);
        }

        [data-testid="stChatInput"] textarea {
            background:transparent !important;
            color:#f5f5f5 !important;
        }

        [data-testid="stChatInput"] textarea::placeholder { color:var(--text-dim) !important; }

        /*================================================================
          ★ SPINNER — gradient ring
          =================================================================*/
        [data-testid="stSpinner"] > div {
            border:3px solid rgba(168,85,247,0.15) !important;
            border-top-color:#a855f7 !important;
            border-right-color:#f472b6 !important;
            border-bottom-color:rgba(96,165,250,0.3) !important;
            border-left-color:#fdba74 !important;
            animation:spin .7s linear infinite !important;
            box-shadow:0 0 15px rgba(168,85,247,0.15);
        }

        @keyframes spin { to{transform:rotate(360deg)} }

        /*================================================================
          ★ ALERTS — card-style
          =================================================================*/
        [data-testid="stAlert"] [data-baseweb="notification"] {
            backdrop-filter:blur(20px);
            border-radius:16px !important;
            padding:14px 18px !important;
            box-shadow:0 8px 30px rgba(0,0,0,0.3);
            animation:fadeInUp3D 0.4s var(--spring) both;
            border-left:3px solid !important;
        }

        [data-testid="stSuccess"] [data-baseweb="notification"],
        [data-testid="stAlert"] [data-baseweb="notification"][style*="green"] {
            background:rgba(34,197,94,0.08) !important;
            border:1px solid rgba(34,197,94,0.15) !important;
            border-left-color:#22c55e !important;
        }

        [data-testid="stWarning"] [data-baseweb="notification"],
        [data-testid="stAlert"] [data-baseweb="notification"][style*="amber"] {
            background:rgba(253,186,116,0.08) !important;
            border:1px solid rgba(253,186,116,0.15) !important;
            border-left-color:#fdba74 !important;
        }

        [data-testid="stError"] [data-baseweb="notification"],
        [data-testid="stAlert"] [data-baseweb="notification"][style*="red"] {
            background:rgba(239,68,68,0.08) !important;
            border:1px solid rgba(239,68,68,0.15) !important;
            border-left-color:#ef4444 !important;
        }

        [data-testid="stInfo"] [data-baseweb="notification"],
        [data-testid="stAlert"] [data-baseweb="notification"][style*="blue"] {
            background:rgba(96,165,250,0.08) !important;
            border:1px solid rgba(96,165,250,0.15) !important;
            border-left-color:#60a5fa !important;
        }

        [data-testid="stAlert"] p { color:#e5e5e5 !important; line-height:1.6; }

        /*================================================================
          ★ MARKDOWN CONTENT
          =================================================================*/
        .stMarkdown p, .stMarkdown li, .stMarkdown span {
            color:var(--text-muted) !important;
            line-height:1.75;
        }
        .stMarkdown strong, .stMarkdown b { color:#f5f5f5 !important; }
        .stMarkdown a {
            color:#a855f7 !important;
            text-decoration:none;
            border-bottom:1px solid rgba(168,85,247,0.2);
            transition:all .15s var(--snappy);
        }
        .stMarkdown a:hover {
            color:#f472b6 !important;
            border-bottom-color:rgba(244,114,182,0.3);
        }
        .stMarkdown code {
            background:rgba(168,85,247,0.08);
            border:1px solid rgba(168,85,247,0.12);
            border-radius:6px;
            padding:2px 7px;
            color:#f472b6;
        }
        .stMarkdown pre {
            background:rgba(15,15,20,0.9) !important;
            border:1px solid var(--border-subtle) !important;
            border-radius:14px !important;
            padding:18px !important;
            box-shadow:inset 0 2px 10px rgba(0,0,0,0.3);
        }
        .stMarkdown pre code {
            background:transparent; border:none; color:#e5e5e5;
        }

        /*================================================================
          ★ IMAGES — rounded with 3D hover
          =================================================================*/
        .stImage > img, .stImage img {
            border-radius:16px !important;
            box-shadow:0 4px 20px rgba(0,0,0,0.4);
            border:1px solid var(--border-subtle);
            transition:all .3s var(--spring);
            transform-style:preserve-3d;
        }
        .stImage > img:hover, .stImage img:hover {
            transform:perspective(600px) scale(1.02) rotateY(2deg) !important;
            box-shadow:0 15px 40px rgba(0,0,0,0.5), 0 0 20px rgba(168,85,247,0.06);
        }

        /*================================================================
          ★ DIVIDERS — gradient fade
          =================================================================*/
        hr, [data-testid="stDivider"] {
            border:none !important;
            height:1px !important;
            background:linear-gradient(90deg,
                transparent 0%,
                rgba(168,85,247,0.2) 30%,
                rgba(244,114,182,0.25) 50%,
                rgba(168,85,247,0.2) 70%,
                transparent 100%) !important;
            margin:24px 0 !important;
        }

        /*================================================================
          ★ SUBHEADER
          =================================================================*/
        .stSubheader {
            color:#f5f5f5 !important;
            background:none !important;
            -webkit-text-fill-color:#f5f5f5 !important;
            border-bottom:1px solid rgba(168,85,247,0.1);
            padding-bottom:10px !important;
        }

        /*================================================================
          ★ METRICS — card style
          =================================================================*/
        [data-testid="stMetric"] {
            background:var(--bg-card) !important;
            border:1px solid var(--border-subtle) !important;
            border-radius:16px !important;
            padding:18px !important;
            transition:all .3s var(--spring);
            transform-style:preserve-3d;
        }
        [data-testid="stMetric"]:hover {
            transform:translateY(-4px) !important;
            box-shadow:0 12px 30px rgba(0,0,0,0.35);
            border-color:rgba(168,85,247,0.2);
        }
        [data-testid="stMetric"] label { color:var(--text-muted) !important; }
        [data-testid="stMetric"] [data-testid="stMetricValue"] {
            color:#f5f5f5 !important;
            font-weight:700;
        }

        /*================================================================
          ★ EXPANDERS
          =================================================================*/
        .stExpander > div > div {
            background:var(--bg-card) !important;
            border:1px solid var(--border-subtle) !important;
            border-radius:16px !important;
            transition:all .3s var(--spring);
        }
        .stExpander > div > div:hover {
            border-color:rgba(168,85,247,0.2);
        }

        /*================================================================
          ★ TABS — pill style (motionsites filter tabs)
          =================================================================*/
        .stTabs [data-baseweb="tab-list"] {
            gap:4px;
            background:var(--bg-card);
            border-radius:9999px !important;
            padding:4px;
            border:1px solid var(--border-subtle);
        }
        .stTabs [data-baseweb="tab"] {
            border-radius:9999px !important;
            color:var(--text-muted) !important;
            transition:all .15s var(--snappy);
            padding:8px 18px !important;
        }
        .stTabs [data-baseweb="tab"]:hover {
            background:rgba(168,85,247,0.08) !important;
            color:#f5f5f5 !important;
        }
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background:rgba(168,85,247,0.15) !important;
            color:#f5f5f5 !important;
            font-weight:600;
            box-shadow:0 0 10px rgba(168,85,247,0.08);
        }

        /*================================================================
          ★ PROGRESS BAR — gradient shimmer
          =================================================================*/
        [data-testid="stProgressBar"] > div > div > div {
            background:linear-gradient(90deg, #a855f7, #f472b6, #fdba74, #a855f7) !important;
            background-size:300% 100% !important;
            animation:marqueeGradient 2s linear infinite !important;
            border-radius:6px !important;
            box-shadow:0 0 12px rgba(168,85,247,0.3);
        }

        /*================================================================
          ★ INPUTS
          =================================================================*/
        [data-testid="stNumberInput"] input,
        [data-testid="stTextInput"] input {
            background:var(--bg-card) !important;
            border:1px solid var(--border-subtle) !important;
            border-radius:12px !important;
            color:#f5f5f5 !important;
            padding:10px 14px !important;
            transition:all .15s var(--snappy);
        }
        [data-testid="stNumberInput"] input:focus,
        [data-testid="stTextInput"] input:focus {
            border-color:rgba(168,85,247,0.4) !important;
            box-shadow:0 0 0 3px rgba(168,85,247,0.08) !important;
            outline:none !important;
        }
        [data-testid="stNumberInput"] label p,
        [data-testid="stTextInput"] label p {
            color:var(--text-muted) !important;
        }

        /*================================================================
          ★ CHECKBOX
          =================================================================*/
        [data-testid="stCheckbox"] label { color:var(--text-muted) !important; transition:color .15s var(--snappy); }
        [data-testid="stCheckbox"] label:hover { color:#f5f5f5 !important; }

        /*================================================================
          ★ SCROLLBARS
          =================================================================*/
        ::-webkit-scrollbar { width:6px; height:6px; }
        ::-webkit-scrollbar-track { background:transparent; }
        ::-webkit-scrollbar-thumb {
            background:rgba(168,85,247,0.25);
            border-radius:3px;
        }
        ::-webkit-scrollbar-thumb:hover { background:rgba(168,85,247,0.4); }

        /*================================================================
          ★ TOOLTIP
          =================================================================*/
        [data-baseweb="tooltip"] {
            background:rgba(23,23,23,0.97) !important;
            border:1px solid var(--border-subtle) !important;
            border-radius:10px !important;
            color:#f5f5f5 !important;
            box-shadow:0 8px 25px rgba(0,0,0,0.5);
        }

        /*================================================================
          ★ CODE BLOCKS
          =================================================================*/
        [data-testid="stCodeBlock"] {
            background:rgba(15,15,20,0.9) !important;
            border:1px solid var(--border-subtle) !important;
            border-radius:16px !important;
            box-shadow:inset 0 2px 10px rgba(0,0,0,0.3);
        }
        [data-testid="stCodeBlock"] code,
        [data-testid="stCodeBlock"] pre { color:#e5e5e5 !important; }

        /*================================================================
          ★ GLOBAL TEXT
          =================================================================*/
        .main div, .main span, .main p, .main label { color:var(--text-muted); }
        .main a { color:#a855f7 !important; }
        .main a:hover { color:#f472b6 !important; }

        /*================================================================
          ★ BLOCK CARDS — subtle 3D depth on all vertical blocks
          =================================================================*/
        [data-testid="stVerticalBlock"] {
            background:rgba(255,255,255,0.015);
            border:1px solid rgba(255,255,255,0.03);
            border-radius:16px;
            padding:2px 0;
            transition:all .3s var(--spring);
            transform-style:preserve-3d;
        }

        [data-testid="stVerticalBlock"]:hover {
            border-color:rgba(255,255,255,0.06);
            background:rgba(255,255,255,0.02);
        }

        [data-testid="stHorizontalBlock"] { gap:16px; }

        /*================================================================
          ★ RESPONSIVE
          =================================================================*/
        @media (max-width:768px) {
            .main .block-container {
                padding-left:16px !important;
                padding-right:16px !important;
            }
            [data-testid="stSidebar"] { width:280px !important; }
            .stChatMessage { margin-left:4px !important; margin-right:4px !important; }
            [data-testid="stDataFrame"]:hover,
            [data-testid="stPlotlyChart"]:hover {
                transform:translateY(-3px) !important;
            }
        }
        @media (max-width:480px) {
            .main h1 { font-size:1.4rem !important; }
            .stButton > button { padding:8px 20px !important; font-size:13px !important; }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


def style_plotly_charts() -> dict:
    """Return a Plotly layout template matching the motionsites dark theme.
    OPTIONAL — the CSS already handles chart containers."""
    return {
        "template": {
            "layout": {
                "paper_bgcolor": "rgba(0,0,0,0)",
                "plot_bgcolor": "#171717",
                "font": {"family": "-apple-system, BlinkMacSystemFont, Segoe UI, Roboto, sans-serif",
                         "color": "#ababab", "size": 13},
                "title": {"font": {"color": "#f5f5f5", "size": 17}},
                "xaxis": {"gridcolor": "rgba(255,255,255,0.06)",
                           "zerolinecolor": "rgba(255,255,255,0.1)",
                           "linecolor": "rgba(255,255,255,0.08)",
                           "tickfont": {"color": "#ababab"},
                           "title": {"font": {"color": "#f5f5f5"}}},
                "yaxis": {"gridcolor": "rgba(255,255,255,0.06)",
                           "zerolinecolor": "rgba(255,255,255,0.1)",
                           "linecolor": "rgba(255,255,255,0.08)",
                           "tickfont": {"color": "#ababab"},
                           "title": {"font": {"color": "#f5f5f5"}}},
                "legend": {"font": {"color": "#ababab", "size": 12},
                           "bgcolor": "rgba(0,0,0,0)",
                           "bordercolor": "rgba(255,255,255,0.08)", "borderwidth": 1},
                "colorway": ["#a855f7", "#f472b6", "#fdba74", "#60a5fa",
                             "#34d399", "#fbbf24", "#f87171", "#818cf8",
                             "#2dd4bf", "#fb923c"],
                "hoverlabel": {"bgcolor": "#292929",
                               "bordercolor": "rgba(168,85,247,0.3)",
                               "font": {"color": "#f5f5f5", "size": 13}},
                "modebar": {"bgcolor": "transparent", "color": "#ababab",
                            "activecolor": "#a855f7"},
            }
        }
    }


def apply_chart_theme(fig) -> object:
    """Apply the motionsites dark theme to a Plotly figure. OPTIONAL."""
    theme = style_plotly_charts()
    fig.update_layout(template=theme["template"]["layout"])
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="#171717")
    for trace in fig.data:
        trace.hoverinfo = "all"
        if hasattr(trace, "marker"):
            trace.marker.line = dict(color="rgba(168,85,247,0.3)", width=1)
        if hasattr(trace, "line"):
            trace.line.width = 2
    return fig
