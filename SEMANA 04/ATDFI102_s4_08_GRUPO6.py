'''En Isla Paraíso (una nueva nación - ficticia - de América), está luchando por tener más recursos. Para esto está
iniciando un ambicioso plan para convertirse en un “paraíso fiscal”. El plan se basa en un sistema de impuestos
claro, simple y barato.El plan se pondrá en práctica el segundo semestre del próximo año. Sin embargo, el esquema de cobro de los
impuestos de primera y segunda categoría ya está definido y las autoridades de la Isla están encargando el desarrollo
de la plataforma informática que apoyará el proceso.
La complejidad del sistema se ha reducido lo más posible y el esquema es el siguiente: cuando a una persona se le
paga un salario (primera categoría) o un honorario (segunda categoría), el emisor del pago debe descontar 5% del
monto y enviarlo a Tesorería General Paradisíaca como Prepago de Impuestos de esta persona. En abril, cada
ciudadano debe indicar el monto total de su Renta Bruta (es decir, sin descuentos) que se le pagaron durante el año
fiscal anterior. A este monto se le descuenta el 40% por concepto de Gastos Presuntos para Ejercer la Actividad. El
monto resultante se conocerá como Renta Afecta. Si la Renta Afecta de un ciudadano es menor a $100.000, queda
exento de pagar impuestos y Tesorería General Pascuense debe devolverle los Prepagos de Impuestos que se le
descontaron. Ahora, si la Renta Afecta es igual a o sobrepasa los $100.000, el ciudadano debe pagar 10% de
impuestos, monto que se conocerá como Impuesto Nominal. Si el Impuesto Nominal es menor que los Prepagos de
Impuestos descontados al ciudadano el año anterior, Tesorería General Pascuense debe devolver la diferencia; pero
si el Impuesto Nominal es mayor que los prepagos realizados, el ciudadano debe pagar la diferencia que se conocerá
como Impuesto Efectivo.
Construye un programa en Python que le pida al usuario su renta bruta anual, e indique si le corresponde
“Devolución” o “Pago” de impuestos, y cuál es el monto en cada caso. Los cálculos que posean decimales se deben
aproximar al entero más cercano.'''

renta_bruta = int(input("Ingresa la Renta Bruta Anual $: "))
retencion_5 = renta_bruta*0.05
renta_afecta = renta_bruta*0.60
if renta_afecta < 100000:
    print(f"Devolucion por: ${int(retencion_5)}")
elif renta_afecta >= 100000:
    impuesto_nominal = renta_afecta*0.1
    if impuesto_nominal < retencion_5:
        print(f"Devolucion por ${int(retencion_5-impuesto_nominal)}")
    else:
        impuesto_efectivo = impuesto_nominal - retencion_5
        print(f"Pago por ${int(impuesto_efectivo)}")
