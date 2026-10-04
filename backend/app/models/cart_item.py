from sqlalchemy import (
    Column,
    Integer,
    ForeignKey,
    DateTime
)
from sqlalchemy.sql import func

from app.database import Base


class CartItem(Base):
    __tablename__ = "cart_items"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    cart_id = Column(
        Integer,
        ForeignKey("carts.id"),
        nullable=False
    )

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    quantity = Column(
        Integer,
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