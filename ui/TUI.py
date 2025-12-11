from dao.JogadorDAO import JogadorDAO
from dao.MesaDAO import MesaDAO
from dao.MestreDAO import MestreDAO
from dao.SistemaDAO import SistemaDAO
from dao.PersonagemDAO import PersonagemDAO

class InterfaceGrafica(object):
    def menu_principal(self):
        
        print("1 - Gerenciar Mestres")
        print("2 - Gerenciar Sistemas")
        print("3 - Gerenciar Jogadores")
        print("4 - Gerenciar Mesas")
        print("5 - Gerenciar Personagens")
        print("0 - Sair")
        opcao = int(input("Digite uma opção [0-5]: "))
        
        if opcao == 1:
            self.menu_entidade("Mestre")
        elif opcao == 2:
            self.menu_entidade("Sistema")
        elif opcao == 3:
            self.menu_entidade("Jogador")
        elif opcao == 4:
            self.menu_entidade("Mesa")
        elif opcao == 5:
            self.menu_entidade("Personagem")
        elif opcao == 0:
            print("Saindo...")
            return
        else:
            print("Opção inválida!")
            self.menu_principal()

    def menu_entidade(self, entidade):
        print(f"\n================================")
        print(f"   GERENCIAR {entidade.upper()}S    ")
        print("================================")
        print("1 - Listar Todos")
        print("2 - Listar por Código")
        print("3 - Inserir")
        print("4 - Atualizar")
        print("5 - Remover")
        print("0 - Voltar")
        print("================================")
        opcao = int(input("Digite uma opção [0-5]: "))
        
        if opcao == 1:
            self.listar_todos(entidade)
        elif opcao == 2:
            self.listar_por_codigo(entidade)
        elif opcao == 3:
            self.inserir(entidade)
        elif opcao == 4:
            self.atualizar(entidade)
        elif opcao == 5:
            self.remover(entidade)
        elif opcao == 0:
            self.menu_principal()
        else:
            print("Opção inválida!")
            self.menu_entidade(entidade)

    def get_dao(self, entidade):
        if entidade == "Mestre":
            return MestreDAO()
        elif entidade == "Sistema":
            return SistemaDAO()
        elif entidade == "Jogador":
            return JogadorDAO()
        elif entidade == "Mesa":
            return MesaDAO()
        elif entidade == "Personagem":
            return PersonagemDAO()
        return None

    def listar_todos(self, entidade):
        dao = self.get_dao(entidade)
        if not dao:
            return
        
        print(f"\nListando todos os {entidade}s...")
        registros = dao.listar_todos()
        
        if not registros:
            print("Nenhum registro encontrado")
        else:
            for registro in registros:
                if entidade == "Mestre":
                    print(f"Código: {registro.codigo} | Nome: {registro.nome} | Experiência: {registro.experiencia} anos")
                elif entidade == "Sistema":
                    print(f"Código: {registro.codigo} | Nome: {registro.nome} | Versão: {registro.versao}")
                elif entidade == "Jogador":
                    print(f"Código: {registro.codigo} | Nome: {registro.nome} | Email: {registro.email}")
                elif entidade == "Mesa":
                    print(f"Código: {registro.codigo} | Nome: {registro.nome} | Mestre: {registro.nome_mestre} | Sistema: {registro.nome_sistema}")
                elif entidade == "Personagem":
                    print(f"Código: {registro.codigo} | Nome: {registro.nome} | Jogador: {registro.nome_jogador} | Mesa: {registro.nome_mesa}")
        
        self.menu_entidade(entidade)

    def listar_por_codigo(self, entidade):
        dao = self.get_dao(entidade)
        if not dao:
            return
        
        codigo = int(input(f"Digite o código do {entidade}: "))
        registro = dao.listar(codigo)
        
        if not registro:
            print(f"{entidade} não encontrado!")
        else:
            if entidade == "Mestre":
                print(f"\nCódigo: {registro.codigo}")
                print(f"Nome: {registro.nome}")
                print(f"Experiência: {registro.experiencia} anos")
            elif entidade == "Sistema":
                print(f"\nCódigo: {registro.codigo}")
                print(f"Nome: {registro.nome}")
                print(f"Versão: {registro.versao}")
            elif entidade == "Jogador":
                print(f"\nCódigo: {registro.codigo}")
                print(f"Nome: {registro.nome}")
                print(f"Email: {registro.email}")
            elif entidade == "Mesa":
                print(f"\nCódigo: {registro.codigo}")
                print(f"Nome: {registro.nome}")
                print(f"Mestre: {registro.nome_mestre}")
                print(f"Sistema: {registro.nome_sistema}")
            elif entidade == "Personagem":
                print(f"\nCódigo: {registro.codigo}")
                print(f"Nome: {registro.nome}")
                print(f"Jogador: {registro.nome_jogador}")
                print(f"Mesa: {registro.nome_mesa}")
        
        self.menu_entidade(entidade)

    def inserir(self, entidade):
        dao = self.get_dao(entidade)
        if not dao:
            return
        
        print(f"\nInserindo novo {entidade}...")
        
        if entidade == "Mestre":
            nome = input("Nome: ")
            experiencia = int(input("Experiência (anos): "))
            resultado = dao.inserir(nome, experiencia)
        elif entidade == "Sistema":
            nome = input("Nome: ")
            versao = input("Versão: ")
            resultado = dao.inserir(nome, versao)
        elif entidade == "Jogador":
            nome = input("Nome: ")
            email = input("Email: ")
            resultado = dao.inserir(nome, email)
        elif entidade == "Mesa":
            nome = input("Nome da mesa: ")
            codigo_mestre = int(input("Código do mestre: "))
            codigo_sistema = int(input("Código do sistema: "))
            resultado = dao.inserir(nome, codigo_mestre, codigo_sistema)
        elif entidade == "Personagem":
            nome = input("Nome do personagem: ")
            codigo_jogador = int(input("Código do jogador: "))
            codigo_mesa = int(input("Código da mesa: "))
            resultado = dao.inserir(nome, codigo_jogador, codigo_mesa)
        
        if resultado and resultado > 0:
            print(f"{entidade} inserido com sucesso!")
        else:
            print(f"Erro ao inserir {entidade}!")
        
        self.menu_entidade(entidade)

    def atualizar(self, entidade):
        dao = self.get_dao(entidade)
        if not dao:
            return
        
        print(f"\nAtualizando {entidade}...")
        codigo = int(input(f"Código do {entidade} a atualizar: "))
        
        if entidade == "Mestre":
            nome = input("Novo nome: ")
            experiencia = int(input("Nova experiência (anos): "))
            resultado = dao.atualizar(codigo, nome, experiencia)
        elif entidade == "Sistema":
            nome = input("Novo nome: ")
            versao = input("Nova versão: ")
            resultado = dao.atualizar(codigo, nome, versao)
        elif entidade == "Jogador":
            nome = input("Novo nome: ")
            email = input("Novo email: ")
            resultado = dao.atualizar(codigo, nome, email)
        elif entidade == "Mesa":
            nome = input("Novo nome da mesa: ")
            codigo_mestre = int(input("Novo código do mestre: "))
            codigo_sistema = int(input("Novo código do sistema: "))
            resultado = dao.atualizar(codigo, nome, codigo_mestre, codigo_sistema)
        elif entidade == "Personagem":
            nome = input("Novo nome do personagem: ")
            codigo_jogador = int(input("Novo código do jogador: "))
            codigo_mesa = int(input("Novo código da mesa: "))
            resultado = dao.atualizar(codigo, nome, codigo_jogador, codigo_mesa)
        
        if resultado and resultado > 0:
            print(f"{entidade} atualizado com sucesso!")
        else:
            print(f"Erro ao atualizar {entidade}!")
        
        self.menu_entidade(entidade)

    def remover(self, entidade):
        dao = self.get_dao(entidade)
        if not dao:
            return
        
        print(f"\nRemovendo {entidade}...")
        codigo = int(input(f"Código do {entidade} a remover: "))
        resultado = dao.remover(codigo)
        
        if resultado and resultado > 0:
            print(f"{entidade} removido com sucesso!")
        else:
            print(f"Erro ao remover {entidade}!")
        
        self.menu_entidade(entidade)

if __name__ == '__main__':
    gui = InterfaceGrafica()
    gui.menu_principal()