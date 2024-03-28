fib1= 0
fib2 = 1

cant = int(input("Ingrese la cantidad de numeros a imprimir: "))
count=0

secuencia = ""

while count <cant:
    if count%2==0 or count==0:
        secuencia+=str(fib1)+" -> "
        fib1 = fib1 + fib2
    else:
        secuencia+=str(fib2)+" -> "
        fib2 = fib1 + fib2
    count+=1

print(secuencia)
