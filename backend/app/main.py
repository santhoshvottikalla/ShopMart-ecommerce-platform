from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database import get_db
from app.routers.products import router as product_router
from app.routers.categories import router as category_router
from app.routers.auth import router as auth_router
from app.exceptions.user_exceptions import (
    UserNotFoundException,
    UsernameAlreadyExistsException,
    EmailAlreadyExistsException,
    InvalidCredentialsException
)

from app.exceptions.handlers import (
    # your existing handlers...
    user_not_found_handler,
    username_already_exists_handler,
    email_already_exists_handler,
    invalid_credentials_handler
)


app = FastAPI(
    title="ShopMart API",
    description="Production-oriented e-commerce platform",
    version="1.0.0"
)


# Include API routers
app.include_router(product_router)
app.include_router(category_router)
app.include_router(auth_router)
app.add_exception_handler(
    UserNotFoundException,
    user_not_found_handler
)

app.add_exception_handler(
    UsernameAlreadyExistsException,
    username_already_exists_handler
)

app.add_exception_handler(
    EmailAlreadyExistsException,
    email_already_exists_handler
)

app.add_exception_handler(
    InvalidCredentialsException,
    invalid_credentials_handler
)


@app.get("/")
def root():
    return {
        "message": "Welcome to ShopMart API",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/health/database")
def database_health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))

    return {
        "status": "healthy",
        "database": "connected"
    }