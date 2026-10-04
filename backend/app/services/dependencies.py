from fastapi import Depends
from sqlalchemy.orm import Session

from app.database import get_db

from app.repositories.product_repository import ProductRepository
from app.repositories.category_repository import CategoryRepository
from app.repositories.user_repository import UserRepository

from app.services.product_service import ProductService
from app.services.category_service import CategoryService
from app.services.user_service import UserService


def get_product_service(
    db: Session = Depends(get_db)
) -> ProductService:

    product_repository = ProductRepository(db)
    category_repository = CategoryRepository(db)

    return ProductService(
        product_repository,
        category_repository
    )


def get_category_service(
    db: Session = Depends(get_db)
) -> CategoryService:

    category_repository = CategoryRepository(db)

    return CategoryService(
        category_repository
    )


def get_user_service(
    db: Session = Depends(get_db)
) -> UserService:

    user_repository = UserRepository(db)

    return UserService(
        user_repository
    )