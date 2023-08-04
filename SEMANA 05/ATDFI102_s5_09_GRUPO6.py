'''Construye un programa en Python que indique si un número entero es primo o compuesto, a partir de un número
mayor 1 ingresado por el usuario.'''

num = int(input("Ingresa un número: "))
n=1

if not num%2==0 and not num%3==0:
    print(f"El número {num} es primo")
else:
    print(f"El número {num} es compuesto")