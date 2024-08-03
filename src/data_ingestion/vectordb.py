from pinecone import Pinecone
import json
from src.utils import create_embeds
import re
import time


pc = Pinecone(api_key="32da42f1-943a-44fa-a759-627e27d4373c")
index = pc.Index("pradigi")



 
with open('src\data_ingestion\preprocessed_data.json', 'r', encoding="utf-8") as openfile:
    json_object = json.load(openfile)

# print(json_object)

# print(create_embeds([json_object[0]['metadata']['text']]))

for i in json_object:
    print(i['metadata']['text'])
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
    time.sleep(5)
    

# index.query(
#     namespace="Default",
#     vector=[0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3],
#     filter={
#         "genre": {"$eq": "documentary"}
#     },
#     top_k=3,
#     include_metadata=True
# )