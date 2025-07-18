# 🐾 Sistema de Registro de Mascotas - Veterinaria

def mostrar_menu():
    """Muestra el menú principal del sistema"""
    print("\n" + "="*50)
    print("🐾 SISTEMA DE REGISTRO DE MASCOTAS - VETERINARIA")
    print("="*50)
    print("1. Registrar una mascota")
    print("2. Listar todas las mascotas registradas")
    print("3. Buscar una mascota por nombre")
    print("4. Mostrar cuántas mascotas hay por especie")
    print("5. Salir del sistema")
    print("="*50)

def registrar_mascota(lista_mascotas):
    """Registra una nueva mascota en el sistema"""
    print("\n--- REGISTRAR NUEVA MASCOTA ---")
    
    # Validar que el nombre no esté vacío
    while True:
        nombre = input("Ingrese el nombre de la mascota: ").strip()
        if nombre:
            break
        print("Error: El nombre no puede estar vacío")
    
    # Validar que la especie no esté vacía
    while True:
        especie = input("Ingrese la especie (perro, gato, etc.): ").strip()
        if especie:
            break
        print("Error: La especie no puede estar vacía")
    
    # Validar que la edad sea un número válido
    while True:
        try:
            edad = int(input("Ingrese la edad de la mascota (años): "))
            if edad >= 0:
                break
            else:
                print("Error: La edad debe ser un número positivo")
        except ValueError:
            print("Error: Ingrese un número válido para la edad")
    
    # Validar que el nombre del dueño no esté vacío
    while True:
        dueno = input("Ingrese el nombre del dueño: ").strip()
        if dueno:
            break
        print("Error: El nombre del dueño no puede estar vacío")
    
    # Crear diccionario con los datos de la mascota
    mascota = {
        "nombre": nombre.title(),
        "especie": especie.lower(),
        "edad": edad,
        "dueno": dueno.title()
    }
    
    # Agregar la mascota a la lista
    lista_mascotas.append(mascota)
    print(f"\n✅ Mascota '{nombre}' registrada exitosamente!")

def listar_mascotas(lista_mascotas):
    """Lista todas las mascotas registradas"""
    print("\n--- TODAS LAS MASCOTAS REGISTRADAS ---")
    
    if not lista_mascotas:
        print("No hay mascotas registradas en el sistema.")
        return
    
    print(f"Total de mascotas registradas: {len(lista_mascotas)}")
    print("-" * 60)
    
    for i, mascota in enumerate(lista_mascotas, 1):
        print(f"{i}. Nombre: {mascota['nombre']}")
        print(f"   Especie: {mascota['especie'].title()}")
        print(f"   Edad: {mascota['edad']} años")
        print(f"   Dueño: {mascota['dueno']}")
        print("-" * 60)

def buscar_mascota(lista_mascotas):
    """Busca una mascota por nombre"""
    print("\n--- BUSCAR MASCOTA POR NOMBRE ---")
    
    if not lista_mascotas:
        print("No hay mascotas registradas en el sistema.")
        return
    
    nombre_buscar = input("Ingrese el nombre de la mascota a buscar: ").strip()
    
    if not nombre_buscar:
        print("Error: Debe ingresar un nombre para buscar")
        return
    
    # Buscar la mascota (sin importar mayúsculas/minúsculas)
    mascota_encontrada = None
    for mascota in lista_mascotas:
        if mascota['nombre'].lower() == nombre_buscar.lower():
            mascota_encontrada = mascota
            break
    
    if mascota_encontrada:
        print(f"\n✅ Mascota encontrada:")
        print(f"   Nombre: {mascota_encontrada['nombre']}")
        print(f"   Especie: {mascota_encontrada['especie'].title()}")
        print(f"   Edad: {mascota_encontrada['edad']} años")
        print(f"   Dueño: {mascota_encontrada['dueno']}")
    else:
        print(f"\n❌ No se encontró ninguna mascota con el nombre '{nombre_buscar}'")

def contar_por_especie(lista_mascotas):
    """Cuenta y muestra cuántas mascotas hay por especie"""
    print("\n--- MASCOTAS POR ESPECIE ---")
    
    if not lista_mascotas:
        print("No hay mascotas registradas en el sistema.")
        return
    
    # Contar mascotas por especie
    contador_especies = {}
    for mascota in lista_mascotas:
        especie = mascota['especie']
        if especie in contador_especies:
            contador_especies[especie] += 1
        else:
            contador_especies[especie] = 1
    
    # Mostrar resultados
    print("Cantidad de mascotas por especie:")
    print("-" * 30)
    for especie, cantidad in contador_especies.items():
        print(f"{especie.title()}: {cantidad}")
    print("-" * 30)
    print(f"Total de especies diferentes: {len(contador_especies)}")

def main():
    """Función principal del programa"""
    # Lista para almacenar todas las mascotas
    lista_mascotas = []
    
    print("¡Bienvenido al Sistema de Registro de Mascotas!")
    
    while True:
        mostrar_menu()
        
        # Obtener opción del usuario
        try:
            opcion = int(input("\nSeleccione una opción (1-5): "))
        except ValueError:
            print("❌ Error: Ingrese un número válido")
            continue
        
        # Ejecutar la opción seleccionada
        if opcion == 1:
            registrar_mascota(lista_mascotas)
        elif opcion == 2:
            listar_mascotas(lista_mascotas)
        elif opcion == 3:
            buscar_mascota(lista_mascotas)
        elif opcion == 4:
            contar_por_especie(lista_mascotas)
        elif opcion == 5:
            print("\n👋 ¡Gracias por usar el Sistema de Registro de Mascotas!")
            print("¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Seleccione una opción entre 1 y 5.")
        
        # Pausa para que el usuario pueda leer el resultado
        input("\nPresione Enter para continuar...")

# Ejecutar el programa
if __name__ == "__main__":
    main()