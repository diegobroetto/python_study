"""
Faça um programa que possua um vetor denominado A que armazene 6 numeros inteiros. 
O programa deve executar os seguintes passos:
a - Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
b - Amazene em uma varível inteira (simples) a soma entre os valores das posições A[0], A[1] e A[5]
do vetor e mostre a soma na tela.
c - Modifique o vetor na posição 4, atribuindo a esta posição o valor de 100
d - Mostre na tela cada valor do vetor A, um em cada linha.
"""

#a - Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
A = [1, 0, 5, -2, -5, 7]

#b - Amazene em uma varível inteira (simples) a soma entre os valores das posições A[0], A[1] e A[5] do vetor e mostre a soma na tela.
soma = A[0] + A[1] + A[5]
print(soma)

#c - Modifique o vetor na posição 4, atribuindo a esta posição o valor de 100
print(A[4])
A. insert(4, 100)
print(A[4])

#d - Mostre na tela cada valor do vetor A, um em cada linha.
for lista in A:
    print(lista)