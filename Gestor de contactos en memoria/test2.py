# -*- coding: utf-8 -*-
import os
import time

def clear_screen():
    """Limpia la pantalla de la terminal."""
    # Para sistemas Unix/Linux/macOS
    if os.name == 'posix':
        _ = os.system('clear')
    # Para sistemas Windows
    else:
        _ = os.system('cls')

def display_menu(title, options):
    """
    Muestra un menú en la terminal y devuelve la opción seleccionada por el usuario.

    Args:
        title (str): El título del menú.
        options (list): Una lista de cadenas, donde cada cadena es una opción del menú.

    Returns:
        int: El número de la opción seleccionada por el usuario.
    """
    while True:
        clear_screen()
        print("=" * 40)
        print(f"{title.center(40)}")
        print("=" * 40)
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        print("-" * 40)
        print("0. Salir")
        print("=" * 40)

        try:
            choice = int(input("Por favor, selecciona una opción: "))
            if 0 <= choice <= len(options):
                return choice
            else:
                print("\nOpción inválida. Por favor, ingresa un número de la lista.")
                time.sleep(1.5) # Espera un momento para que el usuario vea el mensaje
        except ValueError:
            print("\nEntrada inválida. Por favor, ingresa un número.")
            time.sleep(1.5) # Espera un momento para que el usuario vea el mensaje

def main_menu():
    """
    Función principal que ejecuta el menú.
    """
    menu_options = [
        "Ver estado del sistema",
        "Gestionar archivos",
        "Configuración de red",
        "Acerca de"
    ]

    while True:
        choice = display_menu("MENÚ PRINCIPAL DE LA APLICACIÓN", menu_options)

        if choice == 1:
            clear_screen()
            print("Has seleccionado: Ver estado del sistema")
            print("\nSimulando la obtención del estado del sistema...")
            print("CPU: 75% | RAM: 60% | Disco: 40% usado")
            input("\nPresiona Enter para continuar...")
        elif choice == 2:
            clear_screen()
            print("Has seleccionado: Gestionar archivos")
            print("\nSimulando la gestión de archivos...")
            print("1. Listar archivos")
            print("2. Crear nuevo archivo")
            print("3. Eliminar archivo")
            sub_choice = input("Selecciona una sub-opción (1-3): ")
            if sub_choice == '1':
                print("Listando archivos: archivo1.txt, documento.pdf, imagen.jpg")
            elif sub_choice == '2':
                print("Creando nuevo archivo...")
            elif sub_choice == '3':
                print("Eliminando archivo...")
            else:
                print("Sub-opción inválida.")
            input("\nPresiona Enter para continuar...")
        elif choice == 3:
            clear_screen()
            print("Has seleccionado: Configuración de red")
            print("\nSimulando la configuración de red...")
            print("IP: 192.168.1.100 | Estado: Conectado")
            input("\nPresiona Enter para continuar...")
        elif choice == 4:
            clear_screen()
            print("Has seleccionado: Acerca de")
            print("\nEsta es una aplicación de demostración de menú en Python.")
            print("Versión: 1.0")
            input("\nPresiona Enter para continuar...")
        elif choice == 0:
            clear_screen()
            print("Saliendo del programa. ¡Hasta pronto!")
            break

if __name__ == "__main__":
    main_menu()
