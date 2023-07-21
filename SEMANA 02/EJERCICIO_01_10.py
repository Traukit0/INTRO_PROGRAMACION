'''Construye un programa en Python que permita transformar a segundos una cantidad de días, horas, minutos y
segundos, que ingrese el usuario.'''

dias = int(input("Ingresa la cantidad de días: "))
horas = int(input("Ingresa la cantidad de horas: "))
mins = int(input("Ingresa la cantidad de minutos: "))
seg = int(input("Ingresa la cantidad de segundos: "))

print(f"La cantidad equivalente es {dias*86400+horas*3600+mins*60+seg} segundos")