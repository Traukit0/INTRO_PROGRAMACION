'''Construye un programa en Python que reciba desde el usuario una cantidad de dinero mayor a 0 expresada en
pesos chilenos, e indique cuántas y cuáles monedas requiere para construir dicha cantidad. Considera monedas
de $500, $100, $50, $10, $5, $1'''

def contar_monedas(cantidad):
    monedas = [500, 100, 50, 10, 5, 1]
    cantidad_restante = cantidad
    resultado = {}

    for moneda in monedas:
        if cantidad_restante >= moneda:
            cantidad_monedas = cantidad_restante // moneda
            cantidad_restante %= moneda
            resultado[moneda] = cantidad_monedas

    return resultado

def imprimir_monedas(cantidad, conteo_monedas):
    print(f"Cantidad de monedas para ${cantidad}: ")
    for moneda, cantidad_monedas in conteo_monedas.items():
        print(f"{cantidad_monedas} moneda(s) de ${moneda}")

if __name__ == "__main__":
    while True:
        try:
            cantidad = int(input("Ingresa la cantidad de dinero en pesos chilenos (mayor a 0): "))
            if cantidad <= 0:
                raise ValueError
            break
        except ValueError:
            print("Error: Debes ingresar una cantidad válida mayor a 0.")

    conteo_monedas = contar_monedas(cantidad)
    imprimir_monedas(cantidad, conteo_monedas)
