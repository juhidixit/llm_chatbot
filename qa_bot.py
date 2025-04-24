import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from pypdf import PdfReader

def load_and_split_docs(filename):
    # Check file type
    ext = os.path.splitext(filename)[1].lower()
    if ext == ".pdf":
        text = ""
        reader = PdfReader(filename)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    else:  # Default to txt
        with open(filename, 'r') as f:
            text = f.read()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_text(text)
    return chunks

def create_vector_db(chunks):
    embeddings = OpenAIEmbeddings()
    vector_db = Chroma.from_texts(chunks, embedding=embeddings, persist_directory="vector_db")
    vector_db.persist()

def get_qa_chain():
    embeddings = OpenAIEmbeddings()
    vector_db = Chroma(persist_directory="vector_db", embedding_function=embeddings)
    retriever = vector_db.as_retriever()
    llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo-instruct")
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain

