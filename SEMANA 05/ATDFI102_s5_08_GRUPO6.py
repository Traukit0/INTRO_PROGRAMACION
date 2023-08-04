'''Construye un programa en Python que determine y muestre los divisores que posee un número entero mayor a 1
ingresado por el usuario'''

num = int(input("Ingresa un número: "))
n=1
for i in range(num):
    if num%(i+1)==0:
        print(f"Divisor {n}: {i+1}")