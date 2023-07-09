# Prem Challenge x LLMs in Production Conference

### link to challenga 
link to challenge: https://github.com/premAI-io/challenge-with-langchain

### what i have done
create a virtual mahcine wiithout gpu m6a ( just ubuntu/debian are supported)
install using the curl command , the git then docker did not work
open port 8111 and 8000 from publicfacing

No error because hangs
-----------> 4cpu and 16gb of ram takes 4 minutes to answer

content=' Sure! A large language model is a type of artificial intelligence (AI) that is trained on a huge amount of text data to generate human-like language. It can be used for a variety of tasks, such as understanding and generating natural language text, recognizing speech, and even playing games like chess or Go.\n\nLarge language models are typically created using deep learning techniques, which involve training neural networks on massive amounts of data. The resulting models can process and generate human-like language with high accuracy, making them useful for a wide range of applications in fields such as natural language processing (NLP), computer vision,' additional_kwargs={} example=False
real    4m24.155s
user    0m1.714s
sys     0m0.196s

-----------> 16cpu and 16gb of ram takes 1 minutes to answer
content=' Sure! A large language model is a type of machine learning algorithm that can process and generate natural language text. It\'s called "large" because it has been trained on a very large dataset of text, allowing it to learn patterns and relationships in the data that are difficult for smaller models to pick up on.\n\nOne example of a large language model is GPT-3 (Generative Pre-trained Transformer 3), which was created by researchers from Large Model Systems Organization (LMSYS). This model has achieved impressive results in language tasks such as text generation, language translation, and question answering' additional_kwargs={} example=False
real    1m13.620s
user    0m1.820s
sys     0m0.302s


sql2csv --db "sqlite:///LoiLibreQA/faiss_document_store.db" --query "SELECT * FROM document" > documents.csv
Temps pour loader les 46495 documents = 21 minutes [95% - 44544 ]

It takes 29s-59s to answer to my question about urgency with chain_type=stuff and k=1
1 min 38s en exploitant README.md


streamlit run ui-streamlit.py
chainlit run ui-chainlit.py --port 8502
python3 app.py (gradio)

## Resources
https://github.com/pinecone-io/examples/blob/master/generation/langchain/handbook/05-langchain-retrieval-augmentation.ipynb
https://qdrant.tech/articles/langchain-integration/

https://github.com/hwchase17/langchain/issues/6982#issuecomment-1614905760 (prompt examples by qa)
https://github.com/pinecone-io/examples/blob/master/generation/langchain/handbook/01-langchain-prompt-templates.ipynb
https://python.langchain.com/docs/modules/chains/popular/vector_db_qa
https://python.langchain.com/docs/modules/chains/popular/vector_db_qa#return-source-documents