"""
-Módulo Collections: Ordered Dict

Em um dicionários a ordem de inserção não é garantida.

OrderedDict -> É um dicionário que garante a ordem de inserção dos elementos

"""

from collections import OrderedDict


dicionario = OrderedDict({'a': 1, 'c': 2, 'b': 4, 'd': 3, 'e': 5, 'f': 6,})


for chave, valor in dicionario.items():
    print(f'chave={chave} valor={valor}')
