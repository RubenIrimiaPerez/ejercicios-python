def obtener_extension(nombre_archivito):
    partes = nombre_archivito.split('.')
    if len(partes) > 1:
        extensioncita = partes[-1]
        return extensioncita
    else:
        print("No posee extension")


nombre_archivito = input("¿Cual es el nombre del archivo?")
extension = obtener_extension(nombre_archivito)
print(f'La extension se llama {extension} del archivo {nombre_archivito} ')