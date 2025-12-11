from .DAO import DAO
from entities.Sistema import Sistema

class SistemaDAO(DAO):
    def listar_todos(self):
        resultado = []
        query = "SELECT codigo, nome, versao FROM sistema"
        registros = self.executar_query(query, fetch=True)
        
        if registros:
            for linha in registros:
                s = Sistema()
                s.codigo = linha[0]
                s.nome = linha[1]
                s.versao = linha[2]
                resultado.append(s)
        return resultado

    def listar(self, codigo):
        s = None
        query = "SELECT codigo, nome, experiencia FROM mestre WHERE codigo = %s"
        linha = self.executar_query(query, (codigo,), fetchone=True)
        
        if linha:
            s = Sistema()
            s.codigo = linha[0]
            s.nome = linha[1]
            s.versao = linha[2]
        return s

    def inserir(self, nome, versao):
        query = "INSERT INTO sistema (nome, versao) VALUES (%s, %s)"
        return self.executar_query(query, (nome, versao))

    def atualizar(self, codigo, nome, versao):
        query = "UPDATE sistema SET nome = %s, versao = %s WHERE codigo = %s"
        return self.executar_query(query, (nome, versao, codigo))

    def remover(self, codigo):
        query = "DELETE FROM sistema WHERE codigo = %s"
        return self.executar_query(query, (codigo,))