class Animal:
    
    def __init__(self, name):
        self.name = name #atributo público
        self.__age = 0 #atributo privado
        self._tel = 341234124 # atributo protegido

    @staticmethod #static: no hace falta objetos para invocar este metodo
    def autor():
        return "Jon pol Morales"
    
    locomocion = "Acuática"




perro = Animal("Santi")