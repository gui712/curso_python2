#Métodos uteis no set
# - add() -> Adiciona um elemento ao set.
# - clear() -> Remove todos os elementos do set.
# - copy() -> Retorna uma cópia do set.
# discard() -> Remove um elemento específico do set.
# update() -> Atualiza o set com os elementos de outro iterável (como uma lista ou outro set).

s1 = set()
s1.add(1)
s1.add(2)
s1.add('Luiz')
s1.update(('Olá mundo', 1, 2, 3, 4, 5))

# s1.clear()  # Descomente para limpar o set
s1.discard('Olá mundo')  # Remove 'Olá mundo' se existir, não gera erro se não existir

print(s1)