pessoa = {}

chave = 'nome'

pessoa[chave] = 'Luiz Otávio'
pessoa['sobrenome'] = 'Miranda'

print(pessoa[chave])

pessoa[chave] = 'Maria'

del pessoa['sobrenome']
print(pessoa)
print(pessoa['nome'])

if  pessoa.get('sobrenome') is None:
    print('Não existe')
else:
    print(pessoa['sobrenome'])