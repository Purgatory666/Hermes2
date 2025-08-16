<p align="center">
    <img src="https://capsule-render.vercel.app/api?type=waving&color=0:FFFFFF,50:F5F5DC,100:FFD700&height=200&section=header&text=Hermes%20%7C%20AI%20Translation%20Tool&fontSize=40&fontColor=000000&animation=fadeIn&fontAlignY=35" alt="Hermes Banner"/>
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&weight=600&size=22&pause=1000&color=00FFCC&center=true&vCenter=true&width=600&lines=Local+AI-Powered+Translations;Style+%7C+Tone+%7C+Poetic+Control;Built+With+Flask+%26+Ollama" alt="Typing SVG"/>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python"/>
  <img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white" alt="HTML"/>
  <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white" alt="CSS"/>
  <img src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black" alt="JavaScript"/>
  <img src="https://img.shields.io/badge/Ollama-00ffcc?style=for-the-badge" alt="Ollama"/>
</p>

---

## 🚀 Overview
Hermes is a **Flask-based AI translation backend** powered by **Ollama's local LLM models**.  
It intelligently adapts translations based on **style**, **tone**, and **creativity**—even making them poetic when you want.

---

## ✨ Features
- 🎯 **Dynamic Prompt Building** — Fully customized translation prompts
- 🎭 **Style & Tone Control** — Formal, casual, poetic, business, and more
- ⚡ **Local AI Processing** — No external API, powered by `llama3:8b`
- 🌐 **RESTful API** — Simple JSON endpoint for easy integration
- 🔄 **Flexible Model Support** — Plug in other Ollama models

---

## 📦 Installation
```bash
# Clone the repo
git clone https://github.com/Rushorgir/Hermes.git
cd Hermes

# Create virtual environment
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

# Install dependencies
pip install -r requirements.txt
```
---

▶️ Usage

```
Start the server:
python run.py

API will be live at:
http://localhost:5000
```
---

## 🐛 Troubleshooting
- Ollama not running → Run ollama serve
- Model missing → Run ollama pull llama3:8b
- Import errors → Activate venv & pip install -r requirements.txt

---

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:000000,100:00ffcc&height=100&section=footer"/>
</p>
