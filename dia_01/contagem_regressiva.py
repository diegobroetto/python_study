"""
Fazer um algoririmo utilizando o comando while que mostra uma contagem regressiva na tela, 
iniciando em 10 e terminando em 0. Mostra a mensagem "FIM" quando terminar.
"""

import time

contador = 10

while contador >= 0:
    print(contador, end='\r')
    time.sleep(1)
    if contador == 0:
        print("FIM")
        break
    contador -= 1


