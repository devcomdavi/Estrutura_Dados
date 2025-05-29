from no import No

class Fila:
    def __init__(self):
        self.__inicio = None
        self.__fim = None

    def vazia(self):
        return self.__inicio == None

    def primeiro(self):
        return self.__inicio

    def inserir(self, item):
        novo = No(item)

        if self.__inicio == None:
            self.__inicio = novo
            self.__fim = novo
        else:
            self.__fim.prox = novo
            self.__fim = novo

    def remover(self):
        if(self.vazia() == False):
            self.__inicio = self.__inicio.prox

    def __len__(self):
        contador = 0
        p = self.__inicio

        while p != None:
            contador += 1
            p = p.prox
        return contador

    def __str__(self):
        if self.__inicio == None:
            return 'Fila vazia.'
            
        dados = ''
        p = self.__inicio
        while p != None:
            dados = dados + ' ' + p.dado
            p = p.prox       
        return dados