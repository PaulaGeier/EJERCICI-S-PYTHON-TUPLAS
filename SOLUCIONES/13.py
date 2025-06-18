# 13. Crear una tupla de 10 números y mostrar solo los números pares.

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
pares = tuple(n for n in tupla if n % 2 == 0)
print(pares)  # (2, 4, 6, 8, 10)
