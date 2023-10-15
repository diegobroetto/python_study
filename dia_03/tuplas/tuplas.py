"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas;

Existem basicamente duas diferenças:

1 - As tuplas são representadas por parênteses ()

2 - As tuplas são imutáveis, isso significa que ao criar uma tupla ela não muda. Toda
operação em um tupla gera uma nova tupla.

"""

#CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4
print(tupla2)

print(type(tupla2))

#CUIDADO 2: Tuplas com 1 elemento

tupla3 = (4) #Isso não é uma tupla
print((tupla3))

print(type(tupla3))

tupla4 = (4, ) #Isso é uma tupla
print(tupla4)

print(type(tupla4))

tupla5 = 4,
print(tupla4)

print(type(tupla5))

#CONCLUSÃO: Podemos definir que tuplas são definidas pelas vírgula e não pelo uso do parênteses.

#Podemos gerar uma tupla dinamicamente com range
tupla6 = tuple(range(0, 10))
print(tupla6)

#Desempacotamento de tupla

tupla = ('Diego Broetto', 'Sistemas de Informação')

nome, curso = tupla

print(nome)
print(curso)

#Soma*, Valor Máximo*, Valor Mínimo* e Tamanho
# *Se os valores forem todos inteiros ou reais

tupla12 = (1, 2, 3, 4, 5)

print(sum(tupla12))
print(min(tupla12))
print(max(tupla12))
print(len(tupla12))

#concatenação de tuplas

tupla13 = (1, 3, 5)
print(tupla13)

tupla14 = (4, 6, 7)
print(tupla14)

print(tupla13 + tupla14)

#verificar se determinado elemente está contido na tupla

print(1 in tupla13)

#iterando sobre uma tupla

for n in tupla13:
    print(n)

for indice, valor in enumerate(tupla13):
    print(f"Indice{indice}=[{valor}]")

#contando elementos dentro de uma tupla

tupla33 = ('a', 'b', 'c', 'a', 'b')

print(tupla33.count('a'))

nome = tuple('Diego Broetto')

print(nome.count('e'))

#Dicas na utilização de tuplas

#Devemos utilizar tuplas SEMPRE que não precisarmos modificar os dados contidos em uma coleção

#Exemplo 1

meses = ('Janeiro', 'Fevereiro', 'Março')

#O acesso de elementos de uma tupla também é semelhante a de uma lista

print(meses[2])

#iterar com while

i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

#vericar em qual indice um elemente está na lista

print(meses.index('Janeiro'))

#slicing

print(meses[1:2])

"""
Por que utilizar tuplas?

- Tuplas são mais rapidas que listas
- Tuplas deixam seu código mais seguro
(trabalhar com elementos imutáveis traz segurança para o código)




"""