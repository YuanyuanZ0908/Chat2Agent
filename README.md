# 📊 CellChat Chatbot Web Interface

A GitHub-hosted interactive chatbot UI powered by Groq + LLaMA3 API and CellChat R analysis pipeline (via Python `rpy2`).

---

## 📁 Project Structure
```
cellchat-chatbot/
├── frontend/
│   └── index.html        ← UI Chatbot
├── backend/
│   └── main.py           ← FastAPI API Server
├── run_conversation.py   ← Trigger CellChat pipeline from user prompt
├── cellchat_pipeline.py  ← (Place your full R-wrapped workflow here)
└── README.md             ← You are here
```

## 💬 Example Prompt
```text
Perform a full CellChat analysis on my dataset. The input file is 'data_input.csv' and metadata file is 'meta.csv'.
```

---

## ▶️ Usage Instructions

### 🔧 Setup Backend (FastAPI)
```bash
cd backend
python3 -m venv venv && source venv/bin/activate
pip install fastapi uvicorn pydantic rpy2
uvicorn main:app --reload --port 8000
```

### 🌐 Open Frontend
Just open `frontend/index.html` in your browser.

---

## 🔐 API Key Setup (Groq)
```bash
export GROQ_API_KEY="your_key_here"
```

You can embed this in your Python environment or backend function.

---

## 📦 Deployment Options
- **Frontend**: GitHub Pages or Vercel (static)
- **Backend**: Render, Heroku, Railway, or deploy locally

---

## 🧠 CellChat Analysis Steps
✔ Format check  
✔ Database selection  
✔ Communication inference  
✔ Signaling role analysis  
✔ Global communication pattern analysis  
✔ Gene expression plots  
✔ Save `.rds` object

---

## 📂 Sample Datasets
Place these in the root directory:
- `data_input.csv`
- `meta.csv`

---

## 🤖 Future Features (Optional Enhancements)
- File upload
- Step toggle UI
- Downloadable result files
- Chat history storage

---
Made with ❤️ by Yuanyuan Zhu
