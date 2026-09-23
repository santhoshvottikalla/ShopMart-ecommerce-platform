from app.models.category import Category

from app.repositories.category_repository import CategoryRepository

from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate
)

from app.exceptions.category_exceptions import (
    CategoryNotFoundException,
    CategoryAlreadyExistsException
)


class CategoryService:

    def __init__(
        self,
        category_repository: CategoryRepository
    ):
        self.category_repository = category_repository


    def get_all_categories(self):
        return self.category_repository.get_all()


    def get_category(self, category_id: int):

        category = self.category_repository.get_by_id(category_id)

        if not category:
            raise CategoryNotFoundException(category_id)

        return category


    def create_category(
        self,
        category_data: CategoryCreate
    ):

        existing_category = (
            self.category_repository.get_by_name(category_data.name)
        )

        if existing_category:
            raise CategoryAlreadyExistsException(
                category_data.name
            )

        category = Category(
            name=category_data.name,
            description=category_data.description
        )

        return self.category_repository.create(category)


    def update_category(
        self,
        category_id: int,
        category_data: CategoryUpdate
    ):

        category = self.get_category(category_id)

        update_data = category_data.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(category, field, value)

        return self.category_repository.update(category)


    def delete_category(self, category_id: int):

        category = self.get_category(category_id)

        self.category_repository.delete(category)