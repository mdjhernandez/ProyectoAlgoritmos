def quicksort(arr, paso = 0):
    if len(arr) <= 1:
        return arr
    else:
        pivote = arr[len(arr) // 2]
        izquierda = []
        centro = []
        derecha = []
        for x in arr:
            if x < pivote:
                izquierda.append(x)
            elif x == pivote:
                centro.append(x)
            else:
                derecha.append(x)
            print(f"paso {paso}: {arr}, pivote: {pivote}, izquierda: {izquierda}, centro: {centro}, derecha: {derecha}")
            paso += 1

        return quicksort(izquierda, paso=paso) + centro + quicksort(derecha, paso=paso)
    
def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
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
    