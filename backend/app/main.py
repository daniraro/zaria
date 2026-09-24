"""Main application entry point."""
from fastapi import FastAPI

app = FastAPI(title="Zaria API")


@app.get("/")
async def root():
    return {"message": "Welcome to Zaria API"}


@app.get("/health")
async def health():
    return {"status": "healthy"}
