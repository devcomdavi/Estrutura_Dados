class Aluno:
    def __init__(self, matricula, nome, notas):
        self.__matricula = matricula
        self.__nome = nome
        self.__notas = notas
    
    @property
    def matricula(self):
        return str(self.__matricula)
    
    @property
    def nome(self):
        return self.__nome
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    def media(self):
        return f'{(sum(self.__notas)/len(self.__notas)):.2f}'
    
    def adiciona_nota(self, nota):
        self.__notas.append(nota)
    
    def __str__(self):
        return f'Aluno: {self.__nome} | Matrícula: {self.__matricula} | Média: {self.media()}'
    
notas_davi = [10, 7, 8]
aluno = Aluno(1234, 'Davi Holanda', notas_davi)
print(aluno)
print(aluno.nome)
print(aluno.matricula)
print(aluno.media())

aluno.nome = 'João Pedro'
aluno.adiciona_nota(6)
print(f'\n{aluno}')
print(aluno.nome)
print(aluno.media())
