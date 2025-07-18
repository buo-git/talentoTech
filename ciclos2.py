#print("Bienvenido al sistema\n")
#estado = True
#password = ("hola1234")

#while estado == True:
 #   userLog = input ("Ingrese su contraseña: \n")
  #  if userLog == password:
   #     estado = False
    #else:
     #   print("Contraseña errónea\n")

#print("Usted ha ingresado con éxito")


print("Bienvenido al login")

name = input("Ingrese su nombre: \n")
lastName = input("Ingrese su apellido: \n")
cc = input("Ingrese su número de documento: \n")
address = input("Ingrese su dirección: \n")
user = "buo"
password = ("Hola1234")
state = False

while state == False:
    userLog = input("Ingrese su usuario: \n")
    passLog = input("Ingrese su contraseña: \n")

    if passLog == password and userLog == user:
        state = True
    else:
        print("Usuario y contraseña incorrectos, intente nuevamente\n")

print("\nUsted ha ingresado con éxito")
print(f"\nSus datos son los siguientes:\n\nNombre: {name}\nApellido: {lastName}\nDocumento:{cc}\nDirección: {address}")