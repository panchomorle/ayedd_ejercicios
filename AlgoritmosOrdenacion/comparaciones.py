from burbuja_e_insertion import ordernar_burbuja, insertion_sort
from quick_sort import quickSort
import random

#generar array desordenado de 10000 elementos
array = [random.randint(0, 999) for _ in range(10000)]

print("array generado con éxito")

print(array)
quickSort(array)
#ordernar_burbuja(array)
#insertion_sort(array)
print(array)

