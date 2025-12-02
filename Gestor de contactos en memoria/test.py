data = [
    {"nombre": "Ana García", "telefono": "3001234567", "email": "ana.garcia@example.com"},
    {"nombre": "Luis Pérez", "telefono": "3109876543", "email": "luis.perez@example.com"},
    {"nombre": "María Rodríguez", "telefono": "3201122334", "email": "maria.rodriguez.long_email@example.com"},
    {"nombre": "Juan", "telefono": "3055555555", "email": "juan@example.com"}
]

# Definir el ancho máximo para cada columna
# Puedes ajustar estos valores según la longitud máxima esperada de tus datos
ancho_nombre = max(len(d["nombre"]) for d in data)
ancho_telefono = max(len(d["telefono"]) for d in data)
ancho_email = max(len(d["email"]) for d in data)

# Si quieres un poco de margen adicional para que no quede todo pegado
margen = 2
ancho_nombre += margen
ancho_telefono += margen
ancho_email += margen

# Imprimir los encabezados de la tabla
print(f"{'Nombre':<{ancho_nombre}}{'Teléfono':<{ancho_telefono}}{'Email':<{ancho_email}}")
print(f"{'-' * ancho_nombre}{'-' * ancho_telefono}{'-' * ancho_email}")

# Imprimir cada fila de datos
for item in data:
    print(f"{item['nombre']:<{ancho_nombre}}{item['telefono']:<{ancho_telefono}}{item['email']:<{ancho_email}}")