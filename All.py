import re
import time

inventario = []
inventarioFormateado = []
inventarioPrueba = [
    ["002", "Pantalón Negro", 35.50, 5],
    ["001", "Camisa Azul", 25.99, 10],
    ["101", "Amaranta", 49.99, 8],
    ["099", "Cajero", 49.99, 8]
]


#def formatear_inventario():
    #inventarioFormateado.clear()
    #for p in inventario:
        #inventarioFormateado.append(
            #[f"Código: {p[0]}, Nombre: {p[1]}, Precio: {p[2]}, Cantidad: {p[3]}"]
        #)


def revisar_inventario():
    print("Inventario Actual")
    if not inventario:
        print("El inventario está vacio")
    else:
        for producto in inventarioFormateado:
            print(producto)

def ingresarProducto():
    print("Ingresa el producto...")
    codigo = validar_codigo()
    
    # Buscar si el producto ya existe
    producto_existenten = None
    for codigoProducto in inventario:
        if codigoProducto == codigo:
            producto_existenten = codigoProducto
            break
        
        
    if producto_existenten:
        cantidad = int(input(f"Cuantidad para añadir (En el inventario hay{producto_existenten.cantidad})"))
        producto_existenten += cantidad
        print(f"Se actualizo el producto {producto_existenten.nombre}. Hay ahora: {producto_existenten.cantidad}")
    else:
        
        nombre = validar_nombre()
        
        precio = validar_precio()
        
        cantidad = validar_cantidad()   

        producto_nuevo_formateado = [f"Código: {codigo},Nombre: {nombre},Precio: {precio},Cantidad: {cantidad}"]
        producto_nuevo = [codigo,nombre,precio,cantidad]
        inventario.append(producto_nuevo)
        inventarioFormateado.append(producto_nuevo_formateado)
        
        print(f"Producto {nombre} agregado al inventario.")
        
    print(inventarioFormateado)
        
def buscar_inventario():
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


def validar_precio():
    precio_normal = input("Precio del producto: ")
    formato_precio = re.fullmatch(r'^\d+(\.\d{1,2})?$', precio_normal)
        
    while not formato_precio:
            print("Error: El precio no puede contener letras ni números negativos ")
            precio_normal = input("Precio del producto: ")
            formato_precio = re.fullmatch(r'^\d+(\.\d{1,2})?$', precio_normal)
    precio_final = float(precio_normal)
    return precio_final
    
def validar_cantidad():
    cantidad_normal = input("Cantidad del producto: ")    
    formato_cantidad = re.fullmatch(r'^\d+(\.\d{1,2})?$', cantidad_normal)
    while not formato_cantidad:
            print("Error: La cantidad no puede contener letras ni números negativos ")
            cantidad_normal = input("Cantidad del producto: ")
            formato_cantidad = re.fullmatch(r'^\d+(\.\d{1,2})?$', cantidad_normal)
            
    cantidad_final = int(cantidad_normal)
    return cantidad_final

def validar_codigo():
    codigo_normal = input("Código del producto: ")    
    formato_codigo = re.fullmatch(r'^\d+(\.\d{1,2})?$', codigo_normal)
    while not formato_codigo:
            print("Error: El Código no puede contener letras ni números negativos ")
            codigo_normal = input("Código del producto: ")
            formato_codigo = re.fullmatch(r'^\d+(\.\d{1,2})?$', codigo_normal)
            
    codigo_final = int(codigo_normal)
    return codigo_final

def validar_nombre():
    nombre = input("Nombre del producto: ")
    while not nombre.replace(" ", "").isalpha():
            print("Error: El nombre no puede contener números ni caracteres especiales")
            nombre = input("Nombre del producto: ")
    return nombre

def quicksort(mat, paso=0, columna=1):
    if len(mat) <= 1:
        return mat
    else:
        pivote = mat[len(mat) // 2][columna]
        izquierda = []
        centro = []
        derecha = []
        for x in mat:
            if x[columna] < pivote:
                izquierda.append(x)
            elif x[columna] == pivote:
                centro.append(x)
            else:
                derecha.append(x)
            paso += 1
        return quicksort(izquierda, paso=paso) + centro + quicksort(derecha, paso=paso)
    
def merge_sort(array, columna=0):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half, columna)
        merge_sort(right_half, columna)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][columna] < right_half[j][columna]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1


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

    while cantidad_vender > cantidad_disponible:
        print(" No puedes vender más de lo que tienes en inventario.")
        cantidad_vender = input("Ingrese nuevamente la cantidad a vender: ")
        cantidad_vender = int(cantidad_vender)
    while (cantidad_vender <= 0):
        print("Error no puedes vender cantidades negativas.")
        cantidad_vender = input("Ingrese nuevamente la cantidad a vender: ")
        cantidad_vender = int(cantidad_vender)
    else:
        producto_encontrado[3] -= cantidad_vender
        print(f"Venta realizada. Quedan {producto_encontrado[3]} unidades de {nombre}.")


def interfaz():
    print("\n--- SISTEMA DE GESTION DE INVENTARIO ---\n")
    print("1. Ver Todos los productos del inventario")
    print("2. Buscar producto")
    print("3. Ingresar productor")
    print("4. Vender producto")
    print("5. Actualizar por reposicion o compra un producto")
    print("6. Ordenar el inventario")
    print("7. Cargar Archivo del inventario")
    print("7. Guardar Inventario")
    print("9. Salir\n")
    
def main():
    
    while True:
        interfaz()
        opciones = input("Seleciona una de las siguientes opciónes: ")
        if opciones == "1":
            revisar_inventario()
            time.sleep(3)
        elif opciones=="2":
            buscar_inventario()
        elif opciones =="3":
            ingresarProducto()
        elif opciones == "4":
            vender_producto(inventarioFormateado)
        elif opciones=="5":
            pass
        elif opciones =="6": 
            print("\n--De que forma quiere Ordenar el Inventario..--")
            print("1. Por Código")
            print("2. Por Nombre")
            respuesta = input("Selecciona una opción (1 o 2): ")
            if respuesta == "1":
                merge_sort(inventarioPrueba, columna=0)
                print("\nInventario ordenado:")
                for producto in inventarioPrueba:
                    print(f"Codigo: {producto[0]}, Nombre: {producto[1]}, precio: {producto[2]}, Cantidad: {producto[3]}")
            else:
                nombreOrdenado = quicksort(inventarioPrueba, columna=1)  
                print("\nInventario ordenado:")
                for producto in nombreOrdenado:
                    print(f"Codigo: {producto[0]}, Nombre: {producto[1]}, precio: {producto[2]}, Cantidad: {producto[3]}")
            time.sleep(3)
   
        elif opciones =="7":
            pass 
        elif opciones =="8":
            pass 
        elif opciones =="9":
            print("Haz salido del sistema...")
            break
        else:
            print("Introduce un valor que sea valido...")
            time.sleep(3)
        
        
        
if __name__ == "__main__":
    main()