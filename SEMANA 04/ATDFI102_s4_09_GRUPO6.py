'''La política de cobro de la compañía telefónica “Llámame SA” cuando se realiza una llamada, se basa en el tiempo
en minutos que esta dura (si la llamada dura minutos y fracción, se redondea al entero inferior). De esta forma, los
primeros cinco minutos cuestan $100 cada uno, los siguientes tres, $80 cada uno, los siguientes dos minutos, $70
cada uno y, a partir del undécimo minuto, $50 cada minuto. Además, se carga un impuesto de un 3% cuando la
llamada se realiza un sábado o un domingo (no importando la jornada), pero si es un día hábil (de lunes a viernes),
se carga un impuesto de un 15% en jornada diurna y un impuesto de 10% en jornada vespertina.
Construye un programa en Python que reciba la duración de la llamada (en minutos), el día de la semana en el que
se realiza, y la jornada (si corresponde), e indique cuánto es el cobro por la duración, cuánto es el impuesto que se
aplicará, y el total que se deberá pagar. El impuesto deberá presentarse con un decimal, y el total, se debe redondear
al entero más cercano.'''

llamada = int(input("Ingresa la duración de la llamada (minutos): "))
print('''
Considera esta asignación para cada día: 
(1) Lunes
(2) Martes
(3) Miércoles
(4) Jueves
(5) Viernes
(6) Sabado
(7) Domingo
''')
dia = int(input("Indica el día de la llamada: "))

if llamada <= 5:
    valor = llamada * 100
elif llamada <= 8:
    valor = 500 + ((llamada-5)*80)
elif llamada <= 10:
    valor = 740 + ((llamada-8)*70)
else:
    valor = 880 + ((llamada-10)*50)
print("Valor", valor)
if dia == 6 or dia == 7:
    total = valor * 1.03
else:
    jornada = input("Jornada de la llamada (D) 7am-9pm (V) 9pm-7am: ")
    if jornada == "d" or jornada == "D":
        total = valor * 1.15
    elif jornada == "v" or jornada == "V":
        total = valor * 1.1

print(f"Cobro por minutos: ${valor}")
print(f"Impuesto: ${round(total-valor, 1)}")
print(f"Total: ${int(total)}")