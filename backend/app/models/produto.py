from typing import Literal, Optional
from pydantic import BaseModel
from datetime import datetime


class ProdutoCreate(BaseModel):
    """Schema para criar um novo produto"""
    nome: str
    preco: float
    categoria: Literal['lanche', 'bebida', 'sobremesa', 'acompanhamento']
    descricao: Optional[str] = None


class ProdutoResponse(BaseModel):
    """Schema para resposta de produto"""
    id: int
    nome: str
    preco: float
    categoria: str
    descricao: Optional[str] = None
    criado_em: datetime
    
    class Config:
        from_attributes = True


class Resposta(BaseModel):
    """Schema genérico de resposta"""
    mensagem: str
