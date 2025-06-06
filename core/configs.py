from pydantic_settings import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from typing import ClassVar


class Settings(BaseSettings):
    """
    Configurações gerais usadas na aplicação
    """
    
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = 'UrbanFood - Microserviço de Login'
    DB_URL: str = (
        "mysql+aiomysql://urbanfood:Urbanf00dFiap@rds-mysql.c8gkm8vsq6yc.us-east-1.rds.amazonaws.com:3306/urbanfood"
    )
    
    DBBaseModel: ClassVar = (
        declarative_base()
    )

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
