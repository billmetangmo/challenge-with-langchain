import sqlite3
from langchain.embeddings import OpenAIEmbeddings
import os
import json
import urllib3
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams,PointStruct
import uuid

os.environ["OPENAI_API_KEY"] = "random-string"
embeddings = OpenAIEmbeddings(openai_api_base="http://3.76.182.94:8111/v1/")
http = urllib3.PoolManager()
url = 'http://3.76.182.94:8111/v1/embeddings'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/114.0',
    'Accept': 'application/json',
    'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/json',
    'DNT': '1',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'
}

data = {
    "model": "string",
    "input": "string",
    "user": ""
}


def from_text_to_vector(text):
    data = {
    "model": "string",
    "input": text,
    "user": ""
    }
    encoded_data = json.dumps(data).encode('utf-8')
    response = http.request('POST', url, body=encoded_data, headers=headers)
    return json.loads(response.data.decode('utf-8'))

client = QdrantClient(":memory:")
client.create_collection(
    collection_name="loilibreqa",
    vectors_config=VectorParams(size=4096, distance=Distance.COSINE), #pkoi 100 marche pas
)

conn = sqlite3.connect('LoiLibreQA/faiss_document_store.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM document")
rows = cursor.fetchall()
for i,row in enumerate(rows[0:9]):
    text=row[0].encode().decode('unicode_escape')
    decoded_response =from_text_to_vector("string"+str(i))
    print(decoded_response["data"][0]["embedding"][-1])
    client.upsert(
        collection_name="loilibreqa",
        points=[
            PointStruct(
                id=str(uuid.uuid4()),
                vector=decoded_response["data"][0]["embedding"],
                payload={"text":"string"+str(i)}
            )
        ]
    )
conn.close()

# search for similar vectors
query_vector=from_text_to_vector("1")["data"][0]["embedding"]
hits = client.search(
    collection_name="loilibreqa",
    query_vector=query_vector,
    limit=1  # Return 5 closest points
)
print(hits)