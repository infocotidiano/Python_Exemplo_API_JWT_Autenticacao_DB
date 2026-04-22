from database_app.models.cliente import Cliente
from database_app.database.db import get_session
from database_app.core.utils import gerar_secret, gerar_uuid
from database_app.core.crypto import criptografar, descriptografar

from sqlalchemy.exc import IntegrityError

       
def listar_clientes():        
    """
    Listar clientes cadastrados
    """
    session = get_session()
    clientes = session.query(Cliente).all()
    print("\n Listagem de Clientes")
    if not clientes:
        print("Nenhum cliente cadastrado")
        
    for c in clientes:
        print(f"ID: {c.cliente_id}")    
        print(f"Nome: {c.cliente_nome}")    
        print(f"Secret: { descriptografar(c.cliente_secret)}")    
        print(f"Chave App: {descriptografar(c.cliente_chave_app)}")    
        print("-" * 40)
        
    session.close() 
    
def localiza_cliente(id_cliente_requisicao):
    """
    alterar nome do cliente
    """
    session = get_session()
    cliente = session.query(Cliente).filter_by(cliente_id = id_cliente_requisicao).first()
    
    if not cliente:
        print("Cliente ID Não encontrado: ", id_cliente_requisicao)
        session.close()
        return None, None
    
    if cliente:
        retorno_client_id = cliente.cliente_id
        retorno_client_secret = descriptografar(cliente.cliente_secret)
       
    session.close()    
    return retorno_client_id, retorno_client_secret
    
    
    
    
        