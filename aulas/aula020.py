# Função lambda em Python


def executa(funcao, *args):
    return funcao(*args)

# Função lambda para somar dois números
print(
    executa(
        lambda x,y: x + y,
        10,15
    )
)