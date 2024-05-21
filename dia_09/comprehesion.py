"""
List Comprehension

-Utilizando List Comprehension nós podemos gerar novas listas com dados processados a partir de outro iterável.

#Sintaxe

[dado for dado in iterável]
"""

numeros = [1, 2, 3 , 4]

res = [numero * 10 for numero in numeros]

print(res)