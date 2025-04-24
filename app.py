import streamlit as st
import qa_bot

st.title("🧠 Chat With Your Text File")

if "vector_created" not in st.session_state:
    st.session_state.vector_created = False

uploaded_file = st.file_uploader("Upload a .txt file", type="txt")

if uploaded_file and not st.session_state.vector_created:
    with open("temp.txt", "wb") as f:
        f.write(uploaded_file.read())
    chunks = qa_bot.load_and_split_docs("temp.txt")
    qa_bot.create_vector_db(chunks)
    st.session_state.vector_created = True
    st.success("Text processed! Ask anything.")

query = st.text_input("Ask a question:")

if query and st.session_state.vector_created:
    chain = qa_bot.get_qa_chain()
    answer = chain.run(query)
    st.write("Answer:", answer)
