from pinecone import Pinecone
from src.utils import create_embeds
import re

pc = Pinecone(api_key="Key")
index = pc.Index("pradigi")

def retrieve(query: str,k_value: int = 3):
    response=index.query(
        namespace="Default",
        vector=create_embeds([re.sub('\s+',' ',query).strip()]),
        top_k=k_value,
        include_metadata=True,
    )
    return [re.sub('\s+',' ',i['metadata']['text']) for i in response['matches']]

