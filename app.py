from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
import requests

app = FastAPI()
templates = Jinja2Templates(directory="templates")

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL = "mistral"


def query_llm(prompt: str):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )
        return response.json()["response"].strip()
    except Exception as e:
        return f"Erreur LLM: {str(e)}"


def analyze_text(text: str):
    summary_prompt = f"""
    Résume clairement le texte suivant en 4-5 lignes maximum :

    {text}
    """

    classification_prompt = f"""
    Classe le texte dans UNE seule catégorie parmi :
    - Incident technique
    - Réclamation client
    - Demande administrative
    - Problème réseau
    - Autre

    Réponds uniquement par le nom exact de la catégorie.

    Texte :
    {text}
    """

    keywords_prompt = f"""
    Extrait exactement 5 mots-clés importants du texte.
    Réponds uniquement par une liste séparée par des virgules.

    Texte :
    {text}
    """

    return {
        "summary": query_llm(summary_prompt),
        "category": query_llm(classification_prompt),
        "keywords": query_llm(keywords_prompt),
    }


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze", response_class=HTMLResponse)
def analyze_web(request: Request, text: str = Form(...)):
    result = analyze_text(text)

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "original_text": text,
            "summary": result["summary"],
            "category": result["category"],
            "keywords": result["keywords"],
        },
    )


@app.post("/api/analyze")
def analyze_api(payload: dict):
    text = payload.get("text")

    if not text:
        return JSONResponse(status_code=400, content={"error": "Missing 'text' field"})

    result = analyze_text(text)
    return result