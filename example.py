from unicodedata import name


def dividir(dividendo, divisor):
    return dividendo // divisor


def testa_divisao(divisor):
    try:
        resultado = dividir(10, divisor)
        print(f"O resultado da divisão de 10 por {divisor} é {resultado}")
    except ZeroDivisionError:
        print("Erro de divisão por 0 tratado")


try:
    testa_divisao(0)
except AttributeError:
    print('Erro de atributo tratado')
