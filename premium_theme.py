"""
SkyElite-Inspired 3D Animated Premium Theme for Streamlit
=========================================================
Design DNA from the SkyElite private jet landing page:
  - Primary dark: #202A36 | Cards: #1a2229 with glassmorphism
  - Inter font, clean tracking-tighter headings
  - Pill buttons (rounded-full), #202A36 + white/60 overlay
  - Cinematic animated gradient background (video-like feel)
  - Spring-physics 3D transforms, perspective depth
  - Glassmorphism: backdrop-blur, white/60 overlays
  - Subtle floating particles, breathing ambient effects
  - Smooth cubic-bezier(0.16, 1, 0.3, 1) transitions

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
          DESIGN TOKENS — SkyElite DNA
          =================================================================*/
        :root {
            --sky-deep: #202A36;
            --sky-dark: #1a2229;
            --sky-darker: #141c24;
            --sky-card: rgba(255,255,255,0.04);
            --sky-card-solid: #243040;
            --sky-border: rgba(255,255,255,0.08);
            --sky-border-hover: rgba(255,255,255,0.14);
            --sky-glass: rgba(255,255,255,0.55);
            --sky-glass-heavy: rgba(255,255,255,0.75);
            --sky-text: #f0f2f5;
            --sky-text-muted: #94a3b8;
            --sky-text-dim: rgba(255,255,255,0.35);
            --sky-accent: #e2e8f0;
            --spring: cubic-bezier(0.16, 1, 0.3, 1);
            --spring-out: cubic-bezier(0.34, 1.56, 0.64, 1);
            --snappy: cubic-bezier(0.4, 0, 0.2, 1);
            --smooth: cubic-bezier(0.25, 0.46, 0.45, 0.94);
        }

        /*================================================================
          HIDE DEFAULT STREAMLIT CHROME
          =================================================================*/
        #MainMenu { visibility: hidden; }
        footer { visibility: hidden; }
        [data-testid="stHeader"] {
            padding: 0 !important;
            background: transparent !important;
        }

        /*================================================================
          ★ CINEMATIC ANIMATED BACKGROUND
          Mimics the video feel — slow-moving gradient + floating particles
          =================================================================*/
        @keyframes bgPan {
            0%, 100% { background-position: 0% 50%; }
            25% { background-position: 50% 0%; }
            50% { background-position: 100% 50%; }
            75% { background-position: 50% 100%; }
        }
        @keyframes orbDrift1 {
            0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.15; }
            33% { transform: translate(40px, -30px) scale(1.15); opacity: 0.25; }
            66% { transform: translate(-20px, 20px) scale(0.9); opacity: 0.18; }
        }
        @keyframes orbDrift2 {
            0%, 100% { transform: translate(0, 0) scale(1); opacity: 0.1; }
            50% { transform: translate(-35px, -40px) scale(1.2); opacity: 0.22; }
        }
        @keyframes orbDrift3 {
            0%, 100% { transform: translate(0, 0); opacity: 0.08; }
            40% { transform: translate(25px, 30px); opacity: 0.18; }
            80% { transform: translate(-15px, -10px); opacity: 0.1; }
        }
        @keyframes particleFloat {
            0%, 100% { transform: translateY(0) translateX(0); opacity: 0; }
            10% { opacity: 1; }
            90% { opacity: 1; }
            100% { transform: translateY(-100vh) translateX(30px); opacity: 0; }
        }
        @keyframes gridBreath {
            0%, 100% { opacity: 0.015; }
            50% { opacity: 0.04; }
        }
        @keyframes aurora {
            0% { transform: translateX(-50%) rotate(0deg) scale(1); }
            50% { transform: translateX(0%) rotate(3deg) scale(1.1); }
            100% { transform: translateX(50%) rotate(-2deg) scale(1); }
        }

        [data-testid="stAppViewContainer"] {
            background: var(--sky-deep) !important;
            background-image:
                radial-gradient(ellipse 120% 80% at 30% 40%,
                    rgba(32, 42, 54, 0.8) 0%, transparent 70%),
                radial-gradient(ellipse 100% 60% at 70% 70%,
                    rgba(26, 34, 41, 0.6) 0%, transparent 60%);
            background-size: 200% 200% !important;
            animation: bgPan 20s ease infinite !important;
            min-height: 100vh;
            overflow-x: hidden;
        }

        /* Floating ambient orbs */
        [data-testid="stAppViewContainer"]::before {
            content: "";
            position: fixed; inset: 0;
            pointer-events: none; z-index: 0;
            background:
                radial-gradient(circle 600px at 15% 25%, rgba(148, 163, 184, 0.06), transparent 60%),
                radial-gradient(circle 500px at 80% 75%, rgba(226, 232, 240, 0.04), transparent 55%),
                radial-gradient(circle 400px at 50% 50%, rgba(255, 255, 255, 0.02), transparent 50%);
            animation: orbDrift1 14s ease-in-out infinite;
        }
        [data-testid="stAppViewContainer"]::after {
            content: "";
            position: fixed; inset: 0;
            pointer-events: none; z-index: 0;
            background:
                radial-gradient(circle 450px at 75% 20%, rgba(148, 163, 184, 0.04), transparent 55%),
                radial-gradient(circle 350px at 10% 85%, rgba(226, 232, 240, 0.03), transparent 50%);
            animation: orbDrift2 18s ease-in-out infinite;
        }

        /* Subtle animated grid */
        .main .block-container::before {
            content: "";
            position: fixed; inset: 0;
            pointer-events: none; z-index: 0;
            background-image:
                linear-gradient(rgba(255,255,255,0.015) 1px, transparent 1px),
                linear-gradient(90deg, rgba(255,255,255,0.015) 1px, transparent 1px);
            background-size: 80px 80px;
            animation: gridBreath 10s ease-in-out infinite;
        }

        /* Aurora wave overlay */
        .main .block-container::after {
            content: "";
            position: fixed;
            top: 20%; left: -20%;
            width: 140%; height: 40%;
            background: linear-gradient(90deg,
                transparent 0%,
                rgba(148, 163, 184, 0.03) 30%,
                rgba(226, 232, 240, 0.02) 50%,
                rgba(148, 163, 184, 0.03) 70%,
                transparent 100%);
            border-radius: 50%;
            filter: blur(60px);
            animation: aurora 25s ease-in-out infinite;
            pointer-events: none; z-index: 0;
        }

        .main .block-container { position: relative; z-index: 1; }

        /*================================================================
          ★ 3D KEYFRAME LIBRARY
          =================================================================*/
        @keyframes floatCinematic {
            0%, 100% { transform: translateY(0) perspective(800px) rotateX(0deg) rotateY(0deg); }
            25% { transform: translateY(-10px) perspective(800px) rotateX(0.8deg) rotateY(-0.4deg); }
            50% { transform: translateY(-14px) perspective(800px) rotateX(0deg) rotateY(0.5deg); }
            75% { transform: translateY(-7px) perspective(800px) rotateX(-0.6deg) rotateY(-0.2deg); }
        }
        @keyframes shimmerCinematic {
            0% { background-position: -300% center; }
            100% { background-position: 300% center; }
        }
        @keyframes enterFromDepth {
            from { opacity: 0; transform: perspective(800px) translateZ(-40px) translateY(25px) scale(0.96) rotateX(2deg); }
            to   { opacity: 1; transform: perspective(800px) translateZ(0) translateY(0) scale(1) rotateX(0deg); }
        }
        @keyframes slideIn3DLeft {
            from { opacity: 0; transform: perspective(600px) translateX(-50px) rotateY(6deg); }
            to   { opacity: 1; transform: perspective(600px) translateX(0) rotateY(0deg); }
        }
        @keyframes slideIn3DRight {
            from { opacity: 0; transform: perspective(600px) translateX(50px) rotateY(-6deg); }
            to   { opacity: 1; transform: perspective(600px) translateX(0) rotateY(0deg); }
        }
        @keyframes glowBreathe {
            0%, 100% { box-shadow: 0 0 0 rgba(226, 232, 240, 0), inset 0 0 0 rgba(226, 232, 240, 0); border-color: var(--sky-border); }
            50% { box-shadow: 0 0 25px rgba(226, 232, 240, 0.06), inset 0 0 15px rgba(226, 232, 240, 0.02); border-color: var(--sky-border-hover); }
        }
        @keyframes borderShimmer {
            0%, 100% { border-color: var(--sky-border); }
            50% { border-color: rgba(226, 232, 240, 0.25); }
        }
        @keyframes pulseGlow {
            0%, 100% { opacity: 0.4; transform: scale(1); }
            50% { opacity: 0.8; transform: scale(1.05); }
        }
        @keyframes scanSweep {
            0% { top: -5%; }
            100% { top: 105%; }
        }
        @keyframes textGlow {
            0%, 100% { text-shadow: 0 0 8px rgba(226, 232, 240, 0.15); }
            50% { text-shadow: 0 0 20px rgba(226, 232, 240, 0.3), 0 0 40px rgba(226, 232, 240, 0.1); }
        }
        @keyframes spin {
            to { transform: rotate(360deg); }
        }
        @keyframes gradientMarquee {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        @keyframes tiltHover {
            0%, 100% { transform: perspective(1000px) rotateX(0deg) rotateY(0deg); }
            50% { transform: perspective(1000px) rotateX(1.5deg) rotateY(1.5deg); }
        }
        @keyframes breathe {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.015); }
        }

        /*================================================================
          ★ TITLE — Cinematic floating with glassmorphic shimmer
          =================================================================*/
        .main [data-testid="stVerticalBlock"]:first-child {
            animation: floatCinematic 8s ease-in-out infinite;
            transform-style: preserve-3d;
        }

        .main h1,
        .main [data-testid="stTitle"] {
            background: linear-gradient(90deg,
                #f0f2f5 0%, #94a3b8 20%, #e2e8f0 40%,
                #f0f2f5 55%, #cbd5e1 70%, #f0f2f5 85%, #94a3b8 100%);
            background-size: 300% 100% !important;
            -webkit-background-clip: text !important;
            -webkit-text-fill-color: transparent !important;
            background-clip: text !important;
            animation: shimmerCinematic 8s linear infinite !important;
            filter: drop-shadow(0 2px 15px rgba(226, 232, 240, 0.15))
                    drop-shadow(0 8px 25px rgba(0, 0, 0, 0.3));
            font-weight: 700 !important;
            letter-spacing: -0.03em;
            transform-style: preserve-3d;
        }

        .main h2, .main h3 {
            color: var(--sky-text) !important;
            font-weight: 600 !important;
            letter-spacing: -0.02em;
            position: relative;
            display: inline-block;
            animation: textGlow 6s ease-in-out infinite;
        }

        /* Accent underline on h2/h3 */
        .main h2::after, .main h3::after {
            content: "";
            position: absolute;
            bottom: -8px; left: 0;
            width: 32px; height: 2px;
            background: linear-gradient(90deg, #94a3b8, #e2e8f0);
            border-radius: 1px;
            opacity: 0.6;
            animation: pulseGlow 4s ease-in-out infinite;
        }

        .main h4 { color: #cbd5e1 !important; }

        /*================================================================
          ★ SECTIONS — 3D depth entrance with stagger
          =================================================================*/
        .main [data-testid="stVerticalBlock"] {
            animation: enterFromDepth 0.7s var(--spring) both;
            transform-style: preserve-3d;
        }
        .main [data-testid="stVerticalBlock"]:nth-child(1)  { animation-delay: 0s; }
        .main [data-testid="stVerticalBlock"]:nth-child(2)  { animation-delay: 0.07s; }
        .main [data-testid="stVerticalBlock"]:nth-child(3)  { animation-delay: 0.14s; }
        .main [data-testid="stVerticalBlock"]:nth-child(4)  { animation-delay: 0.21s; }
        .main [data-testid="stVerticalBlock"]:nth-child(5)  { animation-delay: 0.28s; }
        .main [data-testid="stVerticalBlock"]:nth-child(6)  { animation-delay: 0.35s; }
        .main [data-testid="stVerticalBlock"]:nth-child(7)  { animation-delay: 0.42s; }
        .main [data-testid="stVerticalBlock"]:nth-child(8)  { animation-delay: 0.49s; }
        .main [data-testid="stVerticalBlock"]:nth-child(9)  { animation-delay: 0.56s; }
        .main [data-testid="stVerticalBlock"]:nth-child(10) { animation-delay: 0.63s; }

        /*================================================================
          ★ SIDEBAR — SkyElite glassmorphism navigation
          =================================================================*/
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg,
                rgba(20, 28, 36, 0.92) 0%,
                rgba(26, 34, 41, 0.88) 50%,
                rgba(20, 28, 36, 0.93) 100%) !important;
            backdrop-filter: blur(24px) saturate(1.3) !important;
            -webkit-backdrop-filter: blur(24px) saturate(1.3) !important;
            border-right: 1px solid var(--sky-border) !important;
            box-shadow: 6px 0 40px rgba(0, 0, 0, 0.3);
            animation: glowBreathe 8s ease-in-out infinite;
        }

        /* Gradient accent line on sidebar edge (like SkyElite nav feel) */
        [data-testid="stSidebar"]::before {
            content: "";
            position: absolute;
            top: 10%; bottom: 10%; left: 0; width: 1px;
            background: linear-gradient(180deg,
                transparent 0%,
                rgba(148, 163, 184, 0.3) 30%,
                rgba(226, 232, 240, 0.4) 50%,
                rgba(148, 163, 184, 0.3) 70%,
                transparent 100%);
            animation: gradientMarquee 8s ease infinite;
            background-size: 200% 200%;
        }

        [data-testid="stSidebar"] h2, [data-testid="stSidebar"] h3 {
            color: var(--sky-text) !important;
            background: none !important;
            -webkit-text-fill-color: var(--sky-text) !important;
            animation: none !important;
            filter: none !important;
        }
        [data-testid="stSidebar"] h2::after,
        [data-testid="stSidebar"] h3::after {
            display: none !important;
        }

        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] span {
            color: var(--sky-text-muted) !important;
            transition: color 0.15s var(--snappy);
        }

        [data-testid="stSidebar"] p:hover,
        [data-testid="stSidebar"] label:hover {
            color: var(--sky-text) !important;
        }

        /* Radio items — clean card style */
        [data-testid="stSidebar"] [data-testid="stRadio"] {
            background: var(--sky-card) !important;
            border: 1px solid var(--sky-border) !important;
            border-radius: 14px !important;
            padding: 6px 14px !important;
            margin-bottom: 6px !important;
            transition: all 0.3s var(--spring) !important;
        }

        [data-testid="stSidebar"] [data-testid="stRadio"]:hover {
            background: rgba(255, 255, 255, 0.06) !important;
            border-color: var(--sky-border-hover) !important;
            transform: translateX(3px);
        }

        /* Active radio — 3D glow */
        [data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] {
            background: rgba(148, 163, 184, 0.1) !important;
            border-color: rgba(148, 163, 184, 0.25) !important;
            border-radius: 10px;
            animation: glowBreathe 5s ease-in-out infinite !important;
        }

        [data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] p,
        [data-testid="stSidebar"] [data-testid="stRadio"] [aria-checked="true"] span {
            color: var(--sky-text) !important;
            font-weight: 600;
        }

        /* Sidebar divider */
        [data-testid="stSidebar"] hr,
        [data-testid="stSidebar"] [data-testid="stDivider"] {
            border: none !important;
            height: 1px !important;
            background: linear-gradient(90deg, transparent, rgba(148, 163, 184, 0.15), transparent) !important;
            margin: 20px 0 !important;
        }

        /* Sidebar sections slide in */
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {
            animation: slideIn3DLeft 0.5s var(--spring) both;
        }
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"]:nth-child(2) { animation-delay: 0.08s; }
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"]:nth-child(3) { animation-delay: 0.16s; }
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"]:nth-child(4) { animation-delay: 0.24s; }
        [data-testid="stSidebar"] [data-testid="stVerticalBlock"]:nth-child(5) { animation-delay: 0.32s; }

        /*================================================================
          ★ BUTTONS — SkyElite pill style (#202A36 primary)
          =================================================================*/
        .stButton > button,
        [data-testid="stButton"] > button,
        [data-testid="stFormSubmitButton"] > button {
            background: var(--sky-deep) !important;
            color: var(--sky-text) !important;
            font-weight: 600 !important;
            font-size: 14px !important;
            letter-spacing: 0.01em;
            border: 1px solid var(--sky-border) !important;
            border-radius: 9999px !important;
            padding: 10px 30px !important;
            box-shadow:
                0 2px 8px rgba(0, 0, 0, 0.2),
                0 8px 24px rgba(0, 0, 0, 0.15),
                inset 0 1px 0 rgba(255, 255, 255, 0.06);
            transition: all 0.3s var(--spring-out) !important;
            cursor: pointer;
            position: relative;
            top: 0;
            text-shadow: 0 1px 2px rgba(0, 0, 0, 0.2);
            backdrop-filter: blur(8px);
        }

        .stButton > button:hover,
        [data-testid="stButton"] > button:hover,
        [data-testid="stFormSubmitButton"] > button:hover {
            background: var(--sky-dark) !important;
            transform: translateY(-3px) scale(1.02) !important;
            box-shadow:
                0 6px 20px rgba(0, 0, 0, 0.3),
                0 14px 35px rgba(0, 0, 0, 0.2),
                0 0 40px rgba(148, 163, 184, 0.05),
                inset 0 1px 0 rgba(255, 255, 255, 0.08);
            border-color: var(--sky-border-hover) !important;
        }

        .stButton > button:active,
        [data-testid="stButton"] > button:active,
        [data-testid="stFormSubmitButton"] > button:active {
            transform: translateY(2px) scale(0.98) !important;
            box-shadow:
                0 1px 3px rgba(0, 0, 0, 0.2),
                inset 0 2px 6px rgba(0, 0, 0, 0.3);
            transition-duration: 0.1s !important;
        }

        /* Secondary button (file uploader) */
        [data-testid="stFileUploader"] button {
            background: rgba(255, 255, 255, 0.08) !important;
            border: 1px solid var(--sky-border) !important;
            color: var(--sky-text) !important;
            border-radius: 9999px !important;
            padding: 8px 22px !important;
            transition: all 0.15s var(--snappy);
        }
        [data-testid="stFileUploader"] button:hover {
            background: rgba(255, 255, 255, 0.14) !important;
            border-color: var(--sky-border-hover) !important;
            box-shadow: 0 0 20px rgba(148, 163, 184, 0.06);
        }

        /*================================================================
          ★ FILE UPLOADER — Animated glass border
          =================================================================*/
        [data-testid="stFileUploader"] section {
            background: var(--sky-card) !important;
            border: 1.5px dashed var(--sky-border) !important;
            border-radius: 20px !important;
            padding: 30px 22px !important;
            animation: borderShimmer 4s ease-in-out infinite !important;
            transition: all 0.3s var(--spring) !important;
            position: relative;
            overflow: hidden;
        }

        /* Scan sweep effect */
        [data-testid="stFileUploader"] section::after {
            content: "";
            position: absolute;
            left: 0; right: 0; height: 50px;
            background: linear-gradient(180deg,
                transparent, rgba(148, 163, 184, 0.04), transparent);
            animation: scanSweep 6s linear infinite;
            pointer-events: none;
        }

        [data-testid="stFileUploader"] section:hover {
            border-color: rgba(148, 163, 184, 0.35) !important;
            background: rgba(255, 255, 255, 0.06) !important;
            box-shadow:
                0 0 40px rgba(148, 163, 184, 0.06),
                inset 0 0 25px rgba(148, 163, 184, 0.02);
            transform: scale(1.005);
        }

        [data-testid="stFileUploader"] label p,
        [data-testid="stFileUploader"] label span {
            color: var(--sky-text-muted) !important;
            transition: color 0.15s var(--snappy);
        }
        [data-testid="stFileUploader"]:hover label p { color: var(--sky-text) !important; }

        /*================================================================
          ★ DATAFRAMES — 3D perspective tilt on hover
          =================================================================*/
        .stDataFrame, .stDataframe, [data-testid="stDataFrame"] {
            background: var(--sky-card) !important;
            border: 1px solid var(--sky-border) !important;
            border-radius: 18px !important;
            overflow: hidden;
            transition: all 0.4s var(--spring) !important;
            transform-style: preserve-3d;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
        }

        .stDataFrame:hover, .stDataframe:hover, [data-testid="stDataFrame"]:hover {
            transform:
                perspective(1200px)
                translateY(-8px)
                rotateX(2deg)
                rotateY(-1.5deg)
                scale(1.005) !important;
            box-shadow:
                0 25px 60px rgba(0, 0, 0, 0.35),
                0 8px 20px rgba(0, 0, 0, 0.2),
                0 0 30px rgba(148, 163, 184, 0.04),
                inset 0 1px 0 rgba(255, 255, 255, 0.06);
            border-color: var(--sky-border-hover) !important;
        }

        /*================================================================
          ★ PLOTLY CHARTS — 3D card lift
          =================================================================*/
        [data-testid="stPlotlyChart"], .stPlotlyChart {
            border: 1px solid var(--sky-border) !important;
            border-radius: 18px !important;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
            transition: all 0.4s var(--spring) !important;
            transform-style: preserve-3d;
        }

        [data-testid="stPlotlyChart"]:hover, .stPlotlyChart:hover {
            transform:
                perspective(1000px)
                translateY(-8px)
                rotateX(1.5deg)
                rotateY(-1deg) !important;
            box-shadow:
                0 20px 50px rgba(0, 0, 0, 0.35),
                0 6px 16px rgba(0, 0, 0, 0.2),
                0 0 35px rgba(148, 163, 184, 0.04);
            border-color: var(--sky-border-hover) !important;
        }

        [data-testid="stPlotlyChart"] iframe,
        .stPlotlyChart iframe {
            background: transparent !important;
        }

        /*================================================================
          ★ SELECTBOX — Clean dropdown
          =================================================================*/
        [data-testid="stSelectbox"] {
            transition: all 0.15s var(--snappy);
        }

        [data-testid="stSelectbox"] label p {
            color: var(--sky-text-muted) !important;
            font-weight: 500;
        }

        [data-testid="stSelectbox"] div[data-baseweb="select"] {
            background-color: rgba(20, 28, 36, 0.8) !important;
            border: 1px solid var(--sky-border) !important;
            border-radius: 12px !important;
            transition: all 0.15s var(--snappy);
        }

        [data-testid="stSelectbox"] div[data-baseweb="select"]:hover {
            border-color: var(--sky-border-hover) !important;
        }

        [data-testid="stSelectbox"] div[data-baseweb="select"] span {
            color: var(--sky-text) !important;
        }

        /* Dropdown popover */
        [data-baseweb="popover"] {
            background: rgba(20, 28, 36, 0.97) !important;
            border: 1px solid var(--sky-border) !important;
            border-radius: 14px !important;
            box-shadow: 0 20px 50px rgba(0, 0, 0, 0.5), 0 0 1px rgba(255,255,255,0.05);
            backdrop-filter: blur(24px);
        }

        [data-baseweb="popover"] li {
            color: var(--sky-text-muted) !important;
            transition: all 0.15s var(--snappy);
            border-radius: 10px;
            margin: 2px 6px;
        }

        [data-baseweb="popover"] li:hover {
            background: rgba(148, 163, 184, 0.1) !important;
            color: var(--sky-text) !important;
            padding-left: 16px;
        }

        [data-baseweb="popover"] li[aria-selected="true"] {
            background: rgba(148, 163, 184, 0.15) !important;
            color: var(--sky-text) !important;
            font-weight: 600;
        }

        /*================================================================
          ★ SLIDERS — Accent styled
          =================================================================*/
        [data-testid="stSlider"] [role="slider"] {
            background: linear-gradient(135deg, #94a3b8, #e2e8f0) !important;
            border: 2px solid rgba(255, 255, 255, 0.15) !important;
            box-shadow: 0 0 12px rgba(148, 163, 184, 0.2), 0 2px 6px rgba(0, 0, 0, 0.3);
            transition: all 0.15s var(--snappy);
            width: 22px !important; height: 22px !important;
        }

        [data-testid="stSlider"] [role="slider"]:hover {
            transform: scale(1.2);
            box-shadow: 0 0 20px rgba(148, 163, 184, 0.35), 0 2px 8px rgba(0, 0, 0, 0.4);
        }

        [data-testid="stSlider"] [role="slider"]:focus {
            box-shadow: 0 0 0 4px rgba(148, 163, 184, 0.12), 0 0 15px rgba(148, 163, 184, 0.2);
        }

        [data-testid="stSlider"] div[class*="Track-active"] {
            background: linear-gradient(90deg, rgba(148, 163, 184, 0.4), rgba(226, 232, 240, 0.4)) !important;
            border-radius: 4px;
        }

        /*================================================================
          ★ TEXT AREA — Dark glass card
          =================================================================*/
        [data-testid="stTextArea"] textarea {
            background: rgba(20, 28, 36, 0.75) !important;
            border: 1px solid var(--sky-border) !important;
            border-radius: 16px !important;
            color: var(--sky-text) !important;
            padding: 16px 20px !important;
            font-size: 15px !important;
            line-height: 1.7;
            transition: all 0.3s var(--spring) !important;
            box-shadow: inset 0 2px 8px rgba(0, 0, 0, 0.25);
            backdrop-filter: blur(8px);
        }

        [data-testid="stTextArea"] textarea::placeholder {
            color: var(--sky-text-dim) !important;
            font-style: normal;
        }

        [data-testid="stTextArea"] textarea:focus {
            border-color: rgba(148, 163, 184, 0.35) !important;
            box-shadow:
                0 0 0 3px rgba(148, 163, 184, 0.06),
                0 0 25px rgba(148, 163, 184, 0.05),
                inset 0 0 10px rgba(148, 163, 184, 0.02) !important;
            outline: none !important;
            background: rgba(26, 34, 41, 0.85) !important;
        }

        [data-testid="stTextArea"] label p {
            color: var(--sky-text-muted) !important;
            font-weight: 500;
        }

        /*================================================================
          ★ CHAT MESSAGES — 3D glassmorphism bubbles
          =================================================================*/
        .stChatMessage {
            border-radius: 20px !important;
            padding: 16px 22px !important;
            margin: 10px 0 !important;
            backdrop-filter: blur(20px) saturate(1.2) !important;
            -webkit-backdrop-filter: blur(20px) saturate(1.2) !important;
            transition: all 0.3s var(--spring) !important;
            transform-style: preserve-3d;
            position: relative;
            overflow: hidden;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.2);
        }

        /* Shine sweep on hover */
        .stChatMessage::before {
            content: "";
            position: absolute;
            top: 0; left: -100%; width: 50%; height: 100%;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.03), transparent);
            transition: left 0.6s ease;
            pointer-events: none;
        }
        .stChatMessage:hover::before { left: 130%; }

        /* User — warm slate tint */
        .stChatMessage:nth-child(odd),
        .stChatMessage[data-testid="stChatMessage-user"] {
            background: rgba(148, 163, 184, 0.06) !important;
            border: 1px solid rgba(148, 163, 184, 0.12) !important;
            box-shadow:
                0 6px 25px rgba(0, 0, 0, 0.25),
                0 0 15px rgba(148, 163, 184, 0.03),
                inset 0 1px 0 rgba(255, 255, 255, 0.04);
            margin-left: 28px !important;
            animation: slideIn3DRight 0.4s var(--spring) both;
        }

        /* Assistant — cool navy tint */
        .stChatMessage:nth-child(even),
        .stChatMessage[data-testid="stChatMessage-assistant"] {
            background: rgba(32, 42, 54, 0.5) !important;
            border: 1px solid rgba(32, 42, 54, 0.8) !important;
            box-shadow:
                0 6px 25px rgba(0, 0, 0, 0.25),
                0 0 15px rgba(226, 232, 240, 0.02),
                inset 0 1px 0 rgba(255, 255, 255, 0.03);
            margin-right: 28px !important;
            animation: slideIn3DLeft 0.4s var(--spring) both;
        }

        .stChatMessage:hover {
            transform:
                perspective(600px)
                translateY(-4px)
                rotateX(2deg)
                scale(1.005) !important;
            box-shadow:
                0 14px 40px rgba(0, 0, 0, 0.35),
                0 0 25px rgba(148, 163, 184, 0.04);
        }

        .stChatMessage p, .stChatMessage span, .stChatMessage div {
            color: #cbd5e1 !important;
            line-height: 1.7;
        }

        /* Chat input */
        [data-testid="stChatInput"] {
            background: rgba(20, 28, 36, 0.7) !important;
            border: 1px solid var(--sky-border) !important;
            border-radius: 16px !important;
            box-shadow: 0 4px 18px rgba(0, 0, 0, 0.25);
            transition: all 0.3s var(--spring);
        }

        [data-testid="stChatInput"]:focus-within {
            border-color: rgba(148, 163, 184, 0.3) !important;
            box-shadow: 0 0 25px rgba(148, 163, 184, 0.06);
        }

        [data-testid="stChatInput"] textarea {
            background: transparent !important;
            color: var(--sky-text) !important;
        }

        [data-testid="stChatInput"] textarea::placeholder { color: var(--sky-text-dim) !important; }

        /*================================================================
          ★ SPINNER — Gradient ring
          =================================================================*/
        [data-testid="stSpinner"] > div {
            border: 3px solid rgba(148, 163, 184, 0.12) !important;
            border-top-color: #94a3b8 !important;
            border-right-color: #e2e8f0 !important;
            border-bottom-color: rgba(148, 163, 184, 0.25) !important;
            border-left-color: #f0f2f5 !important;
            animation: spin 0.7s linear infinite !important;
            box-shadow: 0 0 18px rgba(148, 163, 184, 0.12);
        }

        /*================================================================
          ★ ALERTS — Glass card style
          =================================================================*/
        [data-testid="stAlert"] [data-baseweb="notification"] {
            backdrop-filter: blur(20px);
            border-radius: 16px !important;
            padding: 14px 20px !important;
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.25);
            animation: enterFromDepth 0.4s var(--spring) both;
            border-left: 3px solid !important;
        }

        [data-testid="stSuccess"] [data-baseweb="notification"],
        [data-testid="stAlert"] [data-baseweb="notification"][style*="green"] {
            background: rgba(34, 197, 94, 0.06) !important;
            border: 1px solid rgba(34, 197, 94, 0.12) !important;
            border-left-color: #22c55e !important;
        }

        [data-testid="stWarning"] [data-baseweb="notification"],
        [data-testid="stAlert"] [data-baseweb="notification"][style*="amber"] {
            background: rgba(253, 186, 116, 0.06) !important;
            border: 1px solid rgba(253, 186, 116, 0.12) !important;
            border-left-color: #fdba74 !important;
        }

        [data-testid="stError"] [data-baseweb="notification"],
        [data-testid="stAlert"] [data-baseweb="notification"][style*="red"] {
            background: rgba(239, 68, 68, 0.06) !important;
            border: 1px solid rgba(239, 68, 68, 0.12) !important;
            border-left-color: #ef4444 !important;
        }

        [data-testid="stInfo"] [data-baseweb="notification"],
        [data-testid="stAlert"] [data-baseweb="notification"][style*="blue"] {
            background: rgba(96, 165, 250, 0.06) !important;
            border: 1px solid rgba(96, 165, 250, 0.12) !important;
            border-left-color: #60a5fa !important;
        }

        [data-testid="stAlert"] p { color: #cbd5e1 !important; line-height: 1.65; }

        /*================================================================
          ★ MARKDOWN CONTENT
          =================================================================*/
        .stMarkdown p, .stMarkdown li, .stMarkdown span {
            color: var(--sky-text-muted) !important;
            line-height: 1.8;
        }
        .stMarkdown strong, .stMarkdown b { color: var(--sky-text) !important; }
        .stMarkdown a {
            color: #94a3b8 !important;
            text-decoration: none;
            border-bottom: 1px solid rgba(148, 163, 184, 0.15);
            transition: all 0.15s var(--snappy);
        }
        .stMarkdown a:hover {
            color: #e2e8f0 !important;
            border-bottom-color: rgba(226, 232, 240, 0.25);
        }
        .stMarkdown code {
            background: rgba(148, 163, 184, 0.06);
            border: 1px solid rgba(148, 163, 184, 0.1);
            border-radius: 6px;
            padding: 2px 7px;
            color: #e2e8f0;
        }
        .stMarkdown pre {
            background: rgba(15, 20, 25, 0.9) !important;
            border: 1px solid var(--sky-border) !important;
            border-radius: 14px !important;
            padding: 18px !important;
            box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.3);
        }
        .stMarkdown pre code { background: transparent; border: none; color: #cbd5e1; }

        /*================================================================
          ★ IMAGES — Elegant 3D hover
          =================================================================*/
        .stImage > img, .stImage img {
            border-radius: 16px !important;
            box-shadow: 0 6px 25px rgba(0, 0, 0, 0.35);
            border: 1px solid var(--sky-border);
            transition: all 0.4s var(--spring);
            transform-style: preserve-3d;
        }
        .stImage > img:hover, .stImage img:hover {
            transform: perspective(600px) scale(1.02) rotateY(3deg) !important;
            box-shadow: 0 16px 45px rgba(0, 0, 0, 0.45), 0 0 25px rgba(148, 163, 184, 0.04);
        }

        /*================================================================
          ★ DIVIDERS — Elegant gradient fade
          =================================================================*/
        hr, [data-testid="stDivider"] {
            border: none !important;
            height: 1px !important;
            background: linear-gradient(90deg,
                transparent 0%,
                rgba(148, 163, 184, 0.15) 25%,
                rgba(226, 232, 240, 0.2) 50%,
                rgba(148, 163, 184, 0.15) 75%,
                transparent 100%) !important;
            margin: 28px 0 !important;
        }

        /*================================================================
          ★ SUBHEADER
          =================================================================*/
        .stSubheader {
            color: var(--sky-text) !important;
            background: none !important;
            -webkit-text-fill-color: var(--sky-text) !important;
            border-bottom: 1px solid rgba(148, 163, 184, 0.08);
            padding-bottom: 10px !important;
            animation: none !important;
            filter: none !important;
        }
        .stSubheader::after { display: none !important; }

        /*================================================================
          ★ METRICS — Card style
          =================================================================*/
        [data-testid="stMetric"] {
            background: var(--sky-card) !important;
            border: 1px solid var(--sky-border) !important;
            border-radius: 16px !important;
            padding: 20px !important;
            transition: all 0.3s var(--spring);
            transform-style: preserve-3d;
        }
        [data-testid="stMetric"]:hover {
            transform: perspective(800px) translateY(-5px) rotateX(1.5deg) !important;
            box-shadow: 0 14px 35px rgba(0, 0, 0, 0.3);
            border-color: var(--sky-border-hover);
        }
        [data-testid="stMetric"] label { color: var(--sky-text-muted) !important; }
        [data-testid="stMetric"] [data-testid="stMetricValue"] {
            color: var(--sky-text) !important;
            font-weight: 700;
        }

        /*================================================================
          ★ EXPANDERS
          =================================================================*/
        .stExpander > div > div {
            background: var(--sky-card) !important;
            border: 1px solid var(--sky-border) !important;
            border-radius: 16px !important;
            transition: all 0.3s var(--spring);
        }
        .stExpander > div > div:hover { border-color: var(--sky-border-hover); }

        /*================================================================
          ★ TABS — Pill style
          =================================================================*/
        .stTabs [data-baseweb="tab-list"] {
            gap: 4px;
            background: rgba(20, 28, 36, 0.6);
            border-radius: 9999px !important;
            padding: 4px;
            border: 1px solid var(--sky-border);
            backdrop-filter: blur(12px);
        }
        .stTabs [data-baseweb="tab"] {
            border-radius: 9999px !important;
            color: var(--sky-text-muted) !important;
            transition: all 0.15s var(--snappy);
            padding: 8px 18px !important;
        }
        .stTabs [data-baseweb="tab"]:hover {
            background: rgba(148, 163, 184, 0.08) !important;
            color: var(--sky-text) !important;
        }
        .stTabs [data-baseweb="tab"][aria-selected="true"] {
            background: rgba(148, 163, 184, 0.12) !important;
            color: var(--sky-text) !important;
            font-weight: 600;
            box-shadow: 0 0 12px rgba(148, 163, 184, 0.06);
        }

        /*================================================================
          ★ PROGRESS BAR — Shimmer gradient
          =================================================================*/
        [data-testid="stProgressBar"] > div > div > div {
            background: linear-gradient(90deg, #94a3b8, #e2e8f0, #f0f2f5, #e2e8f0, #94a3b8) !important;
            background-size: 300% 100% !important;
            animation: gradientMarquee 2s linear infinite !important;
            border-radius: 6px !important;
            box-shadow: 0 0 12px rgba(148, 163, 184, 0.2);
        }

        /*================================================================
          ★ INPUTS
          =================================================================*/
        [data-testid="stNumberInput"] input,
        [data-testid="stTextInput"] input {
            background: rgba(20, 28, 36, 0.75) !important;
            border: 1px solid var(--sky-border) !important;
            border-radius: 12px !important;
            color: var(--sky-text) !important;
            padding: 10px 14px !important;
            transition: all 0.15s var(--snappy);
        }
        [data-testid="stNumberInput"] input:focus,
        [data-testid="stTextInput"] input:focus {
            border-color: rgba(148, 163, 184, 0.35) !important;
            box-shadow: 0 0 0 3px rgba(148, 163, 184, 0.06) !important;
            outline: none !important;
        }
        [data-testid="stNumberInput"] label p,
        [data-testid="stTextInput"] label p { color: var(--sky-text-muted) !important; }

        /*================================================================
          ★ CHECKBOX
          =================================================================*/
        [data-testid="stCheckbox"] label {
            color: var(--sky-text-muted) !important;
            transition: color 0.15s var(--snappy);
        }
        [data-testid="stCheckbox"] label:hover { color: var(--sky-text) !important; }

        /*================================================================
          ★ SCROLLBARS — Subtle accent
          =================================================================*/
        ::-webkit-scrollbar { width: 6px; height: 6px; }
        ::-webkit-scrollbar-track { background: transparent; }
        ::-webkit-scrollbar-thumb {
            background: rgba(148, 163, 184, 0.2);
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover { background: rgba(148, 163, 184, 0.35); }

        /*================================================================
          ★ TOOLTIP
          =================================================================*/
        [data-baseweb="tooltip"] {
            background: rgba(20, 28, 36, 0.97) !important;
            border: 1px solid var(--sky-border) !important;
            border-radius: 10px !important;
            color: var(--sky-text) !important;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
        }

        /*================================================================
          ★ CODE BLOCKS
          =================================================================*/
        [data-testid="stCodeBlock"] {
            background: rgba(12, 16, 20, 0.9) !important;
            border: 1px solid var(--sky-border) !important;
            border-radius: 16px !important;
            box-shadow: inset 0 2px 10px rgba(0, 0, 0, 0.3);
        }
        [data-testid="stCodeBlock"] code,
        [data-testid="stCodeBlock"] pre { color: #cbd5e1 !important; }

        /*================================================================
          ★ GLOBAL TEXT
          =================================================================*/
        .main div, .main span, .main p, .main label { color: var(--sky-text-muted); }
        .main a { color: #94a3b8 !important; }
        .main a:hover { color: #e2e8f0 !important; }

        /*================================================================
          ★ BLOCK WRAPPERS — Subtle depth
          =================================================================*/
        [data-testid="stVerticalBlock"] {
            background: rgba(255, 255, 255, 0.012);
            border: 1px solid rgba(255, 255, 255, 0.02);
            border-radius: 14px;
            padding: 2px 0;
            transition: all 0.3s var(--spring);
            transform-style: preserve-3d;
        }

        [data-testid="stVerticalBlock"]:hover {
            border-color: rgba(255, 255, 255, 0.04);
            background: rgba(255, 255, 255, 0.018);
        }

        [data-testid="stHorizontalBlock"] { gap: 16px; }

        /*================================================================
          ★ RESPONSIVE
          =================================================================*/
        @media (max-width: 768px) {
            .main .block-container {
                padding-left: 16px !important;
                padding-right: 16px !important;
            }
            [data-testid="stSidebar"] { width: 280px !important; }
            .stChatMessage { margin-left: 4px !important; margin-right: 4px !important; }
            [data-testid="stDataFrame"]:hover,
            [data-testid="stPlotlyChart"]:hover {
                transform: translateY(-4px) !important;
            }
        }

        @media (max-width: 480px) {
            .main h1 { font-size: 1.5rem !important; }
            .stButton > button { padding: 9px 22px !important; font-size: 13px !important; }
        }

        </style>
        """,
        unsafe_allow_html=True,
    )


