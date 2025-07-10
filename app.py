import streamlit as st
from PIL import Image
from config import show_sidebar

# App Configuration
app_title = "JobMate - For Job Seekers"
app_icon = "💼"

# Set page configuration
st.set_page_config( 
    page_title=app_title,
    page_icon=app_icon,
    layout="centered",
    initial_sidebar_state="collapsed"
    )

# Initialize session state
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.title("🔐 Welcome to JobMate")
    st.markdown("Let’s get to know you before we begin!")


    name = st.text_input("👤 Your Name")
    education = st.selectbox("🎓 Education Level", ["High School", "Diploma", "BSc", "MSc", "PhD"])
    experience = st.selectbox("🧠 Experience Level", ["Beginner", "Intermediate", "Advanced", "Expert"])
    role = st.text_input("💼 What type of job are you targeting? (e.g. Frontend Dev, Data Analyst)")

    if st.button("🚀 Enter JobMate"):
        if name and role:
            st.session_state.logged_in = True
            st.session_state.user = {
                "name": name,
                "education": education,
                "experience": experience,
                "role": role
            }
            st.rerun()
        else:
            st.warning("Please fill in all required fields (Name & Role).")
    st.stop() # Stop further execution if not logged in

# Set Dashboard page config
st.set_page_config(
    page_title="JobMate Dashboard", 
    # page_icon=Image.open("assets/logo.png"),
    layout="centered",
    initial_sidebar_state="expanded",
    )

# Load user info from session state
user = st.session_state.user

# Custom CSS
with open("assets/styles.css") as styles:
    st.markdown(f"<style>{styles.read()}</style>", unsafe_allow_html=True)

# App title
st.markdown("<h1 class='main-title'>JobMate 💼</h1>", unsafe_allow_html=True)
# st.write(f"Welcome back **{user['name']}**, I am your personal assistant for job applications and interview prep.")
st.markdown(f"<h5 style='text-align: center;'>Welcome back <strong>{user['name']}</strong>, I am your personal assistant for job applications and interview prep.</h5>", unsafe_allow_html=True)

# st.write(f"You're a **{user['experience']}**-level applicant with a **{user['education']}** background, aiming for a/an **{user['role']}** role.")
st.markdown(f"<h5 style='text-align: center;'>You're a <strong>{user['experience']}</strong>-level applicant with a <strong>{user['education']}</strong> background, aiming for a/an <strong>{user['role']}</strong> role.</h5>", unsafe_allow_html=True)

# Sidebar navigation
show_sidebar()


# Dashboard buttons
st.markdown("## 🚀 Get Started")
col1, col2 = st.columns(2)

with col1:
    st.page_link("pages/Resume_Builder.py", label="Build My Resume", icon="📄", help="Craft a professional resume with AI assistance")
    st.page_link("pages/CV_Builder.py", label="Build My CV", icon="📝", help="Generate a clean CV in seconds with AI assistance")
    st.page_link("pages/Cover_Letter_Builder.py", label="Write Cover Letter", icon="✉️", help="Create a tailored cover letter for your job applications")

with col2:
    st.page_link("pages/Job_Desc_Analyzer.py", label="Analyze Jobs ", icon="📋", help="Get concise job description analysis and even analyze your fit")
    st.page_link("pages/Interview_Prep.py", label="Practice Interview", icon="🎙️", help="Get custom interview prep questions")
    st.page_link("pages/Tips_and_Resources.py", label="View Career Tips", icon="📘", help="Get tips an resources to boost your professional growth")


# st.write("Session User Info:", st.session_state.user_info)
