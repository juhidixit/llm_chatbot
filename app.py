import streamlit as st
from langchain.llms import OpenAI
from langchain.chains.question_answering import load_qa_chain
from langchain.docstore.document import Document

st.title("🧠 Chat With Your Text File")

uploaded_file = st.file_uploader("Upload a .txt file", type="txt")
query = st.text_input("Ask a question about the file:")

if uploaded_file and query:
    # Read the text file
    text = uploaded_file.read().decode("utf-8")
    doc = Document(page_content=text)

    # Set up OpenAI LLM (requires your OpenAI API key in Streamlit Cloud secrets!)
    llm = OpenAI(temperature=0, model_name="gpt-3.5-turbo-instruct")
    chain = load_qa_chain(llm, chain_type="stuff")

    # Run the QA chain
    answer = chain.run(input_documents=[doc], question=query)
    st.write("**Answer:**", answer)


