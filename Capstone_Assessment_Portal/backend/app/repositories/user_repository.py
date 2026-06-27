from app.database.connection import database


class UserRepository:

    @staticmethod
    async def get_user_by_email(email: str):
        return await database.users.find_one({"email": email})

    @staticmethod
    async def create_user(user: dict):
        return await database.users.insert_one(user)