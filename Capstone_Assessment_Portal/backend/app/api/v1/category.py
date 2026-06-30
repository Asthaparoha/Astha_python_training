from fastapi import APIRouter, Depends

from app.core.exceptions import ResourceExistsException
from app.dependencies.auth_dependency import admin_required
from app.schemas.category_schema import CategoryCreate
from app.services.category_service import CategoryService
from app.utils.response import success_response

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.post("/")
async def create_category(
    category: CategoryCreate,
    current_user=Depends(admin_required)
):

    result = await CategoryService.create_category(category)

    if result is None:
        raise ResourceExistsException("Category already exists")

    return success_response(
        message="Category created successfully",
        data=result,
        status_code=201
    )