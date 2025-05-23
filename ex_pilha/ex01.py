from lib import Pilha

p = Pilha()
opcao = 1

cont = 0
while opcao != 0:    
    print('EDITOR DE PILHA','\n[1] EMPILHAR', '\n[2] DESEMPILHAR', '\n[3] EXIBIR ELEMENTO DO TOPO', '\n[4] EXIBIR A PILHA', '\n[5] TAMANHO DA PILHA', '\n[6] ESVAZIAR A PILHA', '\n[0] SAIR')
    opcao = int(input('DIGITE SUA OPÇÃO: '))
    if opcao == 1:
        p.empilhar(int(input('Valor a ser empilhado: ')))
        print('Feito')
        cont += 1
    if opcao == 2:
        p.desempilhar()
        print('Feito!')
        cont -= 1
    if opcao == 3:
        print(p.topo())
    if opcao == 4:
        print(p)
    if opcao == 5:
        print(cont)
    if opcao == 6:
        while cont != 0:
            p.desempilhar()
        print('Feito')