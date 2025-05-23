class Fila:
    def __init__(self):
        self.__itens = []

    def vazia(self):
        return len(self.__itens) == 0

    def primeiro(self):
        if(self.vazia()):
            return None
        return self.__itens[0]

    def inserir(self, item):
        self.__itens.append(item)

    def remover(self):
        if(self.vazia()):
            return None
        return self.__itens.pop(0)

    def __len__(self):
        return len(self.__itens)

    def __str__(self):
        return self.__itens.__str__()