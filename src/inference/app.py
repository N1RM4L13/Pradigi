import streamlit as st
from llm import llm_call
from retriever import retrieve
import openai

client = openai.OpenAI(
  api_key="fc98e46e525fbaf45ca0c94de7a71cf6a2036649d06f04f9212a3485eb5d7c7a",
  base_url="https://api.together.xyz/v1",
)

st.title("Pradigi's Sage")


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "Hello, How are you?",
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        documents="\n".join(retrieve(text))
        stream=response = client.chat.completions.create(
            model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant. Answer to query only according to the context provided in an informative and descriptive way."},
                {"role": "user", "content": f"Context:\n{documents}\n\nQuery:{text}"},
            ],
            temperature=0.7,max_tokens=2000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=["<|eot_id|>"],
            stream=True
            )
        response=st.write_stream(stream)


