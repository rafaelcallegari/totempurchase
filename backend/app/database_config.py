from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.pool import StaticPool
from config import settings

# Para SQLite (desenvolvimento), usar StaticPool
# Para PostgreSQL (produção), usar pool padrão
kwargs = {}
if "sqlite" in settings.database_url:
    kwargs = {
        "connect_args": {"check_same_thread": False},
        "poolclass": StaticPool,
    }

# Criar engine
engine = create_engine(
    settings.database_url,
    echo=settings.environment == "development",  # Log SQL em desenvolvimento
    **kwargs
)

# Criar session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Session:
    """Dependency para obter session do banco de dados"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
