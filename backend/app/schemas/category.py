from pydantic import BaseModel, Field


class CategoryCreate(BaseModel):
    name: str = Field(
        ...,
        min_length=2,
        max_length=100
    )

    description: str | None = None


class CategoryUpdate(BaseModel):
    name: str | None = Field(
        default=None,
        min_length=2,
        max_length=100
    )

    description: str | None = None


class CategoryResponse(BaseModel):
    id: int
    name: str
    description: str | None

    class Config:
        from_attributes = True