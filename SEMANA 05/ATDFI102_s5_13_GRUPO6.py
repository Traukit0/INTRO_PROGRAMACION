'''Construye un programa en Python que solicite dos números enteros, m y n (ambos mayores a 1) y, a partir de ellos,
“dibuje” el borde de un rectángulo de asteriscos de m asteriscos de ancho, por n asteriscos de alto.'''

m = int(input("Ingrese el ancho del rectángulo (m): "))
n = int(input("Ingrese la altura del rectángulo (n): "))

for i in range(n):
    if i == 0 or i == n - 1:
        print("*" * m)
    else:
        print("*" + " " * (m - 2) + "*")
