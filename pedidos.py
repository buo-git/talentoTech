print("Bienvenido a Juancho Pizza")

menu = []
state = True
while state == True:
    print("\nNUESTRO MENÚ\n================\n")
    print("1. Margarita - $18.000\n2. Hawaiana - $20.000\n3. Pepperoni - $22.000\n4. Vegetariana - $19.000")
    tipo = input("Seleccione una opción del menú")
    cant = input("¿Cuántas desea pedir?")
    menu.append([])
    continuar = input("¿Desea hacer otro pedido? (si/no)")
    if continuar == "no":
        state = False

for pizza in menu:
    enMenu = True
    if tipo == menu:
        enMenu = True
    else:
        enMenu = False
    if enMenu == False:
        print("Su elección no se encuentra en el menú")
        
