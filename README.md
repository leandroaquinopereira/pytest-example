# Pytest

Este projeto é um exemplo de implementação de pilha com realizações de testes usando o Framework Pytest.

As seguintes ações são testadas:
- Pilha vazia
- Elemento inserido
- Comprimento da  pilha
- O primeiro elemento da  pilha
- Número total de elementos
- Retirar elementos da pilha


Instalar o Pytest:

$pip install -U pytest

Executar o código:

$pytest ex1_test.py 

Sobre o código:

#Verfica se está vazia. O  .fixture é chamado durante a realização do teste. 
@pytest.fixture
def pilha():
    return Pilha()

def test_isEmpty(pilha): 
    pilha.isEmpty()
    assert True == pilha.isEmpty()
    
#Verifica o primeiro elemento inserido
def test_push(pilha): 
    pilha.push(32)
    assert 32 == pilha.items[0]

#Verifica o comprimento da pilha somente na primeira dimensão (quando se trabalha com matrizes)
def test_pop(pilha): pilha.push(3)
    pilha.push(18)
    pilha.pop()
    assert 1 == len(pilha.items)
    
#Verifica o primeiro elemento da pilha    
def test_peek(pilha): 
    pilha.push(15)
    pilha.push(0)
    assert 0 == pilha.peek() 
    
#Verifica o número total de elementos na pilha    
def test_size(pilha): 
    pilha.push(11)
    pilha.push(4)
    assert 2 == pilha.size() 

#Verfica se pode retirar elementos quando não há nada na pilha
def test_pop_empty(pilha): 
    with pytest.raises(IndexError):
        pilha.pop()
     
