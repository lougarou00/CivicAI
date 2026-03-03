# CivicAI — Document Intelligence Platform

CivicAI is a professional platform for intelligent document and ticket analysis. Leveraging a **local open-source LLM (Mistral 7B)**, CivicAI provides automated summarization, classification, and keyword extraction for any textual data. Designed to be fast, reliable, and deployable on a private server, it is perfect for projects that require **privacy, local processing, and AI-powered insights**.

---

## 🚀 Key Features

- **Automatic Summarization:** Generate concise summaries from long documents or tickets to quickly understand key points.  
- **Intelligent Classification:** Automatically classify documents into relevant categories such as “Client Complaint”, “Technical Issue”, “Administrative Report”, etc.  
- **Keyword Extraction:** Extract the top 5 essential keywords from any document for fast scanning and indexing.  
- **Web Interface & API:** Interact via a clean, user-friendly web interface or directly through a REST API for integration with other systems.  
- **Local Processing:** Runs entirely on your own server — no cloud dependencies, ensuring data privacy and security.  

---

## 🖥️ Demo Interface

The platform provides a professional and responsive interface where users can:

- Paste text directly into a textarea  
- Click “Analyze” to generate the summary, category, and keywords  
- Use example texts for quick testing  

**Example Input Cases Included:**

1. Client complaint (billing or service issue)  
2. Technical incident report  
3. Administrative progress report  

---

## 🛠️ Technologies Used

- **Backend:** Python 3, FastAPI  
- **LLM Integration:** Mistral 7B via Ollama  
- **Frontend:** HTML, Jinja2, CSS, Font Awesome icons  
- **Server:** Linux VPS (CPU-only, 4 vCPU, 16 GB RAM recommended)  

---

## 📦 Installation & Deployment

1. **Clone the repository:**

```bash
git clone https://github.com/lougarou00/civicai.git
cd civicai
```

2. **Create a Python virtual environment and install dependencies:**

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

3. **Start the Ollama server with Mistral 7B:**

```bash
ollama serve mistral --port 11434
```

4. **Run the FastAPI app (production recommended via Gunicorn or systemd):**

```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --reload
```

5. **Access the platform:**

Open `http://YOUR_SERVER_IP:8000` in your browser

## 🔧 Usage

1. Paste a document or ticket text into the textarea  
2. Click **Analyze**  
3. Wait for the model to generate results (CPU-only mode may take up to 1 minute for long inputs)  
4. View the **Summary**, **Category**, and **Keywords**  
5. Optional: Use the REST API endpoint `/analyze` for programmatic access  

---

## 💡 Advantages

- Full local control — ideal for sensitive data  
- Professional, minimalistic web interface for recruiters or clients  
- Easily extendable: add more categories, tweak prompt engineering, or integrate with internal tools  
- Educational & demonstrative for AI and Data projects

## 📂 Project Structure

```text
civicai/
├── app.py            # FastAPI backend
├── requirements.txt  # Python dependencies
├── templates/
│   └── index.html    # Frontend HTML template
├── static/           # CSS, icons, etc.
└── README.md
```

## ⚠️ Notes

- Currently optimized for CPU-only environments (16GB RAM recommended for Mistral 7B)  
- Execution time depends on input size; expect up to 1 minute for long documents  
- Designed as a demo and professional showcase for data and AI projects  

---

## 📜 License

MIT License — see `LICENSE` for details.