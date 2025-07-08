import os
import pickle
import time
from Include.inventario import revisar_inventario,ingresarProducto, buscar_inventario, inventario
from ventas import vender_producto
from ordenamientos import quicksort, merge_sort

Listainventario = inventario

def interfaz():
    print("\n--- SISTEMA DE GESTION DE INVENTARIO ---\n")
    print("1. Ver Todos los productos del inventario")
    print("2. Buscar producto")
    print("3. Ingresar productor")
    print("4. Vender producto")
    print("5. Actualizar por reposicion o compra un producto")
    print("6. Ordenar el inventario")
    print("7. Cargar Archivo del inventario")
    print("8. Guardar Inventario")
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
            vender_producto(inventario)
        elif opciones=="5":
            pass
        elif opciones =="6": 
            print("\n--De que forma quiere Ordenar el Inventario..--")
            print("1. Por Código")
            print("2. Por Nombre")
            respuesta = input("Selecciona una opción (1 o 2): ")
            if respuesta == "1":
                merge_sort(Listainventario, columna=0)
                print("\nInventario ordenado:")
                for producto in Listainventario:
                    print(f"Codigo: {producto[0]}, Nombre: {producto[1]}, precio: {producto[2]}, Cantidad: {producto[3]}")
            else:
                nombreOrdenado = quicksort(Listainventario, columna=1)  
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