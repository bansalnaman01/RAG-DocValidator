# 🏹 Archer AI Evidence Validator

> A FastAPI-powered backend with a RAG (Retrieval-Augmented Generation) pipeline that automatically audits evidence files stored in Archer, using Groq for ultra-fast AI inference.

---

## 📋 Table of Contents

- [Prerequisites](#-prerequisites)
- [Environment Configuration](#️-environment-configuration)
- [Running the Server](#️-running-the-server)
  - [Option A: Docker (Recommended)](#option-a-using-docker-recommended)
  - [Option B: Local Python](#option-b-manual-setup-local-python)
- [ngrok Tunnel Setup](#-ngrok-tunnel-setup)
- [Project Structure](#-project-structure)
- [Libraries Used](#️-libraries-used)

---

## ✅ Prerequisites

Before starting, ensure you have the following ready:

| Requirement | Description | Link |
|---|---|---|
| **ngrok** | Creates a secure tunnel from Archer to your local machine | [Download](https://ngrok.com/download) |
| **Groq API Key** | Powers ultra-fast AI inference via Llama-3 | [Get Key](https://console.groq.com/) |
| **Runtime** | Docker Desktop *(recommended)* **or** Python 3.10+ | — |

---

## 🛠️ Environment Configuration

Create a `.env` file in the **root directory** of the project. This file stores your credentials and is read by both Docker and the Python scripts.

```env
# Archer Login Credentials
ARCHER_INSTANCE=Default
ARCHER_USERNAME=your_username
ARCHER_PASSWORD=your_password
ARCHER_BASE= base_url

# AI Engine Key (Groq)
GROQ_API_KEY=gsk_your_actual_groq_key_here
```

> ⚠️ **Never commit `.env` to version control.** Ensure it is listed in your `.gitignore`.

---

## ⚙️ Running the Server

### Option A: Using Docker *(Recommended)*

Ensures all dependencies are isolated and avoids environment conflicts.

**1. Build the image:**
```bash
docker build -t archer-ai-service .
```

**2. Run the container:**
```bash
docker run -d -p 8000:8000 --name archer-ai --env-file .env archer-ai-service
```

---

### Option B: Manual Setup (Local Python)

Use this if you prefer running the code directly in your terminal.

**1. Create and activate a virtual environment:**
```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS / Linux / Fedora
source venv/bin/activate
```

**2. Install dependencies:**
```bash
pip install -r requirements.txt
```

**3. Start the server:**
```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

---

## 🌐 ngrok Tunnel Setup

Archer is a cloud platform and cannot reach your local machine directly. ngrok creates a secure public tunnel to your localhost.

**1. Authenticate ngrok** *(one-time setup)*:
```bash
ngrok config add-authtoken YOUR_AUTHTOKEN_HERE
```

**2. Start the tunnel:**
```bash
ngrok http 8000
```

**3. Update the Archer UI:**

- Copy the **Forwarding URL** shown in the terminal (e.g., `https://a1b2-c3d4.ngrok-free.dev`)
- Open the **Archer Custom Object** code
- Update the `BACKEND_URL` in the `CONFIG` section:

```javascript
BACKEND_URL: "https://your-new-url.ngrok-free.dev/validate"
```

> 🔁 **Note:** The ngrok URL changes every time you restart the tunnel (on the free plan). Remember to update `BACKEND_URL` in Archer each time.

---

## 📂 Project Structure

```
archer-ai-evidence-validator/
│
├── api.py                  # Main entry point — receives requests from Archer, manages audit flow
├── Dockerfile              # Instructions for building the containerized environment
├── requirements.txt        # All required Python libraries
├── .env                    # Your credentials (not committed to Git)
│
└── src/                    # Core AI logic — do not modify directly
    └── ...                 # Configured to pull all settings from .env
```

> ⚠️ Do **not** modify files inside `src/` directly. They are configured to pull settings from your `.env` file.

---

## 🗂️ Libraries Used

| Library | Purpose |
|---|---|
| **FastAPI** | High-performance web framework for the API |
| **Uvicorn** | Lightning-fast ASGI server to run FastAPI |
| **Groq** | Ultra-fast inference for the Llama-3 model |
| **LangChain** | Orchestrates the RAG (Retrieval-Augmented Generation) workflow |
| **PyPDF** | Extracts text from evidence PDF files |
| **FAISS** | Vector database for efficient document chunk searching |

---



