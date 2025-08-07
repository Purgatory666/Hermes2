# 🧠 Creative Language Translator  
**CodeZilla '25 Hackathon Project**

A web-based AI-powered translator that goes beyond literal word translation. It smartly retains the **meaning**, **tone**, and **style** of the original content—whether translating between languages or switching between writing styles like **formal**, **casual**, **poetic**, or even **Shakespearean**.

## 🚀 Features
- 🌍 **Multilingual Translation** – Translate between supported languages (e.g. English ⇄ Spanish)  
- ✍️ **Style Transformation** – Convert tone/formality (e.g. formal → casual, prose → poetry)  
- 🧠 **Context-Aware Output** – Maintains tone, voice, and intent of the original input  
- 🎭 **Creative Rephrasing** – Turn text into poems, scripts, lyrics, etc.  
- 🗣️ **Slang and Idiom Support** – Makes translations naturally conversational

## 🛠️ Tech Stack

| Layer        | Tech  |
|--------------|-------|
| Frontend     | HTML, CSS, JavaScript (or React 👨💻 — based on your setup) |
| Backend      | Python (FastAPI / Flask) |
| LLM          | Open-source model (e.g., LLaMA 3, Mistral, or BLOOM) |
| Hosting/API  | Localhost or cloud deployment (e.g. Render, Vercel, or Heroku) |

## 🪢 Architecture Overview

- The **frontend** collects user input and preferences (language/style).
- It sends this data to the **Python backend** via a REST API (`/translate`).
- The backend processes input using an integrated LLM and returns a styled or translated output.
- The frontend then renders this back to the user in real-time.

## 🧑💻 How to Run Locally

### 1. Clone the Repo
```bash
git clone https://github.com/Purgatory666/Hermes
cd hermes-translator
```

### 2. Start the Backend (Python)
```bash
cd backend
pip install -r requirements.txt
python app.py  
```

### 3. Start the Frontend (JavaScript)
```bash
cd frontend
# Use Live Server / local HTTP server / open index.html in browser
```

## 📁 Project Structure
```
.
├── backend/
│   ├── app.py / main.py       # Python backend with LLM integration
│   └── requirements.txt
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
├── README.md
```

## 🎯 Use Cases
- Language learners wanting to practice translation with tone sensitivity  
- Writers and marketers transforming text across voice and intent  
- Creative artists exploring poetic or lyrical reinterpretation of ideas  

## 💡 Future Enhancements
- Add voice input/output (Text-to-Speech, Speech-to-Text)  
- Support more languages and dialects  
- Save translation history per user  
- Dark mode UI 🌙

## 👥 Team
Built within 24 hours as part of **CodeZilla ’25 Hackathon** by [Your Names Here].

## 📜 License
MIT License. See `LICENSE` file for details.