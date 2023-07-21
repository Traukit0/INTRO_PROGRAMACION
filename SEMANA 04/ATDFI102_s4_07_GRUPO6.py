'''En una Universidad el reglamento de evaluaciones consiste en lo siguiente: todas las asignaturas deben tener 3
pruebas y un examen. Después de las tres pruebas, los alumnos con promedio menor que 2,8 reprueban y los con
promedio mayor o igual a 5,2 aprueban. El resto va al examen, instancia en que deben obtener por lo menos un 4,0
para aprobar. Sin embargo, los alumnos que obtienen menos de un 2,2 en las dos primeras pruebas están automáticamente reprobados;
A su vez, los que obtienen más de un 6,4 en las dos primeras pruebas están
automáticamente aprobados. En ambos casos, no deben rendir la tercera prueba.
Construye un programa en Python que refleje este sistema de evaluaciones a partir de las evaluaciones que ha
rendido, y le diga si está aprobado o reprobado.'''

p1 = float(input("Nota Prueba 1: "))
p2 = float(input("Nota Prueba 2: "))

if (p1 + p2)/2 < 2.2:
    print("Reprobado")
elif (p1 + p2)/2 > 6.4:
    print("Aprobado")
else:
    p3 = float(input("Nota Prueba 3: "))
    if (p1+p2+p3)/3 < 2.8:
        print("Reprobado")
    elif (p1+p2+p3)/3 > 5.2:
        print("Aprobado")
    else:
        nex = float(input("Nota Examen: "))
        if nex >= 4.0:
            print("Aprobado")
        else:
            print("Reprobado")  