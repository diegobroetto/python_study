"""
Dicionários

OBS: Em algumas linguagens de programação, os dicionários python são conhecidos
por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por {};

OBS: Sobre dicionários
    -Chave e valor são separados por dois ponto 'chave:valor';
    -Tanto chave quanto valor podem se de qualquer tipo de dados;
    -Podemos misturar tipos de dados

"""
# Forma 1 (Mais Comum)
paises = {
    'br': 'Brasil',
    'eua': 'Estados Unidos',
    'py': 'Paraguai'
}

print(paises)

#Forma 2 (menos comum)

paises2 = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')


#Acessando elementos

#Forma 1 - Acessando via chave da mesma forma que lista/tupla

print(paises['br'])

#Forma 2  - Acessando via get - Recomendado

print(paises.get('br'))
print(paises.get('py'))


pais = paises.get('ru')

if pais:
    print(f'Encontrei o país {paises}')
else:
    print('Não encontrei o pais')


pais = paises.get('ru', 'Não encontrado')


if 'ru' in paises:
    russia = paises['ru']

#Podemos utilizar qualquer tipo de dados (int, float, string, boolean, incluse lista, tupla)

#tuplas por exemplo são bastante interessanter de serem utilizadas como chave de dicionários, por serem imutáveis
localidade = {
    (35.1111, 45.555): 'Escritorio em Tokyo',
    (35.1111, 42.555): 'Escritorio em São Paulo',
    (31.1111, 45.555): 'Escritorio em New York',
}

print(localidade)

#Adicionar elementos em um dicionário

receita = {
    'jan': 100,
    'fev': 200,
    'mar': 345
}

#Forma 1

print(receita)

receita['abr'] = 256

print(receita)

#Forma 2

novo_dado = {'mai': 450}

receita.update(novo_dado)

print(receita)

#Atualizando dados em um dicionário

#Forma 1

receita['mai'] = 400
print(receita)

#Forma 2

receita.update({'mai': 5000})

print(receita)

#Dicionários não aceitam chaves repetidas

#Remover dados de um dicionário

#Forma 1
receita.pop('mar')

#OBS: aqui precisamos sempre informar a chave

#Forma 2

del receita['fev']
print(receita)

#Métodos de Dicionários

d = dict(a=1, b=2, c=3)

#Limpar dicionário

d.clear()

print(d)

#Copiando um dicionários para outro

#Forma 1
d = dict(a=1, b=2, c=3)

novo = d.copy() #Deep copy

novo['d'] = 4

print(d)
print(novo)


#Forma 2
d = dict(a=1, b=2, c=3)

novo = d

novo['f']





