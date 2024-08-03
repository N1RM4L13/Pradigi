import openai

client = openai.OpenAI(
  api_key="fc98e46e525fbaf45ca0c94de7a71cf6a2036649d06f04f9212a3485eb5d7c7a",
  base_url="https://api.together.xyz/v1",
)

response = client.chat.completions.create(
  model="meta-llama/Meta-Llama-3.1-8B-Instruct-Turbo",
  messages=[
    {"role": "system", "content": "You are a travel agent. Be descriptive and helpful."},
    {"role": "user", "content": "Tell me about San Francisco"},
  ],
  temperature=0.5,max_tokens=2000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0,
  stop=["<|eot_id|>"]
)

print(response.choices[0].message.content)
