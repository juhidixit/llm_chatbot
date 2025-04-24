import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

def load_and_split_docs(filename):
    with open(filename, 'r') as f:
        text = f.read()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(text)
    return chunks

def create_vector_db(chunks):
    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.from_texts(chunks, embedding=embeddings)
    vector_db.save_local("vector_db")

def get_qa_chain():
    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.load_local("vector_db", embeddings)
    retriever = vector_db.as_retriever()
    llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo-instruct")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain
