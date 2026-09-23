from fastapi import (
    APIRouter,
    Depends,
    status
)

from app.schemas.category import (
    CategoryCreate,
    CategoryUpdate,
    CategoryResponse
)

from app.services.category_service import (
    CategoryService
)

from app.services.dependencies import (
    get_category_service
)


router = APIRouter(
    prefix="/api/v1/categories",
    tags=["Categories"]
)


@router.get(
    "",
    response_model=list[CategoryResponse]
)
def get_categories(
    service: CategoryService = Depends(
        get_category_service
    )
):

    return service.get_all_categories()


@router.get(
    "/{category_id}",
    response_model=CategoryResponse
)
def get_category(
    category_id: int,
    service: CategoryService = Depends(
        get_category_service
    )
):

    return service.get_category(category_id)


@router.post(
    "",
    response_model=CategoryResponse,
    status_code=status.HTTP_201_CREATED
)
def create_category(
    category_data: CategoryCreate,
    service: CategoryService = Depends(
        get_category_service
    )
):

    return service.create_category(category_data)


@router.put(
    "/{category_id}",
    response_model=CategoryResponse
)
def update_category(
    category_id: int,
    category_data: CategoryUpdate,
    service: CategoryService = Depends(
        get_category_service
    )
):

    return service.update_category(
        category_id,
        category_data
    )


@router.delete(
    "/{category_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_category(
    category_id: int,
    service: CategoryService = Depends(
        get_category_service
    )
):

    service.delete_category(category_id)