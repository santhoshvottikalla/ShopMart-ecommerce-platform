from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserRegister, UserLogin

from app.exceptions.user_exceptions import (
    UsernameAlreadyExistsException,
    EmailAlreadyExistsException,
    InvalidCredentialsException
)

from app.utils.security import (
    hash_password,
    verify_password,
    create_access_token
)


class UserService:

    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def register_user(self, user_data: UserRegister):

        existing_username = (
            self.user_repository
            .get_by_username(user_data.username)
        )

        if existing_username:
            raise UsernameAlreadyExistsException(
                user_data.username
            )

        existing_email = (
            self.user_repository
            .get_by_email(user_data.email)
        )

        if existing_email:
            raise EmailAlreadyExistsException(
                user_data.email
            )

        password_hash = hash_password(
            user_data.password
        )

        user = User(
            username=user_data.username,
            email=user_data.email,
            password_hash=password_hash,
            role="CUSTOMER",
            status="ACTIVE"
        )

        return self.user_repository.create(user)

    def login_user(self, user_data: UserLogin):

        user = self.user_repository.get_by_username(
            user_data.username
        )

        if not user:
            raise InvalidCredentialsException()

        if not verify_password(
            user_data.password,
            user.password_hash
        ):
            raise InvalidCredentialsException()

        if not user.is_active():
            raise InvalidCredentialsException()

        access_token = create_access_token(
            data={
                "sub": str(user.id),
                "username": user.username,
                "role": user.role
            }
        )

        return access_token