class Conta_Corrente:
    def __init__(self, numero, saldo, nome_titular):
        self.__numero = numero
        self.__saldo = saldo
        self.__nome_titular = nome_titular
    
    @property
    def numero(self):
        return self.__numero
   
    @numero.setter
    def numero(self, novo_numero):
        self.__numero = novo_numero
   
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, novo_saldo):
        self.__saldo = novo_saldo

    def depositar(self, valor_depositado):
        self.__saldo += valor_depositado
    
    def sacar(self, valor_sacado):
        if valor_sacado <= self.__saldo:
            self.__saldo -= valor_sacado
            return True
        else:
            return False

lista_conta_corrente = []
for i in range(10):
    conta_corrente = Conta_Corrente(input('Número: '), float(input('Saldo: ')), input('Nome do titular: '))
    lista_conta_corrente.append(conta_corrente)

while True:
    print('[1] Depositar valor','\n[2] Sacar valor', '\n[3] Exibir saldo','\n[4] Sair')
    resposta = input('Digite a opção: ')
    
    if resposta == '1':
        num_conta = input('Número da conta: ')
        valor = float(input('Valor a depositar: '))
        for i in range(len(lista_conta_corrente)):
            if lista_conta_corrente[i].numero == num_conta:
                lista_conta_corrente[i].saldo += valor
    elif resposta == '2':
        num_conta = input('Número da conta: ')
        valor = float(input('Valor a sacar: '))
        for i in range(len(lista_conta_corrente)):
            if lista_conta_corrente[i].numero == num_conta:
                lista_conta_corrente[i].saldo -= valor
    elif resposta == '3':
        num_conta = input('Número da conta: ')
        for i in range(len(lista_conta_corrente)):
            if lista_conta_corrente[i].numero == num_conta:
                print(lista_conta_corrente[i].saldo)   
    elif resposta == '4':
        break    
    else:
        print('Número não reconhecido')