

def vender_producto(inventario):
    producto_encontrado = None  # Inicializamos como None para controlar si se encontró
    
    while producto_encontrado is None:  # Repetir hasta encontrar un producto válido
        print("\nBusca el producto que deseas vender:")
        metodo = input("Busca por (1) Código o (2) Nombre: ")
        
        # Validar método de búsqueda
        while metodo != "1" and metodo != "2":
            print("Error: Introduce una opción válida.")
            metodo = input("Busca por (1) Código o (2) Nombre: ")   
        
        producto_buscar = input("Ingrese el producto a buscar: ").lower()
        productos_encontrados = []
        
        # Buscar en el inventario
        for producto in inventario:
            if (metodo == "1" and str(producto[0]) == producto_buscar) or \
               (metodo == "2" and producto_buscar in producto[1].lower()):
                productos_encontrados.append(producto)
        
        if not productos_encontrados:
            print("Error: Producto no encontrado. Intente nuevamente.")
        else:
            # Seleccionar el producto (asumimos el primero si hay varios)
            producto_encontrado = productos_encontrados[0]
    
    # Proceso de venta (solo si se encontró el producto)
    nombre = producto_encontrado[1]
    cantidad_disponible = producto_encontrado[3]
    print(f"\nProducto seleccionado: {nombre}")
    print(f"Cantidad disponible: {cantidad_disponible}")

    # Validar cantidad a vender
    cantidad = False
    while not cantidad:
        cantidad_vender = input("Ingrese la cantidad a vender: ")
        if cantidad_vender.isdigit():
            cantidad_vender = int(cantidad_vender)
            if cantidad_vender <= 0:
                print("Error: No puedes vender cantidades negativas o cero.")
            elif cantidad_vender > cantidad_disponible:
                print("Error: No puedes vender más de lo que tienes en inventario.")
            else:
                cantidad = True
        else:
            print("Error: Ingrese un número válido.")
    
    # Actualizar inventario
    producto_encontrado[3] -= cantidad_vender
    print(f"Venta realizada. Quedan {producto_encontrado[3]} unidades de {nombre}.")

