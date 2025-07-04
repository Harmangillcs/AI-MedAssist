from src.helper import load_data, text_split, embedding_model
from langchain.vectorstores import FAISS
import faiss

# Load PDF data
extracted_data = load_data(r"G:\End to End Medical Chatbot Using LLama2\data")

# Create text chunks
text_chunks = text_split(extracted_data)

# Load embedding model
embedding = embedding_model()

# Create FAISS vectorstore
vectordb = FAISS.from_texts([t.page_content for t in text_chunks], embedding)

# Save to the research/ folder
vectordb.save_local(r"G:\End to End Medical Chatbot Using LLama2\research\faiss_index")
