# erplib/db/config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PRIMARY_POSTGRES_DB: str = os.getenv('PRIMARY_POSTGRES_DB', 'eppserp')
    PRIMARY_POSTGRES_USER: str = os.getenv('PRIMARY_POSTGRES_USER', 'postgres')
    PRIMARY_POSTGRES_PASSWORD: str = os.getenv('PRIMARY_POSTGRES_PASSWORD', 'epps@123')
    PRIMARY_POSTGRES_HOST: str = os.getenv('PRIMARY_POSTGRES_HOST', 'localhost')
    PRIMARY_POSTGRES_PORT: int = int(os.getenv('PRIMARY_POSTGRES_PORT', 5432))

    POOL_MIN_SIZE: int = int(os.getenv('POOL_MIN_SIZE', 5))
    POOL_MAX_SIZE: int = int(os.getenv('POOL_MAX_SIZE', 10))
    POOL_IDLE_TIMEOUT: int = int(os.getenv('POOL_IDLE_TIMEOUT', 300))
    POOL_MAX_OVERFLOW: int = int(os.getenv('POOL_MAX_OVERFLOW', 15))
    POOL_RECYCLE: int = int(os.getenv('POOL_RECYCLE', 3600))
    POOL_PRE_PING: bool = bool(os.getenv('POOL_PRE_PING', True))

settings = Settings()
