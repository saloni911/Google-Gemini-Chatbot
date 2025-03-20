import os
import streamlit as st
import google.generativeai as genai


# ✅ Set page config at the start
st.set_page_config(page_title="Google Gemini Chatbot")

# ✅ Load API Key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# ✅ Configure Generative AI model
genai.configure(api_key=GOOGLE_API_KEY)

# ✅ Cache the model to avoid reloading it on every query
@st.cache_resource
def get_model():
    return genai.GenerativeModel("gemini-1.5-pro-latest")

# ✅ Use the correct model from the list
model = get_model()

# ✅ Streamlit UI
st.markdown("<h1 style='text-align: center;'>🤖 Chat with Google Gemini AI</h1>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state["messages"] = []

# ✅ Display Chat History
for role, text in st.session_state["messages"]:
    st.chat_message(role).write(text)

# ✅ User Input
user_input = st.chat_input("Ask me anything...")

if user_input:
    # Append user message
    st.session_state["messages"].append(("user", user_input))
    st.chat_message("user").write(user_input)

    # ✅ Enable Streaming
    response = model.generate_content(user_input, generation_config={"max_output_tokens": 500}, stream=True)
    # response = model.generate_content(user_input)
    with st.chat_message("assistant"):
        response_container = st.empty()
        ai_response = ""

        for chunk in response:
            ai_response += chunk.text
            response_container.write(ai_response)  # ✅ Update in real time

    # Append AI response
    st.session_state["messages"].append(("assistant", ai_response))
