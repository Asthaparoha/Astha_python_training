from fastapi import HTTPException

from app.constants.quiz_messages import QuizMessages

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