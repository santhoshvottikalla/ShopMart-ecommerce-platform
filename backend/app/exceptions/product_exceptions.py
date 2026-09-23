class ProductNotFoundException(Exception):
    def __init__(self, product_id: int):
        self.product_id = product_id
        super().__init__(f"Product with ID {product_id} not found")


class ProductAlreadyExistsException(Exception):
    def __init__(self, name: str):
        self.name = name
        super().__init__(f"Product '{name}' already exists")