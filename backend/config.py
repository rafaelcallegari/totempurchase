import os
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Configurações globais da aplicação"""
    
    # Database
    # Em desenvolvimento: SQLite (local)
    # Em produção: PostgreSQL (via .env)
    environment: str = os.getenv("ENVIRONMENT", "development")
    
    database_url: str = os.getenv(
        "DATABASE_URL",
        "sqlite:///./test.db" if os.getenv("ENVIRONMENT", "development") == "development"
        else "postgresql://user:password@localhost:5432/totem_purchase"
    )
    
    # API
    api_host: str = "127.0.0.1"
    api_port: int = 8000
    
    class Config:
        env_file = ".env"
        case_sensitive = False


settings = Settings()

