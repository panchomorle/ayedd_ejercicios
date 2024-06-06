"""
Una empresa de transporte de carga que cuenta con vehículos propios así como vehículos
tercerizados organiza su sistema financiero en centros de costo, donde cada centro de
costo puede tener varios vehículos agregados u otros centros de costo.  Un vehículo
pertenece a un centro de costo, y es el único que genera gastos y facturación.
Un centro de costo representa a una empresa de terceros o la propia empresa que gestiona todas las demás.

a.	Haga una representación gráfica de esta estructura organizacional, utilizando listas
enlazadas para que pueda calcular los gastos/facturación para toda la organización,
así como para un único centro de costos.

b.	Haga una función recursiva para calcular el facturación de la organización.

"""

class CentroDeCosto:
    def __init__(self, ingresos, gastos):
        self.gastos = gastos
        self.ingresos = ingresos

    def __str__(self):
        return f'Node es solo Centro de Costo'

    def calcular_gastos(self):
        return self.gastos

    def calcular_ingresos(self):
        return self.ingresos

class Empresa(CentroDeCosto):
    centros_de_costos = []

    def __init__(self, ingresos, gastos, centros_de_costos):
        super().__init__(ingresos, gastos)
        self.centros_de_costos = centros_de_costos

    def __str__(self):
        return "Node es una Empresa"

    def calcular_gastos(self):
        gastos_total = 0

        for i in self.centros_de_costos:
            gastos_total = gastos_total + i.calcular_gastos()

        self.gastos=gastos_total

        return self.gastos

    def calcular_ingresos(self):
        ingresos_total = 0

        for i in self.centros_de_costos:
            ingresos_total = ingresos_total + i.calcular_ingresos()

        self.ingresos = ingresos_total

        return ingresos_total

class Veiculo(CentroDeCosto):

    def __init__(self, ingresos, gastos, patente_vehiculo):
        super().__init__(ingresos, gastos)
        self.patente_vehiculo = patente_vehiculo

    def __str__(self):
        return f'Veiculo: {self.patente_vehiculo}'



veiculo1 = Veiculo( 1000, 300,"PCN 1A27")
veiculo2 = Veiculo( 400, 5000,"PCN 2222")
veiculo3 = Veiculo( 3000, 200,"PCN 3333")
veiculo4 = Veiculo( 1000, 300,"PCN 4444")
veiculo5 = Veiculo( 400, 5000,"PCN 5555")
veiculo6 = Veiculo( 3000, 200,"PCN 6666")
veiculo7 = Veiculo( 1000, 300,"PCN 7777")
veiculo8 = Veiculo( 400, 5000,"PCN 8888")
veiculo9 = Veiculo( 3000, 200,"PCN 9999")
veiculo10 = Veiculo( 1000, 300,"PCN 1010")
veiculo11 = Veiculo( 430, 5050,"PCN 1111")
veiculo12 = Veiculo( 3020, 200,"PCN 1212")

empresa3 = Empresa(0,0,[veiculo8, veiculo9, veiculo10] )
empresa5 = Empresa(0,0,[veiculo11, veiculo12] )
empresa4 = Empresa(0,0,[empresa5, veiculo6, veiculo7] )
empresa1 = Empresa(0,0,[veiculo3, empresa3] )
empresa2 = Empresa(0,0,[veiculo4, veiculo5, empresa4] )
organizacion = Empresa(0,0,[empresa1, empresa2, veiculo1, veiculo2])

print(f'Organizacion gastos: { organizacion.calcular_gastos() }')
print(f'Organizacion ingressos: { organizacion.calcular_ingresos() }')

