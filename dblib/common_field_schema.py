# /home/epps/poc2/erplib/dblib/common_fields_schema.py
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class CommonFieldsSchema(BaseModel):
    created_by: Optional[str] = None
    created_date: Optional[datetime] = None
    creator_role_code: Optional[int] = None
    updated_by: Optional[str] = None
    updated_date: Optional[datetime] = None
    updator_role_code: Optional[int] = None
    terminal_id: Optional[str] = None

class PaginationMetaSchema(BaseModel):
    page: int
    per_page: int
    total_items: int
