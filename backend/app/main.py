from fastapi import FastAPI

app = FastAPI(
    title="AI Commerce Copilot API",
    description="Backend API for AI Commerce Copilot",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to AI Commerce Copilot 🚀",
        "status": "running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }