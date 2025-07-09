from inventario import inventario, guardar_inventario

def Actualizar():
    producto_encontrado = None
    
    while producto_encontrado is None:
        print("\nBusca el producto que deseas actualizar:")
        metodo = input("Busca el producto por (1) Código o (2) Nombre: ")
        while metodo != "1" and metodo != "2":
            print("Error: Introduce una opción válida.")
            metodo = input("Busca el producto por (1) Código o (2) Nombre: ")
        
        producto_buscar = input("Ingrese el producto a buscar: ").lower()
        productos_encontrados = []
        
        for i, producto in enumerate(inventario):
            if metodo == "1":
                try:
                    codigo_buscar = int(producto_buscar)
                except ValueError:
                    print("Código inválido, ingresa un número entero.")
                    continue
                if producto[0] == codigo_buscar:
                    productos_encontrados.append((i, producto))
                    print(producto)
            else:
                if producto_buscar in producto[1].lower():
                    productos_encontrados.append((i, producto))
                    print(producto)
        
        if not productos_encontrados:
            print("Ese producto no se encuentra en el inventario, ¿Desea incluirlo?")
            select = input("Seleccione (1) para Sí, (2) para No: ")
            if select == "1":
                from inventario import ingresarProducto
                ingresarProducto()
                return
            else:
                return
        else:
            indice, producto_encontrado = productos_encontrados[0]

    print("\nQué cualidad desea modificar:")
    print("1. Código")
    print("2. Nombre")
    print("3. Precio")
    print("4. Cantidad")
    res = input("Seleccione una de las opciones:\n")

    if res == "1":
        new_codigo = int(input("Ingrese el nuevo código para el producto: "))
        inventario[indice][0] = new_codigo
    elif res == "2":
        new_nombre = input("Ingrese el nuevo nombre para el producto: ")
        inventario[indice][1] = new_nombre
    elif res == "3":
        new_precio = float(input("Ingrese el nuevo precio para el producto: "))
        inventario[indice][2] = new_precio
    elif res == "4":
        new_cantidad = int(input("Ingrese la cantidad a añadir: "))
        inventario[indice][3] += new_cantidad
    else:
        print("Opción inválida.")
        return

    print("Actualización realizada.")
    guardar_inventario()
