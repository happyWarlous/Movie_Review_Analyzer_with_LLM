from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from retriever import get_retriever
from llm import get_light_llm, get_prompt

def build_rag_chain():
    retriever = get_retriever()
    prompts = get_prompt()
    llm = get_light_llm()

    rag_chain = (
        RunnableParallel(
            context=retriever,
            question=RunnablePassthrough()
        )
        | prompts
        | llm
    )
    return rag_chain
