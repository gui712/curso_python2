#função par ou impar

def parOrImpar(numero):
    multiplo_dois = numero % 2 == 0

    if multiplo_dois:
        return f'{numero} é par'
    return f'{numero} é ímpar'


print(parOrImpar(2))
print(parOrImpar(3))
print(parOrImpar(15))
print(parOrImpar(8))    