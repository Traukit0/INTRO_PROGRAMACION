'''Construye un programa en Python que permita evaluar un polinomio de grado n ingresado por el usuario. Para
esto, el usuario debe ingresar el valor en el que desea evaluar, el grado del polinomio y cada uno de sus coeficientes.
(Recuerda que el grado de un polinomio corresponde a la mayor potencia que posee x).'''

grado = int(input("Grado del polinomio: "))+1
valor = int(input("Valor para evaluar el polinomio: "))
grados = []
n = 0
for i in range(grado):
    grados.append(n)
    n += 1
grados.reverse()
resultado = 0
for t in grados:
    coef = int(input(f"Coeficiente para x^{t}: "))
    resultado += coef*(valor**t)

print(f"Polinomio evaluado en {valor}: {round(float(resultado), 1)}")
