# criar uma função. para dobrar, triplicar, quadruplicar

def criar_multiplicador(multplicador):
    def multiplicar(numero):
        return numero * multplicador
    return multiplicar

duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadruplicar = criar_multiplicador(4)

print(duplicar(4))
print(triplicar(4))
print(quadruplicar(4))