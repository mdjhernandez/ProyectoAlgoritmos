inventario = [
    ["001", "Camisa Azul", 25.99, 10],
    ["002", "Pantalón Negro", 35.50, 5],
    ["101", "Zapatos Deportivos", 49.99, 8]
]

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
buscar_inventario()