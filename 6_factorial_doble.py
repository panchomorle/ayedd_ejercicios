def fact_doble(n):
    if n==1:
        return 1
    
    resul = 1
    while n>1:
        resul *= n
        n = n-2
    return resul

def fact_doble2(n): ##supongamos que ingresa 7
    if n==1:
        return 1
    
    aux = n-2 #5
    while aux>1:
        n = n*aux #7x5
        aux = aux-2 #3
    return n

while True:

    number = int(input("Ingrese un numero impar: "))

    try:
        if number%2==0 and number<0:
            raise Exception("El número introducido no es positivo ni impar")
        elif number%2==0:
            raise Exception("El número introducido no es impar")
        elif number<0:
            raise Exception("El número introducido no es positivo")
        else:
            print(f"El factorial doble de {number} es: {fact_doble2(number)}")
            break
    except Exception as e:
        print(e)