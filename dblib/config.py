# erplib/config.py
from pydantic_settings import BaseSettings
from pydantic import Extra

class Settings(BaseSettings):
    PRIMARY_POSTGRES_DB: str
    PRIMARY_POSTGRES_USER: str
    PRIMARY_POSTGRES_PASSWORD: str
    PRIMARY_POSTGRES_HOST: str
    PRIMARY_POSTGRES_PORT: int

    POOL_MIN_SIZE: int
    POOL_MAX_SIZE: int
    POOL_IDLE_TIMEOUT: int
    POOL_MAX_OVERFLOW: int
    POOL_RECYCLE: int
    POOL_PRE_PING: bool

    HOST: str
    PORT: int
    PRIMARY_DB_URI: str

    class Config:
        env_file = ".env"
        env_prefix = "ERPLIB_"
        extra = Extra.ignore

settings = Settings()
print("Loaded settings:", settings.dict())
