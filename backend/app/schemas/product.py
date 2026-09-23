from decimal import Decimal

from pydantic import BaseModel, Field


class ProductCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=150
    )

    description: str | None = None

    price: Decimal = Field(
        ...,
        gt=0
    )

    stock_quantity: int = Field(
        ...,
        ge=0
    )

    category_id: int


class ProductUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=150
    )

    description: str | None = None

    price: Decimal | None = Field(
        default=None,
        gt=0
    )

    stock_quantity: int | None = Field(
        default=None,
        ge=0
    )

    category_id: int | None = None


class ProductResponse(BaseModel):
    id: int
    name: str
    description: str | None
    price: Decimal
    stock_quantity: int
    category_id: int

    class Config:
        from_attributes = True