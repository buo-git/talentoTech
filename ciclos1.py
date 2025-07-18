print("Bienvenido a la calculadora")
number = int(input("Escribe un número para saber su tabla: \n"))
operation = input("¿qué operación quieres hacer? (sumar/restar/multiplicar/dividir): \n")

if operation == "sumar":
    for n in range(1,11):
        suma = number + n
        print(f" {number} + {n} = {suma}")
elif operation == "restar":
    for n in range(1,11):
        resta = number - n
        print(f"{number} - {n} = {resta}")
elif operation == "multiplicar":
    for n in range(1,11):
        multi = number * n
        print(f"{number} * {n} = {multi}")
elif operation == "dividir":
    for n in range(1,11):
        divi = number / n
        print(f"{number} / {n} = {divi}")