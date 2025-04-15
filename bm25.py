import jieba
from typing import List, Any
#from langchain_community.retrievers import BM25Retriever
from langchain_core.documents import Document
from rank_bm25 import BM25Okapi
from config import SEARCH_RESULT_NUM

def preprocessing_func(text: str) -> list[Any] | list[Document]:
    return list(jieba.cut(text))

def bm25_search(docs, query):
    texts = [i.page_content for i in docs]
    texts_processed = [preprocessing_func(t) for t in texts]
    vectorizer = BM25Okapi(texts_processed)
    return vectorizer.get_top_n(preprocessing_func(query), texts, n=SEARCH_RESULT_NUM)