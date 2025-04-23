# qa_bot.py

def load_and_split_docs(filename):
    """Load text file and split into lines as simple 'chunks'."""
    with open(filename, 'r') as f:
        text = f.read()
    # For demo: just return each sentence as a "chunk"
    return text.split('\n')

def create_vector_db(chunks):
    """Just store the chunks for now (not a real vector DB)."""
    # We'll just keep it as a list for demo
    global TEXT_CHUNKS
    TEXT_CHUNKS = chunks

def get_qa_chain():
    """Return a simple function to answer from our stored text."""
    def run(query):
        # Look for any lines that match keywords in the question
        results = []
        for chunk in TEXT_CHUNKS:
            if any(word.lower() in chunk.lower() for word in query.split()):
                results.append(chunk)
        if results:
            return '\n'.join(results)
        else:
            return "Sorry, I couldn't find an answer in your text file."
    return type("DummyChain", (), {"run": staticmethod(run)})()
