class Sistema(object):
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
    def versao(self):
        return self._versao

    @versao.setter
    def versao(self, versao):
        self._versao = versao
