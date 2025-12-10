from DAO import DAO
from entities.Personagem import Personagem

class PersonagemDAO(DAO):
    def listar_todos(self):
        resultado = []
        query = "SELECT codigo, nome, codigo_jogador, codigo_mesa FROM personagem"
        registros = self.executar_query(query, fetch=True)

        if registros:
            for linha in registros:
                p = Personagem()
                p.codigo = linha[0]
                p.nome = linha[1]
                p.codigo_jogador = linha[2]
                p.codigo_mesa = linha[3]
                resultado.append(p)
        return resultado

    def listar(self,codigo):
        p = None
        query = "SELECT codigo, nome, codigo, nome, codigo_jogador, codigo_mesa WHERE codigo =%s"
        linha = self.executar_query(query, (codigo, ), fetchone=True)

        if linha:
            p = Personagem()
            p.codigo = linha[0]
            p.nome = linha[1]
            p.codigo_jogador = linha[2]
            p.codigo_mesa = linha[3]
        return p
    
    def inserir(self, codigo, nome, codigo_jogador, codigo_mesa):
        pass
    def atualizar(self, codigo, nome, codigo_jogador, codigo_mesa):
        pass
    def remover(self, codigo):
        pass