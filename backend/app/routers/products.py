from fastapi import (
    APIRouter,
    Depends,
    status
)

from app.schemas.product import (
    ProductCreate,
    ProductUpdate,
    ProductResponse
)

from app.services.product_service import (
    ProductService
)

from app.services.dependencies import (
    get_product_service
)


router = APIRouter(
    prefix="/api/v1/products",
    tags=["Products"]
)


@router.get(
    "",
    response_model=list[ProductResponse]
)
def get_products(
    service: ProductService = Depends(
        get_product_service
    )
):

    return service.get_all_products()


@router.get(
    "/{product_id}",
    response_model=ProductResponse
)
def get_product(
    product_id: int,
    service: ProductService = Depends(
        get_product_service
    )
):

    return service.get_product(product_id)


@router.post(
    "",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED
)
def create_product(
    product_data: ProductCreate,
    service: ProductService = Depends(
        get_product_service
    )
):

    return service.create_product(product_data)


@router.put(
    "/{product_id}",
    response_model=ProductResponse
)
def update_product(
    product_id: int,
    product_data: ProductUpdate,
    service: ProductService = Depends(
        get_product_service
    )
):

    return service.update_product(
        product_id,
        product_data
    )


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_product(
    product_id: int,
    service: ProductService = Depends(
        get_product_service
    )
):

    service.delete_product(product_id)