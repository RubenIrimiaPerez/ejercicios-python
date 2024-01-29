import random  # Importa la biblioteca random para generar números aleatorios

# Genera un número aleatorio entre 1 y 100 y lo asigna a la variable numero_aleatorio
numero_aleatorio = random.randint(1, 100)

# Muestra un mensaje para indicar al usuario que adivine el número
print("Adivina el número entre 1 y 100")

while True:  # Inicia un bucle que se ejecutará hasta que se rompa explícitamente

    # Solicita al usuario que ingrese un número y lo convierte a entero
    intento = int(input("Ingresa tu intento: "))

    # Verifica si el intento del usuario es correcto
    if intento == numero_aleatorio:
        print(f"¡Correcto! El número era {numero_aleatorio}")
        break  # Rompe el bucle ya que el usuario ha adivinado correctamente
    elif intento < numero_aleatorio:
        print("Intenta con un número más grande.")
    else:
        print("Intenta con un número más pequeño.")

# El programa llega a esta línea cuando el bucle ha sido roto (usuario ha adivinado correctamente)
