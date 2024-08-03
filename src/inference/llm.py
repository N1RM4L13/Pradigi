import openai

client = openai.OpenAI(
  api_key="fc98e46e525fbaf45ca0c94de7a71cf6a2036649d06f04f9212a3485eb5d7c7a",
  base_url="https://api.together.xyz/v1",
)

def llm_call(query,context):
    response = client.chat.completions.create(
    model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant. Answer to query only according to the context provided in an informative and descrbed."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuery:{query}"},
    ],
    temperature=0.7,max_tokens=2000,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0,
    stop=["<|eot_id|>"]
    )

    return response.choices[0].message.content
