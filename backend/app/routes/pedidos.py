from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database_config import get_db

router = APIRouter(prefix="/pedidos", tags=["Pedidos"])


@router.post("")
def finalizar_pedido(db: Session = Depends(get_db)):
    """Rota temporária - será reformulada com sistema de sessão no BLOCO 2"""
    return {"mensagem": "Recurso em desenvolvimento - use /sessions/{session_id}/checkout"}