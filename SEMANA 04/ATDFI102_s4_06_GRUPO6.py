'''Construye un programa en Python que le pida al usuario el valor de x, y calcule la función “escalón”, definida como:'''

num = float(input("Ingresa X: "))
if num <= -1:
    print(f"escalon({round(num, 1)}) = 0")
elif num > -1 and num < 1:
    calc = (num+1)/2
    print(f"escalon({round(num, 1)}) = {calc}")
elif num >= 1:
    print(f"escalon({round(num, 1)}) = 1")