# 12. Crear una tupla con strings y mostrar solo los que tienen más de 5 letras.

tupla = ("gato", "elefante", "perro", "jirafa")
largos = tuple(palabra for palabra in tupla if len(palabra) > 5)
print(largos)  # ('elefante', 'jirafa')
