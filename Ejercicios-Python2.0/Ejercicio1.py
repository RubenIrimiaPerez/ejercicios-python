#Leer el contenido de una carpeta diferenciando entre ficheros y directorios.

import os


def archivo_directorio(ruta_carpeta):
    try:
        print(f"Contenido de la carpeta : {ruta_carpeta}")

        #Obtener la lista de archivos y directorios de la carpeta
        contenido_ruta = os.listdir(ruta_carpeta)

        for elemento in contenido_ruta:
            ruta_completa = os.path.join(ruta_carpeta, elemento)

            # Diferenciar entre archivos y directorios
            if os.path.isfile(ruta_completa):
                print(f"Archivo: {elemento}")
            elif os.path.isdir(ruta_completa):
                print(f"Directorio: {elemento}")
            else:
                print(f"Otro tipo de elemento: {elemento}")

    except FileNotFoundError:
        print(f"La carpeta {ruta_carpeta} no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")


# Preguntar la ruta al usuario
ruta_usuario = input("Ingrese la ruta de la carpeta: ")

archivo_directorio(ruta_usuario)

