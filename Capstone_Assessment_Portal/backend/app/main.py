from fastapi import FastAPI
from app.core.security import hash_password
from app.config.settings import settings
from app.database.connection import database
from app.api.v1.auth import router as auth_router
from app.api.v1.category import router as category_router
from fastapi import Depends

from app.dependencies.auth_dependency import get_current_user
app = FastAPI(
    title="Assessment Portal API",
    description="Backend API for Assessment Portal",
    version="1.0.0",
)
@app.get("/profile", tags=["Authentication"])
async def profile(current_user=Depends(get_current_user)):
    return current_user

@app.get("/", tags=["Home"])
async def home():
    return {
        "password": hash_password("Admin@123")
    }

app.include_router(auth_router)
app.include_router(category_router)
