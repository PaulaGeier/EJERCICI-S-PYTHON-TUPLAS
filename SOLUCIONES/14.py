# 14. Contar cuántos elementos de una tupla de nombres comienzan con vocal.

tupla = ("Ana", "Esteban", "Oscar", "Luis", "Iván", "Pedro")
vocales = "aeiouAEIOU"
cantidad = sum(1 for nombre in tupla if nombre[0] in vocales)
print(cantidad)  # 4
