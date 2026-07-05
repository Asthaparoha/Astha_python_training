from fastapi import APIRouter, Depends

from app.constants.result_messages import ResultMessages
from app.dependencies.auth_dependency import student_required
from app.services.result_service import ResultService
from app.utils.response import success_response

router = APIRouter(
    prefix="/results",
    tags=["Results"]
)


@router.get("/{attempt_id}")
async def get_result(
    attempt_id: str,
    current_user=Depends(student_required)
):
    """
    Fetch result of a submitted attempt.
    """

    result = await ResultService.get_result(
        attempt_id,
        current_user
    )

    response = success_response(
        message=ResultMessages.RESULT_FETCHED,
        data=result
    )

    return response