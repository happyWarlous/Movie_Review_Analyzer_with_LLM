from langchain_chroma import Chroma
from embeddings import get_embeddings

def get_retriever():
    emb = get_embeddings()
    vectordb = Chroma(
        collection_name="movie_reviews",
        embedding_function=emb,
        persist_directory=r"../data/chroma_db"
    )
    retriever = vectordb.as_retriever(search_kwargs={"k": 5})
    return retriever
