# 🤖 AI Virtual Assistant

<p align="center">
  <img width="1586" height="799" alt="Screenshot 2026-11-02 163103" src="https://github.com/user-attachments/assets/1b4ed149-fdea-46af-8612-78970b9121c4" />
<img width="1596" height="776" alt="Screenshot 2026-11-02 163250" src="https://github.com/user-attachments/assets/3490bcf7-050b-4754-84a0-d2fa58ae33d0" />

</p>

<p align="center">
  <strong>An Intelligent AI-Powered Chat Assistant Built with Flask and Groq LLM</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask">
  <img src="https://img.shields.io/badge/AI-Groq%20LLM-orange">
  <img src="https://img.shields.io/badge/API-OpenAI%20Compatible-green">
  <img src="https://img.shields.io/badge/Status-Active-success">
  <img src="https://img.shields.io/badge/License-MIT-yellow">
</p>

---

## 📌 Project Overview

**AI Virtual Assistant** is an intelligent web-based chatbot application developed using Python and Flask. It integrates Groq-hosted Large Language Models (LLMs) through an OpenAI-compatible API to generate fast, intelligent, and context-aware responses.

The application provides a simple and user-friendly chat interface where users can interact with an AI assistant, ask questions, and receive AI-generated responses in real time.

## ✨ Key Features

- 🤖 **AI-Powered Conversations** – Interact with an intelligent language model.
- ⚡ **Fast AI Responses** – Powered by Groq inference technology.
- 💬 **Interactive Chat Interface** – Simple and user-friendly design.
- 🌐 **Web-Based Application** – Accessible through a browser.
- 🔗 **API Integration** – Uses Groq's OpenAI-compatible API.
- 🔐 **Secure API Configuration** – API key managed through environment variables.
- 🐍 **Python & Flask Backend** – Lightweight and easy to maintain.

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Backend web framework |
| Groq API | AI model integration |
| Large Language Model (LLM) | Natural language generation |
| HTML5 | Web page structure |
| CSS3 | User interface styling |
| JavaScript | Frontend interaction |

## 📂 Project Structure

```text
AI_VIRTUAL_ASSISTANT/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   └── index.html
│
├── app.py
├── requirements.txt
├── aifinal.png
├── .gitignore
└── README.md
```

*Note: The folder structure above is illustrative. Adjust it to match your actual project files.*

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd AI_VIRTUAL_ASSISTANT
```

### 3. Create a Virtual Environment (Recommended)

**Windows:**

```powershell
py -m venv venv
venv\Scripts\activate
```

**macOS / Linux:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies

```bash
py -m pip install -r requirements.txt
```

For macOS/Linux:

```bash
python3 -m pip install -r requirements.txt
```

## 🔑 Groq API Configuration

To use the AI assistant, you need a Groq API key.

1. Visit [Groq Console](https://console.groq.com/keys).
2. Create an account or sign in.
3. Generate a new API key.
4. Configure the key as an environment variable.

**Windows PowerShell:**

```powershell
$env:GROQ_API_KEY = "your-groq-api-key"
```

**macOS / Linux:**

```bash
export GROQ_API_KEY="your-groq-api-key"
```

⚠️ **Security Notice:** Never expose your API key publicly or commit it to GitHub.

## 🚀 Run the Application

Start the Flask application:

**Windows:**

```powershell
py app.py
```

**macOS / Linux:**

```bash
python3 app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

Now you can start chatting with your AI Virtual Assistant!

To stop the server, press `Ctrl + C` in the terminal.

## 🔐 Environment Variables

| Variable | Description |
|---|---|
| `GROQ_API_KEY` | Secret API key used to authenticate Groq API requests |

## 🎯 Project Objectives

- Develop an AI-powered conversational application.
- Integrate Large Language Models into a web application.
- Understand API-based AI application development.
- Build a practical Python Flask project.
- Explore real-world applications of Generative AI.

## 🔮 Future Improvements

- [ ] Chat history and conversation memory.
- [ ] User authentication and registration.
- [ ] Voice input and speech responses.
- [ ] Multiple AI model selection.
- [ ] Dark and light themes.
- [ ] Responsive mobile interface.
- [ ] Chat export functionality.

## 👨‍💻 Author

**Methun Hossain**

Computer Science & Engineering Student | Software Developer | AI/ML Enthusiast

<p>
  <a href="https://github.com/YOUR_GITHUB_USERNAME">
    <img src="https://img.shields.io/badge/GitHub-Profile-black?logo=github">
  </a>
  <a href="https://www.linkedin.com/">
    <img src="https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin">
  </a>
</p>

## 📄 License

This project is licensed under the MIT License.

---

<p align="center">
  <strong>Built with ❤️ using Python, Flask & Groq AI</strong>
</p>

<p align="center">
  ⭐ If you find this project useful, consider giving it a star!
</p>
