'''Construye un programa en Python que le pida al usuario un número del 1 al 7 y diga el día de la semana que le
corresponde. Si el número está fuera del rango, también debe indicarlo.'''

dia = int(input("Ingresa un nº del 1 al 7: "))

if dia >= 1 and dia <= 7:
    if dia == 1:
        print("LUNES")
    elif dia == 2:
        print("MARTES")
    elif dia == 3:
        print("MIERCOLES")
    elif dia == 4:
        print("JUEVES")
    elif dia == 5:
        print("VIERNES")
    elif dia == 6:
        print("SABADO")
    elif dia == 7:
        print("DOMINGO")
else:
    print("El número está fuera de rango.")