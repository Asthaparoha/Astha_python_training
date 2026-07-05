from bson import ObjectId

from app.constants.result_messages import ResultMessages
from app.core.exceptions import (
    InvalidAttemptIdException,
    ResourceNotFoundException,
)
from app.repositories.attempt_repository import AttemptRepository
from app.repositories.quiz_repository import QuizRepository


class ResultService:
    """
    Business logic for Result Management.
    """

    @staticmethod
    async def get_result(
        attempt_id: str,
        current_user
    ):
        """
        Fetch result of a submitted attempt.
        """

        if not ObjectId.is_valid(
            attempt_id
        ):
            raise InvalidAttemptIdException()

        attempt = await AttemptRepository.get_attempt_by_id(
            attempt_id
        )

        if attempt is None:
            raise ResourceNotFoundException(
                ResultMessages.RESULT_NOT_FOUND
            )

        if (
            attempt["student_email"]
            !=
            current_user["email"]
        ):
            raise ResourceNotFoundException(
                ResultMessages.RESULT_NOT_FOUND
            )

        if (
            attempt["status"]
            !=
            "submitted"
        ):
            raise ResourceNotFoundException(
                ResultMessages.RESULT_UNAVAILABLE
            )

        quiz = await QuizRepository.get_quiz_by_id(
            attempt["quiz_id"]
        )

        percentage = (
            attempt["score"]
            /
            quiz["total_marks"]
        ) * 100

        result = {

            "quiz_title": quiz["title"],

            "score": attempt["score"],

            "total_marks": quiz["total_marks"],

            "percentage": round(
                percentage,
                2
            ),

            "status": (
                "PASS"
                if percentage >= 40
                else "FAIL"
            ),

            "submitted_at": attempt["submitted_at"]

        }

        response = result

        return response