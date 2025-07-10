print("Bienvenido al sistema de incentivos")
#Datos del empleado
name = input("Digite el nombre del empleado: \n")
cargo = input("Digite su cargo: \n")
salary = int(input("Digite su salario: \n"))
cal = int(input("Digite su calificación (de 1 a 5): \n"))
incentive = 0
extra_bono = 0


if cal == 5:
    incentive = salary * 30/100
elif cal == 4:
    incentive = salary * 20/100
elif cal == 3:
    incentive = salary * 10/100
elif cal < 3:
    incentive = 0

#Datos del usuario

print ("DATOS DEL USUARIO\n")
print (f"El nombre del empleado es: {name}\nCargo: {cargo}\nCalificación: {cal}")

if cargo == "técnico" and cal >= 4:
    extra_bono = 150000
elif cargo == "operario" and cal ==5:
    print ("El empleado se beneficia con un 1 día libre adicional")
elif salary < 1500000 and cal < 3 :
    print("Evaluación crítica, requiere seguimiento")

print(f"Incentivo total: {incentive + extra_bono}\nSalario + incentivos: {salary + incentive + extra_bono }")