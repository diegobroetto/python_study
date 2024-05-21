import random

#função cria uma array 4x4 com números aleatórios
def create_array():
    array = []
    for i in range(4):
        line = []
        for j in range(4):
            line.append(random.randint(1, 10))
        array.append(line)
    return array

#função imprimi um array
def print_array(array):
    for line in array:
        print(line)

#Criando array
array_4x4 = create_array()

#Imprimindo Array
print_array(array_4x4)