def style_plotly_charts() -> dict:
    """Plotly layout template matching the SkyElite dark theme. OPTIONAL."""
    return {
        "template": {
            "layout": {
                "paper_bgcolor": "rgba(0,0,0,0)",
                "plot_bgcolor": "#202A36",
                "font": {
                    "family": "Inter, -apple-system, BlinkMacSystemFont, sans-serif",
                    "color": "#94a3b8",
                    "size": 13,
                },
                "title": {"font": {"color": "#f0f2f5", "size": 17}},
                "xaxis": {
                    "gridcolor": "rgba(148,163,184,0.06)",
                    "zerolinecolor": "rgba(148,163,184,0.1)",
                    "linecolor": "rgba(148,163,184,0.08)",
                    "tickfont": {"color": "#94a3b8"},
                    "title": {"font": {"color": "#e2e8f0"}},
                },
                "yaxis": {
                    "gridcolor": "rgba(148,163,184,0.06)",
                    "zerolinecolor": "rgba(148,163,184,0.1)",
                    "linecolor": "rgba(148,163,184,0.08)",
                    "tickfont": {"color": "#94a3b8"},
                    "title": {"font": {"color": "#e2e8f0"}},
                },
                "legend": {
                    "font": {"color": "#94a3b8", "size": 12},
                    "bgcolor": "rgba(0,0,0,0)",
                    "bordercolor": "rgba(148,163,184,0.08)",
                    "borderwidth": 1,
                },
                "colorway": [
                    "#e2e8f0", "#94a3b8", "#fdba74", "#60a5fa",
                    "#34d399", "#f472b6", "#f87171", "#818cf8",
                    "#2dd4bf", "#fb923c",
                ],
                "hoverlabel": {
                    "bgcolor": "#1a2229",
                    "bordercolor": "rgba(148,163,184,0.2)",
                    "font": {"color": "#f0f2f5", "size": 13},
                },
                "modebar": {
                    "bgcolor": "transparent",
                    "color": "#94a3b8",
                    "activecolor": "#e2e8f0",
                },
            }
        }
    }


def apply_chart_theme(fig) -> object:
    """Apply the SkyElite dark theme to a Plotly figure. OPTIONAL."""
    theme = style_plotly_charts()
    fig.update_layout(template=theme["template"]["layout"])
    fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", plot_bgcolor="#202A36")
    for trace in fig.data:
        trace.hoverinfo = "all"
        if hasattr(trace, "marker"):
            trace.marker.line = dict(color="rgba(148,163,184,0.25)", width=1)
        if hasattr(trace, "line"):
            trace.line.width = 2
    return fig
