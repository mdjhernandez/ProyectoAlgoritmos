import os
import pickle
from validaciones import validar_precio, validar_cantidad, validar_codigo, validar_nombre

INVENTARIO_PATH = "inventario.bin"
inventario = []

def cargar_inventario():
    global inventario
    if os.path.exists(INVENTARIO_PATH):
        with open(INVENTARIO_PATH, "rb") as archivo:
            inventario = pickle.load(archivo)

def guardar_inventario():
    with open(INVENTARIO_PATH, "wb") as archivo:
        pickle.dump(inventario, archivo)

def revisar_inventario():
    print("Inventario Actual")
    if not inventario:
        print("El inventario está vacío")
    else:
        for producto in inventario:
            print(producto)

def ingresarProducto():
    print("Ingresa el producto...")
    codigo = validar_codigo()
    
    # Buscar si el producto ya existe
    producto_existente = None
    for producto in inventario:
        if producto[0] == codigo:
            producto_existente = producto
            break

    if producto_existente:
        cantidad = int(input(f"Cantidad para añadir (Actualmente hay {producto_existente[3]}): "))
        producto_existente[3] += cantidad
        print(f"Se actualizó el producto {producto_existente[1]}. Ahora hay: {producto_existente[3]}")
    else:
        nombre = validar_nombre()
        precio = validar_precio()
        cantidad = validar_cantidad()

        producto_nuevo = [codigo, nombre, precio, cantidad]
        inventario.append(producto_nuevo)
        print(f"Producto {nombre} agregado al inventario.")
    
    guardar_inventario()

def buscar_inventario():
    metodo = input("Busca por (1) Código o (2) Nombre: ")
    while metodo != "1" and metodo != "2":
        print("Error: Introduce una opción válida.")
        metodo = input("Busca por (1) Código o (2) Nombre: ")
    producto_buscar = input("Ingrese el producto a buscar: ").lower()

    productos_encontrados = []
    for producto in inventario:
        if (metodo == "1" and str(producto[0]) == producto_buscar) or \
           (metodo == "2" and producto_buscar in producto[1].lower()):
            productos_encontrados.append(producto)
    
    if productos_encontrados:
        print("Productos encontrados:")
        for p in productos_encontrados:
            print(p)
    else:
        print("No se encontraron productos.")
    
    return productos_encontrados
