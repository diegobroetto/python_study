"""
-Módulo Collection - Deque

Podemos dizer que o deque é uma lista de alta performance.

"""

from collections import deque


deq = deque('diego')

print(deq)

#Adicionando Elementos

deq.append('y') #adiciona no final

print(deq)

deq.appendleft('e') #adiciona no começo

print(deq)

#remover elementos

print(deq.pop()) #remove no fim

print(deq.popleft()) #remove no inicio