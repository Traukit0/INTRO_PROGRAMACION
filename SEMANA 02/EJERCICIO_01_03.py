'''Construye un programa en Python que calcule y muestre por pantalla el área de un
trapecio, cuyas bases y altura son ingresados por el usuario. El resultado deberá
estar redondeado a 3 decimales'''

print("""
    ---CALCULADORA AREA DE TRAPECIO---
          ------------------
          INGRESE LOS DATOS
    """)

base_menor = float(input("Ingrese la base menor: "))
altura = float(input("Ingrese la altura: "))
base_mayor = float(input("Ingrese la base mayor: "))

area = ((base_mayor+base_menor)/2)*altura

print(f"El área del trapecio es: {round(area, 2)}")