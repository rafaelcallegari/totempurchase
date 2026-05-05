from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database_config import get_db
from app.models.produto import ProdutoCreate, ProdutoResponse, Resposta
from app.models.database import ProdutoModel

router = APIRouter(prefix="/produtos", tags=["Produtos"])


@router.get("", response_model=list[ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    """Listar todos os produtos disponíveis"""
    produtos = db.query(ProdutoModel).all()
    return produtos


@router.get("/{produto_id}", response_model=ProdutoResponse)
def obter_produto(produto_id: int, db: Session = Depends(get_db)):
    """Obter um produto específico por ID"""
    produto = db.query(ProdutoModel).filter(ProdutoModel.id == produto_id).first()
    
    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    
    return produto


@router.post("", response_model=Resposta)
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    """Criar um novo produto"""
    novo_produto = ProdutoModel(**produto.dict())
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    
    return {"mensagem": f"Produto '{novo_produto.nome}' criado com sucesso"}