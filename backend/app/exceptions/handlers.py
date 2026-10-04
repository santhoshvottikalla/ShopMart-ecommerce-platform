from fastapi.responses import JSONResponse
from fastapi import Request

from app.exceptions.user_exceptions import (
    UserNotFoundException,
    UsernameAlreadyExistsException,
    EmailAlreadyExistsException,
    InvalidCredentialsException
)


def user_not_found_handler(
    request: Request,
    exc: UserNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "error": "USER_NOT_FOUND",
            "message": str(exc)
        }
    )


def username_already_exists_handler(
    request: Request,
    exc: UsernameAlreadyExistsException
):
    return JSONResponse(
        status_code=409,
        content={
            "error": "USERNAME_ALREADY_EXISTS",
            "message": str(exc)
        }
    )


def email_already_exists_handler(
    request: Request,
    exc: EmailAlreadyExistsException
):
    return JSONResponse(
        status_code=409,
        content={
            "error": "EMAIL_ALREADY_EXISTS",
            "message": str(exc)
        }
    )


def invalid_credentials_handler(
    request: Request,
    exc: InvalidCredentialsException
):
    return JSONResponse(
        status_code=401,
        content={
            "error": "INVALID_CREDENTIALS",
            "message": str(exc)
        },
        headers={
            "WWW-Authenticate": "Bearer"
        }
    )