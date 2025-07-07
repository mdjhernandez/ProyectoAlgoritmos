
inventario = [
    ["001", "Camisa Azul", 25.99, 10],
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
    
def merge_sort(array, columna=0):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half, columna)
        merge_sort(right_half, columna)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i][columna] < right_half[j][columna]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

codigo=merge_sort(inventario, columna=0)
print("\nInventario ordenado:")
for codigo in inventario:
    print(codigo)

nombre=quicksort(inventario)
print("Nombre")
for fila in nombre:
    print(fila)