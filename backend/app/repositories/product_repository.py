from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Product).all()

    def get_by_id(self, product_id: int):
        return (
            self.db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

    def get_by_name(self, name: str):
        return (
            self.db.query(Product)
            .filter(Product.name == name)
            .first()
        )

    def create(self, product: Product):
        self.db.add(product)
        self.db.commit()
        self.db.refresh(product)

        return product

    def update(self, product: Product):
        self.db.commit()
        self.db.refresh(product)

        return product

    def delete(self, product: Product):
        self.db.delete(product)
        self.db.commit()