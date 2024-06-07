# /home/epps/poc2/erplib/dblib/common_fields.py
from sqlalchemy import Column, String, DateTime, SmallInteger, Text
from .db_connection import Base  # Import Base from your connection module

class CommonFields(Base):
    __abstract__ = True
    createdBy = Column('created_by', String(15), nullable=True)
    createdDate = Column('created_dt', DateTime, nullable=True)
    creatorRoleCode = Column('creator_role_cd', SmallInteger, nullable=True)
    updatedBy = Column('updated_by', String(15), nullable=True)
    updatedDate = Column('updated_dt', DateTime, nullable=True)
    updatorRoleCode = Column('updator_role_cd', SmallInteger, nullable=True)
    terminalId = Column('terminal_id', Text, nullable=True)
