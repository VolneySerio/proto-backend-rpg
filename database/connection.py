import psycopg2
from psycopg2 import Error
import config

def criar_conexao():

    try:
        conexao = psycopg2.connect(
            host=config.DB_HOST,
            database=config.DB_NAME,
            user=config.DB_USER,
            password=config.DB_PASSWORD,
            port=config.DB_PORT  
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao PostgreSQL: {e}")
        return None