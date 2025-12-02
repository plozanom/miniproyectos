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

if minusculas == 'si' and mayusculas == 'no' and numeros == 'no' and especiales == 'no':# Solo minusculas
    password = ''.join(choices(letras_minusculas, k= longitud_passwd))
elif minusculas == 'no' and mayusculas == 'si' and numeros == 'no' and especiales == 'no':# Solo mayusculas
    password = ''.join(choices(letras_mayusculas, k= longitud_passwd))
elif minusculas == 'no' and mayusculas == 'no' and numeros == 'si' and especiales == 'no':# Solo digitos
    password = ''.join(choices(digitos, k= longitud_passwd))
elif minusculas == 'no' and mayusculas == 'no' and numeros == 'no' and especiales == 'si':# Solo caracteres especiales
    password = ''.join(choices(caracteres_especiales, k= longitud_passwd))
elif minusculas == 'si' and mayusculas == 'si' and numeros == 'no' and especiales == 'no':# Minusculas y Mayusculas
    password = ''.join(choices(letras_minusculas + letras_mayusculas, k= longitud_passwd))
elif minusculas == 'si' and mayusculas == 'no' and numeros == 'si' and especiales == 'no':# Minusculas y digitos
    password = ''.join(choices(letras_minusculas + digitos, k= longitud_passwd))
elif minusculas == 'si' and mayusculas == 'no' and numeros == 'no' and especiales == 'si':# Minusculas y caracteres especiales
    password = ''.join(choices(letras_minusculas + caracteres_especiales, k= longitud_passwd)) 
elif minusculas == 'no' and mayusculas == 'si' and numeros == 'si' and especiales == 'no':# Mayusculas y digitos
    password = ''.join(choices(letras_mayusculas + digitos, k= longitud_passwd))
elif minusculas == 'no' and mayusculas == 'si' and numeros == 'no' and especiales == 'si':# Mayusculas y caracteres especiales
    password = ''.join(choices(letras_mayusculas + caracteres_especiales, k= longitud_passwd))
elif minusculas == 'no' and mayusculas == 'no' and numeros == 'si' and especiales == 'si':# Digitos y caracteres especiales
    password = ''.join(choices(digitos + caracteres_especiales, k= longitud_passwd))
elif minusculas == 'si' and mayusculas == 'si' and numeros == 'si' and especiales == 'no':# Minusculas, mayusculas y digitos
    password = ''.join(choices(letras_minusculas + letras_mayusculas + digitos, k= longitud_passwd))
elif minusculas == 'si' and mayusculas == 'si' and numeros == 'no' and especiales == 'si':# Minusculas, mayusculas y caracteres especiales
    password = ''.join(choices(letras_minusculas + letras_mayusculas + caracteres_especiales, k= longitud_passwd))
elif minusculas == 'si' and mayusculas == 'no' and numeros == 'si' and especiales == 'si':# Minusculas, digitos y caracteres especiales
    password = ''.join(choices(letras_minusculas + digitos + caracteres_especiales, k= longitud_passwd))
elif minusculas == 'no' and mayusculas == 'si' and numeros == 'si' and especiales == 'si':# Mayusculas, digitos y caracteres especiales
    password = ''.join(choices(letras_minusculas + letras_mayusculas + digitos, k= longitud_passwd))
elif minusculas == 'si' and mayusculas == 'si' and numeros == 'si' and especiales == 'si':# Todos los caracteres
    password = ''.join(choices(letras_minusculas + letras_mayusculas + digitos + caracteres_especiales, k= longitud_passwd))
else:
    password = '-'*longitud_passwd

print(password)