from fastapi import FastAPI

app = FastAPI(title="Zaria API")

@app.get("/")
async def root():
    return {"message": "Zaria API"}

@app.get("/health")
async def health():
    return {"status": "ok"}
