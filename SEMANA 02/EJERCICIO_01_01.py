'''
Construye un programa en Python que calcule y muestre por pantalla la raíz cúbica
de un número entero ingresado por el usuario. El resultado deberá estar redondeado
a 2 decimales'''
num_1 = float(input("Ingresa un número: "))
process = num_1**(1/3)
print(f"La raíz cúbica de {num_1} es: {round(process, 2)}")