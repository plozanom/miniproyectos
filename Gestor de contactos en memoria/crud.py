contactos = []

def create(nombre, telefono, email):
    """Crea un nuevo contacto"""

    contacto = {}
    
    contacto['nombre'] = nombre
    contacto['telefono'] = telefono
    contacto['email'] = email

    contactos.append(contacto)

    return 'Se agregó un nuevo contacto'

def read_all():
    """Muestra una tabla con todos los contactos"""

    margen = 3
    ancho_nombre = max(len(contacto['nombre']) for contacto in contactos) + margen
    ancho_telefono = max(len(contacto['telefono']) for contacto in contactos) + margen
    ancho_email = max(len(contacto['email']) for contacto in contactos) + margen

    # Creacion de la tabla
    print(f" {'_' * (ancho_nombre + 1)}{'_' * (ancho_telefono + 1)}{'_' * (ancho_email)}")
    print(f"|{'Nombre':^{ancho_nombre}}|{'Teléfono':^{ancho_telefono}}|{'Email':^{ancho_email}}|")
    print(f"|{'-' * ancho_nombre}|{'-' * ancho_telefono}|{'-' * ancho_email}|")

    for item in contactos:
        print(f"|{item['nombre']:<{ancho_nombre}}|{item['telefono']:<{ancho_telefono}}|{item['email']:<{ancho_email}}|")
    
    print(f"|{'_' * ancho_nombre}|{'_' * ancho_telefono}|{'_' * ancho_email}|")

def read(nombre):
    """Muestra los datos de un contacto el cual se busca por el nombre completo"""

    for contacto in contactos:
        if contacto['nombre'] == nombre:
            return f"Nombre: {contacto['nombre']}\nTelefono: {contacto['telefono']}\nEmail: {contacto['email']}"
    else:
        return f'El contacto {nombre} no se encuentra en la base de datos'

def update(nombre, parametro, cambio):
    """Actualiza los datos de un contacto"""

    for contacto in contactos:
        if contacto['nombre'] == nombre:
            if parametro == 'nombre':
                contacto['nombre'] = cambio
                return f'El cambio de nombre para el contacto {nombre} se ha hecho de manera exitosa'
            elif parametro == 'telefono':
                contacto['telefono'] = cambio
                return f'El cambio de telefono para el contacto {nombre} se ha hecho de manera exitosa'
            elif parametro == 'email':
                contacto['email'] = cambio
                return f'El cambio de email para el contacto {nombre} se ha hecho de manera exitosa'
            else:
                return f'{parametro} no es un campo dentro de la base de datos'
    else:
        return f'El contacto {nombre} no ha sido encontrado'

def delete(nombre):
    """Borra un contacto el cual se encuentra por su nombre"""
    
    for contacto in contactos:
        if contacto['nombre'] == nombre:
            contactos.remove(contacto)
            return f'Se ha borrado el contacto {nombre}'
    else:
        return 'Contacto no encontrado'
    
"""create('Pedro Lozano', '3177937319', 'amail@mail.com')
read_all()"""