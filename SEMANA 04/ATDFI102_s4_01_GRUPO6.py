'''Construye un programa en Python que le pida al usuario un número del 2 al 10 y diga si es primo o compuesto (no
primo). Si el número está fuera del rango, también debe indicarlo.'''

num = int(input("Ingresa un nº del 2 al 10: "))

if num >= 2 and num <= 10:
    if num == 3 or num == 5 or num == 7:
        print("El número es primo.")
    else:
        print("EL número es compuesto.")
else:
    print("El número está fuera de rango")
