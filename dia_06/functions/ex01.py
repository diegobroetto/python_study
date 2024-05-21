from datetime import datetime
from num2words import num2words

def receber_data(data):
    data_obj = datetime.strptime(data, '%d/%m/%Y')

    dia = data_obj.day
    mes = data_obj.month
    ano = data_obj.year

    dia_extenso = num2words(dia, lang='pt_BR')
    ano_extenso = num2words(ano, lang='pt_BR')

    meses = [
        'janeiro', 'fevereiro', 'março', 'abril',
        'maio', 'junho', 'julho', 'agosto',
        'setembro', 'outubro', 'novembro', 'dezembro'
    ]

    mes_extenso = meses[mes - 1]
    data_extenso = f'{dia_extenso} de {mes_extenso} de {ano_extenso}'

    return data_extenso 

print(receber_data('10/05/2024'))




