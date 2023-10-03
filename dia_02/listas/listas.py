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

# Remover todos os elementos da lista
print(lista1)
lista1.clear()
print(lista1)

#Podemos repetir elementos em uma lista

nova = [1, 2, 4]
print(nova)
nova = nova * 3
print(nova)

#Podemos coverter uma string para uma lista
#OBS: por padrão o split separa os elementos da lista pelo espaço entre elas

nome = 'Diego Broetto'
print(nome)
nome.split()
print(nome)

#Exemplo 2, usando outro elemento como separador

nome2 = "Diego,de,Padua,Broetto"
nome2 = nome2.split(',')
print(nome2)

#Conveter uma lista em uma string
nome3 = ["Testando", "Funções", "de", "Listas", "em", "Python"]
print(nome3)
#Abaixo estamos falando, pegar a lista nome3, coloca espaço entre cada elemento e tranforma em string
nome3 = ' '.join(nome3)
print(nome3)

#Iterando sobre listas

#Exemplo 1

lista_nova = [1, 1, 2, 99, 23, 44, 55]

soma = 0
for elemento in lista_nova:
    print(elemento)
    soma = soma + elemento
print(soma)

#Exemplo 2 - Utilizando while

carrinho = []
produto = []

while produto != 'sair':
    print("Adicione ou produto na lista ou digite 'sair' para sair")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

#utilizado variáveis em listas

numero = [1, 2, 3, 4, 5]


num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

#gerar indice em um for

for indice, numeros in enumerate(numero):
    print(f"Indice[{indice}]={numeros}")

#encontrar o índice de um elemento na lista

print(numero.index(1))

#Soma, Valor Máximo, Valo Mínimo, Tamanho

valor1 = [1, 2, 3, 4, 5]

print(sum(valor1))
print(max(valor1))
print(min(valor1))
print(len(valor1))

#tranformar lista em tupla

valor2 = [1, 2, 3, 4, 5]
print(valor2)
print(type(valor2))

tupla = tuple(valor2)
print(valor2)
print(type(valor2))

#Copiando uma lista para outro (Shallow Copy e Deep Copy)
"""
Quando utilizamos .copy() copiamos os dados da lista para uma nova lista, mas elas
ficaram totalmente independentes, ou seja, modificando uma lista, não afeta a outra.
Isso em Python é chamado de Deep Copy
"""
valor3 = [1, 2, 3, 4, 5]

nova = valor3.copy()

#Forma 2 - Shallow Copy

valor4 = [1, 2, 3, 4, 5]

nova2 = valor4
nova2.append(6)

"""
Acima utilizamos a cópia via atribuição e copiamos os dados da lista para a nova lista, mas 
após realizar modificações em uma das listas, essa modificação se refletiu em ambas as lista.
Isso em Python é chamado Shallow Copy
"""