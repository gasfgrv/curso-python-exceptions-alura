def dividir(dividendo, divisor):
    if not (isinstance(dividendo, int) and isinstance(divisor, int)):
        raise ValueError("dividir() deve appenas receber argumentos inteiros.")

    try:
        return dividendo / divisor
    except:
        print(f'Não foi possível dividir {dividendo} por {divisor}')
        raise


def testa_divisao(divisor):
    resultado = dividir(10, divisor)
    print(f"O resultado da divisão de 10 por {divisor} é {resultado}")


if __name__ == '__main__':
    try:
        testa_divisao(0)
    except AttributeError as E:
        print('Erro de atributo tratado')
    except ZeroDivisionError as E:
        print("Erro de divisão por 0 tratado")
