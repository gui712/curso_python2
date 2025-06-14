# Métodos úteos dos dicionarios em Python
# len, keys, values, item

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome': 'Miranda'
}

#print(pessoa)
#print(len(pessoa))  # Retorna a quantidade de itens no dicionário
#print(pessoa.keys())  # Retorna as chaves do dicionário
#print(list(pessoa.keys()))  # Converte as chaves em uma lista
#print(pessoa.values())  # Retorna os valores do dicionário podemos converter em lista
#print(list(pessoa.items()))  # Retorna os itens do dicionário como tuplas (chave, valor)

pessoa.setdefault('idade', 0)  # Adiciona a chave 'idade' com valor 0 se não existir
