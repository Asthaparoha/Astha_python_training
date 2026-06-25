from fastapi import FastAPI

app = FastAPI(
    title="Assessment Portal API",
    description="Backend API for Assessment Portal",
    version="1.0.0",
)


@app.get("/", tags=["Home"])
async def home():
    return {
        "success": True,
        "message": "Assessment Portal API is running successfully"
    }