from no import No

class ListaEncadeada:
    def __init__(self):
        self.__inicio = None

    def vazia(self):
        return self.__inicio == None
    
    def tamanho(self):
        if self.vazia():
            return 0
        cont = 1
        p = self.__inicio
        while p.prox != None:
            cont += 1
            p = p.prox
        return cont

    def buscar_valor(self, dado):
        if self.vazia():
            return None
        p = self.__inicio
        i = 0
        while p is not None:
            if p.dado == dado:
                return i
            i += 1
            p = p.prox
        return None

    def buscar_posicao(self, pos):
        if self.vazia():
            return None
        if pos >= self.tamanho():
            return None
        p = self.__inicio
        for i in range(pos):
            p = p.prox
        return p.dado
    
    def buscar_ocorrencias(self, dado):
        if self.vazia():
            return None
        p = self.__inicio
        cont = 0
        while p.prox != None:
            if p.dado == dado:
                cont += 1
            p = p.prox
        if cont == 0:
            return None
        return cont

    def inserir_inicio(self, dado):
        novo = No(dado)
        novo.prox = self.__inicio
        self.__inicio = novo
    
    def inserir(self, dado, pos=None):
        novo = No(dado)
        if pos == None:
            self.inserir_final(dado)
            return
        if self.tamanho() < pos:
            print('Posição inválida')
            return
        if pos == 0:
            self.inserir_inicio(dado)
            return
        cont = 0
        p = self.__inicio
        while cont < pos - 1:
            p = p.prox
            cont += 1
        novo.prox = p.prox
        p.prox = novo

    def inserir_final(self, dado):
        novo = No(dado)
        if not self.vazia():
            p = self.__inicio
            while p.prox != None:
                p = p.prox
            p.prox = novo
        else:
            self.__inicio = novo

    def remover_incio(self):
        if self.vazia():
            return
        self.__inicio = self.__inicio.prox

    def remover(self, pos=None):
        if pos == None:
            self.remover_final()
            return
        if pos >= self.tamanho():
            print('Posição inválida')
            return
        if pos == 0:
            self.remover_incio()
            return
        cont = 0
        p = self.__inicio
        while cont < pos - 1:
            p = p.prox
            cont += 1
        p.prox = p.prox.prox
    
    def remover_final(self):
        if self.vazia():
            return
        if self.tamanho() == 1:
            self.remover_incio()
            return
        p = self.__inicio
        while p.prox.prox != None:
            p = p.prox
        p.prox = None

    def __str__(self):
        saida = '['
        p = self.__inicio
        while p != None:
            saida += f'{p.dado}'
            p = p.prox
            if p != None:
                saida += ' '
        saida += ']'
        return saida
    
# Criando uma instância da ListaEncadeada
minha_lista = ListaEncadeada()
print(f"Lista inicial: {minha_lista}")

# Método: vazia()
print(f"A lista está vazia? {minha_lista.vazia()}")

# Método: inserir_final()
minha_lista.inserir_final(10)
print(f"Após inserir 10 no final: {minha_lista}")
minha_lista.inserir_final(20)
print(f"Após inserir 20 no final: {minha_lista}")

# Método: tamanho()
print(f"Tamanho da lista: {minha_lista.tamanho()}")

# Método: inserir_inicio()
minha_lista.inserir_inicio(5)
print(f"Após inserir 5 no início: {minha_lista}")
print(minha_lista.buscar_valor(20))
print(minha_lista.buscar_posicao(2))

# Método: inserir(dado, pos)
minha_lista.inserir(15, 1)
print(f"Após inserir 15 na posição 1: {minha_lista}")
minha_lista.inserir(25, 4) # Tentativa de inserir em posição inválida
print(f"Após tentativa de inserir 25 na posição 4: {minha_lista}")
minha_lista.inserir(0, 0)
print(f"Após inserir 0 na posição 0: {minha_lista}")
minha_lista.inserir(0, 0)
print(f"Após inserir 0 na posição 0: {minha_lista}")
minha_lista.inserir(0, 4)
print(f"Após inserir 0 na posição 4: {minha_lista}")
print(f'ocorrencias do 0: {minha_lista.buscar_ocorrencias(0)}')


# Método: remover_incio()
minha_lista.remover_incio()
print(f"Após remover do início: {minha_lista}")

# Método: remover_final()
minha_lista.remover_final()
print(f"Após remover do final: {minha_lista}")

# Método: remover(pos)
minha_lista.remover(1)
print(f"Após remover da posição 1: {minha_lista}")
minha_lista.remover() # Remover do final sem especificar posição
print(f"Após remover do final (sem posição): {minha_lista}")
minha_lista.remover(5) # Tentativa de remover de posição inválida

# Método: __str__() já foi usado nos prints

# Exemplo de lista vazia após remoções
while not minha_lista.vazia():
    minha_lista.remover_incio()
print(f"Lista após remover todos os elementos: {minha_lista}")
print(f"A lista está vazia agora? {minha_lista.vazia()}")
print(f"Tamanho da lista agora: {minha_lista.tamanho()}")