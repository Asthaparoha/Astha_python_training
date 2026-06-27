from datetime import datetime

from app.config.settings import settings
from app.core.security import (
    create_access_token,
    hash_password,
    verify_password,
)
from app.repositories.user_repository import UserRepository


class AuthService:

    @staticmethod
    async def register_student(student):

        existing_user = await UserRepository.get_user_by_email(student.email)

        if existing_user:
            return None

        user_data = {
            "full_name": student.full_name,
            "email": student.email,
            "password": hash_password(student.password),
            "role": "student",
            "is_active": True,
            "created_at": datetime.utcnow()
        }

        await UserRepository.create_user(user_data)

        return user_data

    @staticmethod
    async def login(login_data):

        # Hardcoded Admin Login
        if (
            login_data.email == settings.ADMIN_EMAIL
            and login_data.password == settings.ADMIN_PASSWORD
        ):
            token = create_access_token(
                {
                    "email": settings.ADMIN_EMAIL,
                    "role": "admin"
                }
            )

            return {
                "access_token": token,
                "token_type": "bearer",
                "role": "admin"
            }

        # Student Login
        user = await UserRepository.get_user_by_email(login_data.email)

        if user is None:
            return None

        if not verify_password(
            login_data.password,
            user["password"]
        ):
            return None

        token = create_access_token(
            {
                "email": user["email"],
                "role": user["role"]
            }
        )

        return {
            "access_token": token,
            "token_type": "bearer",
            "role": user["role"]
        }