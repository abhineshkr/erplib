# /home/epps/poc2/erplib/dblib/common_fields.py
from sqlalchemy import Column, String, DateTime, SmallInteger, Text
from .db_connection import Base  # Import Base from your connection module

class CommonFields(Base):
    __abstract__ = True
    company_code = Column('comp_cd', SmallInteger, primary_key=True, nullable=False)
    created_by = Column('created_by', Text, nullable=True)
    created_date = Column('created_dt', DateTime, nullable=True)
    creator_role_code = Column('creator_role_cd', SmallInteger, nullable=True)
    updated_by = Column('updated_by', Text, nullable=True)
    updated_date = Column('updated_dt', DateTime, nullable=True)
    updator_role_rode = Column('updator_role_cd', SmallInteger, nullable=True)
    terminal_id = Column('terminal_id', Text, nullable=True)
    active_yn = Column('active_yn', SmallInteger, nullable=True, default=1)
