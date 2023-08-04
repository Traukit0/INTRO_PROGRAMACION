'''Construye un programa en Python que muestre la tabla de multiplicar de un valor n ingresado por el usuario,
considerando los resultados desde el 1 al 15'''

num = int(input("Ingresa el número: "))
print("""
Tabla de multiplicar
--------------------
""")
for i in range (1, 16):
    print(f"{num} * {i} = {num*i}")