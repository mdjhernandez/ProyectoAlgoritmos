import pickle
import os

listaInventario = "inventario.bin"

def cargar_inventario():
    if os.path.exists(listaInventario):
        with open(listaInventario,"rb") as archivo:
            return pickle.load(archivo)
    
    
def guardar_inventario(lista):
    with open(listaInventario,"wb") as archivo:
        pickle.dump(lista,archivo)
        
inventario = cargar_inventario()