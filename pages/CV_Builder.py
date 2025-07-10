import streamlit as st
from config import show_sidebar

show_sidebar()

# App Configuration
app_title = "CV Builder"
app_icon = "📝"

# Set page configuration
st.set_page_config( 
    page_title=app_title,
    page_icon=app_icon,
    layout="centered",
    initial_sidebar_state="collapsed"
    )

st.title(" CV Builder")
st.write("This feature is coming soon! 🚧")
