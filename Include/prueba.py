
inventario = [
    ["001", "Camisa Azul", 25.99, 10],
    ["002", "Pantalón Negro", 35.50, 5],
    ["101", "Amaranta", 49.99, 8]
]




def buscar_inventario(inventario):
    metodo = input("Busca por (1) Código o (2) Nombre: ")
    
    while metodo != "1" and metodo != "2":
        print("Error: Introduce una opcion valida. ")
        metodo = input("Busca por (1) Código o (2) Nombre: ")
        
        
        
    producto_buscar = input("Ingrese el producto a buscar: ")
    
    productos_encontrados = []
    
    for producto in inventario:
        if metodo == "1" and str(producto[0]) == producto_buscar:
            productos_encontrados.append(producto)
        elif metodo == "2" and producto_buscar in producto[1].lower():
            productos_encontrados.append(producto)
            
    if productos_encontrados:
        print("Productos Encontrados: ")
        for x in productos_encontrados:
            print(x)
    else:
        print("No se encontraron productos ")
    return productos_encontrados


def vender_producto(inventario):
    print("Busca el producto que deseas vender:")
    productos = buscar_inventario()
    #if len(productos) > 1:
        #print("Hay varios productos encontrados. Por favor sé más específico.")
        #return
    producto_encontrado = productos[0]
    nombre = producto_encontrado[1]
    cantidad_disponible = producto_encontrado[3]

    print(f"\nProducto seleccionado: {nombre}")
    print(f"Cantidad disponible: {cantidad_disponible}")

    cantidad_vender = input("Ingrese la cantidad a vender: ")

    while not int(cantidad_vender) <= 0:
        print(" Debes ingresar un número entero positivo.")
        cantidad_vender = input("Cantidad a vender: ")

    cantidad_vender = int(cantidad_vender)

    if cantidad_vender > cantidad_disponible:
        print(" No puedes vender más de lo que tienes en inventario.")
    else:
        producto_encontrado[3] -= cantidad_vender
        print(f" Venta realizada. Quedan {producto_encontrado[3]} unidades de {nombre}.")





buscar_inventario(inventario)
vender_producto(inventario)

