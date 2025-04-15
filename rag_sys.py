import os
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from config import HUGGINGFACE_MODEL_NAME_EMB, SEARCH_RESULT_NUM

def rag(docs, query):
    embeddings = HuggingFaceEmbeddings(model_name=HUGGINGFACE_MODEL_NAME_EMB, model_kwargs={'device': 'cuda:0'})
    if os.path.exists("db"):
        # 如果本地的 db 存在，直接加载
        db = FAISS.load_local("db", embeddings,allow_dangerous_deserialization=True)
    else:
        # 如果本地的 db 不存在，构建 db
        print("正在搭建本地数据库")
        print("----------------------------------------------------------------------")
        db = FAISS.from_documents(docs, embeddings)
        db.save_local("db")
    return db.similarity_search(query, k=SEARCH_RESULT_NUM)