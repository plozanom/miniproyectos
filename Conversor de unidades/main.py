"""Mini-Proyecto: Convertidor de Unidades Interactivo:
 - Presenta al usuario un menú de conversiones posibles (ej: Celsius a Fahrenheit, Metros a Pies, Kilogramos a
 Libras).
 - Pide al usuario que elija una conversión.
 - Pide al usuario el valor a convertir.
 - Realiza la conversión usando funciones separadas para cada tipo de conversión.
 - Imprime el resultado formateado.
 - Usa bucles y condicionales para el menú y la selección."""

import menu
import distancia
import masa
import tiempo
import temperatura

def main():

    while True:
        print(menu.principal())
        eleccion = str(input('>>>> '))


        if eleccion == '1':
            print(menu.eleccion_sistema())
            eleccion = str(input('>>>> '))

            if eleccion == '1':
                print(menu.distancia_si())
                eleccion = str(input('>>>> '))

                if eleccion == '1':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.Km_a_m(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '2':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.Hm_a_m(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '3':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.Dm_a_m(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '4':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.dm_a_m(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '5':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.cm_a_m(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '6':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.mm_a_m(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '7':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.um_a_m(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '8':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.nm_a_m(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '0':
                    print('Saliendo...')
                    break
                else:
                    print('Elija una opcion correcta')

            elif eleccion == '2':
                print(menu.distancia_ingles())
                eleccion = str(input('>>>> '))

                if eleccion == '1':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.in_a_ft(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '2':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.ft_a_yd(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '3':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.yd_a_mi(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '4':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.nmi_a_ft(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '0':
                    print('Saliendo...')
                    break
                else:
                    print('Elija una opcion correcta')

            elif eleccion == '3':
                print(menu.distancia_entre_sistemas())
                eleccion = str(input('>>>> '))

                if eleccion == '1':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.in_a_cm(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '2':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.cm_a_in(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '3':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.in_a_m(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '4':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.m_a_in(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '5':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.mi_a_km(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '6':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.km_a_mi(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '7':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.nmi_a_km(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '8':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(distancia.km_a_nmi(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '0':
                    print('Saliendo...')
                    break
                else:
                    print('Elija una opcion correcta')

            elif eleccion == '0':
                print('Saliendo...')
                break
            else:
                print('Elija una opcion correcta')

        elif eleccion == '2':
            print(menu.eleccion_sistema())
            eleccion = str(input('>>>> '))

            if eleccion == '1':
                print(menu.masa_si())
                eleccion = str(input('>>>> '))

                if eleccion == '1':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.kg_a_g(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '2':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.hg_a_g(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '3':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.dag_a_g(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '4':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.dg_a_g(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '5':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.cg_a_g(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '6':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.mg_a_g(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '7':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.ton_a_g(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '0':
                    print('Saliendo...')
                    break
                else:
                    print('Elija una opcion correcta')

            elif eleccion == '2':
                print(menu.masa_ingles())
                eleccion = str(input('>>>> '))

                if eleccion == '1':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.oz_a_lb(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '2':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.lb_a_oz(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '3':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.lb_a_st(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '4':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.st_a_lb(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '5':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.lb_a_short_ton(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '6':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.short_ton_a_lb(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '0':
                    print('Saliendo...')
                    break
                else:
                    print('Elija una opcion correcta')

            elif eleccion == '3':
                print(menu.masa_entre_sistemas())
                eleccion = str(input('>>>> '))

                if eleccion == '1':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.lb_a_kg(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '2':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.kg_a_lb(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '3':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.lb_a_g(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '4':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.g_a_lb(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '5':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.oz_a_g(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '6':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.g_a_oz(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '7':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.ton_a_short_ton(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '8':
                    valor = float(input('Ingrese el valor a convertir: '))
                    print(masa.short_ton_a_ton(valor))
                    input("Presione 'ENTER' para volver al menu principal...")
                elif eleccion == '0':
                    print('Saliendo...')
                    break
                else:
                    print('Elija una opcion correcta')

            elif eleccion == '0':
                print('Saliendo...')
                break
            else:
                print('Elija una opcion correcta')

        elif eleccion == '3':
            print(menu.tiempo())
            eleccion = str(input('>>>> '))

            if eleccion == '1':
                valor = float(input('Ingrese el valor a convertir: '))
                print(tiempo.s_a_ms(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '2':
                valor = float(input('Ingrese el valor a convertir: '))
                print(tiempo.ms_a_s(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '3':
                valor = float(input('Ingrese el valor a convertir: '))
                print(tiempo.s_a_min(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '4':
                valor = float(input('Ingrese el valor a convertir: '))
                print(tiempo.min_a_s(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '5':
                valor = float(input('Ingrese el valor a convertir: '))
                print(tiempo.min_a_h(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '6':
                valor = float(input('Ingrese el valor a convertir: '))
                print(tiempo.h_a_min(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '7':
                valor = float(input('Ingrese el valor a convertir: '))
                print(tiempo.h_a_s(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '8':
                valor = float(input('Ingrese el valor a convertir: '))
                print(tiempo.s_a_h(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '9':
                valor = float(input('Ingrese el valor a convertir: '))
                print(tiempo.dia_a_h(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '10':
                valor = float(input('Ingrese el valor a convertir: '))
                print(tiempo.h_a_dia(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '0':
                print('Saliendo...')
                break
            else:
                print('Elija una opcion correcta')

        elif eleccion == '4':
            print(menu.temperatura())
            eleccion = str(input('>>>> '))

            if eleccion == '1':
                valor = float(input('Ingrese el valor a convertir: '))
                print(temperatura.celsius_a_fahrenheit(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '2':
                valor = float(input('Ingrese el valor a convertir: '))
                print(temperatura.fahrenheit_a_celsius(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '3':
                valor = float(input('Ingrese el valor a convertir: '))
                print(temperatura.celsius_a_kelvin(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '4':
                valor = float(input('Ingrese el valor a convertir: '))
                print(temperatura.kelvin_a_celsius(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '5':
                valor = float(input('Ingrese el valor a convertir: '))
                print(temperatura.fahrenheit_a_kelvin(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '6':
                valor = float(input('Ingrese el valor a convertir: '))
                print(temperatura.kelvin_a_fahrenheit(valor))
                input("Presione 'ENTER' para volver al menu principal...")
            elif eleccion == '0':
                print('Saliendo...')
                break
            else:
                print('Elija una opcion correcta')

        elif eleccion == '0':
            print('Saliendo...')
            break

        else:
            print('Elija una opcion correcta')

if __name__== '__main__':
    main()