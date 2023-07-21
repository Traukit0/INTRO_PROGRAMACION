'''Construye un programa en Python que calcule y muestre por pantalla la media aritmética (o promedio simple) de
tres números ingresados por el usuario. El resultado deberá estar redondeado a 1 decimal.'''

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
num3 = float(input("Ingresa el tercer número: "))

prom = (num1+num2+num3)/3
print(f"El promedio es {round(prom, 1)}")