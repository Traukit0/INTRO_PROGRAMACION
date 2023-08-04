'''.Construye un programa en Python que permita calcular el VAN de un proyecto en cada período hasta que sea
positivo. Para esto, el usuario deberá ingresar el monto de la inversión inicial (llamado I0 en la fórmula mostrada),
la tasa de interés (llamada r en la fórmula mostrada), y cada flujo neto (llamado F1, F2, …, Fn en la fórmula mostrada).
Luego del ingreso de un flujo el programa deberá mostrar el VAN acumulado hasta ese período.'''

inv = int(input("Inversión inicial: "))*-1
tasa = int(input("Tasa en %: "))
van = 0
mes = 1
while van <= 0:
    flujo = int(input(f"Flujo mes {mes}: "))
    inv = flujo/(1+(tasa/100))**mes + inv
    van = inv
    mes += 1
    print(f"VAN = {round(van, 2)}")
