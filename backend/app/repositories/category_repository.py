from sqlalchemy.orm import Session

from app.models.category import Category


class CategoryRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Category).all()

    def get_by_id(self, category_id: int):
        return (
            self.db.query(Category)
            .filter(Category.id == category_id)
            .first()
        )

    def get_by_name(self, name: str):
        return (
            self.db.query(Category)
            .filter(Category.name == name)
            .first()
        )

    def create(self, category: Category):
        self.db.add(category)
        self.db.commit()
        self.db.refresh(category)

        return category

    def update(self, category: Category):
        self.db.commit()
        self.db.refresh(category)

        return category

    def delete(self, category: Category):
        self.db.delete(category)
        self.db.commit()