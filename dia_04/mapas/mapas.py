"""

Mapas ->  Conhecidos em Python como Dicionários

Dicionários em Python são representados por chaves {}
"""

receita = {
    'jan': 100,
    'fev': 200,
    'mar': 345
}

#Iterar sobre dicionários

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(chave)

for chave in receita:
    print(f'{chave} : {receita[chave]}')

for chave in receita.keys():
    print(receita[chave])

print(receita.values())

for valor in receita.values():
    print(valor)

#Desempacotamento de dicionários

print(receita.items())

for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')


#Soma*, valor Máximo*, Valor Mínimo*, Tamanho

#Se os valores forem todos inteiros

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))
      

