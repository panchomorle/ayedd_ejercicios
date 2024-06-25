from Persona import Persona
from Persona import raiz as arbolPersona

# Quick sort en Python

# Función para determinar el pivot
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
  print("semiprocesado: ", end='')
  print(*array)
  print("\n\n")
  return i + 1

#ordenación del array 
def quickSort(array, low, high):
  if low < high:
    pi = partition(array, low, high)

    # ordenar a la izq del punto particionado
    quickSort(array, low, pi - 1)

    # ordenar a la derecha del punto particionado
    quickSort(array, pi + 1, high)

#parse de un arbol binario en array // en inorden
def parseArbolToArray(tree, array):
    if tree is None:
        return array
    
    parseArbolToArray(tree.left,array)
    array.append(tree)
    parseArbolToArray(tree.right,array)
    
    return array

#parse de un array in arbol binário 
def parseArrayToArbol(arrayArbol):

    if arrayArbol is None:
        return None
    
    raiz=arrayArbol[0]
    i=0
    lenArray=len(arrayArbol)
    for i in range(lenArray):
        left=i+1
        right=i+2
        node=arrayArbol[i]
        
        if(left<lenArray):
            node.left=arrayArbol[left]
        else:
            node.left=None
            break
            
        if(right<lenArray):
            node.right=arrayArbol[right]
        else:
            node.right=None       
         
    return raiz

print("arbolPersona")
#print(arbolPersona)
print("\n\n")
arrayPersonas = parseArbolToArray(arbolPersona,[])

print("Array original: ")
print(*arrayPersonas)

quickSort(arrayPersonas, 0, len(arrayPersonas) - 1)
print('Luego de ordenar:')
print(*arrayPersonas)
"""
arbolPersonaSorted = parseArrayToArbol(arrayPersonas)
print("\n\n")
print("arbolPersonaSorted")
print(arbolPersonaSorted)
"""