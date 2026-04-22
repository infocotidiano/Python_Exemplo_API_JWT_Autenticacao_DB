from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
import os
from dotenv import load_dotenv

load_dotenv()

DB_USER= os.getenv("DB_USER")
DB_PASSWORD= os.getenv("DB_PASSWORD")
DB_HOST= os.getenv("DB_HOST")
DB_NAME= os.getenv("DB_NAME")

url = URL.create(
    drivername="mysql+pymysql",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB_HOST,
    database=DB_NAME
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)

def get_session():
    """
    Retorna seção de conexao do BD
    """
    return Session()
