class Personagem(object):
    
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, codigo):
        self._codigo = codigo

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def codigo_jogador(self):
        return self._codigo_jogador

    @codigo_jogador.setter
    def codigo_jogador(self, codigo_jogador):
        self._codigo_jogador = codigo_jogador

    @property
    def codigo_mesa(self):
        return self._codigo_mesa

    @codigo_mesa.setter
    def codigo_mesa(self, codigo_mesa):
        self._codigo_mesa = codigo_mesa