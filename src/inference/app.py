import streamlit as st
from openai import OpenAI

st.title("Pradigi Bot")

# Set OpenAI API key from Streamlit secrets
client = OpenAI(
    api_key="fc98e46e525fbaf45ca0c94de7a71cf6a2036649d06f04f9212a3485eb5d7c7a",
    base_url="https://api.together.xyz/v1",
)

# Set a default model
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

with st.chat_message("assistant"):
    stream = client.chat.completions.create(
        model=st.session_state["openai_model"],
        messages=[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.messages
        ],
        stream=True,
    )
    response = st.write_stream(stream)
st.session_state.messages.append({"role": "assistant", "content": response})