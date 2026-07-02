from fastapi import APIRouter, Depends

from app.constants.quiz_messages import QuizMessages
from app.dependencies.auth_dependency import (
    admin_required,
    get_current_user,
)
from app.schemas.quiz_schema import QuizCreate
from app.services.quiz_service import QuizService
from app.utils.response import success_response

router = APIRouter(
    prefix="/quizzes",
    tags=["Quizzes"]
)


@router.post("/")
async def create_quiz(
    quiz: QuizCreate,
    current_user=Depends(admin_required)
):
    """
    Create a new quiz.
    """

    result = await QuizService.create_quiz(
        quiz
    )

    response = success_response(
        message=QuizMessages.QUIZ_CREATED,
        data=result,
        status_code=201
    )

    return response


@router.get("/")
async def get_all_quizzes(
    current_user=Depends(get_current_user)
):
    """
    Fetch all quizzes.
    """

    quizzes = await QuizService.get_all_quizzes()

    response = success_response(
        message=QuizMessages.QUIZZES_FETCHED,
        data=quizzes
    )

    return response


@router.get("/{quiz_id}")
async def get_quiz_by_id(
    quiz_id: str,
    current_user=Depends(get_current_user)
):
    """
    Fetch quiz by id.
    """

    quiz = await QuizService.get_quiz_by_id(
        quiz_id
    )

    response = success_response(
        message=QuizMessages.QUIZ_FETCHED,
        data=quiz
    )

    return response


@router.put("/{quiz_id}")
async def update_quiz(
    quiz_id: str,
    quiz: QuizCreate,
    current_user=Depends(admin_required)
):
    """
    Update quiz.
    """

    await QuizService.update_quiz(
        quiz_id,
        quiz
    )

    response = success_response(
        message=QuizMessages.QUIZ_UPDATED
    )

    return response


@router.delete("/{quiz_id}")
async def delete_quiz(
    quiz_id: str,
    current_user=Depends(admin_required)
):
    """
    Delete quiz.
    """

    await QuizService.delete_quiz(
        quiz_id
    )

    response = success_response(
        message=QuizMessages.QUIZ_DELETED
    )

    return response