import streamlit as st
import google.generativeai as genai

def get_api_key():
    if 'GEMINI_API_KEY' in st.secrets:
        st.success('API key already provided!', icon='✅')
        return st.secrets['GEMINI_API_KEY']
    else:
        api_key = st.text_input('Enter Gemini API token:', type='password')
        if not api_key:
            st.warning('Please enter your API key!', icon='⚠️')
            st.stop()
        else:
            st.success('API key set. Ready to chat!', icon='👉')
            return api_key

def get_model(model_name="gemini-2.5-flash"):
    api_key = get_api_key()
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(model_name)

def call_gemini(prompt, model_name="gemini-2.5-flash"):
    model = get_model(model_name)
    response = model.generate_content(prompt)
    return response.text


# Sidebar navigation
def show_sidebar():
    hide_sidebar = """
    <style>
        [data-testid="stSidebarNav"] {
            display: none;
        }
    </style>
    """
    st.markdown(hide_sidebar, unsafe_allow_html=True)
    st.sidebar.title("📂 Navigation")
    st.sidebar.page_link("app.py", label="Dashboard", icon="🏠")
    st.sidebar.page_link("pages/Resume_Builder.py", label="Resume Builder", icon="📄")
    st.sidebar.page_link("pages/CV_Builder.py", label="CV Builder", icon="📝")
    st.sidebar.page_link("pages/Cover_Letter_Builder.py", label="Cover Letter Builder", icon="✉️")
    st.sidebar.page_link("pages/Job_Desc_Analyzer.py", label="Job Description Analyzer", icon="📋")
    st.sidebar.page_link("pages/Interview_Prep.py", label="Interview Prep", icon="🎙️")
    st.sidebar.page_link("pages/Tips_and_Resources.py", label="Tips & Resources", icon="📘")
