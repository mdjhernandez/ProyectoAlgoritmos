import re
precio_valido = False

while not precio_valido:
            
            precio_normal = input("Precio: ").strip()
            formato_precio = re.fullmatch(r'^\d+(\.\d{1,2})?$', precio_normal)
        
            if not formato_precio:
                print("Error: Debe ingresar un número positivo con hasta 2 decimales")
            else:
             precio = float(precio_normal)
        
        
        
            if precio <= 0:
                print("Error: El precio debe ser mayor que cero")
            else:
                precio_valido = True

