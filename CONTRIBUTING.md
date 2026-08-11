# 🚀 Workshop Quick-Start Checklist

A fast, no-fluff guide to get from zero to a deployed, shared project. Follow the sections in order.

---

## 1️⃣ Python Setup

### Remove other Python versions
Multiple Python versions on one machine can cause confusing conflicts. Clean up first:

| OS | How |
|---|---|
| Windows | Settings → Apps → search "Python" → Uninstall each version found |
| macOS (Homebrew) | `brew uninstall python@3.13` *(repeat for any other version)* |
| Linux | Leave system Python alone — just always call `python3.12` explicitly for this project |

> 💡 Not comfortable removing other versions? That's fine — just always type `python3.12` (or `py -3.12` on Windows), never plain `python`, so there's no ambiguity about which one runs.

### Download & install Python 3.12.10
This is the last 3.12 release with official binary installers — our standard for the workshop.

| | Link |
|---|---|
| Windows (64-bit) | [python-3.12.10-amd64.exe](https://www.python.org/ftp/python/3.12.10/python-3.12.10-amd64.exe) |
| macOS | [python-3.12.10-macos11.pkg](https://www.python.org/ftp/python/3.12.10/python-3.12.10-macos11.pkg) |
| Release notes | [python.org/downloads/release/python-31210](https://www.python.org/downloads/release/python-31210/) |

**Windows:** run the `.exe` → ✅ check **"Add python.exe to PATH"** → **Install Now**
**macOS:** run the `.pkg` → follow the default prompts

### ✅ Verify it worked
```bash
# Windows
py -3.12 --version

# macOS / Linux
python3.12 --version
```
Expected output: `Python 3.12.10`

---

## 2️⃣ Account Setup

Five accounts, roughly 10–15 minutes total. Do this before the workshop starts.

### VS Code
🔗 [code.visualstudio.com](https://code.visualstudio.com)
1. Download and install for your OS
2. Open VS Code → **Accounts** icon (bottom-left) → **Sign in with GitHub** *(optional, syncs your settings)*
3. **Extensions** (left sidebar) → search **Python** → install the official Microsoft extension

### GitHub
🔗 [github.com](https://github.com)
1. **Sign up** (skip if you already have an account)
2. Verify your email
3. This is the account you'll fork the workshop repo and submit your project with

### Groq
🔗 [console.groq.com](https://console.groq.com)
1. Sign up (GitHub or Google login is fastest)
2. **API Keys** (left sidebar) → **Create API Key** → name it
3. **Copy it immediately** — shown only once

### Hugging Face
🔗 [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
1. Sign up at [huggingface.co/join](https://huggingface.co/join) and verify your email *(the token button stays greyed out until you do)*
2. Back at **Settings → Access Tokens** → **Create new token**
3. Name it → role: **Read** → **Generate** → copy it

### Streamlit
🔗 [share.streamlit.io](https://share.streamlit.io)
1. **Sign up** → **Continue with GitHub**
2. Authorize when prompted

> 🔒 Keep your Groq key and Hugging Face token safe — you'll paste them into a `.env` file in Section 3.

---

## 3️⃣ Repository: Fork → Clone → Build → Submit

### Fork it to your account
1. Open [github.com/Dev-Samaj/BEST-AI-RAG-Workshop](https://github.com/Dev-Samaj/DevSprint_S1_BEST-AI_Revolution_RAG_Hands_On-2026.git
)
2. Click **Fork** (top-right) → **Create fork**

### Clone it to your machine
```bash
git clone https://github.com/YOUR-USERNAME/BEST-AI-RAG-Workshop.git
cd BEST-AI-RAG-Workshop
```
| Command | What it does |
|---|---|
| `git clone <url>` | Downloads your fork onto your computer |
| `cd BEST-AI-RAG-Workshop` | Moves your terminal into that folder |

### Set up your environment
```bash
# Windows
py -3.12 -m venv venv
venv\Scripts\activate

# macOS / Linux
python3.12 -m venv venv
source venv/bin/activate

pip install -r requirements.txt
```

### Create your branch + submission folder
```bash
git checkout -b submission-YOUR-USERNAME
mkdir submissions/YOUR-USERNAME
```
| Command | What it does |
|---|---|
| `git checkout -b submission-YOUR-USERNAME` | Creates and switches to your own branch |
| `mkdir submissions/YOUR-USERNAME` | Your personal folder for your project files |

### Update your code
Add/edit your files inside `submissions/YOUR-USERNAME/` — your `app.py`, `requirements.txt`, and a project `README.md` describing what you built.

### Commit your work
Commit after every meaningful step — not just once at the end.
```bash
git add .
git commit -m "Add RAG project - YOUR-USERNAME"
```
| Command | What it does |
|---|---|
| `git add .` | Stages your changed files |
| `git commit -m "..."` | Saves a checkpoint with a description |

### Push it
```bash
git push origin submission-YOUR-USERNAME
```
Uploads your branch and commits to your fork on GitHub.

### Create a Pull Request
1. Go to your fork on GitHub → click **Compare & pull request**
2. Confirm it merges into `Dev-Samaj/BEST-AI-RAG-Workshop`
3. Add a short description → **Create pull request**

---

## 4️⃣ Deploy on Streamlit

1. Push your finished code to GitHub *(already done if you followed Section 3)*
2. Go to [share.streamlit.io](https://share.streamlit.io) and log in
3. **Create app** → **Deploy a public app from GitHub**
4. Fill in:
   - **Repository:** your fork
   - **Branch:** `submission-YOUR-USERNAME`
   - **Main file path:** `submissions/YOUR-USERNAME/app.py`
5. Choose your app's name — this becomes your public URL:
   `https://YOUR-APP-NAME.streamlit.app`
   *(pick something clear, e.g. `yourname-rag-chat`)*
6. **Advanced settings** → add your secrets:
   ```toml
   GROQ_API_KEY = "your_groq_api_key_here"
   HF_TOKEN = "your_huggingface_token_here"
   ```
7. Click **Deploy** and wait a few minutes

🎉 Live at `https://YOUR-APP-NAME.streamlit.app`

---

## 5️⃣ Share It on LinkedIn

### ✅ What to include
- [ ] A short description of what you built (PDF Chat Assistant using RAG)
- [ ] Your live Streamlit link
- [ ] Your GitHub repo / PR link
- [ ] Tech stack: Python, Streamlit, ChromaDB, Groq, Hugging Face
- [ ] One thing you learned
- [ ] Tag the community

### Post template
```
Just built my first RAG (Retrieval-Augmented Generation) application! 🚀

At the Dev Samaj BEST AI RAG Workshop, I learned how to build an AI
chatbot that answers questions from any PDF — grounded in real content,
not guesses.

🔧 Tech stack: Python, Streamlit, ChromaDB, Groq (Llama 3.3),
Hugging Face embeddings

🔗 Try it live: https://YOUR-APP-NAME.streamlit.app
💻 Code: https://github.com/YOUR-USERNAME/BEST-AI-RAG-Workshop

Key takeaway: [share one thing you learned]

#RAG #AI #MachineLearning #Python #DevSamaj #Streamlit
```

### Tag the community
- Dev Samaj's official LinkedIn page *(ask your facilitator for the exact handle)*
- The workshop facilitator(s)
- Fellow participants, if you'd like

> 💡 A screenshot or short screen-recording of your app answering a question adds a lot — posts with visuals get far more engagement than text-only ones.

---

**Happy building! 🚀**
