"""Todos los menu de la aplicacion"""

def principal():
    return f'Elija la magnitud:\n1. Distancia\n2. Masa\n3. Tiempo\n4. Temperatura\n0. Salir'

def eleccion_sistema():
    return f'Elija el sistema a usar:\n1. Sistema Internacional\n2. Sitema Imperial\n3. Conversion entre sistemas\n0. Salir'

def distancia_si():
    return f'Elija que medida transformar a metros:\n1. Kilometros a metros\n2. Hectometros a metros\n3. Decametros a metros\n4. Decimetros a metros\n5. Centimetros a metros\n6. Milimetros a metros\n7. Micrometros a metros\n8. Nanometros a metros\n0. Salir'

def distancia_ingles():
    return f'Elija su conversion en el Sistema Ingles:\n1. Pulgadas a pies\n2. Pies a yardas\n3. Yardas a millas\n4. Millas nauticas a pies\n0. Salir'

def distancia_entre_sistemas():
    return f'Elija su conversion entre sistemas\n1. Pulgadas a centimetros\n2. Centimetros a pulgadas\n3. Pulgasda a metros\n4. Metros a pulgadas\n5. Millas a kilometros\n6. Kilometros a millas\n7. Millas nauticas a kilometros\n8. Kilometros a millas nauticas\n0. Salir'

def masa_si():
    return f'Elija que medida transformar a gramos:\n1. Kilogramos a gramos\n2. Hectogramos a gramos\n3. Decagramos a gramos\n4. Decigramos a gramos\n5. Centigramos a gramos\n6. Miligramos a gramos\n7. Toneladas a gramos\n0. Salir'

def masa_ingles():
    return f'Elija su conversion en el Sistema Ingles:\n1. Onzas a libras\n2. Libras a onzas\n3. Libras a stones\n4. Stones a libras\n5. Libras a toneldas cortas\n6.Toneladas cortas a libras\n0. Salir'

def masa_entre_sistemas():
    return f'Elija su conversion entre sistemas:\n1. Libras a kilogramos\n2. Kilogramos a libras\n3 Libras a gramos\n4. Gramos a libras\n5. Onzas a gramos\n6. Gramos a onzas\n7. Toneladas a toneladas cortas\n8. Toneladas cortas a toneladas\n0. Salir'

def tiempo():
    return f'Elija su conversion:\n1. Segundos a milisegundos\n2. Milisegundos a segundos\n3. Segundos a minutos\n4. Minutos a segundos\n5. Minutos a horas\n6. Horas a minutos\n7. Horas a segundos\n8. Segundos a horas\n9. Dias a horas\n10. Horas a dias\n0. Salir'

def temperatura():
    return f'Elija su conversion:\n1. Celsius a Fahrenheit\n2. Fahrenheit a Celsius\n3. Celsius a Kelvin\n4. Kelvin a Celsius\n5. Fahrenheit a Kelvin\n6. Kelvin a Fahrenheit\n0. Salir'