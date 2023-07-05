import os
from langchain.embeddings import OpenAIEmbeddings
from icecream import ic
from langchain.vectorstores import Qdrant
import qdrant_client
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

"""
import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
"""

os.environ["OPENAI_API_KEY"] = "random-string"
qdrant_url="http://3.124.184.48:6333"


embeddings = OpenAIEmbeddings(openai_api_base="http://3.124.184.48:8444/v1")
#text = "Prem is an easy to use open source AI platform."
#query_result = embeddings.embed_query(text)
#doc_result = embeddings.embed_documents(data)

client = qdrant_client.QdrantClient(qdrant_url,api_key=None)
doc_store = Qdrant(
    client=client, collection_name="loilibreqa", 
    embeddings=embeddings,
)

llm = ChatOpenAI(openai_api_base="http://3.124.184.48:8111/v1", max_tokens=2048)
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=doc_store.as_retriever()
)
qa.run("Que faire en cas d'urgence ?")