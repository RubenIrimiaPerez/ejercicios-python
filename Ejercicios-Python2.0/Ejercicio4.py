# Modificar el contenido de un fichero.

fichero_craedo = open("fichero-craedo.txt","a")
fichero_craedo.write("\n holaaaaaaa he añadido una lineas mas")

fichero_craedo = open("fichero-craedo.txt","r")
print(fichero_craedo.read())


