#Exercicio com funções

def multiplica(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

mult = multiplica(10,2,3,4,5)
print(mult)