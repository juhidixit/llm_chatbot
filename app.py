import streamlit as st

st.title("🧠 Chat With Your Text File")

uploaded_file = st.file_uploader("Upload a .txt file", type="txt")
if uploaded_file is not None:
    st.write("File uploaded successfully!")
query = st.text_input("Ask a question:")
if query:
    st.write("Your question was:", query)
