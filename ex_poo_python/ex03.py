class Pais:
    def __init__(self, nome, capital, dimensao):
        self.__nome = nome
        self.__capital = capital
        self.__dimensao = dimensao
        self.__fronteira = []

    @property
    def nome(self):
        return self.__nome
    @property
    def capital(self):
        return self.__capital
    @property
    def dimensao(self):
        return self.__dimensao
    
    def paises_fronteira(self):
        return self.__fronteira
    
    def adiciona_pais(self, nome_pais):
        nome = nome_pais.upper()
        if nome not in self.__fronteira:
            self.__fronteira.append(nome_pais)
    
    def __str__(self):
        fronteira_fotmatada = ', '.join(self.__fronteira) if self.__fronteira else 'Nenhuma'
        return f'País: {self.__nome}\nCapital: {self.__capital}\nDimensão: {self.__dimensao} km²\n Fronteira: {fronteira_fotmatada}'
    
brasil = Pais("Brasil", "Brasília", 8515767)
brasil.adiciona_pais("Argentina")
brasil.adiciona_pais("Uruguai")
brasil.adiciona_pais("Argentina")  
print(brasil)

print("Nome do país:", brasil.nome)
print("Capital:", brasil.capital)
print("Dimensão em km²:", brasil.dimensao)
print("Fronteira:", brasil.paises_fronteira())