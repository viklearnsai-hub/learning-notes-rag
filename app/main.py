from fastapi import FastAPI

app = FastAPI(title="Learning notes rag assistant")


@app.get("/health")
def health_check():
    return {"status":"ok"}