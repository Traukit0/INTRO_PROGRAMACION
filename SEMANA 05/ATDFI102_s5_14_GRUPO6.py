'''Construye un programa en Python que permita administrar las ventas de una fábrica de mermeladas. El detalle
de sus posibles ventas es:
Tipo de Envase Capacidad (Kg) Precio ($)
BOLSA ¼ 300
BOLSA ½ 500
FRASCO 1 1200
FRASCO 2 2400
Se necesita construir el siguiente menú (y los cálculos asociados):A. Ingresar venta
B. Kilos vendidos
C. Frascos vendidos
D. Ingreso por bolsas
E. Salir
Para la opción A, deberás construir un submenú, que permita mostrar las combinaciones de bolsas y frascos de
mermeladas que se pueden comprar.'''

opcion_1 = ""
bolsa_025 = 0
bolsa_05 = 0
frasco_1 = 0
frasco_2 = 0

while opcion_1 != "e" and opcion_1 != "E":
    print('''
        MENU
       ======
    A. Ingresar venta
    B. Kilos vendidos
    C. Frascos vendidos
    D. Ingreso por bolsas
    E. Salir
    ''')
    opcion_1 = input("Ingresa una opción: ")

    if opcion_1 == "A" or opcion_1 == "a":
        opcion_2 = ""
        while opcion_2 != "5":
            print('''
            VENTAS
            ======
        1. Bolsa de 0.25 kg. ($300)
        2. Bolsa de 0.5 kg. ($500)
        3. Frasco de 1 kg. ($1200)
        4. Frasco de 2 kg. ($2400)
        5. Salir
        ''')
            opcion_2 = input("Ingresa una opción: ")

            if opcion_2 == "1":
                cantidad = float(input("Ingresa una cantidad: "))
                bolsa_025 += 300 * cantidad
            elif opcion_2 == "2":
                cantidad = float(input("Ingresa una cantidad: "))
                bolsa_05 += 500 * cantidad
            elif opcion_2 == "3":
                cantidad = float(input("Ingresa una cantidad: "))
                frasco_1 += 1200 * cantidad
            elif opcion_2 == "4":
                cantidad = float(input("Ingresa una cantidad: "))
                frasco_2 += 2400 * cantidad

    elif opcion_1 == "B" or opcion_1 == "b":
        kilos_vendidos = (bolsa_025 * 0.25) + (bolsa_05 * 0.5) + (frasco_1 * 1) + (frasco_2 * 2)
        print("Kilos vendidos:", kilos_vendidos)

    elif opcion_1 == "C" or opcion_1 == "c":
        frascos_vendidos = bolsa_025/0.25 + bolsa_05/0.5 + frasco_1/1 + frasco_2/2
        print("Frascos vendidos:", frascos_vendidos)

    elif opcion_1 == "D" or opcion_1 == "d":
        ingreso_bolsas = bolsa_025 + bolsa_05
        print("Ingreso por bolsas:", ingreso_bolsas)

print("Hasta luego!")
