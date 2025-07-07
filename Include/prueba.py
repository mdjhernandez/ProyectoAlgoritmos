
inventario = [
    ["001", "Camisa Azul", 25.99, 10,],
    ["002", "Pantalón Negro", 35.50, 5],
    ["101", "Amaranta", 49.99, 8]
]

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
    

nombre=quicksort(inventario)
print("Nombre")
for fila in nombre:
    print(f"Codigo: {fila[0]}, Nombre: {fila[1]}, precio: {fila[2]}, Cantidad: {fila[3]}")