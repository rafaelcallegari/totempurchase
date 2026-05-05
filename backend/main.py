from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database_config import engine
from app.models.database import Base
from app.routes import produtos, carrinho, pedidos

# Criar as tabelas
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Totem Purchase API",
    description="API de autoatendimento para totem de vendas",
    version="0.1.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(produtos.router)
app.include_router(carrinho.router)
app.include_router(pedidos.router)

@app.get("/")
def home():
    return {
        "message": "🍔 Totem Purchase API rodando!",
        "version": "0.1.0",
        "docs": "/docs"
    }