class Jogador(object):
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
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email