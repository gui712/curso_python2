#Dicionarios em Python (tipo dict)
#São estruturas de dados do tipo chave e valor

pessoa = {
    'nome': 'Luiz Otavio',
    'sobrenome': 'Miranda',
    'idade': 18,
    'altura': 1.80,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 345}
    ]

}

for chave in pessoa:
    print(chave, pessoa[chave])

#print(pessoa)
print()
print(pessoa['nome'])