# 15. Crear una tupla de tuplas con nombre y edad, y mostrar solo las personas mayores de 18.

personas = (("Juan", 17), ("Ana", 21), ("Luis", 19))
mayores = tuple(p for p in personas if p[1] >= 18)
print(mayores)  # (('Ana', 21), ('Luis', 19))
