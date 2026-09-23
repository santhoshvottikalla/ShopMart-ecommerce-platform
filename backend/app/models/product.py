from sqlalchemy import (
    Column,
    Integer,
    String,
    Text,
    Numeric,
    ForeignKey,
    DateTime,
    CheckConstraint
)
from sqlalchemy.sql import func

from app.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(
        String(150),
        nullable=False
    )

    description = Column(
        Text,
        nullable=True
    )

    price = Column(
        Numeric(10, 2),
        nullable=False
    )

    stock_quantity = Column(
        Integer,
        nullable=False,
        default=0
    )

    category_id = Column(
        Integer,
        ForeignKey("categories.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    __table_args__ = (
        CheckConstraint(
            "price >= 0",
            name="check_product_price"
        ),
        CheckConstraint(
            "stock_quantity >= 0",
            name="check_product_stock"
        ),
    )

    def is_available(self, quantity):
        return self.stock_quantity >= quantity

    def reduce_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")

        if not self.is_available(quantity):
            raise ValueError("Insufficient stock")

        self.stock_quantity -= quantity