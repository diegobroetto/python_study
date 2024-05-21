def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.items():
        print(f'Cor favorita de {pessoa.title()} é {cor}')



cores_favoritas (diego='vermelho', julia='amarelo')

cores_favoritas()

