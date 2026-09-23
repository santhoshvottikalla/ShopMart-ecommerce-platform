from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from app.repositories.category_repository import CategoryRepository

from app.schemas.product import (
    ProductCreate,
    ProductUpdate
)

from app.exceptions.product_exceptions import (
    ProductNotFoundException,
    ProductAlreadyExistsException
)

from app.exceptions.category_exceptions import (
    CategoryNotFoundException
)


class ProductService:

    def __init__(
        self,
        product_repository: ProductRepository,
        category_repository: CategoryRepository
    ):
        self.product_repository = product_repository
        self.category_repository = category_repository

    def get_all_products(self):
        return self.product_repository.get_all()

    def get_product(self, product_id: int):

        product = self.product_repository.get_by_id(
            product_id
        )

        if not product:
            raise ProductNotFoundException(product_id)

        return product

    def create_product(
        self,
        product_data: ProductCreate
    ):

        existing_product = (
            self.product_repository.get_by_name(
                product_data.name
            )
        )

        if existing_product:
            raise ProductAlreadyExistsException(
                product_data.name
            )

        category = (
            self.category_repository.get_by_id(
                product_data.category_id
            )
        )

        if not category:
            raise CategoryNotFoundException(
                product_data.category_id
            )

        product = Product(
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            stock_quantity=product_data.stock_quantity,
            category_id=product_data.category_id
        )

        return self.product_repository.create(product)

    def update_product(
        self,
        product_id: int,
        product_data: ProductUpdate
    ):

        product = self.get_product(product_id)

        update_data = product_data.model_dump(
            exclude_unset=True
        )

        if "category_id" in update_data:

            category = (
                self.category_repository.get_by_id(
                    update_data["category_id"]
                )
            )

            if not category:
                raise CategoryNotFoundException(
                    update_data["category_id"]
                )

        for field, value in update_data.items():
            setattr(product, field, value)

        return self.product_repository.update(product)

    def delete_product(self, product_id: int):

        product = self.get_product(product_id)

        self.product_repository.delete(product)