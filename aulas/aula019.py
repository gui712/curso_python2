# Função lambda em Python
# Funções lambda são funções anônimas, ou seja, não possuem um nome definido.
# Elas são criadas usando a palavra-chave 'lambda' e podem ter qualquer número de argumentos
# mas apenas uma expressão.

#lista = [ 4,32,1,34,5,6,6,21,2,3,4,5,6,7,8,9,10 ]

#lista.sort()
#print(f"Lista ordenada: {lista}")

lista = [
    {'nome': 'João', 'sobrenome': 'Affonso'},
    {'nome': 'Maria', 'sobrenome': 'Silva'},
    {'nome': 'Pedro', 'sobrenome': 'Santos'},
    {'nome': 'Ana', 'sobrenome': 'Oliveira'},
    {'nome': 'Daniels', 'sobrenome': 'Jackson'},
    {'nome': 'Carlos', 'sobrenome': 'Miranda'},
    {'nome': 'Lucas', 'sobrenome': 'Souza'},
]

#lista.sort(key=lambda item: item['nome'])

def exibir(lista):
    for item in lista:
        #print(f"{item['nome']} {item['sobrenome']}")
        print(item)
    print()

l1 = sorted(lista, key=lambda item: item['nome'])
l2 = sorted(lista, key=lambda item: item['sobrenome'])

exibir(l1)
exibir(l2)