from fila import Fila

fila = Fila()

opcao = 1
while opcao != 0:    
    print('EDITOR DE FILA','\n[1] INSERIR', '\n[2] REMOVER', '\n[3] EXIBIR PRIMEIRO', '\n[4] EXIBIR A FILA', '\n[5] TAMANHO DA FILA', '\n[6] ESVAZIAR A FILA', '\n[0] SAIR')
    opcao = int(input('DIGITE SUA OPÇÃO: '))
    if opcao == 1:
        fila.inserir(int(input('Valor a ser inserido: ')))
        print('Feito')
    if opcao == 2:
        fila.remover()
        print('Feito!')
    if opcao == 3:
        print(fila.primeiro())
    if opcao == 4:
        print(fila)
    if opcao == 5:
        print(len(fila))
    if opcao == 6:
        while len(fila) != 0:
            fila.remover()
        print('Feito')