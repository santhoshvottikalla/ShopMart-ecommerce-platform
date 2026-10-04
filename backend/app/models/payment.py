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


class Payment(Base):
    __tablename__ = "payments"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    order_id = Column(
        Integer,
        ForeignKey("orders.id"),
        nullable=False
    )

    payment_method = Column(
        String(20),
        nullable=False
    )

    status = Column(
        String(20),
        nullable=False,
        default="PENDING"
    )

    transaction_reference = Column(
        String(100),
        unique=True,
        nullable=True
    )

    amount = Column(
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