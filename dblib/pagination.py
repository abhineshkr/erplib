from pydantic import BaseModel

class PaginationMetaSchema(BaseModel):
    page: int
    per_page: int
    total_items: int
