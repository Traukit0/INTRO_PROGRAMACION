'''Construye un programa en Python que calcule y muestre por pantalla el área y el perímetro de un triángulo, cuyas
longitudes de sus lados son ingresados por el usuario (usa la fórmula de Herón). El resultado deberá estar
redondeado a 2 decimales'''

lado1 = float(input("Ingresa la longitud del primer lado: "))
lado2 = float(input("Ingresa la longitud del segundo lado: "))
lado3 = float(input("Ingresa la longitud del tercer lado: "))
s = (lado1+lado2+lado3)/2

area = (s*(s-lado1)*(s-lado2)*(s-lado3))**1/2

print(f"El área del triángulo es: {round(area, 2)} cm2")
print(f"El perímetro del triángulo es: {round(lado1+lado2+lado3, 2)} cm.")