import random

def create_array():
    array = []
    for i in range(3):
        line = []
        for j in range(6):
            line.append(random.randint(1,10))
        array.append(line)
    return array

def print_impar(array):
    sum = 0
    for colum in range(1, len(array[0]), 2):
        for line in range(len(array)):
            sum += array[line][colum]
    print(f"Soma dos elementos das colunas ímpares é {sum}")


array = create_array()

print_impar(array)

