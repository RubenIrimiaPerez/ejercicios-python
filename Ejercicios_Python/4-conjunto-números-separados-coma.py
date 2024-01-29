# Obtener la entrada del usuario
entrada_usuario = input("Ingrese un conjunto de números separados por coma: ")

# Dividir la entrada en una lista usando la coma como delimitador
numeros_str = entrada_usuario.split(',')
print(numeros_str)
# Convertir los números de cadena a enteros
numeros_enteros = [int(numero) for numero in numeros_str]

# Imprimir la lista resultante
print("Lista de números:", numeros_enteros)