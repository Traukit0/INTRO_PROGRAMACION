'''Construye un programa en Python que calcule el logaritmo en base x, de un número. Tanto la base como el número
lo debe ingresar el usuario. El resultado debe tener 3 decimales de precisión (Recuerda que calcular un logaritmo
en base x de un número, corresponde a encontrar el exponente al que debes elevar x para conseguir el número)'''

import math 

num = int(input("Ingresa un número: "))
base = int(input("Ingresa la base del logaritmo: "))

print(f"Log (base {base}) de {num}: {round(math.log(num, base), 3)}")