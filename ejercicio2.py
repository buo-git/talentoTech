print("Bienvenido al sistema de pagos")
#Defino una variable para pedir los datos del usuario
name = input("Digite su nombre: ")
lastname = input("Digite su apellido: ")
#Defino una variable para el valor de la hora de trabajo
hour_value = 10000
#Defino una variable que almacene el total de horas trabajadas
worked_hours = int(input("¿Cuántas horas trabajó?: "))
#La propiedad "Input" siempre toma los datos en formato string (texto).
#para convertir un tipo de información a otro se le llama "parcear o transformar" por ejemplo de tipo texto a tipo numero entero, se usa int ().

#Defino una variable para guardar el total
#Los símbolos aritméticos son: Suma(+) Resta (-) Multiplicación (*) División (/)
total_value = hour_value * worked_hours
print("\nValor a pagar al empleado")
print("\n------------------")
print("\nDatos del empleado")
print("Nombre: ", name, "\nApellido: ", lastname)
print("\nValor de la hora: ", hour_value, "\nHoras trabajadas: ", worked_hours)
print("\n-----------------------------------")
print("\nVALOR TOTAL A PAGAR: ", total_value)

