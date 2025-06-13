#Trabajando con archivos de texto en python
#1, Abrir el archivo en modo creación
#Ejemplo, solicitando el nombre del archivo al usuario
ruta=input("Nombre del archivo: ")
archi1=open(ruta,"a")
#archi1.write(primera linea\n)
archi1.write("Segunda Linea \n")
archi1.write("Tercera Linea \n")