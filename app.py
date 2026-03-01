import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Happy Birthday Kusuma 💖", page_icon="💝", layout="wide")

# ---------- BACKGROUND IMAGE ----------
background_url = "https://i.imgur.com/your_uploaded_image.jpg"  # Replace with your uploaded photo URL

# ---------- CSS STYLING ----------
st.markdown(f"""
<style>
html, body, [class*="css"] {{
    height: 100%;
    margin: 0;
}}
body {{
    background: url("{background_url}") no-repeat center center fixed;
    background-size: cover;
}}
[data-testid="stAppViewContainer"] > .main {{
    background-color: rgba(255, 192, 203, 0.55);
    backdrop-filter: blur(6px);
    height: 100vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
}}
h1, h2, h3 {{
    text-align: center;
    font-family: 'Comic Sans MS', cursive;
}}
.heart {{
    font-size: 80px;
    animation: float 2s ease-in-out infinite;
}}
@keyframes float {{
    0%, 100% {{transform: translateY(0);}}
    50% {{transform: translateY(-15px);}}
}}
audio {{
    display: none;
}}
.rose-img {{
    width: 200px;
}}
.center-btn {{
    display: flex;
    justify-content: center;
    margin-top: 30px;
}}
</style>

<!-- 🎵 Peaceful Romantic Piano Melody -->
<audio autoplay loop>
  <source src="https://cdn.pixabay.com/audio/2024/02/06/audio_4b8b6c6f4a.mp3" type="audio/mp3">
</audio>
""", unsafe_allow_html=True)

# ---------- PAGE STATE ----------
if "page" not in st.session_state:
    st.session_state.page = 1

# ---------- PAGE 1 ----------
if st.session_state.page == 1:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.markdown("<img class='rose-img' src='https://i.imgur.com/BaV0aAW.png'>", unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div style='text-align:center;'>
                <div class='heart'>❤️</div>
                <h1 style='color:purple;'>Happy Birthday Kusuma 💖</h1>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<div class='center-btn'>", unsafe_allow_html=True)
        if st.button("Love U 💞"):
            st.session_state.page = 2
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<img class='rose-img' src='https://i.imgur.com/BaV0aAW.png'>", unsafe_allow_html=True)

# ---------- PAGE 2 ----------
elif st.session_state.page == 2:
    col1, col2, col3 = st.columns([1, 2, 1])
    with col1:
        st.markdown("<img class='rose-img' src='https://i.imgur.com/BaV0aAW.png'>", unsafe_allow_html=True)
    with col2:
        st.markdown("""
            <div style='text-align:center;'>
                <h2 style='color:darkblue;'>You are the brightest star in my world 🌟</h2>
            </div>
        """, unsafe_allow_html=True)
        st.markdown("<div class='center-btn'>", unsafe_allow_html=True)
        if st.button("Mee too 💕"):
            st.session_state.page = 3
            st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<img class='rose-img' src='https://i.imgur.com/BaV0aAW.png'>", unsafe_allow_html=True)

# ---------- PAGE 3 ----------
elif st.session_state.page == 3:
    st.markdown("""
        <div style='text-align:center;'>
            <img src='https://i.imgur.com/yBvO0nC.png' width='350'>
            <h2 style='color:red;'>Happy Birthday Kusuma 💐</h2>
            <div class='heart'>❤️❤️❤️</div>
            <h3 style='color:maroon;'>These red roses are just a small piece of my love for you 🌹</h3>
        </div>
    """, unsafe_allow_html=True)
