#Operadores uteis em set
# - union() -> Retorna a união de dois sets.
# - intersection() -> Retorna a interseção de dois sets. itens presentes em ambos os sets.
# - difference() -> Retorna a diferença entre dois sets. itens presentes apenas no primeiro set.

s1 = {1, 2, 3, 4, 5}
s2 = {4, 5, 6, 7, 8}
s3 = s1 | s2  # União
print(f"União: {s3}")
s4 = s1 & s2  # Interseção
print(f"Interseção: {s4}")
s5 = s1 - s2  # Diferença
print(f"Diferença: {s5}")
s6 = s1 ^ s2  # Diferença simétrica
print(f"Diferença simétrica: {s6}")