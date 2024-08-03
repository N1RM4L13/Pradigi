from pinecone import Pinecone
from src.utils import create_embeds
import re

pc = Pinecone(api_key="32da42f1-943a-44fa-a759-627e27d4373c")
index = pc.Index("pradigi")

def retrieve(query: str,k_value: int = 3):
    response=index.query(
        namespace="Default",
        vector=create_embeds([re.sub('\s+',' ',query).strip()]),
        top_k=k_value,
        include_metadata=True,
    )
    return response