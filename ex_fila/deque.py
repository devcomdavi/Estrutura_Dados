class Deque:
    def __init__(self):
        self.__itens = []

    def vazia(self):
        return len(self.__itens) == 0

    def primeiro(self):
        if(self.vazia()):
            return None
        return self.__itens[0]

    def ultimo(self):
        if(self.vazia()):
            return None
        return self.__itens[-1]

    def inserir_inicio(self, item):
        self.__itens.insert(0,item)

    def inserir_final(self, item):
        self.__itens.append(item)

    def remover_inicio(self):
        if(self.vazia()):
            return None
        return self.__itens.pop(0)

    def remover_final(self):
        if(self.vazia()):
            return None
        return self.__itens.pop()

    def __len__(self):
        return len(self.__itens)

    def __str__(self):
        return self.__itens.__str__()