# 19. Dada una tupla con datos de personas (nombre, edad, ciudad), imprimirlos en formato legible. Ejemplo del resultado esperado: "Juan tiene 18 años y viven en Mendoza"

personas = (
    ("Ana", 30, "Rosario"),
    ("Luis", 25, "Córdoba"),
    ("Sofía", 28, "Mendoza")
)

for nombre, edad, ciudad in personas:
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")
