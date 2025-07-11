print("Bienvenido al sistema\n")
estado = True
password = ("hola1234")

while estado == True:
    userLog = input ("Ingrese su contraseña: \n")
    if userLog == password:
        estado = False
    else:
        print("Contraseña errónea\n")
        
print("Usted ha ingresado con éxito")
