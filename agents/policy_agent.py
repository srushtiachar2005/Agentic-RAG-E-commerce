from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory="vector_store/policy_index",
    embedding_function=embeddings
)

retriever = vectorstore.as_retriever()


def policy_agent(state):

    query = state["query"]

    docs = retriever.get_relevant_documents(query)

    state["result"] = docs[0].page_content

    return state