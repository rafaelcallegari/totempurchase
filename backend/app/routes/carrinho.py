from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database_config import get_db

router = APIRouter(prefix="/carrinho", tags=["Carrinho"])


@router.post("/{id}")
def adicionar_ao_carrinho(id: int, db: Session = Depends(get_db)):
    """Rota temporária - será reformulada com sistema de sessão no BLOCO 2"""
    return {"mensagem": "Recurso em desenvolvimento - use /sessions/{session_id}/cart"}


@router.get("")
def listar_carrinho(db: Session = Depends(get_db)):
    """Rota temporária - será reformulada com sistema de sessão no BLOCO 2"""
    return {"mensagem": "Recurso em desenvolvimento - use /sessions/{session_id}/cart"}


@router.get("/total")
def calcular_total(db: Session = Depends(get_db)):
    """Rota temporária - será reformulada com sistema de sessão no BLOCO 2"""
    return {"total": 0}


@router.delete("/{id}")
def remover_do_carrinho(id: int, db: Session = Depends(get_db)):
    """Rota temporária - será reformulada com sistema de sessão no BLOCO 2"""
    return {"mensagem": "Recurso em desenvolvimento"}


@router.delete("")
def limpar_carrinho(db: Session = Depends(get_db)):
    """Rota temporária - será reformulada com sistema de sessão no BLOCO 2"""
    return {"mensagem": "Recurso em desenvolvimento"}