import requests


def create_embeds(text:str):
    url = "https://api.together.xyz/v1/embeddings"
    
    payload = {
        "model": "togethercomputer/m2-bert-80M-8k-retrieval",
        "input": text
        }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": "Bearer fc98e46e525fbaf45ca0c94de7a71cf6a2036649d06f04f9212a3485eb5d7c7a"
        }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()["data"][0]["embedding"]