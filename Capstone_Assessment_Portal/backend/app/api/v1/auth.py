from fastapi import APIRouter

from app.core.exceptions import AuthenticationException, ResourceExistsException
from app.schemas.auth_schema import StudentRegister, UserLogin
from app.services.auth_service import AuthService
from app.utils.response import success_response

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
async def register_student(student: StudentRegister):

    user = await AuthService.register_student(student)

    if user is None:
        raise ResourceExistsException(
            "Email already registered"
        )

    return success_response(
        message="Student registered successfully"
    )


@router.post("/login")
async def login(login_data: UserLogin):

    result = await AuthService.login(login_data)

    if result is None:
        raise AuthenticationException()

    return success_response(
        message="Login successful",
        data=result
    )