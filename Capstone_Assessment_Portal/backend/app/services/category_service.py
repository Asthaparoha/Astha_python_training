from datetime import datetime

from app.repositories.category_repository import CategoryRepository


class CategoryService:

    @staticmethod
    async def create_category(category):

        existing_category = await CategoryRepository.get_category_by_name(
            category.name
        )

        if existing_category:
            return None

        category_data = {
            "name": category.name,
            "description": category.description,
            "created_at": datetime.utcnow().isoformat()
        }

        category_id = await CategoryRepository.create_category(category_data)

        category_data.pop("_id", None)

        category_data["id"] = str(category_id)

        return category_data