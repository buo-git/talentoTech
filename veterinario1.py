print("BIENVENIDO AL SISTEMA DE REGISTRO DE MASCOTAS\n===============================\n")

opcionMenu = 0
mascotas = []

perros = 0
gatos = 0
otra = 0

while opcionMenu != 5:
    print("Opciones del menú\n\n1. Nuevo registro\n2. Listar datos\n3. Buscar mascota\n4. Categorización\n5. Salir")
    opcionMenu = int(input("\n¿Que desea hacer? "))

    if opcionMenu == 1:
        print("\nREGISTRO DE NUEVA MASCOTA")
        nombre = input("\nNombre de la mascota: \n")
        edad = input("\nEdad de la mascota en años: \n")
        propietario = input("\nNombre del propietario de la mascota: \n")
        especie = input("\nEspecie de la mascota: \n- Perro\n- Gato\n- Otra: \n")
        mascotas.append({
                "nombre": nombre,
                "edad": edad,
                "propietario": propietario,
                "especie": especie
            })
        print("\nRegistro exitoso\n===================\n")
        

    if opcionMenu == 2:
        for mascota in mascotas:
            print(f"Nombre: {mascota['nombre']}")
            print(f"Edad: {mascota['edad']} años")
            print(f"Dueño: {mascota['propietario']}")
            print(f"Especie: {mascota['especie']}\n")


    if opcionMenu == 3:
        if len(mascotas) > 0:
            encontrada = True
            nombre_a_buscar = input("Digite el nombre de la mascota")
            for mascota in mascotas:
                if nombre_a_buscar == mascota['nombre']:
                    print(f"Nombre: {mascota['nombre']}")
                    print(f"Edad: {mascota['edad']}")
                    print(f"Dueño: {mascota['propietario']}")
                    print(f"Especie: {mascota['especie']}\n")
                    encontrada = True
                    break
                else:
                    encontrada = False
            if encontrada == False:
                print("Lo sentimos! la mascota a buscar no existe")
        else:
            print("Lo sentimos! no existen datos registrados aún.")