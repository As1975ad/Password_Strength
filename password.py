import streamlit as st
import re

st.set_page_config(page_title="Password Mood Meter", layout="centered")

st.markdown("""
    <h2 style='text-align: center; color: #7F00FF;'>🔒 Password Mood Meter</h2>
    <p style='text-align: center; font-size:16px;'>Your password strength... in vibes! 🌈</p>
""", unsafe_allow_html=True)

# Strength Analyzer
def get_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r"[a-z]", password): score += 1
    if re.search(r"[A-Z]", password): score += 1
    if re.search(r"[0-9]", password): score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password): score += 1
    return score

# Mood mapping
def get_mood(score):
    if score <= 1:
        return "😢 Too Weak", "#FFCCCC"
    elif score == 2:
        return "😐 Getting Better", "#FFE4B5"
    elif score == 3:
        return "🙂 Not Bad", "#FFFACD"
    elif score == 4:
        return "😊 Almost Strong", "#D0F0C0"
    else:
        return "😎 Super Strong!", "#C6F6D5"

# Input box
password = st.text_input("🔑 Type your password", type="password", placeholder="Try mixing things up...")

if password:
    score = get_strength(password)
    mood_text, bg_color = get_mood(score)

    # Mood Box
    st.markdown(f"""
        <div style='background-color:{bg_color}; padding:20px; text-align:center; border-radius:10px;'>
            <h3>{mood_text}</h3>
        </div>
    """, unsafe_allow_html=True)

    # Progress bar
    st.progress(score / 5)

    # Friendly reminder
    with st.expander("💡 Friendly Advice"):
        st.markdown("""
        - ✅ Minimum 8 characters  
        - ✅ Use a mix of upper & lower case  
        - ✅ Add numbers  
        - ✅ Use symbols like @, %, # etc.  
        - ❌ Avoid using your name or birth year  
        """)
else:
    st.info("Type a password to see the strength mood 😊")





