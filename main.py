from rag_chain import build_rag_chain
from KEY_FILE import MISTRAL_API_KEY
import os

os.environ["MISTRAL_API_KEY"] = MISTRAL_API_KEY

def main():
    rag_chain = build_rag_chain()

    new_review = "The movie was visually beautiful, but the story was slow and I got bored by the end."
    resp = rag_chain.invoke(new_review)

    print(resp.content)

if __name__ == "__main__":
    main()
