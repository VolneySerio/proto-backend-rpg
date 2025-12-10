import traceback
import psycopg2


class DAO(object):
    def __init__(self):
        self.connection_params = {}
        
    def executar_query(self, query, params=None, fetch=False, fetchone=False):
        resultado = None
        connection = None
        try:
            connection = psycopg2.connect(**self.connection_params)
            cursor = connection.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            
            if fetch:
                resultado = cursor.fetchall()
            elif fetchone:
                resultado = cursor.fetchone()
            else:
                connection.commit()
                resultado = cursor.rowcount
            
            cursor.close()
        except (Exception, psycopg2.Error) as error:
            traceback.print_exc()
            resultado = None
        finally:
            if connection:
                connection.close()
        return resultado