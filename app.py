import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker")

st.title("🔐 Password Strength Checker")

password = st.text_input("Enter your password", type="password")

def check_strength(pw):
    score = 0
    if len(pw) >= 8:
        score += 1
    if re.search(r"[A-Z]", pw):
        score += 1
    if re.search(r"[a-z]", pw):
        score += 1
    if re.search(r"[0-9]", pw):
        score += 1
    if re.search(r"[@$!%*?&#]", pw):
        score += 1
    return score

if password:
    strength = check_strength(password)

    if strength <= 2:
        st.error("Weak password ❌")
    elif strength == 3:
        st.warning("Medium password ⚠️")
    else:
        st.success("Strong password ✅")

    st.progress(strength / 5)
