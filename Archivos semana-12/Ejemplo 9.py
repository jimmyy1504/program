#Eliminar lineas del archivo 
#Abrir el archivo y leer las lineas
with open("datos.txt", "r", encoding="uft-8") as archivo:
    lineas = archivo.readlines()
    
#Filtrar las lineas que no contengan "Segunda Linea"
lineas_filtradas = [linea for linea in lineas if linea.strip() != "Segunda Linea"]

#Sobreescribir el archivo con las lineas filtradas 
with open("datos.txt", "w", encoding="utf-8") as archivo:
    archivo.writelines(lineas_filtradas)    
    