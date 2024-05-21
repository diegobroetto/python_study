"""
Lambdas

Conhecidas por expressões Lambdas, sõ funções sem nome, ou seja, funções anonimas.
"""


#expressão Lambda
lambda x: 3 * x + 1

autores = ["Jane Austen", "George Orwell", "J.K. Rowling", "Harper Lee", "Stephen King", "Agatha Christie", "Tolkien", "J.R.R. Martin"]
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)


#testando função quadratica

#f(x) = a * x ** 2 + b * x + c
def gerarFuncQuadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = gerarFuncQuadratica(2, 3, -4)

print(teste(2))