"""
A função filter serve para filtrar dados de uma determinada coleção

Filter

filter()
"""
#biblioteca utilizada para trabalhar com dados estatísticos
import statistics

dados = [1.3, 2.4, 0.8, 4.3, -0.1]

#calculando a média dos dados utilizando a função mean()

media = statistics.mean(dados)

print(media)

#filter recebe dois parâmetros, uma funão e um iterável

res = filter(lambda valor: valor > media, dados)
print(list(res))

paises = ['', 'Brasil', '', "Chile", '', '', 'Equador']

#tira os valores vazios da lista
res = filter(None, paises)

print(list(res))


#Exemplo mais completo

usuarios = [
    {"username": "diego", "tweets": ["eu adoro bolos", "eu adoro pizzas"]},
    {"username": "pablo", "tweets": ["eu adoro terra"]},
    {"username": "lucas", "tweets": []},
    {"username": "nayara", "tweets": ["eu adoro lanche"]},
    {"username": "marcelo", "tweets": ["eu adoro bolos", "eu adoro pizzas", "eu adoro arroz"]}
]

#filtrar usuarios que estão inativos

inativos = list(filter(lambda usuario: len(usuario['tweets']) == 0, usuarios))
print(inativos)

inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))
print(inativos)

#combinar filter e map

nomes = ['Vanessa', 'Ana', 'Maria']

#devemos criar uma lista contendo 'Sua intrutora é' + nome, desde de que cada nome tenha menos que 5 caracteres

lista = list(map(lambda nome: f'Sua instrutor é {nome}', filter(lambda nome: len(nome) <= 5, nomes)))

print(lista)