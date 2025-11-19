# Movie_Review_Analyzer_with_LLM
Анализатор тональности отзывов с объяснением, с помощью LLM с RAG механикой.

## Как запустить?
Чтобы запустить проект сначала нужно установить все зависимости, а после запустить Streamlit скрипт:
```
pip install -r requirements.txt
streamlit run app.py
```

## Структура проекта

```
Movie_Review_Analyzer_with_LLM/
├── data/
│   └── chroma_db/        # Векторная база данных, основаная на отзывах фильмов
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
