"""Dos amigos están a jugar y propusieron escribir una carta donde todas las vocales están
cambiadas por números, uno escribe la carta y el otro tiene que traducir para español. Las
vocales aeiou estarán cambiadas por 49271. En la solución el usuario informa el texto a
traducir y su programa deberá tener una función que recibe una string como parámetro
obligatorio, esta string será la carta, y retorna otra string que será la carta en su idioma
original. La traduciõn debe ser impressa en pantalla"""

import copy
vocal = ['a','e','i','o','u']

def vocales(msg: str):
    cifra_vocal = ['4','9','2','7','1']

    carta_descifrada = copy.copy(msg)
    for j, num in enumerate(cifra_vocal):
        carta_descifrada = carta_descifrada.replace(num, vocal[j]) #1st parameter -> target; 2nd parameter -> new value
    return carta_descifrada

"""Considerando la cuestión anterior, los amigos ahora cambiaron la codificación, haga las
alteraciones necesarias para que la función reciba ahora dos parámetros uno obligatorio y
string, el otro también una string pero que por defecto será 49271. La solución deberá buscar
para cada número del texto su letra correspondiente utilizando la posición de la letra, o sea
aeiou corresponde a los caracteres de la string código C0C1C2C3C4, por defecto tenemos a=4, e=9,
i=2, o=7, u= 1. La tradición debe ser mostrada en pantalla y el usuario elegir si quiere informar
o no una nueva codificación."""

def vocales2(msg: str, code: str = "49271"):
    
    carta_descifrada = copy.copy(msg)
    for j, num in enumerate(code):
        carta_descifrada = carta_descifrada.replace(num, vocal[j])
    
    return carta_descifrada

#49271
#L7s c4s7s 9sp9c24l9s n7 s7n l7 s1f2c29nt9m9nt9 9sp9c24l9s p4r4 r7mp9r l4s r9gl4s 
mensaje = input("Introduzca la carta: ")
print(vocales(mensaje))

#59713
#L1s c5s1s 9sp9c75l9s n1 s1n l1 s3f7c79nt9m9nt9 9sp9c75l9s p5r5 r1mp9r las r9gl5s.
mensaje = input("Introduzca otra carta: ")
codigo = input("Introduzca el código: ")
print(vocales2(mensaje, codigo))