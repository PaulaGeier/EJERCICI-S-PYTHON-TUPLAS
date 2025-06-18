# 20. Crear una tupla de tuplas con nombre y puntaje, y ordenarla por puntaje en orden descendente.
datos = (
    ("Juan", 88),
    ("María", 95),
    ("Pedro", 76),
    ("Lucía", 92)
)

ordenado = tuple(sorted(datos, key=lambda x: x[1], reverse=True))
print(ordenado)  
# (('María', 95), ('Lucía', 92), ('Juan', 88), ('Pedro', 76))
