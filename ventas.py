from inventario import inventario, guardar_inventario

def vender_producto():
    producto_encontrado = None
    
    while producto_encontrado is None:
        print("\nBusca el producto que deseas vender:")
        metodo = input("Busca por (1) Código o (2) Nombre: ")
        while metodo != "1" and metodo != "2":
            print("Error: Introduce una opción válida.")
            metodo = input("Busca por (1) Código o (2) Nombre: ")
        
        producto_buscar = input("Ingrese el producto a buscar: ").lower()
        productos_encontrados = []
        
        for producto in inventario:
            if metodo == "1":
                try:
                    codigo_buscar = int(producto_buscar)
                except ValueError:
                    print("Código inválido, ingresa un número entero.")
                    continue
                if producto[0] == codigo_buscar:
                    productos_encontrados.append(producto)
            else:
                if producto_buscar in producto[1].lower():
                    productos_encontrados.append(producto)
        
        if not productos_encontrados:
            print("Producto no disponible.")
        else:
            producto_encontrado = productos_encontrados[0]

    nombre = producto_encontrado[1]
    cantidad_disponible = producto_encontrado[3]
    print(f"\nProducto seleccionado: {nombre}")
    print(f"Cantidad disponible: {cantidad_disponible}")

    while True:
        cantidad_vender = input("Ingrese la cantidad a vender: ")
        if cantidad_vender.isdigit():
            cantidad_vender = int(cantidad_vender)
            if cantidad_vender <= 0:
                print("Error: No puedes vender cantidades negativas o cero.")
            elif cantidad_vender > cantidad_disponible:
                print(f"No hay suficiente cantidad. Solo hay {cantidad_disponible}.")
            else:
                break
        else:
            print("Error: Ingrese un número válido.")

    producto_encontrado[3] -= cantidad_vender
    print(f"Venta realizada. Quedan {producto_encontrado[3]} unidades de {nombre}.")

    guardar_inventario()
