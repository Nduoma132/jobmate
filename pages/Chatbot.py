import streamlit as st
from config import get_chatbot, show_sidebar
from prompts import chatbot_prompt

show_sidebar()

st.title("🤖 Chat Assistant")

# st.write(st.session_state.user)

# Personalized greeting
user = st.session_state.get("user", {})
if not user:
    st.error("You need to log in to use the Chat Assistant.")
    st.stop()
st.markdown(f"Hey **{user['name']}**, I'm here to assist you. Ask me anything related to your career!")

# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state.messages = []

# Initialize multi-turn chat with system prompt
if "chat" not in st.session_state:
    st.session_state.chat = get_chatbot(user)  # ✅ Call the function

# Display previous messages
for msg in st.session_state.messages:
    with st.chat_message("user" if msg["role"] == "user" else "assistant"):
        st.markdown(msg["message"])  # Read from "message" key

# Handle user input
if prompt := st.chat_input("Ask JobMate 🧠..."):

    # Save user message
    user_msg = {"role": "user", "message": prompt}
    st.session_state.messages.append(user_msg)

    # Show user message bubble
    with st.chat_message("user"):
        st.markdown(prompt)

    # Multi-turn chat with memory
    response = st.session_state.chat.send_message(prompt).text

    # Show assistant bubble
    with st.chat_message("assistant"):
        st.markdown(response)

    # Save assistant message
    assistant_msg = {"role": "assistant", "message": response}
    st.session_state.messages.append(assistant_msg)



# Debugging: Show session state messages
# st.write("Session Messages:", st.session_state.messages)