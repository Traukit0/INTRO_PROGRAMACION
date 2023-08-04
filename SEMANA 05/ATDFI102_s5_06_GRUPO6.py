'''Construye un programa en Python que encuentre y muestre el valor mayor de una secuencia de n valores
ingresados por el usuario. El valor de n también lo debe ingresar el usuario.'''

num = int(input("Ingresa la cantidad de números: "))
n=0
numeros = []
for n in range(num):
    numero = int(input(f"Ingresa el número {n+1}:"))
    numeros.append(numero)
print(f"El valor mayor es: {max(numeros)}")
