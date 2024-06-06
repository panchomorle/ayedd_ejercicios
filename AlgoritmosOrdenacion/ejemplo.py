class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def __str__(self):
        return self.nombre+" "+str(self.edad)

lista = [Persona("Pedro", 31), Persona("Blocky", 21), Persona("Furibe", 17), Persona("Gordito", 80), Persona("Jon pol", 40)]

def ordernar_burbuja(lista):
    #el index "i" va a ir aumentando para limitar al siguiente for
    for i in range(len(lista)-1): #in range(7) gives 0 to 6
        for j in range(len(lista)-i-1): # in range(7) gives 0 to 6
                                        # despues 0 to 5, 0 to 4 ...
            if lista[j].edad > lista[j+1].edad: #compara 0-1, 1-2 ... 6-7
                #swap
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1]= aux
                #pythonic way:
                #lista[j], lista[j+1] = lista[j+1], lista[j]

def insertion_sort(array):
    for step in range(1, len(array)):
        #print(step)
        key = array[step]
        j= step - 1

        #Iterará e irá comparando el valor rescatado con cada
        #elemento de la izquierda
        while j>= 0 and key.edad < array[j].edad:
            array[j+1] = array[j]
            j = j - 1
        
        array[j+1] = key

print(*lista)
insertion_sort(lista)
print(*lista)
