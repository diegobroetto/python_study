"""
Módulo Collections - Counter 

Collections -> High-performance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collection Counter que é parecido com um 
dicionário, contendo como chave um elemento da lista e como valor a quantidade de ocorreências desse elemento.

"""

#Utilizando o Counter

from collections import Counter

lista = [1, 1, 1, 2, 2, 3, 3, 4, 4, 6, 6, 7, 55, 77, 77]


#Utilizando o Coutner
res = Counter(lista)

print(type(res))
print(res)

#Counter({1: 3, 2: 2, 3: 2, 4: 2, 6: 2, 77: 2, 7: 1, 55: 1})
# Veja que para cada elemento da listam, o Counter criou uma chave e colocou como valor a quantidade de ocorrências

print(Counter('Diego Broetto'))

#Counter({'o': 3, 'e': 2, 't': 2, 'D': 1, 'i': 1, 'g': 1, ' ': 1, 'B': 1, 'r': 1})
#Para cada elemento ele criou uma chave e colocou a quantidade de ocorrênciass.

texto = """
No meio de um campo vasto e verdejante, onde o sol dançava sobre as copas das árvores, havia uma pequena cabana de madeira. Suas paredes desgastadas pelo tempo testemunhavam histórias antigas e segredos guardados. No entanto, o seu telhado resistia bravamente às intempéries, protegendo o seu interior.
Dentro da cabana, havia uma atmosfera serena e acolhedora. O aroma de madeira envelhecida misturava-se com o suave perfume das flores silvestres que alguém deixara num jarro sobre a mesa. As janelas de vidro embaçado permitiam a entrada de pequenos raios de sol, pintando o chão de um brilho dourado.
Ao redor, livros empilhados em estantes de carvalho pareciam contar histórias por si só, enquanto uma lareira crepitava suavemente, aquecendo o ambiente. Um gato preto descansava preguiçosamente em cima de uma poltrona surrada, observando o movimento com olhos curiosos.
No canto mais distante da cabana, uma escrivaninha de madeira maciça era o lar de um velho escrevente. Canetas, papéis e tintas se espalhavam como um labirinto criativo, testemunhando as palavras que ganhavam vida sob sua pena. Cada traço, cada palavra escrita, ecoava com a melodia única da imaginação.
Do lado de fora, borboletas dançavam entre as flores silvestres, e o som suave do riacho próximo oferecia uma trilha sonora tranquila para aquele refúgio. Era um lugar onde o tempo parecia desacelerar, convidando à contemplação e à criação, um santuário para a mente inquieta e para os sonhadores.
"""

palavras = texto.split()

#print(palavras)

res = Counter(palavras)

#print(res)

#encontrando as 5 palavras com mais ocorencia no texto
print(res.most_common(5))