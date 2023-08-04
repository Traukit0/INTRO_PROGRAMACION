'''2. Construye un programa en Python que muestre cada código ASCII y su correspondiente carácter.
'''
for i in range (32, 127):
    print(f"Código {i} - caracter {chr(i)}")