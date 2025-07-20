# EMpacotamento e Desempacotamento de Dicionarios

a, b = 1, 2
a, b = b, a  # Troca de valores
#print(a, b)  # Saída: 2 1

#a , b = pessoa.values()  # Desempacotamento de valores do dicionário
#print(a,b)

#for chave, valor in pessoa.items():
#    print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

dados_pessoa = {
    'idade': 16,
    'altura': 1.76,
}

pessoa_completa = {**pessoa, **dados_pessoa}

print(pessoa_completa)

# kwargs - keyword arguments (argumentos nomeados)

def mostro_argumentos(*args, **kwargs):
    print('Não Nomeados:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


mostro_argumentos(12, 45,6, nome='Joana', qualquer='Valorqualquer')
print('---------------------------')
mostro_argumentos(**pessoa_completa)