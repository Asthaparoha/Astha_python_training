from datetime import datetime

from bson import ObjectId

from app.constants.quiz_messages import QuizMessages
from app.core.exceptions import (
    InvalidQuizIdException,
    QuizAlreadyExistsException,
    QuizNotFoundException,
    ResourceNotFoundException,
)
from app.core.logger import logger
from app.repositories.category_repository import CategoryRepository
from app.repositories.quiz_repository import QuizRepository


class QuizService:
    """
    Business logic for Quiz Management.
    """

    @staticmethod
    async def create_quiz(quiz):
        """
        Create a new quiz.
        """

        existing_quiz = await QuizRepository.get_quiz_by_title(
            quiz.title
        )

        if existing_quiz:
            raise QuizAlreadyExistsException()

        if not ObjectId.is_valid(quiz.category_id):
            raise ResourceNotFoundException(
                QuizMessages.INVALID_CATEGORY_ID
            )

        category = await CategoryRepository.get_category_by_id(
            quiz.category_id
        )

        if category is None:
            raise ResourceNotFoundException(
                QuizMessages.CATEGORY_NOT_FOUND
            )

        quiz_data = {
            "title": quiz.title,
            "description": quiz.description,
            "category_id": quiz.category_id,
            "duration": quiz.duration,
            "total_marks": quiz.total_marks,
            "is_active": True,
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": None
        }

        quiz_id = await QuizRepository.create_quiz(
            quiz_data
        )

        quiz_data["id"] = str(quiz_id)

        logger.info("Quiz created successfully")

        response = quiz_data

        return response

    @staticmethod
    async def get_all_quizzes():
        """
        Fetch all quizzes.
        """

        quizzes = await QuizRepository.get_all_quizzes()

        response = quizzes

        return response

    @staticmethod
    async def get_quiz_by_id(
        quiz_id: str
    ):
        """
        Fetch quiz by id.
        """

        if not ObjectId.is_valid(quiz_id):
            raise InvalidQuizIdException()

        quiz = await QuizRepository.get_quiz_by_id(
            quiz_id
        )

        if quiz is None:
            raise QuizNotFoundException()

        response = quiz

        return response

    @staticmethod
    async def update_quiz(
        quiz_id: str,
        quiz
    ):
        """
        Update quiz.
        """

        if not ObjectId.is_valid(quiz_id):
            raise InvalidQuizIdException()

        existing_quiz = await QuizRepository.get_quiz_by_id(
            quiz_id
        )

        if existing_quiz is None:
            raise QuizNotFoundException()

        existing_title = await QuizRepository.get_quiz_by_title_except_id(
            quiz.title,
            quiz_id
        )
        if existing_title:
            raise QuizAlreadyExistsException()

        if not ObjectId.is_valid(
            quiz.category_id
        ):
            raise ResourceNotFoundException(
                QuizMessages.INVALID_CATEGORY_ID
            )

        category = await CategoryRepository.get_category_by_id(
            quiz.category_id
        )

        if category is None:
            raise ResourceNotFoundException(
                QuizMessages.CATEGORY_NOT_FOUND
            )

        data = {
            "title": quiz.title,
            "description": quiz.description,
            "category_id": quiz.category_id,
            "duration": quiz.duration,
            "total_marks": quiz.total_marks,
            "updated_at": datetime.utcnow().isoformat()
        }

        await QuizRepository.update_quiz(
            quiz_id,
            data
        )

        logger.info("Quiz updated successfully")

        response = True

        return response

    @staticmethod
    async def delete_quiz(
        quiz_id: str
    ):
        """
        Delete quiz.
        """

        if not ObjectId.is_valid(
            quiz_id
        ):
            raise InvalidQuizIdException()

        quiz = await QuizRepository.get_quiz_by_id(
            quiz_id
        )

        if quiz is None:
            raise QuizNotFoundException()

        await QuizRepository.delete_quiz(
            quiz_id
        )

        logger.info("Quiz deleted successfully")

        response = True

        return response