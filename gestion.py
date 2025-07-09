import time
from inventario import revisar_inventario, ingresarProducto, buscar_inventario, cargar_inventario, guardar_inventario
from ventas import vender_producto
from ordenamientos import quicksort, merge_sort
from Actualizacion import Actualizar
from inventario import inventario

def interfaz():
    print("\n--- SISTEMA DE GESTION DE INVENTARIO ---\n")
    print("1. Ver Todos los productos del inventario")
    print("2. Buscar producto")
    print("3. Ingresar producto")
    print("4. Vender producto")
    print("5. Actualizar por reposición o compra un producto")
    print("6. Ordenar el inventario")
    print("7. Cargar archivo del inventario")
    print("8. Guardar inventario")
    print("9. Salir\n")

def main():
    cargar_inventario()  # Cargar inventario al iniciar

    while True:
        interfaz()
        opciones = input("Selecciona una opción: ")
        if opciones == "1":
            revisar_inventario()
            time.sleep(3)
        elif opciones == "2":
            buscar_inventario()
            time.sleep(3)
        elif opciones == "3":
            ingresarProducto()
            time.sleep(3)
        elif opciones == "4":
            vender_producto()
            time.sleep(3)
        elif opciones == "5":
            Actualizar()
            time.sleep(3)
        elif opciones == "6":
            print("\n-- ¿Cómo quieres ordenar el inventario? --")
            print("1. Por Código")
            print("2. Por Nombre")
            respuesta = input("Selecciona una opción (1 o 2): ")
            if respuesta == "1":
                merge_sort(inventario, columna=0)
            else:
                inventario[:] = quicksort(inventario, columna=1)  # actualizar lista en sitio
            
            print("\nInventario ordenado:")
            for producto in inventario:
                print(f"Código: {producto[0]}, Nombre: {producto[1]}, Precio: {producto[2]}, Cantidad: {producto[3]}")
            time.sleep(3)
        elif opciones == "7":
            cargar_inventario()
            print("Inventario cargado.")
            time.sleep(3)
        elif opciones == "8":
            guardar_inventario()
            print("Inventario guardado.")
            time.sleep(3)
        elif opciones == "9":
            print("Haz salido del sistema...")
            break
        else:
            print("Introduce un valor válido...")
            time.sleep(3)

if __name__ == "__main__":
    main()
