from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="vector_store/product_index",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever(search_kwargs={"k":3})


def product_agent(state):

    query = state["query"]

    docs = retriever.get_relevant_documents(query)

    result = "\n\n".join([d.page_content for d in docs])

    state["result"] = result

    return state