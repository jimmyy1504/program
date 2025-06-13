#Solicitar datos al user
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = input("Ingresa tu edad: ")
salario = input("Ingresa tu salario: ")
 
 #Formar los datos en una linea
linea: f"{nombre},{apellido},{edad},{salario}\n"
 
 #Guardar los datos en un archivo
with open("datos_usuario.txt","a") as archivo: 
     archivo.write(linea)

print("Datos guardados correctamente en datos_usuario.txt")

