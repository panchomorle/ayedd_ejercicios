array_alfabeto = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z'] ##MANEJAR LETRAS CON TILDE
alfabeto_len = len(array_alfabeto)#==> 27, simplemente almaceno la longitud del array para reutilizarla

def main():
    bucle = True
    while(bucle):
        print("\n--------------------------------------\n")
        print("0. Cerrar")
        print("1. Cifrar")
        print("2. Descifrar")
        print("3. Bombe machine")
        op = input(" Elige una opción: ")
        if op == '':
            op = 9999
        else:
            op = int(op)
            
        while True:
            match op:
                case 0:
                    bucle = False
                    break
                case 1:
                    frase = input("Ingresa la frase a cifrar: ")
                    desfase = int( input("Ingresa el desfase: "))
                    cifrado(frase, desfase)
                    break
                case 2:
                    frase = input("Ingresa la frase a descifrar: ")
                    desfase = int( input("Ingresa el desfase: "))
                    cifrado(frase, -desfase)
                    break
                case 3:
                    print("\n--------------------------------------")
                    print("La bombe machine descifrará la frase sin saber el desfase.")
                    frase = input("Ingresa la frase a descifrar: ")
                    bombe(frase)
                    break
                case _:
                    print("ERROR: ingrese un valor válido.")
                    break

def cifrado(_frase, _desfase):
    frase = _frase
    desfase = _desfase
    
    if desfase > alfabeto_len-1:                 #manejo que el rotor pueda dar más de 1 vuelta entera
        vueltas = desfase//alfabeto_len     #(cosa que es inútil pero por las dudas)
        desfase = desfase - alfabeto_len*vueltas

    frase_split = list(frase) #list() crea una lista con cada letra del string, incluye espacios

    frase_cifrada = [] #creo una lista vacia
    for i in range(0, len(frase_split), 1): 
        frase_cifrada.append(0) #le agrego celdas en 0 por cada letra de la frase

    for i in range(0, len(frase_cifrada), 1): # 'i' es un index que itera por cada letra de la frase
        for j in range(0, alfabeto_len, 1): # 'j' es un index que itera por cada letra del alfabeto
            
            if frase_split[i] == ' ': #Si habia espacio,
                frase_cifrada[i] = ' ' # habrá espacio
                
            elif frase_split[i] == array_alfabeto[j]: #si en i y j las letras coinciden,
                if j+desfase > alfabeto_len-1: # si al cifrar nos vamos a ir más allá de la z [26],
                    #en la misma posicion que la frase original, la nueva letra será
                    #una letra del alfabeto cuyo indice esté a "desfase" de distancia
                    #pero restamos la longitud del alfabeto para despreciar el sobrepaso
                    frase_cifrada[i] = array_alfabeto[j+desfase - alfabeto_len] 
                else: #si no,
                    frase_cifrada[i] = array_alfabeto[j+desfase] #simplemente agregamos una letra a "desfase" distancia.
                break #agregué el break para dejar de iterar sobre el alfabeto si ya se encontró una letra coincidente en la posición 'j'.
    resultado = ''.join(frase_cifrada)
    print("\n Su resultado es: ", resultado)

"""------------------------------------------------------------------------------------"""

def bombe(_frase):
    frase = _frase
    
    archivo = 'diccionario.txt' #cargo el archivo donde está el diccionario
    #creo el array diccionario con cada palabra existente
    #esto es para comparar las palabras cifradas con palabras reales
    with open(archivo, 'r', encoding='utf8') as file: 
        array_diccionario =[]
        for line in file.readlines(): #file.readlines() => devuelve un array separando por lineas
            palabra = line.rstrip() #line.rstrip limpia un string sacandole los espacios y saltos de linea
            array_diccionario.append(palabra) #agrego cada palabra al array

    diccionario_len = len(array_diccionario)
    #split(caracter, max_split) vacío divide por espacios
    
    frase_split = list(frase) #list() crea una lista con cada letra del string, incluye espacios
    frase_desfasada = [] #creo una lista vacia
    for i in range(0, len(frase_split), 1): 
        frase_desfasada.append(0) #le agrego celdas en 0 por cada letra de la frase

    desfase = 0
    operar = True

    while operar:
        for i in range(0, len(frase_desfasada), 1): # 'i' es un index que itera por cada letra de la frase
            for j in range(0, alfabeto_len, 1): # 'j' es un index que itera por cada letra del alfabeto
                if frase_split[i] == ' ': #Si habia espacio,
                    frase_desfasada[i] = ' ' # habrá espacio
                    break
                elif frase_split[i] == array_alfabeto[j]:
                    if j+desfase > alfabeto_len-1:
                        frase_desfasada[i] = array_alfabeto[j+desfase - alfabeto_len] #####MANEJAR ERROR POR SI DESFASE DA VUELTA EL ALFABETO
                        break
                    else:
                        frase_desfasada[i] = array_alfabeto[j+desfase]
                        break
                        

        array_palabras = ''.join(frase_desfasada).split(' ')
        cant_palabras = len(array_palabras)
        acumulador = 0
        
        for i in range(0, cant_palabras, 1):
            for j in range(0, diccionario_len, 1):
                if array_palabras[i] == array_diccionario[j]:
                    acumulador+=1
                    break

        if acumulador > cant_palabras/2:
            operar = False
            print("Frase descifrada con éxito:")
            print(f"El desfase utilizado fue de {desfase*-1} o {alfabeto_len - desfase}")
            frase_final = ' '.join(array_palabras)
            print(f'La frase es: "{frase_final}"')
        else:
            print(f"Intento n° {desfase}")
            acumulador = 0
            desfase+=1
            if desfase > alfabeto_len-1:
                operar = False
                print("No se ha podido descifrar :C")
            
main()


