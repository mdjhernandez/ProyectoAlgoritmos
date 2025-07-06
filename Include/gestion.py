import os
import pickle
import time
from Include.inventario import revisar_inventario,ingresarProducto, buscar_inventario




def interfaz():
    print("\n--- SISTEMA DE GESTION DE INVENTARIO ---")
    print("1. Checkear el inventario")
    print("2. Buscar producto")
    print("3. Ingresar productor")
    print("4. Eliminar producto")
    print("5. Actualizar producto")
    print("6. Ordenar inventario")
    print("7. Salir")
    
def main():
    
    while True:
        interfaz()
        opciones = input("Seleciona una opción: ")
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
            print("Introduce un valor valido...")
            time.sleep(3)
        
        
if __name__ == "__main__":
    main()
    