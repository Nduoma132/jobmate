# import streamlit as st
# from config import call_gemini

# # Page title
# st.title("🤖 Chat Assistant")

# # Personalized greeting
# user = st.session_state.get("user_resume_data", {})
# user_name = user.get("name", "there")
# st.markdown(f"Hey **{user_name}**, I'm here to assist you. Ask me anything related to your career!")


# # Initialize session state for messages
# if "messages" not in st.session_state:
#     st.session_state.messages = []

# # Display previous messages
# for msg in st.session_state.messages:
#     with st.chat_message("user" if msg["role"] == "user" else "assistant"):
#         st.markdown(msg["message"])


# # Handle user input
# if prompt := st.chat_input("Ask EduBot 🧠..."):

#     # Save user message
#     user_msg = {"role": "user", "parts": [prompt]}
#     st.session_state.messages.append(user_msg)

#     # Show user message bubble
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     # Get Gemini response using your call_gemini function
#     response = call_gemini(prompt)

#     # Show assistant bubble
#     with st.chat_message("assistant"):
#         st.markdown(response)

#     # Save assistant message
#     assistant_msg = {"role": "assistant", "parts": [response]}
#     st.session_state.messages.append(assistant_msg)


import streamlit as st
from config import call_gemini

# Page title
st.title("🤖 Chat Assistant")

# # Debugging: Check session state
# st.write(st.session_state.user)

# Personalized greeting
user = st.session_state.get("user", {})
user_name = user.get("name")
st.markdown(f"Hey **{user_name}**, I'm here to assist you. Ask me anything related to your career!")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["message"])  # Read from "message" key

# Handle user input
if prompt := st.chat_input("Ask JobMate 🧠..."):

    # Save user message
    user_msg = {"role": "user", "message": prompt}  # Use "message" not "parts"
    st.session_state.messages.append(user_msg)

    # Show user message bubble
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get Gemini response
    response = call_gemini(prompt)

    # Show assistant bubble
    with st.chat_message("assistant"):
        st.markdown(response)

    # Save assistant message
    assistant_msg = {"role": "assistant", "message": response}  # Same here
    st.session_state.messages.append(assistant_msg)


# st.write("Session Messages:", st.session_state.messages)