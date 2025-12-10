# dao/DAO.py
from database.connection import criar_conexao

class DAO:
    def executar_query(self, query, parametros=None, fetch=False, fetchone=False):
       
        conexao = None
        cursor = None
        resultado = None
        
        try:
            conexao = criar_conexao()
            if conexao is None:
                return None
                
            cursor = conexao.cursor()
            
            if parametros:
                cursor.execute(query, parametros)
            else:
                cursor.execute(query)
            
            if fetch:
                resultado = cursor.fetchall()
            elif fetchone:
                resultado = cursor.fetchone()
            else:
                conexao.commit()
                resultado = cursor.rowcount
                
        except Exception as e:
            if conexao:
                conexao.rollback()
            print(f"Erro na query: {e}")
            raise e
            
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()
                
        return resultado