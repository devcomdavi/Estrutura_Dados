from fila import Fila
from pilha import Pilha

if __name__ == "__main__":
    # Testando Pilha
    print('=== PILHA ===')
    pilha = Pilha()
    
    print('Empilhado: A')
    pilha.empilhar('A')
    print('Empilhado: B')
    pilha.empilhar('B')
    print('Empilhado: C')
    pilha.empilhar('C')
    
    print('Pilha:', pilha)

    print(f'Topo: {pilha.topo_pilha()}')
    print('Desempilhado: C')
    pilha.desempilhar()
    print('Pilha após desempilhar:', pilha)
    print('Desempilhado: B')
    pilha.desempilhar()
    print('Desempilhado: A')
    pilha.desempilhar()
    print(pilha) # Testando pilha vazia


    # Testando Fila
    print('\n=== FILA ===')
    fila = Fila()
    print('Enfileirado: 1')
    fila.inserir('1')
    print('Enfileirado: 2')
    fila.inserir('2')
    print('Enfileirado: 3')
    fila.inserir('3')
    print('Fila:', fila)

    print(f'Início: {fila.primeiro()}')
    
    print('Desenfileirado: 1')
    fila.remover()
    print('Fila após desenfileirar:', fila)
    print('Desenfileirado: 2')
    fila.remover()
    print('Desenfileirado: 3')
    fila.remover()
    print(fila)  # Testando fila vazia