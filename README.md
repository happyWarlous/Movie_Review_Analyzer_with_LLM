# Movie_Review_Analyzer_with_LLM
Анализатор тональности отзывов с объяснением, с помощью LLM с RAG механикой.
<img width="924" height="702" alt="изображение-Photoroom" src="https://github.com/user-attachments/assets/dce88e16-05cd-4508-aac6-373a0201d658" />

## Как запустить?
1. В файл `KEY_FILE.py` вставьте свой ключ для работы с API Mistral
2. Далее нужно установить все зависимости, а после запустить Streamlit скрипт:
```
pip install -r requirements.txt
streamlit run app.py
```

## Структура проекта

```
Movie_Review_Analyzer_with_LLM/
├── data/
│   └── chroma_db/        # Векторная база данных, основаная на отзывах фильмов
├── KEY_FILE.py           # Ключ для работы с API Mistral
├── app.py                # Точка запуска Streamlit
├── config.py             # Конфигурационные константы, в том числе метапромт
├── embeddings.py         # Эмбендинги
├── llm.py                # LLM которые используются
├── main.py               # Тестовый скрипт, для проверки работы модели
├── rag_chain.py          # RAG-chain
├── requirements.txt      # Python зависимости
├── retriever.py          # Retriever для работы с векторной БД
└── README.md             # Документация
```
