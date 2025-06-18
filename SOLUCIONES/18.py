# 18. Crear una función que reciba una tupla de números y devuelva otra con solo los que estén entre 10 y 20.

def filtrar_tupla(tupla):
    return tuple(num for num in tupla if 10 <= num <= 20)

original = (5, 12, 19, 25, 8, 15)
print(filtrar_tupla(original))  # (12, 19, 15)
