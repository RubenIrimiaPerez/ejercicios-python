import hashlib
import json

def obtener_hash(texto):
    # Función para obtener el hash de un texto usando SHA-256
    return hashlib.sha256(texto.encode()).hexdigest()

def registrar_usuario():
    # Función para registrar un nuevo usuario
    usuario = input("Ingrese un nombre de usuario: ")

    # Verificar si el usuario ya existe
    try:
        with open('usuarios.json', 'r') as archivo_usuarios:
            usuarios = json.load(archivo_usuarios)
            if usuario in usuarios:
                print(f"El usuario '{usuario}' ya existe.")
                return
    except FileNotFoundError:
        usuarios = {}

    # Solicitar la contraseña y realizar la doble comprobación
    while True:
        contraseña = input("Ingrese una contraseña: ")
        confirmar_contraseña = input("Confirme la contraseña: ")

        if contraseña == confirmar_contraseña:
            # Hash de la contraseña
            contraseña_encriptada = obtener_hash(contraseña)

            # Guardar en el diccionario y escribir en el archivo
            usuarios[usuario] = contraseña_encriptada
            with open('usuarios.json', 'w') as archivo_usuarios:
                json.dump(usuarios, archivo_usuarios)
            print(f"Usuario '{usuario}' registrado exitosamente.")
            break
        else:
            print("Las contraseñas no coinciden. Intenta de nuevo.")

def iniciar_sesion():
    # Función para iniciar sesión
    usuario = input("Ingrese su nombre de usuario: ")

    # Verificar si el usuario existe
    try:
        with open('usuarios.json', 'r') as archivo_usuarios:
            usuarios = json.load(archivo_usuarios)
            if usuario not in usuarios:
                print(f"El usuario '{usuario}' no existe.")
                return

            # Solicitar la contraseña
            contraseña = input("Ingrese su contraseña: ")
            # Verificar que la contraseña coincida con el hash almacenado
            if obtener_hash(contraseña) == usuarios[usuario]:
                print(f"Bienvenido, {usuario}!")
            else:
                print("Contraseña incorrecta.")
    except FileNotFoundError:
        print("No hay usuarios registrados.")

def main():
    while True:
        print("\n1. Registrar usuario\n2. Iniciar sesión\n3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            registrar_usuario()
        elif opcion == '2':
            iniciar_sesion()
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()
