'''Construye un programa en Python que le pida al usuario una letra y detecte si es una vocal o si es una consonante
(la letra puede estar en mayúscula o en minúscula, pero no puede ser una vocal con tilde). Si lo ingresado no es una
letra, también debe indicarlo'''

letra = input("Ingresa una letra: ").lower()

vocales = ["a", "e", "i", "o", "u"]
consonantes = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'ñ', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

if letra in vocales:
    print("la letra es una vocal.")
elif letra in consonantes:
    print("La letra es una consonante")
else:
    print("El caracter ingresado no es una letra")