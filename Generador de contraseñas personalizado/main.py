"""Mini-Proyecto: Generador de Contraseñas Personalizado:
- Pide al usuario la longitud deseada para la contraseña.
- Pregunta si quiere incluir letras mayúsculas, minúsculas, números y/o símbolos.
- Genera una contraseña aleatoria que cumpla con los criterios seleccionados.
- Usa el módulo random y operaciones con cadenas.
- Maneja el caso en que el usuario no seleccione ningún tipo de carácter."""

import string
from random import choices

letras_minusculas = string.ascii_lowercase
letras_mayusculas = string.ascii_uppercase
digitos = string.digits
caracteres_especiales = string.punctuation

password = ''

longitud_passwd = int(input('Por favor ingrese de qué tamaño será su contraseña: '))

minusculas = str(input('Quiere minusculas en la contraseña? (si/no): '))
mayusculas = str(input('Quiere mayusculas en la contraseña? (si/no): '))
numeros = str(input('Quiere numeros en la contraseña? (si/no): '))
especiales = str(input('Quiere caracteres especiales en la contraseña? (si/no): '))

minusculas = minusculas.lower()
mayusculas = mayusculas.lower()
numeros = numeros.lower()
especiales = especiales.lower()

elecciones = [minusculas, mayusculas, numeros, especiales]
alfabeto = [letras_minusculas, letras_mayusculas, digitos, caracteres_especiales]

eleccion = ''
negaciones = 0

for i in range(4):
    if elecciones[i] == 'si':
        eleccion += alfabeto[i]
    else:
        negaciones += 1

if negaciones < 4:
    password= ''.join(choices(eleccion, k= longitud_passwd))
else:
    password = '+'*longitud_passwd

print(f'Tu contraseña personalizada es: {password}')