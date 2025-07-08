import re

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

