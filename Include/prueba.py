
inventario = [
    ["001", "Camisa Azul", 25.99, 10],
    ["002", "Pantalón Negro", 35.50, 5],
    ["101", "Amaranta", 49.99, 8]
]



def vender_producto(inventario):
    print("Busca el producto que deseas vender:")
    #productos = buscar_inventario(inventario)
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
        for x in productos_encontrados:
            print(x)
    productos= productos_encontrados
    producto_encontrado = productos[0]
    nombre = producto_encontrado[1]
    cantidad_disponible = producto_encontrado[3]

    print(f"\nProducto seleccionado: {nombre}")
    print(f"Cantidad disponible: {cantidad_disponible}")

    cantidad_vender = input("Ingrese la cantidad a vender: ")
    cantidad_vender = int(cantidad_vender)

    if cantidad_vender > cantidad_disponible:
        print(" No puedes vender más de lo que tienes en inventario.")
        cantidad_vender = input("Ingrese nuevamente la cantidad a vender: ")
        cantidad_vender = int(cantidad_vender)
    elif (cantidad_vender <= 0):
        print("La cantidad a Vender no puede ser un numero negativo")
    else:
        producto_encontrado[3] -= cantidad_vender
        print(f" Venta realizada. Quedan {producto_encontrado[3]} unidades de {nombre}.")


vender_producto(inventario)
print()