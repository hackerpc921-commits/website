# CYBERHARI Labs 🛡️

**CYBERHARI Labs** is an elite, interactive cybersecurity learning platform. It provides a safe, sandbox environment for running real-world Python security tools through a sleek, high-tech web interface.

## 🚀 Features
- **24 Specialized Security Tools**: Interactive terminal for reconnaissance, exploitation, and more.
- **Dynamic UI**: Modern, responsive design with Matrix-style backgrounds.
- **Easy Hosting**: Pre-configured for Vercel, Render, and Railway.

## 🏁 Setup & Deployment

### Local Development
1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
2. **Start the server**:
   ```bash
   python run.py
   ```
3. **Open the browser**:
   Visit `http://localhost:8000`

### 🌍 Deployment (Hosting)

#### Frontend (Vercel)
The project is now optimized for Vercel. Simply connect your GitHub repository to Vercel and it will find `index.html` at the root automatically.

#### Backend (Render / Railway)
The project includes a `Procfile` and `render.yaml`.
- **Render**: Create a "Web Service", connect your repo, and use `python run.py` as the start command.

## 💻 Tech Stack
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Backend**: FastAPI (Python)
- **Database**: SQLite (SQLAlchemy)

## ⚠️ Disclaimer
**CYBERHARI Labs** is for **educational purposes only**. Always act ethically.
