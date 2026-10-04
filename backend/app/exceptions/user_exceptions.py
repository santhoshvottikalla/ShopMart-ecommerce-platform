class UserNotFoundException(Exception):

    def __init__(self, user_id: int):
        self.user_id = user_id

        super().__init__(
            f"User with ID {user_id} not found"
        )


class UsernameAlreadyExistsException(Exception):

    def __init__(self, username: str):
        self.username = username

        super().__init__(
            f"Username '{username}' already exists"
        )


class EmailAlreadyExistsException(Exception):

    def __init__(self, email: str):
        self.email = email

        super().__init__(
            f"Email '{email}' already exists"
        )


class InvalidCredentialsException(Exception):

    def __init__(self):
        super().__init__("Invalid username or password")