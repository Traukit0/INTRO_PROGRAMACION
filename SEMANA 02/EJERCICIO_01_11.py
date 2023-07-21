'''Construye un programa en Python que calcule y muestre el sueldo neto de un trabajador, a partir de las horas
trabajadas y del pago por hora que le corresponde, ambos ingresados por el usuario. El sueldo base se calcula
como horas trabajadas por el pago por hora, a ese monto, le debes agregar un 25% por concepto de beneficios,
realizar un 10% de descuentos, y descontar un 5% de los beneficios por concepto de consignación. El resultado
debe estar aproximado al entero superior.'''

horas_trab = int(input("Ingresa las horas trabajadas: "))
valor_hora = int(input("Ingresa elv alor hora en $: "))

sueldo_base = horas_trab*valor_hora

sueldo = sueldo_base + sueldo_base*0.1

print(f"El sueldo neto mensual será de ${round(sueldo, 0)} pesos")