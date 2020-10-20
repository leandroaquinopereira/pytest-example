import pytest
from src.ClassPilha import Pilha
 
@pytest.fixture
def pilha():
    return Pilha()

def test_isEmpty(pilha): # verfica se está vazia
    pilha.isEmpty()
    assert True == pilha.isEmpty()

def test_push(pilha): # verifica o primeiro elemento inserido
    pilha.push(32)
    assert 32 == pilha.items[0]

def test_pop(pilha): # verifica o comprimento da pilha somente na primeira dimensão (quando se trabalha com matrizes)
    pilha.push(3)
    pilha.push(18)
    pilha.pop()
    assert 1 == len(pilha.items)
    
def test_peek(pilha): # verifica o primeiro elemento da pilha
    pilha.push(15)
    pilha.push(0)
    assert 0 == pilha.peek() 
    
def test_size(pilha): # verifica o número total de elementos na pilha
    pilha.push(11)
    pilha.push(4)
    assert 2 == pilha.size() 
    
def test_pop_empty(pilha): # verfica se pode retirar elementos quando não há nada na pilha
    with pytest.raises(IndexError):
        pilha.pop()
     