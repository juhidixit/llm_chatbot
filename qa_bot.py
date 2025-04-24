import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain_community.chains import RetrievalQA
from pypdf import PdfReader

def load_and_split_docs(filename):
    # Check file type
    ext = os.path.splitext(filename)[1].lower()
    if ext == ".pdf":
        text = ""
        reader = PdfReader(filename)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    else:  # Default to txt
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()

