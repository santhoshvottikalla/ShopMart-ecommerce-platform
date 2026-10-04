from fastapi import APIRouter, Depends, status

from app.schemas.user import (
    UserRegister,
    UserLogin,
    UserResponse,
    TokenResponse
)

from app.services.user_service import UserService
from app.services.dependencies import get_user_service

from app.utils.auth import get_current_user
from app.models.user import User


router = APIRouter(
    prefix="/api/v1/auth",
    tags=["Authentication"]
)


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
def register(
    user_data: UserRegister,
    service: UserService = Depends(get_user_service)
):
    return service.register_user(user_data)


@router.post(
    "/login",
    response_model=TokenResponse
)
def login(
    user_data: UserLogin,
    service: UserService = Depends(get_user_service)
):
    access_token = service.login_user(user_data)

    return {
        "access_token": access_token,
        "token_type": "bearer"
    }


@router.get(
    "/me",
    response_model=UserResponse
)
def get_current_user_info(
    current_user: User = Depends(get_current_user)
):
    return current_user