# 17. Dada una tupla anidada con pares de números, sumar cada par y mostrar los resultados.

tupla = ((1, 2), (3, 4), (5, 6))
sumas = tuple(a + b for a, b in tupla)
print(sumas)  # (3, 7, 11)
