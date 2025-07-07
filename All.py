import re
import time

inventario = []
inventarioFormateado = []

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





























































def interfaz():
    print("\n--- SISTEMA DE GESTION DE INVENTARIO ---")
    print()
    print("1. Ver Todos los productos del inventario")
    print("2. Buscar producto")
    print("3. Ingresar productor")
    print("4. Eliminar producto")
    print("5. Actualizar producto")
    print("6. Ordenar inventario")
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
            pass
        elif opciones=="5":
            pass
        elif opciones =="6":
            pass    
        elif opciones =="7":
            print("Haz salido del sistema...")
            break
        else:
            print("Introduce un valor que sea valido...")
            time.sleep(3)
        
        
        
if __name__ == "__main__":
    main()