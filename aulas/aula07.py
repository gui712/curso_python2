#args - Argumentos não nomeados

x, y, *resto = 1, 2, 3, 4
print(x,y, resto)



#def soma(x, y):
#    return x + y


def soma(*args):
    total = 0
    for numero in args:
        total += numero
    return total


soma_1 = soma(1,2,3,4,5,6)
print(soma_1)

outra_soma = soma(7,8,9,10,15,10)
print(outra_soma)