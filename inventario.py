import os
import pickle
import re
from Include.validaciones import validar_precio, validar_cantidad, validar_codigo, validar_nombre
# Lista de inventario
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

    
