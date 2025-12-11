from DAO import DAO
from entities.Mesa import Mesa

class MesaDAO(DAO):
    def lista_todos(self):
        resultado = []
        query = "SELECT codigo, nome, codigo_mestre, codigo_sistema FROM mesa"
        registros  = self.executar_query(query, fetch=True)


        if registros:
            for linha in registros:
                mesa = Mesa()
                mesa.codigo = linha[0]
                mesa.nome = linha[1]
                mesa.codigo_mestre = linha[2]
                mesa.codigo_sistema = linha[3]
                mesa.nome_mestre = linha[4]
                mesa.nome_sistema = linha[5]
                resultado.append(mesa)
        return resultado

        
    def lista(self, codigo):
        mesa = None
        query = """
        SELECT m.codigo, m.nome, m.codigo_mestre, m.codigo_sistema, 
               mest.nome as nome_mestre, sis.nome as nome_sistema
        FROM mesa m
        LEFT JOIN mestre mest ON m.codigo_mestre = mest.codigo
        LEFT JOIN sistema sis ON m.codigo_sistema = sis.codigo
        WHERE m.codigo = %s
        """
        linha = self.executar_query(query, (codigo, ), fetchone=True)

        if linha:
            mesa = Mesa()
            mesa.codigo = linha[0]
            mesa.nome = linha[1]
            mesa.codigo_mestre = linha[2]
            mesa.codigo_sistema = linha[3]
            mesa.nome_mestre = linha[4]
            mesa.nome_sistema = linha[5]
        return mesa
        
    def inserir(self, nome, codigo_mestre, codigo_sistema):
        query = "INSERT INTO mesa (nome, codigo_mestre, codigo_sistema) VALUES (%s, %s, %s,)"
        return self.executar_query(query, (nome, codigo_mestre, codigo_sistema))
        
    def atualizar(self):
        query = "INSERT INTO mesa (nome, codigo_mestre, codigo_sistema) VALUES (%s, %s, %s,)"
        return self.executar_query(query, ())
        
    def remover(self, codigo):
        query = "DELETE FROM mesa WHERE codigo = %s"
        return self.executar_query(query, (codigo, ))
    

print(MesaDAO)
        