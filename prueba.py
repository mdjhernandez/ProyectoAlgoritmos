inventarioPrueba = [
    ["002", "Pantalón Negro", 35.50, 5],
["001", "Camisa Azul", 25.99, 10],
    ["101", "Amaranta", 49.99, 8],
    ["099", "Cajero", 49.99, 8]
]


def Actualizar(inventario):
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
            if (metodo == "1" and str(producto[0]) == producto_buscar) or \
               (metodo == "2" and producto_buscar in producto[1].lower()):
                productos_encontrados.append((i, producto))
                for fila in productos_encontrados:
                    f = fila[0]
                    print(inventario[f])
        
        if not productos_encontrados:
            print("Ese Producto no se encuentra en el inventario, ¿Desea incluirlo?")
            select = input("Seleccione (1) para Sí, (2) para No: ")
            if select == "1":
                pass
                #ingresarProducto()  
            else:
                break  # Se regresa
        else:
            indice, producto_encontrado = productos_encontrados[0]
    
    print("\nQué cualidad desea modificar:")
    print("1. Código")
    print("2. Nombre")
    print("3. Precio")
    print("4. Cantidad")
    res = input("Seleccione una de las opciones:\n")

    if res == "1":
        codigo_anterior = inventario[indice][0]
        nombre = inventario[indice][1]
        print(f"\nProducto seleccionado: {nombre}")
        print(f"Código actual: {codigo_anterior}")
        new_cant = input("Ingrese el nuevo código para el producto: ")
        inventario[indice][0] = new_cant
        print(f"Actualización realizada. Ahora el producto {nombre} tiene por código {new_cant}.")
    
    if res == "2":
        nombre_actual = inventario[indice][1]
        print(f"\nProducto seleccionado: {nombre_actual}")
        print(f"Nombre actual: {nombre_actual}")
        new_nombre = input("Ingrese el nuevo nombre para el producto: ")
        inventario[indice][1] = new_nombre
        print(f"Actualización realizada. Ahora el producto se llama {new_nombre}.")

    if res == "3":
        precio_anterior = inventario[indice][2]
        nombre = inventario[indice][1]
        print(f"\nProducto seleccionado: {nombre}")
        print(f"Precio actual: {precio_anterior}")
        new_precio = float(input("Ingrese el nuevo precio para el producto: "))
        inventario[indice][2] = new_precio
        print(f"Actualización realizada. Ahora el producto {nombre} cuesta {new_precio}.")

    if res == "4":
        nombre = inventario[indice][1]
        cantidad_disponible = inventario[indice][3]
        print(f"\nProducto seleccionado: {nombre}")
        print(f"Cantidad disponible: {cantidad_disponible}")
        new_cant = int(input("Ingrese la cantidad de productos comprados: "))
        inventario[indice][3] += new_cant
        print(f"Actualización realizada. Ahora el producto cuenta con {inventario[indice][3]} unidades de {nombre}.")
        


print("\nInventario actualizado:")
    
for fila in inventarioPrueba:
    print(fila)
    
Actualizar(inventarioPrueba)
    