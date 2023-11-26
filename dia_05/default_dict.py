"""
Módulo Collection - Default Dict

Ao criar um dicionário utitilizando default dict, nós informamos uma valor default,
podendo utilizar um lambda para isso. Este valor será utilizado sempre que não houver um valor definido.
Caso tentemos acessar uma chave que não existe, essa chave será criado e o valor default será atrivbuido.

OBS: Lambda são funções sem nome, que podem ou não receber parâmetros de entrada e retornar valores.

"""

dicionario = {'nome': 'Diego Broetto'}

#print(dicionario)
#print(dicionario['nome'])

from collections import defaultdict

dicionario2 = defaultdict(lambda: 0)

dicionario2['nome'] = 'Diego Broetto'

#print(dicionario2)

print(dicionario2['outro'])