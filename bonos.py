print("Bienvenido al sistema de bonos de productividad\n")
name = input("\nDigite su nombre y apellidos: \n")
department = input("\nDigite su departamento (ventas/soporte): \n")
bono = 0

#sells = input("Digite el número de ventas obtenidas: \n")
#tickets = input("Digite el número de tickets resueltos: \n")

if department == "ventas":
    sells = int(input("\nDigite el número de ventas realizadas: \n"))
    if sells >20:
        bono = 500000
    elif sells >=10 and sells <=20:
        bono = 300000
elif department == "soporte":
    tickets = int(input("\nDigite el número de tickets resueltos: \n"))
    if tickets >50:
        bono = 400000
    elif tickets >=20 and tickets <=50:
        bono = 200000


#Datos obtenidos

print(f"\nEl bono del empleado {name} del departamento de {department} es de:\n{bono}")
