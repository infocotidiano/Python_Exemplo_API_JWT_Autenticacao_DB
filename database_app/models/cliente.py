from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, LargeBinary

Base = declarative_base()

class Cliente(Base):
    """
    Classe de cliente
    """
    __tablename__ = "cliente"
    
    cliente_id = Column(String(36), primary_key=True)
    cliente_nome = Column(String(150), nullable=False )
    cliente_secret = Column(LargeBinary(255), nullable=False, unique=True)
    cliente_chave_app = Column(LargeBinary(255), nullable=False)
    