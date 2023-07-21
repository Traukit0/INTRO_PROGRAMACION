'''Construye un programa en Python que le pida al usuario un carácter cualquiera, y le muestre por pantalla el
código ASCII que le corresponde a ese carácter.'''

car = input("Ingrese un caracter: ")
ascii_code = ord(car)

print("El codigo ASCII de {} es {}".format(car, ascii_code))
