# 📊 AI-MedAssist: End-to-End Medical Chatbot Using LLaMA 2

AI-MedAssist is a local, privacy-preserving **Generative AI-powered chatbot** built using the **LLaMA-2 model**, capable of answering medical queries. The project uses vector search, LangChain, FAISS, and Flask to create a real-time interactive experience.

---

## 🚀 Features

* ✅ Locally hosted LLaMA-2 model (no OpenAI/GPT API required)
* 📄 Answers based on your custom PDF medical data
* 🔍 Fast document search using FAISS
* 🌐 Simple web interface using Flask
* 🧠 Uses LangChain for chaining and prompt templating
* 🖼️ Clean user interface using HTML & CSS

---

## 📁 Folder Structure

```
├── app.py
├── store_index.py
├── requirements.txt
├── model/
│   └── llama-2-7b-chat.ggmlv3.q4_0.bin
├── faiss_index/
│   ├── index.faiss
│   └── index.pkl
├── static/
│   ├── style.css
│   └── Doctor_img.webp
├── templates/
│   └── Index.html
├── data/
│   └── (your medical PDFs)
└── src/
    ├── helper.py
    └── prompt.py
```

---

## 🛠️ How to Run the Project

### ✅ Step 1: Clone the repository

```bash
git clone https://github.com/Harmangillcs/AI-MedAssist.git
cd AI-MedAssist
```

### ✅ Step 2: Create and activate a virtual environment

```bash
py -3.10 -m venv mchatbot
mchatbot\Scripts\activate  # For Windows
```

### ✅ Step 3: Install Python dependencies

```bash
pip install -r requirements.txt
```

### ✅ Step 4: Download and place the model manually

Download the model file from Hugging Face:
🔗 [https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML)

Choose the file:

```
llama-2-7b-chat.ggmlv3.q4_0.bin
```

Place it inside the `model/` folder:

```
model/llama-2-7b-chat.ggmlv3.q4_0.bin
```

### ✅ Step 5: Prepare the FAISS index (run once)

Ensure your medical PDFs are in the `data/` folder, then run:

```bash
python store_index.py
```

This script loads your PDFs, creates embeddings, and saves the FAISS index.

### ✅ Step 6: Start the chatbot

```bash
python app.py
```

Then open your browser and go to:
🔗 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🔐 .gitignore Recommendation

To avoid pushing large files like models and Python environments:

```
model/
mchatbot/
__pycache__/
*.pyc
*.pkl
*.bin
*.log
.env
```

---

## 🔍 Notes

* This chatbot is for **educational use only**. Not for real medical use.
* You can try **TinyLLaMA** for faster local testing.
* If GitHub blocks push due to large files:

  * Use [Git LFS](https://git-lfs.github.com)
  * Or remove files using `.gitignore` and `git rm --cached`

---

## 📜 License

This project is for **non-commercial**, academic, and research purposes only.
Check LLaMA license terms from Meta/Hugging Face separately.

---

## 👩‍💼 Author

**Harman Gill**

GitHub: [https://github.com/Harmangillcs](https://github.com/Harmangillcs)

Feel free to connect or fork the repo if you're working on similar ideas!
