#Continuando set em python
# Sets são coleções de elementos únicos e não ordenados.
# Eles são úteis quando você precisa garantir que não haja duplicatas em uma coleção.
# Set são eficientes para remover valores duplicados e realizar operações de conjunto, como união, interseção e diferença.
# Seus valores são sempre únicos e não há ordem definida.
# não existe indexação, fatiamento ou concatenação em sets. e não aceita valores mutáveis como listas ou dicionários.
s1 = {1,2,3,3,3,3,3,3,7,1}
print(s1, type(s1))

print(3 in s1)  # Verifica se o valor 3 está no set
print(4 in s1)  # Verifica se o valor 4 está no set

for numero in s1:
    print(numero)
    