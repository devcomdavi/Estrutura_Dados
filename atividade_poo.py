# Métodos
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calculaArea(self):
        return (self.base*self.altura)
    
    def ehQuadrado(self):
        if self.base == self.altura:
            return True
        else:
            return False

# Métodos modificadores get e set   
class ContaCorrente:
    def __init__(self, conta, agencia, saldo):
        self.__conta = conta
        self.__agencia = agencia
        self.__saldo = saldo
    def get__conta(self):
        return self.__conta
    def get__agencia(self):
        return self.__agencia
    def get__saldo(self):
        return self.__saldo
    
    def set__conta(self, conta):
        self.__conta = conta
    
    def set__agencia(self, agencia):
        self.__agencia = agencia
    
    def set__saldo(self, saldo):
        self.__saldo = saldo

# Encapsulamento com Propriedades
class Aluno:
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    
    @property
    def matricula(self):
        return self.__matricula
    @matricula.setter
    def matricula(self, matricula):
        self.__matricula = matricula

    def __str__(self):
        return 'O aluno {self.__nome} de matrícula {self.matricula} está aprovado!'
