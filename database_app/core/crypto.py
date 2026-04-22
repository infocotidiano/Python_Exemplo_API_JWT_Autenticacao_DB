from cryptography.fernet import Fernet
import os
from dotenv import load_dotenv

load_dotenv()
CHAVE = os.getenv("SECRET_KEY")
fernet = Fernet(CHAVE)

def criptografar(valor: str) -> bytes:
    """
    Criptografar dados
    """
    if isinstance(valor, str):
        valor = valor.encode()
    return fernet.encrypt(valor)    

def descriptografar(valor: bytes) -> str:
    """
    Descriptografar dados
    """
    if isinstance(valor, str):
        valor = valor.encode()
    return fernet.decrypt(valor).decode()
    

