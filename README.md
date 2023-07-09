# French Legal Text QA Application

This application aims to provide QA functionalities for French legal texts, using only open-source solutions. 

## Prerequesites
```bash
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Preprocessing Data

The first step is to convert our SQLite database into a CSV file. This can be achieved with `sql2csv` as follows:

```bash
sql2csv --db "sqlite:///data/french_laws.db" --query "SELECT * FROM document" > documents.csv
```

After obtaining the CSV file, we then use `from_csv_to_qdrant.py` to move all documents to Qdrant:

```bash
python from_csv_to_qdrant.py
```

## Running the Application

To start the application, use the following commands:

For Streamlit, enter:

```bash
streamlit run ui/streamlit.py
```

For Chainlit, start it on port 8502:

```bash
chainlit run ui/chainlit.py --port 8502
```

Lastly, for the main application (powered by Gradio), use:

```bash
python3 ui/app.py
```

Enjoy exploring the French legal corpus through our intuitive QA application!

## Resources
https://github.com/pinecone-io/examples/blob/master/generation/langchain/handbook/05-langchain-retrieval-augmentation.ipynb
https://qdrant.tech/articles/langchain-integration/

https://github.com/hwchase17/langchain/issues/6982#issuecomment-1614905760 (prompt examples by qa)
https://github.com/pinecone-io/examples/blob/master/generation/langchain/handbook/01-langchain-prompt-templates.ipynb
https://python.langchain.com/docs/modules/chains/popular/vector_db_qa
https://python.langchain.com/docs/modules/chains/popular/vector_db_qa#return-source-documents