from fastapi import HTTPException


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