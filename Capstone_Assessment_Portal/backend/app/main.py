from fastapi import FastAPI

from app.config.settings import settings
from app.database.connection import database

app = FastAPI(
    title="Assessment Portal API",
    description="Backend API for Assessment Portal",
    version="1.0.0",
)


@app.get("/", tags=["Home"])
async def home():
    return {
        "success": True,
        "database": settings.DATABASE_NAME,
    }


@app.get("/health", tags=["Health"])
async def health_check():
    await database.command("ping")

    return {
        "success": True,
        "message": "Database connected successfully"
    }