"""
Aprendendo sobre como utilizar listas em Python

Listas em python funcionam como vetores/matrizes (arrays) em outras linguagem, com a diferença de serem DINÂMICO
e também podemos colocar QUALQUER tipo de dados.

"""

lista1 = [1, 1, 2, 99, 23, 44, 55]

lista2 = ['D', 'I', 'E', 'G', 'O']

lista3 = []

lista4 = list(range(11))

#Podemos checar se determinado valor está contiudo na lista

if 2 in lista1:
    print('Encontrei o numero 2')
else:
    print('Não econtrei o numero 2')

if 'G' in lista2:
    print('Encontrei a letra G')
else:
    print('Não encontrei a letra G')

#Podemos ordernar uma lista facilmente
print(f"Lista desordenada: {lista1}")
lista1.sort()
print(f"Lista ordenada: {lista1}")

print(f"Lista desordenada: {lista2}")
lista2.sort()
print(f"Lista ordenada: {lista2}")

#Podemos facilmente contar o número de ocorrências em uma lista
print(f"Quandidade de Nº 1 dentro da lista: {lista1.count(1)}")
print(f"Quandide de letras D dentro da lista: {lista2.count('D')}")

#Adicionar elementos detro de uma lista

"""
Para adicionar elementos em uma lista, utilizamos a função append

OBS: Com append, nós só conseguimos adicionar 1 elemento por vez
"""

print(f"Lista antes de adicionar valor {lista1}")
lista1.append(123)
print(f"Lista após adicionar valor : {lista1}")

#É possível também adicionar um elemento do tipo lista:

lista1.append([1, 3, 4])
print(f"Lista após adicionar outra elemento lista : {lista1}")

if [1, 3, 4] in lista1:
    print("Encontrei a lista [1, 3, 4]")
else:
    print("Não encontrei a lista [1, 3, 4]")

#A função extend adiciona varios valores dentro da lista de forma individual

lista1.extend([55, 56, 77])
print(f"Lista após adicionar valores com extend : {lista1}")

#Podemos inserir um novo elemento na lista informando a posição do index

lista1.insert(2, 'Novo valor')
print(f"Lista após adicionar valor no indice 2 : {lista1}")

#Podemos também juntar duas listas

lista6 = lista1 + lista2
print(f"Soma das listas 1 e 2 : {lista6}")

#Imprimir a lista de forma inversa
lista1.reverse()
print(f"Lista 1 invertida : {lista1}")

#Copiar uma lista
lista7 = lista1.copy()
print(f"Copiando a lista 1 para uma nova lista : {lista7}")

#Remover ultmo elemento de uma lista
print(f"Lista antes de remover valor {lista1}")
lista1.pop()
print(f"Lista após remover ultimo valor : {lista1}")

#É possível passar qual indice você gostaria de remover
print(f"Lista antes de remover valor do indice 2 {lista1}")
lista1.pop(2)
print(f"Lista após remover valor do indice 2 : {lista1}")


