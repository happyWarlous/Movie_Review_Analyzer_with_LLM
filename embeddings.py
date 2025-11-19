from langchain_mistralai import MistralAIEmbeddings
from config import EMBEDDING_MODEL

def get_embeddings():
    return MistralAIEmbeddings(
        model=EMBEDDING_MODEL
    )
