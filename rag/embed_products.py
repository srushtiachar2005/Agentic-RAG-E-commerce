import pandas as pd
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document

df = pd.read_csv("data/products.csv")

docs = []

for _, row in df.iterrows():

    text = f"""
    Product: {row['name']}
    Category: {row['category']}
    Price: {row['price']}
    Rating: {row['rating']}
    Description: {row['description']}
    """

    docs.append(Document(page_content=text))

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma.from_documents(
    docs,
    embeddings,
    persist_directory="vector_store/product_index"
)

vectorstore.persist()