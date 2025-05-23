from lib import Pilha

palavra = input().strip()
lista = []

for i in palavra:
    lista.append(i)
print(lista)

for i in range(len(palavra)):
    if not palavra[i].isalpha():
        palavra.remove(palavra[i])
print(palavra)
