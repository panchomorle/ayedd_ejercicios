class Posicion:
    """
        Esta clase gestiona la posición inicial del rotor:
        Un rotor respecto de la entrada de la derecha va cambiando a medida que 
        gira.
        Cuando la posición inicial del rotor en el "visor" es "A" entonces coincide
        con la permutación de letras puras del rotor (por ejemplo rotor V si la
        entrada es C la salida es R (no olvidar que antes de calcular hay que rotar una posición))
        Si la posicion inicial del rotor es B ya queda desfazada de la entrada un lugar:
        por ejemplo para el Rotor_V si la entrada es C la salida es G (no olvidar rotar una posición antes de calcular).
    """
    abecedario = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]    
    x = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    posicion_inicial = "A"
    
    def __init__(self, letra):
        self.posicion_inicial = letra
        self.reset()
        #print(self.abecedario)
        #print(self.x)
        #print("---")
        
    def reset(self):
        self.x = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        for pos, l in enumerate(self.abecedario):
            if self.posicion_inicial == l:
                for i in range(pos):
                    self.rotar()
                break
                        
    def rotar(self):
        self.x.append(self.x[0])
        del self.x[0]
    
    def calcular_entrada_real(self, letra):
        for pos, l in enumerate(self.abecedario):
            if letra == l:
                return self.x[pos]
    def calcular_salida_real(self, letra):
        for pos, l in enumerate(self.x):
            if letra == l:
                return self.abecedario[pos]        

class Rotor_V:
    """
        Esta clase tiene toda la funcionalidad y combinación de la permutación propia del Rotor_V histórico
        (https://en.wikipedia.org/wiki/Enigma_rotor_details)
    """
    posicion = None
    entrada = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    salida = ["V", "Z", "B", "R", "G", "I", "T", "Y", "U", "P", "S", "D", "N", "H", "L", "X", "A", "W", "M", "J", "Q", "O", "F", "E", "C", "K"]
        
    def __init__(self, pos_inicial="A"):
        self.posicion = Posicion(pos_inicial)

    def directa(self, letra):
        letra = self.posicion.calcular_entrada_real(letra)
        for pos, l in enumerate(self.entrada):
            if letra == l:
                letra = self.salida[pos]
                break
        return letra
    
    def inversa(self, letra):        
        for pos, l in enumerate(self.salida):
            if letra == l:
                letra = self.entrada[pos]
                break
        letra = self.posicion.calcular_salida_real(letra)
        return letra
        
#------------------------------------------------------------------
#Pruebas varias

#Inicialiar el Rotor_V y arranca en la posición B        
s3 = Rotor_V("B")

frase = input("Ingrese una frase: ").upper()

# Como cifrar una frase con un solo rotor---------------------------
cifrado = ""
for letra in frase:
    if letra != " ":
        s3.posicion.rotar()
        cifrado += s3.directa(letra)
    else:
        cifrado += " "

print("Frase cifrada: " + cifrado)

# Como descifrar una frase con un solo rotor-------------------------
# Antes de descifrar volver a su posición inicial el rotor
s3.posicion.reset()

descifrado = ""
for letra in cifrado:
    if letra != " ":
        s3.posicion.rotar()
        descifrado += s3.inversa(letra)
    else:
        descifrado += " "
        
print("Descifrado: " + descifrado)


