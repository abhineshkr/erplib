# erplib/db/connection.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.pool import QueuePool
from .config import settings


print({settings.PRIMARY_POSTGRES_PORT})
DATABASE_URL = f"postgresql://{settings.PRIMARY_POSTGRES_USER}:{settings.PRIMARY_POSTGRES_PASSWORD}@{settings.PRIMARY_POSTGRES_HOST}:{settings.PRIMARY_POSTGRES_PORT}/{settings.PRIMARY_POSTGRES_DB}"
print(DATABASE_URL)

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=settings.POOL_MIN_SIZE,
    max_overflow=settings.POOL_MAX_OVERFLOW,
    pool_timeout=settings.POOL_IDLE_TIMEOUT,
    pool_recycle=settings.POOL_RECYCLE,
    pool_pre_ping=settings.POOL_PRE_PING
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()