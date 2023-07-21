'''Construye un programa en Python que le permita a un alumno de una asignatura conocer su Nota de
Presentación a Examen (NPE) y la nota mínima que necesita en el examen para aprobarla.'''

# Combinar los inputs
sol = [float(input(f"Ingresa nota solemne {i+1}: ")) for i in range(3)]
con = [float(input(f"Ingresa nota control {i+1}: ")) for i in range(3)]

# Diferentes ponderaciones como lista
weight_solemn = [0.2, 0.25, 0.3]
weight_control = 0.25

# Calcular npe (Nota Presentación a Examen)
npe = sum(sol[i] * weight_solemn[i] for i in range(3)) + (sum(con) / 3) * weight_control

# Calcular ne (Nota Examen)
ne = (4 - npe * 0.7) / 0.3

# Imprimir resultados
print(f"La nota de presentación a examen es: {round(npe, 1)}")

if npe >= 5.0:
    print(f"No va a examen. Nota final es {npe}")
elif 1.0 <= npe <= 4.9:
    print("Va a examen")
    print(f"La nota mínima que debe obtener en el examen es: {round(ne, 1)}")
