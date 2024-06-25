"""
Dada la siguiente información construir utilizando POO las instacias correspondientes y ponerlas dentro de una lista. Luego ordenar la lista utilizando el método que te tocó en el papel según promedio de cantidad de goles por partido

Jugadores selección:
1) Messi:
    * Peso: 70KG
    * Goles: 1000
    * Partidos: 800
    
2) DiMaría:
    * Peso: 73KG
    * Goles: 700
    * Partidos: 900
    
3) Martinez:
    * Peso: 91KG
    * Goles: 0
    * Partidos: 200
    
4) Paredes:
    * Peso: 82KG
    * Goles: 50
    * Partidos: 450
"""
class Jugador:
    def __init__(self, nombre, peso, goles, partidos):
        self.nombre = nombre
        self.peso = peso
        self.goles = goles
        self.partidos = partidos

    def __str__(self) -> str:
        return self.nombre+" "+str(round(self.promedioGoles(), 2))
    
    def promedioGoles(self):
        return self.goles/self.partidos

    def __lt__(self, jugador):
        return self.promedioGoles() < jugador.promedioGoles()
    
jugadores = [Jugador("Messi", "70KG", 1000, 800),
             Jugador("DiMaría", "73KG", 700, 900),
             Jugador("Martinez", "91KG", 0, 200),
             Jugador("Paredes", "82KG", 50, 450),]

def mergeSort(array):
    if len(array) > 1:
        #FASE de dividir el array en 2 partes
        
        # middle es el puntero donde el array es dividido en 2 subarrays
        middle = len(array) // 2
        L = array[:middle] #mitad izquierda
        R = array[middle:] #mitad derecha

        # Ordenar las 2 mitades
        mergeSort(L)
        mergeSort(R)
        
        #FASE de hacer el merge de los subarrays

        # necesitamos 3 punteros:
        # 2 para para ir señalando elementos en los subarrays (mitades)
        # y un 3ro para usar con el el array combinado resultante
        i = j = k = 0


        # Recorrer tanto el subarrays L como M hasta alcanzar el final de alguno
        # de ellos. Compara el elemento de L contra el de M y reubicar en el
        # array general
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i]
                i += 1
            else:
                array[k] = R[j]
                j += 1
            k += 1

        # Pasamos los restantes elemenos de L al array general 
        # (en el caso que M tenga menos elementos que L)
        while i < len(L):
            array[k] = L[i]
            i += 1
            k += 1

        # Lo mismo que lo anterior pero si M tenía más elementos que L
        while j < len(R):
            array[k] = R[j]
            j += 1
            k += 1

print(*jugadores)
mergeSort(jugadores)
print(*jugadores)