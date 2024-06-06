"""
7) Una empresa de transporte de carga que cuenta con vehículos propios
así como vehículos tercerizados organiza su sistema financiero en
centros de costo, donde cada centro de costo puede tener varios
vehículos agregados u otros centros de costo. Un vehículo pertenece a
un centro de costo, y es el único que genera gastos y facturación. Un
centro de costo representa a una empresa de terceros o la propia
empresa que gestiona todas las demás.
a. Haga una representación gráfica de esta estructura
organizacional, utilizando listas enlazadas para que pueda
calcular los gastos/facturación para toda la organización, así
como para un único centro de costos.
b. Haga una función recursiva para calcular el facturación de la
organización.  
"""
class Empresa:
    def __init__(self, letra):
        self.letra = letra
        self.siguiente_letra = None