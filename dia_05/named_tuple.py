"""
-Módulo Collectiond - Named Tuple


Named Tuple -> São tuplas diferenciadas, onde, especificamos um nome para a mesma e também parâmetros

"""

from collections import namedtuple

#Precisamos definir o nome e parâmetro

#Forma 1: Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

#Forma 2:  Declaração Named Tuple

cachorro1 = namedtuple('cachorro', 'idade, raca, nome')

#Forma 3: Declaração Named Tuple

cachorro2 = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#Usando

ray = cachorro(idade=2, raca='Chow Chow', nome='Ray')

print(ray)

#Forma 1 
print(f'Nome: {ray[2]} Raça: {ray[1]} Idade: {ray[0]}')

#Forma 2 
print(f'Nome: {ray.nome} Raça: {ray.raca} Idade: {ray.idade}')