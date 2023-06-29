import numpy as np
from faiss import read_index
from haystack.document_stores import FAISSDocumentStore
from qdrant_client import QdrantClient
from qdrant_client.models import PointStruct
# Load the FAISS index
faiss_index = read_index("LoiLibreQA/faiss_index.index")
# Load the FAISS DocumentStore
document_store = FAISSDocumentStore.load(
    index_path=faiss_index,
    config_path="LoiLibreQA/faiss_config.json"
)
# Get all documents from the FAISS DocumentStore
all_docs = document_store.get_all_documents()
# Initialize the QdrantClient
client = QdrantClient()
# Upsert vectors into Qdrant from the FAISS DocumentStore
for doc in all_docs:
    client.upsert(
        collection_name="my_collection",
        points=[
            PointStruct(
                id=doc.id,
                vector=doc.embedding,
                payload=doc.meta
            )
        ]
    )