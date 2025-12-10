from DAO import DAO
from entities.Mesa import Mesa

class MesaDAO(DAO):
    def lista_todos(self):
        pass
    def lista(self, codigo):
        
        pass
    def inserir(self, nome, codigo_mestre, codigo_sistema):
        query = "INSERT INTO mesa (nome, codigo_mestre, codigo_sistema) VALUES (%s, %s, %s,)"
        return self.executar_query(query, (nome, codigo_mestre, codigo_sistema))
        #pass
    def atualizar(self):
        pass
    def remover(self, codigo):
        query = "DELETE FROM mesa WHERE codigo = %s"
        return self.executar_query(query, (codigo, ))
        #pass