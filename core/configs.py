from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar


class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    DB_URL: str = (
        "postgresql+asyncpg://postgres.tascqincqdsjvmdjdwnh:123456@aws-0-us-east-2.pooler.supabase.com:5432/postgres"
    )
    DBBaseModel: ClassVar = (
        declarative_base()
    )  # Adicionando ClassVar para evitar o erro

    JWT_SECRET: str = "asBop3YPd4kNkLvbf_hkxjbFhnIqGmx_phMYOH2RBjM"
    """
    import secrets

    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = "HS256"
    # 60 minutos * 24 horas * 7 dias => 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
