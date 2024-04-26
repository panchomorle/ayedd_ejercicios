"""usando insert()
usando [] and +
usando Slicing
usando extend()"""

lista = [2,3,4,5]
lista.insert(0, 1) #inserta un 1 en la posicion 0
print(lista)

lista = [2,3,4,5]
lista = [1] + lista
print(lista)

lista= [2,3,4,5]
lista[:0] = [1,8] #li= (start:end:step)
print ("Usando Slicing : " + str(lista))

lista= [2,3,4,5]
x = [1]
x.extend(lista)
lista = x
print(lista)