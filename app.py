from flask import Flask, render_template, jsonify, request
from src.helper import embedding_model
import faiss
from langchain.vectorstores import FAISS
from langchain import PromptTemplate
from langchain.chains import RetrievalQA
from langchain.llms import CTransformers
from src.prompt import * 
import os

app = Flask(__name__)

# Load embedding model
embedding = embedding_model()

# Load vectorstore database from new research folder
vectordb = FAISS.load_local(
    r"G:\End to End Medical Chatbot Using LLama2\research\faiss_index", 
    embeddings=embedding
)

# Prompt template
PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

chain_type_kwargs = {"prompt": PROMPT}

# Load LLM model
'''llm = CTransformers(
    model=r"G:\End to End Medical Chatbot Using LLama2\model\llama-2-7b-chat.ggmlv3.q4_0.bin",
    model_type="llama",
    config={
        "max_new_tokens": 512,
        "temperature": 0.8
    }
)'''

llm = CTransformers(
    model=r"G:\End to End Medical Chatbot Using LLama2\model\tinyllama-1.1b-chat-v1.0.Q5_0.gguf",
    model_type="llama",
    config={
        "max_new_tokens": 250,
        "temperature": 0.7
    }
)



# Set up QA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectordb.as_retriever(search_kwargs={'k': 2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

# Default Flask route
@app.route("/")
def index():
    return render_template("Index.html")

# Chat route
@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    print("User:", msg)

    try:
        result = qa({"query": msg})
        print("Response:", result["result"])
        return str(result["result"])
    except Exception as e:
        print("Error:", e)
        return "Error processing your query."

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
