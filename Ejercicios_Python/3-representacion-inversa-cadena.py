# Solicita al usuario que ingrese una cadena de caracteres
cadena_ingresada = input("Ingresa una cadena de caracteres: ")

# Obtiene la representación inversa utilizando slicing
cadena_inversa = cadena_ingresada[::-1] # que vaya cogiendo de uno en uno al reves

# Muestra la representación inversa
print(f"La representación inversa de '{cadena_ingresada}' es: '{cadena_inversa}'")



#otro metodo

cadena = input("Introduce una cadena")

for i in range(len(cadena)-1, -1, -1):
    print(cadena[i])
