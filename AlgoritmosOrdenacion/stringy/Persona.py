class Persona:
    nome = None
    edad = None
    left = None
    right = None

    def __init__(self, nome, edad):
        self.nome = nome
        self.edad = edad

    def __str__(self):
        return self.nome + "," + str(self.edad)

    #llamado por el operador ==
    def __eq__(self, otra_persona):
        return self.edad == otra_persona.edad

    #llamado por el operador !=
    def __ne__(self, otra_persona):
        return self.edad != otra_persona.edad

    #llamado por el operador >
    def __gt__(self, otra_persona):
        return self.edad > otra_persona.edad

    #llamado por el operador <
    def __lt__(self, otra_persona):
        return self.edad < otra_persona.edad

    #llamado por el operador >=
    def __ge__(self, otra_persona):
        return self.edad >= otra_persona.edad

    #llamado por el operador <=
    def __le__(self, otra_persona):
        return self.edad <= otra_persona.edad


# crea la arbol del ejercicio
#nivel 5
node19 = Persona("P19",19)
node21 = Persona("P21",21)
node2 = Persona("P2",2)
node13 = Persona("P13",13)
node10 = Persona("P10",10)
node16 = Persona("P16",16)

#nivel 4
node15 = Persona("P15",15)
node15.left=node19

node20 = Persona("P20",20)
node20.left=node21

node3 = Persona("P3",3)
node3.left=node2

node1 = Persona("P1",1)

node4 = Persona("P4",4)
node4.left=node13

node14 = Persona("P14",14)
node14.left=node10

node17 = Persona("P17",17)
node17.left=node16

node18 = Persona("P18",18)

#nivel 3
node11 = Persona("P11",11)
node11.left=node15
node11.right=node20

node7 = Persona("P7",7)
node7.left=node3
node7.right=node1

node6 = Persona("P6",6)
node6.left=node4
node6.right=node14

node12 = Persona("P12",12)
node12.left=node17
node12.right=node18

#nivel 2
node9 = Persona("P9",9)
node9.left=node11
node9.right=node7

node5 = Persona("P5",5)
node5.left=node6
node5.right=node12

#nivel 1
node8 = Persona("P8",8)
node8.left=node9
node8.right=node5

raiz = node8




