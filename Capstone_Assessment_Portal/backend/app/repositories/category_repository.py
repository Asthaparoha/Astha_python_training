from bson import ObjectId

from app.database.connection import database


class CategoryRepository:

    @staticmethod
    async def create_category(category: dict):
        result = await database.categories.insert_one(category)
        return result.inserted_id

    @staticmethod
    async def get_category_by_name(name: str):
        return await database.categories.find_one(
            {"name": name}
        )

    @staticmethod
    async def get_all_categories():
        categories = []

        async for category in database.categories.find():
            category["id"] = str(category["_id"])
            del category["_id"]
            categories.append(category)

        return categories

    @staticmethod
    async def get_category_by_id(category_id: str):
        return await database.categories.find_one(
            {
                "_id": ObjectId(category_id)
            }
        )

    @staticmethod
    async def update_category(category_id: str, data: dict):

        return await database.categories.update_one(
            {
                "_id": ObjectId(category_id)
            },
            {
                "$set": data
            }
        )

    @staticmethod
    async def delete_category(category_id: str):

        return await database.categories.delete_one(
            {
                "_id": ObjectId(category_id)
            }
        )