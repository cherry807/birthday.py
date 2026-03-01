import streamlit as st

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Happy Birthday Kusuma 💖", page_icon="💝", layout="centered")

# ---------- CSS STYLING ----------
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 100%);
    animation: gradient 10s ease infinite;
    background-size: 400% 400%;
}
@keyframes gradient {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}
h1, h2 {
    text-align: center;
    font-family: 'Comic Sans MS', cursive;
}
.heart {
    font-size: 80px;
    animation: float 2s ease-in-out infinite;
}
@keyframes float {
    0%, 100% {transform: translateY(0);}
    50% {transform: translateY(-15px);}
}
audio {
    display: none;
}
</style>
<audio autoplay loop>
  <source src="https://cdn.pixabay.com/audio/2023/03/13/audio_9c64bfa43b.mp3" type="audio/mp3">
</audio>
""", unsafe_allow_html=True)

# ---------- PAGE STATE ----------
if "page" not in st.session_state:
    st.session_state.page = 1

# ---------- PAGE 1 ----------
if st.session_state.page == 1:
    st.markdown("""
        <div style='text-align:center;'>
            <div class='heart'>❤️</div>
            <h1 style='color:purple;'>Happy Birthday Kusuma 💖</h1>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Love U 💞"):
        st.session_state.page = 2
        st.experimental_rerun()

# ---------- PAGE 2 ----------
elif st.session_state.page == 2:
    st.markdown("""
        <div style='text-align:center;'>
            <h2 style='color:darkblue;'>You are the brightest star in my world 🌟</h2>
        </div>
    """, unsafe_allow_html=True)
    if st.button("Mee too 💕"):
        st.session_state.page = 3
        st.experimental_rerun()

# ---------- PAGE 3 ----------
elif st.session_state.page == 3:
    st.markdown("""
        <div style='text-align:center;'>
            <img src='https://i.imgur.com/5d1xX4t.png' width='300'>
            <h2 style='color:navy;'>Happy Birthday Kusuma 💐</h2>
            <div class='heart'>💙💙💙</div>
        </div>
    """, unsafe_allow_html=True)
