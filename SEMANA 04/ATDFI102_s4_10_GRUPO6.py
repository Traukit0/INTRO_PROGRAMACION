'''En el Hotel “KdateINJaus”, a los pasajeros que ingresan se les asigna un código que corresponde a un número con
exactamente 16 cifras. El significado de estas cifras es el siguiente:
− Los 8 primeros dígitos corresponden a la fecha de ingreso (aaaammdd)
− Los siguientes 2 dígitos representan el número de noches de estadía.
− Los siguientes 3 dígitos corresponden al número de la habitación que ha ocupado.
− El siguiente dígito corresponde al tipo de servicios que incluye su estadía (1: solo desayuno, 2: todo incluido
en alimentación y otros: piscina, spa, tours, espectáculos).
− Los últimos 2 dígitos corresponden al número de veces que se ha alojado en el Hotel.
Para calcular el monto que debe cancelar el pasajero por la actual estadía, se deben aplicar los siguientes criterios
en conjunto:
− El precio base por la estadía de 1 noche es de $70.000.
− Las habitaciones con número par tienen vista al lago. Por este motivo su precio base aumenta en un 10%.
− Si el tipo de estadía es todo incluido, el precio base incrementa en un 15%.
− Si el período en el que ingresa el pasajero está en el rango de fechas desde el 20 de diciembre al 5 de marzo
(ambas fechas incluidas), o entre el 10 de septiembre al 20 de septiembre (ambas fechas incluidas), se
considera temporada alta. Si el período de ingreso es en cualquier otra fecha, se considera temporada
baja. En el caso de temporada alta, el precio base se aumenta en un 20% la estadía del pasajero.
− Si el pasajero ha alojado antes en el Hotel, entonces se le aplica un descuento de un 3% por cada vez sobre
el precio base.
Construye un programa en Python que reciba el código de un pasajero, y que imprima por pantalla la siguiente
información:
− Fecha de ingreso: (en formato dd-mm-aaaa)
− Noches de estadía:
− Número de habitación:
− Tipo de servicio:
− Número de veces que ha alojado:
− Valor de estadía completa''' 

codigo = input("Ingresa el código del pasajero: ")
fecha_ingreso = int(codigo[0:8])
mes_dia = int(codigo[4:8])
print(mes_dia)
noches_estadia = int(codigo[8:10])
habitacion = int(codigo[10:13])
servicios = int(codigo[13])
estadia_anterior = int(codigo[14:])
precio_dia = 70000
precio_base = precio_dia*noches_estadia
if habitacion%2==0:
    precio_con_habitacion = precio_base*.1
if servicios == 2:
    precio_con_servicios = precio_base*.15
# temporada alta: 20 de diciembre al 5 de marzo (ambas fechas incluidas),
# o entre el 10 de septiembre al 20 de septiembre (ambas fechas incluidas),
# se considera temporada alta.
if 0 < mes_dia <= 503 or 910 <= mes_dia <= 920 or 1220 <= mes_dia <= 1231:
    precio_temporada_alta = precio_base*.2
if estadia_anterior != 0:
   precio_descuento = precio_base*(estadia_anterior*.03)

precio_total = precio_base+precio_con_habitacion+precio_con_servicios+precio_temporada_alta-precio_descuento
print(f'''
Fecha de ingreso: {codigo[6:8]}-{codigo[4:6]}-{codigo[0:4]}
Noches de estadía: {noches_estadia}
Número de habitación: {habitacion}
Tipo de servicio: {servicios}
Número de veces que ha alojado: {estadia_anterior}
Valor de estadía completa: $ {round(precio_total, 0)}
      ''')