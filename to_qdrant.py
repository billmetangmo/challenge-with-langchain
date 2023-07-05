from langchain.document_loaders import CSVLoader
import os
from langchain.embeddings import OpenAIEmbeddings
from icecream import ic
from langchain.vectorstores import Qdrant
import csv

"""
import logging
logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)
"""


os.environ["OPENAI_API_KEY"] = "random-string"
qdrant_url="http://3.124.184.48:6333"

def clean_csv(path):
    with open(path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        # Create a list to store modified rows
        modified_rows = []
        
        # Iterate over each row in the input file
        for row in reader:
            # Modify the "content" column
            modified_content = row['content'].encode().decode('unicode_escape')
            row['content'] = modified_content
            
            # Append the modified row to the list
            modified_rows.append({'content': modified_content})

    with open('content.csv', 'w') as output_file:
        writer = csv.DictWriter(output_file, fieldnames=['content'])
        writer.writeheader()
        writer.writerows(modified_rows)

clean_csv('documents.csv')
loader = CSVLoader(file_path='content.csv')
data = loader.load()
print(len(data))


embeddings = OpenAIEmbeddings(openai_api_base="http://3.124.184.48:8444/v1")
#text = "Prem is an easy to use open source AI platform."
#query_result = embeddings.embed_query(text)
#doc_result = embeddings.embed_documents(data)

doc_store = Qdrant.from_documents(
    data, embeddings, url=qdrant_url, collection_name="loilibreqa"
)

# Search for relevant documents
query="Que se passe t-il en cas d'urgence"
res = doc_store.similarity_search_with_score(query,k=3)
ic(res)

