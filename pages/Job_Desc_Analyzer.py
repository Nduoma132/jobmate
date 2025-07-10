import streamlit as st
import re
from config import call_gemini, show_sidebar
from prompts import extract_prompt, analyze_prompt

show_sidebar()

def display_score_bar(score):
    color = "green" if score >= 75 else "orange" if score >= 50 else "red"
    st.markdown(f"""
        <div>
            <div style="background-color: #ddd; border-radius: 5px; height: 10px;">
                <div style="
                    width: {score}%;
                    background-color: {color};
                    height: 100%;
                    border-radius: 5px;">
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

job_description = st.text_area("📋 Paste the Job Description / Ad here", height=200)

col1, col2 = st.columns(2)
with col1:
    extract_btn = st.button("🔍 Extract Job Requirements")
with col2:
    analyze_btn = st.button("📊 Analyze My Fit")

# Extract key details from job description
if extract_btn and job_description:
    with st.spinner("Extracting key details..."):
        prompt = extract_prompt(job_description)
        response = call_gemini(prompt)
        st.markdown(response)

# Analyze fit based on user profile and job description
if analyze_btn and job_description:
    user = st.session_state.get("user_info", {})
    user_resume_data = st.session_state.get("user_resume_data", {})

    if not user or not user_resume_data:
        st.warning("Please log in and build your resume first!")
    else:
        with st.spinner("Analyzing fit based on your profile..."):
            prompt = analyze_prompt(user, job_description)
            response = call_gemini(prompt)
            result_text = response

            # Extract score
            # match = re.search(r"\b(\d{1,3})\b", result_text)
            match = re.search(r"Score[:\s]*?(\d{1,3})", result_text, re.IGNORECASE)
            fit_score = int(match.group(1)) if match else 0

            # Show result
            st.metric(label="Fit Score", value=f"{fit_score}%")
            # st.progress(fit_score)
            display_score_bar(fit_score)
            st.markdown(result_text)
