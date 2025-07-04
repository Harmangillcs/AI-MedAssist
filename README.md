# 🩺 AI-MedAssist: End-to-End Medical Chatbot Using LLaMA 2

AI-MedAssist is a local, privacy-preserving **Generative AI-powered chatbot** built using the **LLaMA-2 model**, capable of answering medical queries. The project uses vector search, LangChain, FAISS, and Flask to create a real-time interactive experience.

---

## 🚀 Features

- ✅ Locally hosted LLaMA-2 model (no OpenAI/GPT API required)
- 📄 Answers based on your custom PDF medical data
- 🔍 Fast document search using FAISS
- 🌐 Simple web interface using Flask
- 🧠 Uses LangChain for chaining and prompt templating
- 🖼️ Clean user interface using HTML & CSS

---

## 📁 Folder Structure

├── app.py
├── store_index.py
├── requirements.txt
├── model/
│ └── llama-2-7b-chat.ggmlv3.q4_0.bin
├── faiss_index/
│ └── index.faiss
│ └── index.pkl
├── static/
│ ├── style.css
│ └── Doctor_img.webp
├── templates/
│ └── Index.html
├── data/
│ └── (your medical PDFs)
└── src/
├── helper.py
└── prompt.py

yaml
Copy
Edit

---

## 🛠️ How to Run the Project

### ✅ Step 1: Clone the repository

```bash
git clone https://github.com/Harmangillcs/AI-MedAssist.git
cd AI-MedAssist
✅ Step 2: Create and activate a virtual environment
bash
Copy
Edit
py -3.10 -m venv mchatbot
mchatbot\Scripts\activate  # For Windows
✅ Step 3: Install Python dependencies
bash
Copy
Edit
pip install -r requirements.txt
✅ Step 4: Download and place the model manually
Download the model file from Hugging Face:
🔗 https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML

Choose:
llama-2-7b-chat.ggmlv3.q4_0.bin

Place it inside the following folder:

bash
Copy
Edit
model/llama-2-7b-chat.ggmlv3.q4_0.bin
✅ Step 5: Prepare the FAISS index (run once)
This script loads your medical PDFs and generates embeddings.

bash
Copy
Edit
python store_index.py
Make sure your PDFs are inside the data/ folder.

✅ Step 6: Start the chatbot
bash
Copy
Edit
python app.py
Then open your browser and go to:
🔗 http://127.0.0.1:5000

🔐 .gitignore Recommendation
To avoid pushing large files like models and Python environment:

gitignore
Copy
Edit
model/
mchatbot/
__pycache__/
*.pyc
*.pkl
*.bin
*.log
.env
🔍 Notes
This chatbot is for educational use only. Do not use for real medical advice.

You can use a smaller model like TinyLLaMA for faster testing.

If GitHub blocks your push due to large files, use Git LFS or remove those files from the repo before pushing.

📜 License
This project is for non-commercial, academic, and research use only. Please review the LLaMA model license separately via Meta/Hugging Face.

👩‍💻 Author
Harman Gill
GitHub: https://github.com/Harmangillcs

