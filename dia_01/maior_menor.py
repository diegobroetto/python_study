<<<<<<< HEAD
"""
Escrever um programa que leia 10 valores coloque dentro de uma lsita  e imprima o menor e o maior valor
"""

valor = []

for count in range (0, 10):
    valor.append(input(f"Digite o valor numero {count+1}: "))

for indice, valor in enumerate(valor):
    print(f"Valor[{indice+1}] = {valor}")

min_valor = min(valor)
max_valor = max(valor)

print(f"O menor valor da lista é: {min_valor}")
print(f"O maior valor da lista é: {max_valor }")

=======
"""
Escrever um programa que leia 10 valores coloque dentro de uma lsita  e imprima o menor e o maior valor
"""

valor = []

for count in range (0, 10):
    valor.append(input(f"Digite o valor numero {count+1}: "))

for indice, valor in enumerate(valor):
    print(f"Valor[{indice+1}] = {valor}")

min_valor = min(valor)
max_valor = max(valor)

print(f"O menor valor da lista é: {min_valor}")
print(f"O maior valor da lista é: {max_valor }")

>>>>>>> 9ae3a8573194a595b142dad84754fcf68f2219a0
