'''Construye un programa en Python que calcule la raíz n-esima de un número entero ingresado por el usuario. El
índice de la raíz (n), también lo debe ingresar el usuario. El resultado debe mostrarse con 3 decimales y no puedes
utilizar el operador **.'''

from math import exp, log

num = int(input("Ingresa un número: "))
n = int(input("Ingresa el valor de n: "))

print(f"Raíz {n} de {num} es {round(exp(log(num)/n), 2)}")