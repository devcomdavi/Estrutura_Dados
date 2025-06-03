def somar(list):
    if list == None:
        return 0
    ult = list.pop()
    return somar(list) + ult

lista = [1,2,3,4,5]
print(somar(lista))