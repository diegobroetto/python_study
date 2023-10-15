"""
Escrever um programa que leia 10 valores e some-os
"""

valores = 0

for count in range (0, 10):
    valores += int(input(f"Digite o valor {count+1}: "))
print(f"Soma dos valores: {valores}")
