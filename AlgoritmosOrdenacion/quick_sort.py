# Quick sort en Python
#data = [8, 7, 6, 1, 0, 9, 2]

# Función para determinar el pivot 0, len(data) - 1
def partition(array, low, high):
  # seleccionar el último elemento del array como pivot
  pivot = array[high]

  # esta variable la usaremos para señalar elementos mas grandes que el pivot
  i = low - 1

  # Buscar todos los elementos menores al pivot y reubicarlos
  for j in range(low, high):
    if array[j] <= pivot:
      # Si hay un element menor que el pivot intercamabiarlos por el de la position i
      i = i + 1
      (array[i], array[j]) = (array[j], array[i])

  # finalmente, intercamabiar el pivot por el contenido del sigueinte lugar de i
  (array[i + 1], array[high]) = (array[high], array[i + 1])

  # Retornar la posición dónde se partió
  #print("semiprocesado: ", end='')
  #print(array)
  return i + 1

def quickSort(array, low=0, high=None):
  if high == None:
    high = len(array) - 1
  if low < high:
    pi = partition(array, low, high)

    # ordenar a la izq del punto particionado
    quickSort(array, low, pi - 1)

    # ordenar a la derecha del punto particionado
    quickSort(array, pi + 1, high)


"""
print("Array original: ")
print(data)

quickSort(data, 0, len(data) - 1)

print('Luego de ordenar:')
print(data)
"""
