from pinecone import Pinecone
import json
from src.utils import create_embeds
import re
import time


pc = Pinecone(api_key="")
index = pc.Index("pradigi")


with open('src\data_ingestion\preprocessed_data.json', 'r', encoding="utf-8") as openfile:
    json_object = json.load(openfile)


for i in json_object:
    index.upsert(
        vectors=[
            {
                "id":i['id'],
                "values":create_embeds([re.sub('\s+',' ',i['metadata']['text']).strip()]),
                "metadata":i['metadata'],
            }
        ],
        namespace="Default"
    )
    time.sleep(5) # Since together provides only 1QPS in free-tier
    
