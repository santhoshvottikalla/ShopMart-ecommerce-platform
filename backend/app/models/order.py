from sqlalchemy import (
    Column,
    Integer,
    String,
    Numeric,
    ForeignKey,
    DateTime
)
from sqlalchemy.sql import func

from app.database import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    status = Column(
        String(30),
        nullable=False,
        default="CREATED"
    )

    total_amount = Column(
        Numeric(10, 2),
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

    def can_cancel(self):
        return self.status in {
            "CREATED",
            "PENDING"
        }

    def cancel(self):
        if not self.can_cancel():
            raise ValueError(
                "Order cannot be cancelled in its current state"
            )

        self.status = "CANCELLED"