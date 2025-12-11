from .DAO import DAO
from entities.Jogador import Jogador

class JogadorDAO(DAO):
    def lista_todos(self):
        resultado = []
        query = "SELECT codigo, nome, email, codigo_sistema FROM Jogador"
        registros  = self.executar_query(query, fetch=True)


        if registros:
            for linha in registros:
                j = Jogador()
                j.codigo = linha[0]
                j.nome = linha[1]
                j.codigo_mestre = linha[2]
                j.codigo_sistema = linha[3]
                j.nome_mestre = linha[4]
                j.nome_sistema = linha[5]
                resultado.append(j)
        return resultado

        
    def lista(self, codigo):
        j = None
        query = """
        SELECT m.codigo, m.nome, m.codigo_mestre, m.codigo_sistema, 
               mest.nome as nome_mestre, sis.nome as nome_sistema
        FROM Jogad m
        LEFT JOIN mestre mest ON m.codigo_mestre = mest.codigo
        LEFT JOIN sistema sis ON m.codigo_sistema = sis.codigo
        WHERE m.codigo = %s
        """
        linha = self.executar_query(query, (codigo, ), fetchone=True)

        if linha:
            j = Jogador()
            j.codigo = linha[0]
            j.nome = linha[1]
            j.codigo_mestre = linha[2]
            j.codigo_sistema = linha[3]
            j.nome_mestre = linha[4]
            j.nome_sistema = linha[5]
        return j
        
    def inserir(self, nome, codigo_mestre, codigo_sistema):
        query = "INSERT INTO jogador (nome, codigo_mestre, codigo_sistema) VALUES (%s, %s, %s,)"
        return self.executar_query(query, (nome, codigo_mestre, codigo_sistema))
        
    def atualizar(self):
        query = "INSERT INTO jogador (nome, codigo_mestre, codigo_sistema) VALUES (%s, %s, %s,)"
        return self.executar_query(query, ())
        
    def remover(self, codigo):
        query = "DELETE FROM jogador WHERE codigo = %s"
        return self.executar_query(query, (codigo, ))
        