from uuid import uuid4
import secrets
import string

def gerar_secret(tamanho=16):
    """
    gerar senha aleatoria
    """
    caracteres = string.ascii_letters + string.digits
    return ''.join(secrets.choice(caracteres) for _ in range(tamanho) )

def gerar_uuid():
    """
    gerar UUID como string
    """
    return str(uuid4())