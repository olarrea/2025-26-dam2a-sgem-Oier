carFeatures = [
    ('brand', 'Lamborghini'),
    ('model', 'Huracan'),
    ('hp', 750),
    ('gasoil', False)
]

diccionario = {}

for clave, valor in carFeatures:
    diccionario[clave] = valor

print()
for clave, valor in diccionario.items():
    print(f"La etiqueta {clave} tiene el valor {valor}")
