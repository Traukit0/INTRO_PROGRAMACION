'''Construye un programa en Python que le pida al usuario 3 números enteros y los muestre en pantalla de menor a
mayor'''

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

lista_num = [num1, num2, num3]

lista_num.sort()

print(lista_num)