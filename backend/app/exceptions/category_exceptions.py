class CategoryNotFoundException(Exception):
    def __init__(self, category_id: int):
        self.category_id = category_id
        super().__init__(f"Category with ID {category_id} not found")


class CategoryAlreadyExistsException(Exception):
    def __init__(self, name: str):
        self.name = name
        super().__init__(f"Category '{name}' already exists")