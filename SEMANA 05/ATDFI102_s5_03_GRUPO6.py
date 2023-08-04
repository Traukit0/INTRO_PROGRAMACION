'''Construye un programa en Python que le permita al usuario adivinar un número secreto entre 0 y 300 (que tú,
programador, defines). Si no acierta, el programa debe decir por pantalla si debe ingresar un número mayor o menor
para acercarse al número meta. Cuando el usuario acierte, el programa debe además indicar en cuántos intentos
logró adivinar el usuario'''

import random

acierto = random.randint(0, 300)

contador = 0
num = -1
while num != acierto:
    num = int(input("Ingresa un número entre 0 y 300: "))
    if num > acierto:
        print("Ingresa un número menor")
    elif num < acierto:
        print("Ingresa un número mayor")
    contador += 1
print(f"Acertaste en {contador} intento(s)!")