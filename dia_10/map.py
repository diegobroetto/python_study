"""
Com o map, fazemos mapeamento de valores para função

"""

import math

def area(r):
    """calcula a area de um circulo com raio 'r' """
    return math.pi * (r ** 2)

print(area(20))


raios = [2, 4, 55, 67, 88, 99]

#forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)

#forma utilizando Map

#Map é uma função que recebe dois parâmetros: primeiro uma função, o segundo um iterável

areas = map(area, raios)
print(list(areas))

#pegar uma lista com cidades e temperaturas em C e converter para F

cidades = [('Berlim', 29), ('São Paulo', 22), ('Los Angeles', 20)]

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))