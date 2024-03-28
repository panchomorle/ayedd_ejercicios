archivo = 'diccionario.txt' #cargo el archivo donde está el diccionario
array_alfabeto = ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
alfabeto_len = len(array_alfabeto)#==> 27
#creo el array diccionario con cada palabra existente
#esto es para comparar las palabras cifradas con palabras reales
with open(archivo, 'r', encoding='utf8') as file: 
    array_diccionario =[]
    for line in file.readlines(): #file.readlines() => devuelve un array separando por lineas
        palabra = line.rstrip() #line.rstrip limpia un string sacandole los espacios y saltos de linea
        array_diccionario.append(palabra) #agrego cada palabra al array
        
frase = input("Ingresa la frase a cifrar: ")
desfase = int( input("Ingresa el desfase: "))

if desfase > alfabeto_len-1:
    vueltas = desfase//alfabeto_len
    desfase = desfase - alfabeto_len*vueltas

frase_split = list(frase) #list() crea una lista con cada letra del string, incluye espacios
print(frase_split)

frase_cifrada = [] #creo una lista vacia

for i in range(0, len(frase_split), 1): 
    frase_cifrada.append(0) #le agrego celdas en 0 por cada letra de la frase

for i in range(0, len(frase_cifrada), 1):
    for j in range(0, alfabeto_len, 1):
        
        if frase_split[i] == ' ':
            frase_cifrada[i] = ' '
        elif frase_split[i] == array_alfabeto[j]:
            if j+desfase > alfabeto_len-1: #mayor a 26
                frase_cifrada[i] = array_alfabeto[(j - alfabeto_len)+desfase]
            else:
                frase_cifrada[i] = array_alfabeto[j+desfase]
            break

print(''.join(frase_cifrada))
