import os
import gradio as gr
from langchain.embeddings import OpenAIEmbeddings
from icecream import ic
from langchain.vectorstores import Qdrant
import qdrant_client
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.prompts.chat import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    SystemMessagePromptTemplate,
)

import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

os.environ["OPENAI_API_KEY"] = "random-string"
qdrant_url="http://3.70.244.22:6333"
system_template = """Vous êtes LoiLibreQA, un assistant AI open source pour l'assistance juridique.
Vous recevez une question et fournissez une réponse claire et structurée.Lorsque cela est pertinent, utilisez des points et des listes pour structurer vos réponses.

Utilisez les éléments de contexte suivants pour répondre à la question de l'utilisateur. 
Si vous ne connaissez pas la réponse, dites simplement que vous ne savez pas, n'essayez pas d'inventer une réponse.
----------------
{context}"""
messages = [
    SystemMessagePromptTemplate.from_template(system_template),
    HumanMessagePromptTemplate.from_template("{question}"),
]
CHAT_PROMPT = ChatPromptTemplate.from_messages(messages)


embeddings = OpenAIEmbeddings(openai_api_base="http://3.70.244.22:8444/v1")

client = qdrant_client.QdrantClient(qdrant_url,api_key=None)
doc_store = Qdrant(
    client=client, collection_name="loilibreqa", 
    embeddings=embeddings,
)

# prompt template is 107/512 tokens https://platform.openai.com/tokenizer 
llm = ChatOpenAI(openai_api_base="http://3.70.244.22:8111/v1", max_tokens=200,temperature=0)
chain_type_kwargs = {"prompt": CHAT_PROMPT}
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=doc_store.as_retriever(search_kwargs={"k": 1}),
    chain_type_kwargs=chain_type_kwargs,
    return_source_documents=True
)

def get_answer(query):
    result = qa({"query": query})
    ic(result)
    return result

iface = gr.Interface(fn=get_answer, inputs="text", outputs="text")
iface.launch()
