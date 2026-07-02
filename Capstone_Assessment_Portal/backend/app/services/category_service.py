from datetime import datetime

from app.repositories.category_repository import CategoryRepository


class CategoryService:

    @staticmethod
    async def create_category(category):

        existing = await CategoryRepository.get_category_by_name(category.name)

        if existing:
            return None

        category_data = {
            "name": category.name,
            "description": category.description,
            "created_at": datetime.utcnow().isoformat()
        }

        category_id = await CategoryRepository.create_category(category_data)

        return {
            "id": str(category_id),
            "name": category_data["name"],
            "description": category_data["description"],
            "created_at": category_data["created_at"]
        }
    @staticmethod
    async def get_all_categories():

        return await CategoryRepository.get_all_categories()

    @staticmethod
    async def get_category(category_id):

        return await CategoryRepository.get_category_by_id(
            category_id
        )

    @staticmethod
    async def update_category(category_id, category):

        data = {
            "name": category.name,
            "description": category.description
        }

        result = await CategoryRepository.update_category(
            category_id,
            data
        )

        return result.modified_count

    @staticmethod
    async def delete_category(category_id):

        result = await CategoryRepository.delete_category(
            category_id
        )

        return result.deleted_count