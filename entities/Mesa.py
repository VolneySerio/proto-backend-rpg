class Mesa(object):
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
    def codigo_mestre(self):
        return self._codigo_mestre

    @codigo_mestre.setter
    def codigo_mestre(self, codigo_mestre):
        self._codigo_mestre = codigo_mestre

    @property
    def codigo_sistema(self):
        return self._codigo_sistema

    @codigo_sistema.setter
    def codigo_sistema(self, codigo_sistema):
        self._codigo_sistema = codigo_sistema