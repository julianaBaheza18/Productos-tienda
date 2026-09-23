# Programa: Registro de productos de una tienda
# Semana 15 - Funciones, Colecciones y Archivos

productos = {}


def agregar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))

    productos[codigo] = {
        "nombre": nombre,
        "precio": precio
    }

    print("Producto agregado correctamente.")


def mostrar_productos():
    if not productos:
        print("No hay productos registrados.")
    else:
        print("\n--- PRODUCTOS REGISTRADOS ---")

        for codigo, producto in productos.items():
            print("Código:", codigo)
            print("Nombre:", producto["nombre"])
            print("Precio: $", producto["precio"])
            print("-----------------------------")


def buscar_producto():
    codigo = input("Ingrese el código del producto que desea buscar: ")

    if codigo in productos:
        print("\nProducto encontrado:")
        print("Nombre:", productos[codigo]["nombre"])
        print("Precio: $", productos[codigo]["precio"])
    else:
        print("Producto no encontrado.")


def eliminar_producto():
    codigo = input("Ingrese el código del producto que desea eliminar: ")

    if codigo in productos:
        del productos[codigo]
        print("Producto eliminado correctamente.")
    else:
        print("Producto no encontrado.")


# Menú principal
while True:
    print("\n===== REGISTRO DE PRODUCTOS =====")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Buscar producto")
    print("4. Eliminar producto")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()

    elif opcion == "2":
        mostrar_productos()

    elif opcion == "3":
        buscar_producto()

    elif opcion == "4":
        eliminar_producto()

    elif opcion == "5":
        print("Programa finalizado.")
        break

    else:
        print("Opción no válida. Intente nuevamente.")
