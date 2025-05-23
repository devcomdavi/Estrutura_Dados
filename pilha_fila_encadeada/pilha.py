from no import No

class Pilha:
    def __init__(self):
        self.__topo = None

    def vazia(self):
        return self.__topo is None

    def topo_pilha(self):
        if self.vazia():
            return None
        return self.__topo.dado

    def empilhar(self, item):
        no = No(item)
        no.prox = self.__topo
        self.__topo = no

    def desempilhar(self):
        if(self.vazia()):
            return None
        self.__topo = self.__topo.prox

    def __str__(self):
        if self.__topo == None:
            return 'Pilha vazia.'
        else:
            dados = ''
            p = self.__topo

            while p != None:
                dados = dados + ' ' + str(p.dado)
                p = p.prox
            
            return dados.strip()