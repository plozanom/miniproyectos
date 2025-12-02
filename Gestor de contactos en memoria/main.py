"""Mini-Proyecto: Gestor de Contactos en Memoria:
 - Usa una lista de diccionarios para almacenar contactos (cada diccionario representa un contacto con nombre, telefono, email ).
 - Implementa un menú con opciones para:
   -- Agregar un nuevo contacto.
   -- Ver todos los contactos.
   -- Buscar un contacto por nombre.
   -- Eliminar un contacto por nombre.
 - Los datos se perderán al cerrar el programa (es "en memoria").
 - Usa bucles, condicionales, listas y diccionarios."""

from crud import *
from utils import *

def main_menu():

   while True:
      
      menu_options = ["Crear nuevo contacto", "Ver todos los contactos", "Buscar un contacto", "Actualizar un contacto", "Eliminar un contacto"]

      display_menu('GESTOR DE CONTACTOS', menu_options)

      opcion = str(input("Elige una opcion: "))

      if opcion == '1':
         clear_screen()
         print("Usted ha elegido Crear un nuevo contacto")
         nombre = str(input("Por favor ingrese el nombre del nuevo contacto: "))
         telefono = str(input("Ingrese el numero de telefono: "))
         email = str(input("Por ultimo, ingrese el correo electronico: "))
         print(create(nombre, telefono, email))
         input("\nPresiona Enter para continuar...")
      elif opcion == '2':
         clear_screen()
         read_all()
         input("\nPresiona Enter para continuar...")
      elif opcion == '3':
         nombre = str(input("Ingrese el nombre del contacto a hallar: "))
         print(read(nombre))
         input("\nPresiona Enter para continuar...")
      elif opcion == '4':
         clear_screen()
         nombre = str(input("Ingrese el nombre del contacto a actualizar: "))
         parametro = str(input("Ingrese el parametro a cambiar: "))
         cambio = str(input("Ingrese el cambio que se le hará al parametro: "))
         print(update(nombre, parametro, cambio))
         input("\nPresiona Enter para continuar...")
      elif opcion == '5':
         clear_screen()
         nombre = str(input("Ingrese el nombre del contacto a borrar: "))
         print(delete(nombre))
         input("\nPresiona Enter para continuar...")
      elif opcion == '0':
         clear_screen()
         print("Usted ha elegido cerrar el programa\nQue tenga un buen día")
         break
      else:
         clear_screen()
         print(f'{opcion} no es una opción dentro de la lista.\nPor favor ingrese una opción valida')
         input("\nPresiona Enter para continuar...")

if __name__ == "__main__":
    main_menu()