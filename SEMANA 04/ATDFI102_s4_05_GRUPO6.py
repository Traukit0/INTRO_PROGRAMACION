'''Construye un programa en Python que le pida al usuario el número de horas trabajadas, y determine el monto a
pagar a su empleado considerando el incentivo que le corresponde de acuerdo con la información de la siguiente
tabla:
El programa debe ser capaz de mostrar un mensaje de error si las horas no están en el rango especificado. Además,
considera un sueldo base de $500.000, y se debe aproximar el resultado al entero más cercano.'''

horas = int(input("Ingrese la cantidad de horas trabajadas: "))
base = 500000
if horas >= 25 and horas <= 30:
    sueldo = base * 1.05
    print(f"El monto a pagar es: ${int(sueldo)}")
elif horas >= 31 and horas <= 35:
    sueldo = base * 1.1
    print(f"El monto a pagar es: ${int(sueldo)}")
elif horas >= 36 and horas <= 40:
    sueldo = base * 1.15
    print(f"El monto a pagar es: ${int(sueldo)}")
elif horas >= 41 and horas <= 50:
    sueldo = base * 1.25
    print(f"El monto a pagar es: ${int(sueldo)}")
else:
    print("Error: cantidad de horas inválidas")