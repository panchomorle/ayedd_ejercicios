#1
a = int(input("1. Ingrese un numero A: "))
if(a%2==0):
    print("el numero ingresado es PAR")
else: print("el numero ingresado es IMPAR")

#2
edad1 = int(input("2. Ingresar edad de persona 1: "))
edad2 = int(input("Ingresar edad de persona 2: "))
print(edad1>edad2)

#3
p1 = int(input("3. Ingresar edad de persona 1: "))
p2 = int(input("Ingresar edad de persona 2: "))
p3 = int(input("Ingresar edad de persona 3: "))
pueden_viajar = p1>=18 or p2>=18 or p3>=18
print("Pueden viajar?: "+str(pueden_viajar))

#4
pueden_mirar_peli = p1>=18 and p2>=18 and p3>=18
print("Pueden mirar la peli?: "+str(pueden_mirar_peli))

#5
A = int(input("Ingrese un numero A: "))
B = int(input("Ingrese un numero B: "))
print(!(A%2==0 and B%2==0))

#6
diarios=int(input("Cuantos cigarrillos fuma por dia?: "))
dias_fumando=int(input("Hace cuantos años fuma?: "))*365
cigarros_fumados=dias_fumando*diarios
minutos_perdidos=cigarros_fumados*10
dias_perdidos=(minutos_perdidos/60)/24
print("usted ha perdido {0} dias de vida".format(dias_perdidos))

#7
print("O'Reilly Media, antes llamada O'Reilly & Associates, es una empresa editorial estadounidense fundada y dirigida por Tim O'Reilly que está principalmente enfocada a libros de tecnología e informática.")

#8
var_1= "O'Reilly Media, antes llamada O'Reilly & Associates, es una empresa editorial estadounidense fundada y dirigida"
var_2= " por Tim O'Reilly que está principalmente enfocada a libros de tecnología e informática."
print(var_1, var_2)

#9
nombre = "juan"
edad = 19
disci = "ingeniero"
anio = 2024
print(nombre, edad, disci, anio, sep = " - ")

#10
print("{0} - {1} - {2} - {3}".format(nombre, edad, disci, anio))


