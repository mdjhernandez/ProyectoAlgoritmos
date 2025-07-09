import time
from Include.inventario import revisar_inventario,ingresarProducto, buscar_inventario, inventario

def Actualizar(inventario):
    producto_encontrado = None  # Inicializamos como None para controlar si se encontró
    
    while producto_encontrado is None:  # Repetir hasta encontrar un producto válido
        print("\nBusca el producto que deseas actualizar:")
        metodo = input("Busca el producto por (1) Código o (2) Nombre: ")
        # Validar método de búsqueda
        while metodo != "1" and metodo != "2":
            print("Error: Introduce una opción válida.")
            metodo = input("Busca el producto por (1) Código o (2) Nombre: ")   
        producto_buscar = input("Ingrese el producto a buscar: ").lower()
        productos_encontrados = []
        # Buscar en el inventario
        for producto in inventario:
            if (metodo == "1" and str(producto[0]) == producto_buscar) or \
               (metodo == "2" and producto_buscar in producto[1].lower()):
                productos_encontrados.append(producto)
        
        if not productos_encontrados:
            print("Ese Producto no se encuentra en el inventario, Desea incluirlo?")
            select=input("Seleccione (1) para Si, (2) si es No")
            if (select==1):
                ingresarProducto()
            else:
                break #
        else:
            # Seleccionar el producto (asumimos el primero si hay varios)
            producto_encontrado = productos_encontrados[0]
    
    # Proceso de Actualizacion (solo si se encontró el producto)
    print("\nQue cualidad desea Modificar \n")
    print("1. Codigo")
    print("2. Nombre")
    print("3. Precio")
    print("4. Cantidad")
    res=input("Seleccione una opcion")
    nombre = producto_encontrado[1]
    if (res==1):
        codigo_anterior = producto_encontrado[0]
        nombre=producto_encontrado[1]
        print(f"\nProducto seleccionado: {nombre}")
        print(f"Codigo Actual: {codigo_anterior}")
        new_cant=int(input("Ingrese el nuevo Codigo para el producto ")) #ARREGLAR ESTA PREGUNTA
        producto_encontrado[0] == new_cant
        print(f"Actualizacion realizada. Ahora el producto {nombre} tiene por codigo {new_cant}.")
    if (res==2):
        nombre=producto_encontrado[1]
        print(f"\nProducto seleccionado: {nombre}")
        print(f"Nombre Actual: {nombre}")
        new_cant=int(input("Ingrese el nuevo Nombre para el producto ")) #ARREGLAR ESTA PREGUNTA
        producto_encontrado[1] == new_cant
        print(f"Actualizacion realizada. Ahora el producto {nombre} tiene por nombre {new_cant}.")
    if (res==3):
        precio_anterior = producto_encontrado[2]
        nombre=producto_encontrado[1]
        print(f"\nProducto seleccionado: {nombre}")
        print(f"Precio Actual: {precio_anterior}")
        new_cant=int(input("Ingrese el nuevo Precio para el producto ")) #ARREGLAR ESTA PREGUNTA
        producto_encontrado[2] == new_cant
        print(f"Actualizacion realizada. Ahora el producto {nombre} tiene por codigo {new_cant}.")
    if (res==4):
        cantidad_disponible = producto_encontrado[3]
        print(f"\nProducto seleccionado: {nombre}")
        print(f"Cantidad disponible: {cantidad_disponible}")
        new_cant=int(input("Ingrese la cantidad de productos comprados para el producto ")) #ARREGLAR ESTA PREGUNTA
        producto_encontrado[3] += new_cant
        print(f"Actualizacion realizada. Ahora el producto cuenta con {producto_encontrado[3]} unidades de {nombre}.") #Bonito no esta