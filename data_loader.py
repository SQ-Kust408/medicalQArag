from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from config import CHUNK_SIZE, CHUNK_OVERLAP

# 语料库分块
def data_loader(file_path):
    loader = TextLoader(file_path=file_path, encoding="utf8")
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP,
        length_function=len,
        separators=['\n']
    )
    docs = text_splitter.split_documents(documents)
    return docs