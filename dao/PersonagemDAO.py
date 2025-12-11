from .DAO import DAO
from entities.Personagem import Personagem

class PersonagemDAO(DAO):
    def listar_todos(self):
        resultado = []
        query = """
        SELECT p.codigo, p.nome, p.codigo_jogador, p.codigo_mesa,
               j.nome as nome_jogador, m.nome as nome_mesa
        FROM personagem p
        LEFT JOIN jogador j ON p.codigo_jogador = j.codigo
        LEFT JOIN mesa m ON p.codigo_mesa = m.codigo
        """
        registros = self.executar_query(query, fetch=True)

        if registros:
            for linha in registros:
                p = Personagem()
                p.codigo = linha[0]
                p.nome = linha[1]
                p.codigo_jogador = linha[2]
                p.codigo_mesa = linha[3]
                p.nome_jogador = linha[4]
                p.nome_mesa = linha[5]
                resultado.append(p)
        return resultado

    def listar(self,codigo):
        p = None
        query = """
        SELECT p.codigo, p.nome, p.codigo_jogador, p.codigo_mesa,
               j.nome as nome_jogador, m.nome as nome_mesa
        FROM personagem p
        LEFT JOIN jogador j ON p.codigo_jogador = j.codigo
        LEFT JOIN mesa m ON p.codigo_mesa = m.codigo
        WHERE p.codigo = %s
        """

        linha = self.executar_query(query, (codigo, ), fetchone=True)

        if linha:
            p = Personagem()
            p.codigo = linha[0]
            p.nome = linha[1]
            p.codigo_jogador = linha[2]
            p.codigo_mesa = linha[3]
            p.nome_jogador = linha[4]
            p.nome_mesa = linha[5]
        return p
    
    def inserir(self, nome, codigo_jogador, codigo_mesa):
        #Detalhe importante, o codigo e setado automaticamente por meio do SERIAL no DDL 
        query = "INSERT INTO personagem (nome, codigo_jogador, codigo_mesa) VALUES (%s, %s, %s)"
        return self.executar_query(query, (nome, codigo_jogador, codigo_mesa))
        
    def atualizar(self, codigo, nome, codigo_jogador, codigo_mesa):
        query = "UPDATE personagem SET nome = %s, codigo_jogador = %s, codigo_mesa = %s WHERE codigo = %s"
        return self.executar_query(query, (nome, codigo_jogador, codigo_mesa, codigo))
    
    def remover(self, codigo):
        query = "DELETE FROM personagem WHERE codigo = %s"
        return self.executar_query(query, (codigo, ))
        pass