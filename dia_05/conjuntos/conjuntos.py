"""
-Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos
da matemática.

-No python, os conjuntos são chamados de Sets

Dito isto, da mesma forma que na matemática:

-Sets (conjuntos) não póssuem valores duplicados;
-Sets (conjuntos) não possuem valores ordenados;
-Elementos não são acessados via índice, ou seja, conjuto não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados

Os conjuntos (sets) são referênciados em Python com chaves {}

Diferenças entre Conjuntos (Sets) e Mapas (Dicionários) em Python:
    -Um dicionário tem chave/valor;
    -Um conjunto tem apenas valor;

"""

#Definindo um conjunto:

#Forma 1

s = set({1, 2, 3, 4, 5, 6, 2 ,4}) #repare que temos valores repetidos

print(s)
print(type(s))
 
# Ao criar um conjunto, caso seja adicionado uma valor já existente, o mesmo
#será ignorado sem gerar erro e não fará parte do conjunto

#Forma 2 (mais comum)

s2 = {1, 2, 3, 4, 5, 6, 2 ,4}
print(s2)
print(type(s2))

#Importante lembrar que, além de não termos valores duplicados, não temos ordem.

lista = [99, 4, 44, 6]
print(f'Lista: {lista}')

s3 = {99, 4, 44, 6}
print(f'Set: {s3}')

#Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets

s4 = {1, 'b', True, 23.22, 55}
print(s4)

#podemos iterar sobre um set

for valor in s4:
    print(valor)

#Usos interessante com sets

#Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes informam manualmente a cidade de onde vieram.

#Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos e ter repetição

cidades = ["São Paulo", 
           "Rio de Janeiro",
           "Rio de Janeiro",
           "Rio de Janeiro", 
           "Salvador", 
           "Brasília", 
           "Fortaleza", 
           "Manaus", 
           "Curitiba", 
           "Recife",
           "Recife",
           "Recife", 
           "Goiânia"]


print(len(cidades))

#Agora precisamos saber quantas cidade distintas, ou seja, únicas, temos.

#Podemos utilizar um set para isso:

print(len(set(cidades)))

#Adicionando elementos em um conjunto

s5 = {1, 2, 3}
s5.add(5)
s5.add(5) #duplicidade não gera erro, simpleste é ignorado e não adicionado
print(s5)

#Remover elementos em um conjunto

#Forma 1

s5.remove(3) #não é índice
print(s5)

#OBS: Caso o valor não seja encontrado será gerado o erro KeyError. Nenhum valor é retornado

#Forma 2

s5.discard(2)
print(s5)

#Copiando um conjunto para outro
s6 = {1, 2, 3, 7, 8}

#Forma 1 - Deep Copy
novo = s6.copy()

print(novo)

#Forma 2 - Shallow Copy

novo3 = s6

novo3.add(9)

print(novo)
print(s6)

#Métodos Matemáticos de Conjuntos

#Imagine que temos dois conjuntos: Um contendo estudantes do curso de Python e
#um contendo estudantes do curso de Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia'}
estudantes_java = {'Fernando', 'Lucas', 'Julia', 'Ana', 'Marcos'}

#Veja que alguns alunos que estudam Python também estudam Java.


#Precisamos gerar um cojunto com nomes de estudantes únicos

#Forma 1 - Utilizando Union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

#Forma 2 - Utilizando o caractere pipe |

unicos2 = estudantes_python | estudantes_java
print(unicos2)

#Gerar um conjuntos de estudantes que estão em ambos os conjuntos

#Forma 1 - Utilizando Intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

#Forma 2 - Utilizando &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

#Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

#Soma*, Valor Máximo*, Valor Mínimo*, Tamanho

#Se os valores forem todos inteiros ou reais

s10 = {1, 2, 3, 4, 5, 6, 2 ,4}

print(sum(s10))
print(max(s10))
print(min(s10))
print(len(s10))