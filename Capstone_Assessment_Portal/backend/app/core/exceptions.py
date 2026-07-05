from fastapi import HTTPException
from app.constants.attempt_messages import AttemptMessages
from app.constants.quiz_messages import QuizMessages
from app.constants.question_messages import QuestionMessages

class AppException(HTTPException):
    def __init__(self, status_code: int, message: str):
        super().__init__(
            status_code=status_code,
            detail=message
        )
class AuthenticationException(HTTPException):
    def __init__(self, detail="Invalid email or password"):
        super().__init__(
            status_code=401,
            detail=detail
        )


class AuthorizationException(HTTPException):
    def __init__(self, detail="Access denied"):
        super().__init__(
            status_code=403,
            detail=detail
        )


class ResourceExistsException(HTTPException):
    def __init__(self, detail="Resource already exists"):
        super().__init__(
            status_code=400,
            detail=detail
        )


class ResourceNotFoundException(HTTPException):
    def __init__(self, detail="Resource not found"):
        super().__init__(
            status_code=404,
            detail=detail
        )
class QuizNotFoundException(AppException):
    def __init__(self):
        super().__init__(
            status_code=404,
            message=QuizMessages.QUIZ_NOT_FOUND
        )
class QuizAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__(
            status_code=409,
            message=QuizMessages.QUIZ_ALREADY_EXISTS
        )


class InvalidQuizIdException(AppException):
    def __init__(self):
        super().__init__(
            status_code=400,
            message=QuizMessages.INVALID_QUIZ_ID
        )
class QuestionNotFoundException(AppException):
    def __init__(self):
        super().__init__(
            status_code=404,
            message=QuestionMessages.QUESTION_NOT_FOUND
        )


class QuestionAlreadyExistsException(AppException):
    def __init__(self):
        super().__init__(
            status_code=409,
            message=QuestionMessages.QUESTION_ALREADY_EXISTS
        )


class InvalidQuestionIdException(AppException):
    def __init__(self):
        super().__init__(
            status_code=400,
            message=QuestionMessages.INVALID_QUESTION_ID
        )
class AttemptNotFoundException(AppException):
    def __init__(self):
        super().__init__(
            status_code=404,
            message=AttemptMessages.ATTEMPT_NOT_FOUND
        )


class InvalidAttemptIdException(AppException):
    def __init__(self):
        super().__init__(
            status_code=400,
            message=AttemptMessages.INVALID_ATTEMPT_ID
        )


class AttemptLimitReachedException(AppException):
    def __init__(self):
        super().__init__(
            status_code=409,
            message=AttemptMessages.ATTEMPT_LIMIT_REACHED
        )


class AttemptAlreadySubmittedException(AppException):
    def __init__(self):
        super().__init__(
            status_code=409,
            message=AttemptMessages.ATTEMPT_ALREADY_SUBMITTED
        )