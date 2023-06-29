import os

from langchain.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage

os.environ["OPENAI_API_KEY"] = "random-string"

chat = ChatOpenAI(openai_api_base="http://127.0.0.1:8111/api/v1", max_tokens=128)

messages = [
    HumanMessage(content="Can you explain what is a large language model?")
]
chat(messages)

print(chat(messages))
