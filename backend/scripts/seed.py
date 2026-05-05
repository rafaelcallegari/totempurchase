"""
Script para popular o banco de dados com produtos iniciais
Executar: python -m scripts.seed
"""
import sys
import os

# Adicionar o diretório backend ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from sqlalchemy.orm import Session
from app.database_config import engine, SessionLocal
from app.models.database import Base, ProdutoModel


def criar_tabelas():
    """Criar todas as tabelas no banco de dados"""
    print("📦 Criando tabelas...")
    Base.metadata.create_all(bind=engine)
    print("✅ Tabelas criadas com sucesso!")


def popular_produtos(db: Session):
    """Popular produtos iniciais"""
    produtos_iniciais = [
        {
            "nome": "Hamburguer Clássico",
            "preco": 20.0,
            "categoria": "lanche",
            "descricao": "Carne 180g, alface, tomate"
        },
        {
            "nome": "Batata Frita",
            "preco": 10.0,
            "categoria": "acompanhamento",
            "descricao": "Porção média, crocante"
        },
        {
            "nome": "Refrigerante",
            "preco": 8.0,
            "categoria": "bebida",
            "descricao": "Lata 350ml"
        },
        {
            "nome": "Sorvete",
            "preco": 12.0,
            "categoria": "sobremesa",
            "descricao": "2 bolas, sabores variados"
        },
        {
            "nome": "Suco Natural",
            "preco": 10.0,
            "categoria": "bebida",
            "descricao": "Laranja ou limão 300ml"
        },
        {
            "nome": "Onion Rings",
            "preco": 11.0,
            "categoria": "acompanhamento",
            "descricao": "Anéis empanados crocantes"
        },
        {
            "nome": "Pizza Mussarela",
            "preco": 35.0,
            "categoria": "lanche",
            "descricao": "Fatias grandes, queijo derretido"
        },
        {
            "nome": "Milk Shake",
            "preco": 14.0,
            "categoria": "bebida",
            "descricao": "Sabores: chocolate, morango, baunilha"
        },
    ]
    
    print("🍔 Populando produtos...")
    for produto_data in produtos_iniciais:
        # Verificar se já existe
        existe = db.query(ProdutoModel).filter(
            ProdutoModel.nome == produto_data["nome"]
        ).first()
        
        if not existe:
            produto = ProdutoModel(**produto_data)
            db.add(produto)
            print(f"  ✅ Adicionado: {produto_data['nome']}")
    
    db.commit()
    print("✅ Produtos populados com sucesso!")


def main():
    """Executar todo o processo de seed"""
    print("=" * 60)
    print("🌱 Iniciando seed do banco de dados...")
    print("=" * 60)
    
    try:
        # Criar tabelas
        criar_tabelas()
        
        # Popular produtos
        db = SessionLocal()
        popular_produtos(db)
        db.close()
        
        print("=" * 60)
        print("✅ Seed completado com sucesso!")
        print("=" * 60)
    except Exception as e:
        print(f"❌ Erro durante seed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
