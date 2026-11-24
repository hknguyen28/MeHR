from fastapi import FastAPI

app = FastAPI(title="MeHR")

@app.get("/health")
def health():
    return {"status": "ok"}