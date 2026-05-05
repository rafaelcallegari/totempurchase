from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, JSON, Enum as SQLEnum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import enum
import uuid

Base = declarative_base()


class ProdutoModel(Base):
    """Modelo de Produto no banco de dados"""
    __tablename__ = "produtos"
    
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(255), nullable=False)
    preco = Column(Float, nullable=False)
    categoria = Column(String(50), nullable=False)
    descricao = Column(String(500), nullable=True)
    criado_em = Column(DateTime, default=datetime.utcnow)
    
    # Relacionamentos
    itens_carrinho = relationship("CartItemModel", back_populates="produto", cascade="all, delete-orphan")
    itens_pedido = relationship("OrderItemModel", back_populates="produto", cascade="all, delete-orphan")


class SessionModel(Base):
    """Modelo de Sessão do Cliente"""
    __tablename__ = "sessions"
    
    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    criada_em = Column(DateTime, default=datetime.utcnow)
    atualizada_em = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relacionamentos
    itens_carrinho = relationship("CartItemModel", back_populates="sessao", cascade="all, delete-orphan")
    pedidos = relationship("OrderModel", back_populates="sessao", cascade="all, delete-orphan")


class CartItemModel(Base):
    """Modelo de Item do Carrinho"""
    __tablename__ = "cart_items"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(36), ForeignKey("sessions.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    quantidade = Column(Integer, default=1, nullable=False)
    criado_em = Column(DateTime, default=datetime.utcnow)
    
    # Relacionamentos
    sessao = relationship("SessionModel", back_populates="itens_carrinho")
    produto = relationship("ProdutoModel", back_populates="itens_carrinho")


class OrderModel(Base):
    """Modelo de Pedido"""
    __tablename__ = "orders"
    
    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(String(36), ForeignKey("sessions.id"), nullable=False)
    cpf = Column(String(11), nullable=True)
    total = Column(Float, nullable=False)
    status = Column(String(50), default="PENDING")  # PENDING, PAID, FAILED, CANCELLED
    criado_em = Column(DateTime, default=datetime.utcnow)
    
    # Relacionamentos
    sessao = relationship("SessionModel", back_populates="pedidos")
    itens = relationship("OrderItemModel", back_populates="pedido", cascade="all, delete-orphan")


class OrderItemModel(Base):
    """Modelo de Item do Pedido"""
    __tablename__ = "order_items"
    
    id = Column(Integer, primary_key=True, index=True)
    pedido_id = Column(Integer, ForeignKey("orders.id"), nullable=False)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=False)
    quantidade = Column(Integer, nullable=False)
    preco_unitario = Column(Float, nullable=False)
    subtotal = Column(Float, nullable=False)
    
    # Relacionamentos
    pedido = relationship("OrderModel", back_populates="itens")
    produto = relationship("ProdutoModel", back_populates="itens_pedido")


class AnalyticsEventModel(Base):
    """Modelo de Evento para Analytics"""
    __tablename__ = "analytics_events"
    
    id = Column(Integer, primary_key=True, index=True)
    tipo_evento = Column(String(50), nullable=False)  # viewed, added_to_cart, recommended, purchased, etc
    session_id = Column(String(36), ForeignKey("sessions.id"), nullable=True)
    produto_id = Column(Integer, ForeignKey("produtos.id"), nullable=True)
    pedido_id = Column(Integer, ForeignKey("orders.id"), nullable=True)
    dados_adicionais = Column(JSON, nullable=True)  # dados adicionais
    criado_em = Column(DateTime, default=datetime.utcnow, index=True)
