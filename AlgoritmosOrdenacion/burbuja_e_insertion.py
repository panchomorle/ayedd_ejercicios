#lista = [6, 5, 3, 1, 8, 7, 2, 4] #len=8

def ordernar_burbuja(lista):
    #el index "i" va a ir aumentando para limitar al siguiente for
    for i in range(len(lista)-1): #in range(7) gives 0 to 6
        for j in range(len(lista)-i-1): # in range(7) gives 0 to 6
                                        # despues 0 to 5, 0 to 4 ...
            if lista[j] > lista[j+1]: #compara 0-1, 1-2 ... 6-7
                #swap
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
                #pythonic way:
                #lista[j], lista[j+1] = lista[j+1], lista[j]

def insertion_sort(array):
    for step in range(1, len(array)):
        #print(step)
        key = array[step] #almaceno el valor en la segunda posicion
        j= step - 1 #almaceno el indice de la primera posicion

        #Iterará e irá comparando el valor rescatado con cada
        #elemento de la izquierda
        while j>= 0 and key < array[j]:
        #si el indice es mayor o igual a 0
        #si el valor de la segunda posicion es menor que el de la primera
            #se copia el valor anterior a la siguiente posicion
            #(se desplaza todo a la derecha)
            #el valor al que se reemplazó no se pierde porque
            #está en la key.
            array[j+1] = array[j] 
            
            j = j - 1 #decrementamos el indice
        
        array[j+1] = key
        #finalmente colocamos la key cuando salimos del while

#ordernar_burbuja(lista)
#print(lista)
