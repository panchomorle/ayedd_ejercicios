# MergeSort en Python
array = [6, 5, 12, 10, 9, 1]

def mergeSort(array):
    if len(array) > 1:

        #FASE de dividir el array en 2 partes
        
        # middle es el puntero donde el array es dividido en 2 subarrays
        middle = len(array) // 2
        L = array[:middle] #mitad izquierda
        R = array[middle:] #mitad derecha

        # Ordenar las 2 mitades
        mergeSort(L)
        mergeSort(R)
        
        #FASE de hacer el merge de los subarrays

        # necesitamos 3 punteros:
        # 2 para para ir señalando elementos en los subarrays (mitades)
        # y un 3ro para usar con el el array combinado resultante
        i = j = k = 0


        # Recorrer tanto el subarrays L como M hasta alcanzar el final de alguno
        # de ellos. Compara el elemento de L contra el de M y reubicar en el
        # array general
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # Pasamos los restantes elemenos de L al array general 
        # (en el caso que M tenga menos elementos que L)
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        # Lo mismo que lo anterior pero si M tenía más elementos que L
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1


mergeSort(array)

print("Array ordenado: ")
for i in range(len(array)):
    print(array[i], end=' ')
print("")

