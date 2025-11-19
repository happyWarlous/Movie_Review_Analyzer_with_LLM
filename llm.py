from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from config import CLASSIFY_MODEL, CLASSIFY_METAPROMT

def get_prompt():
    return ChatPromptTemplate.from_template(CLASSIFY_METAPROMT.strip())

def get_main_llm():
    return ChatMistralAI(
        model=CLASSIFY_MODEL,
        temperature=0.2
    )

def get_light_llm():
    return ChatMistralAI(
        model=CLASSIFY_MODEL,
        temperature=0.0
    )
