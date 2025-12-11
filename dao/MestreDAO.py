from .DAO import DAO
from entities.Mestre import Mestre

class MestreDAO(DAO):
    def listar_todos(self):
        resultado = []
        query = "SELECT codigo, nome, experiencia FROM mestre"
        registros = self.executar_query(query, fetch=True)
        
        if registros:
            for linha in registros:
                m = Mestre()
                m.codigo = linha[0]
                m.nome = linha[1]
                m.experiencia = linha[2]
                resultado.append(m)
        return resultado

    def listar(self, codigo):
        m = None
        query = "SELECT codigo, nome, experiencia FROM mestre WHERE codigo = %s"
        linha = self.executar_query(query, (codigo,), fetchone=True)
        
        if linha:
            m = Mestre()
            m.codigo = linha[0]
            m.nome = linha[1]
            m.experiencia = linha[2]
        return m

    def inserir(self, nome, experiencia):
        query = "INSERT INTO mestre (nome, experiencia) VALUES (%s, %s)"
        return self.executar_query(query, (nome, experiencia))

    def atualizar(self, codigo, nome, experiencia):
        query = "UPDATE mestre SET nome = %s, experiencia = %s WHERE codigo = %s"
        return self.executar_query(query, (nome, experiencia, codigo))

    def remover(self, codigo):
        query = "DELETE FROM mestre WHERE codigo = %s"
        return self.executar_query(query, (codigo,))