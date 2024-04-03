"""Escriba una función que recibiendo del usuario un número hasta el 1000 lo convierta en
número romano y muestre el resultado por pantalla.
Para la solución observe que a los números enteros en la lista N corresponden respectivamente
los números romanos en la lista R
N: 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1
R: M, CM, D, CD, C, XC, L, XL, X, IX, V, IV, I"""
def convertir_a_romanos():
    matriz =[
            [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1],
            ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
            ]

    nro = int(input("Ingrese un numero del 1 al 1000: "))
    calcular = True

    if nro < 1 or nro > 1000: #Manejo de núms válidos
        print("ERROR: ingrese un número válido")
        calcular = False

    resultado = ""
    i = 0
    while calcular:
        divisor = matriz[0][i]
        letra = matriz[1][i]

        if nro >= divisor:
            cociente = nro // divisor
            resto = nro%divisor
            resultado+=letra*cociente

            nro = resto
        if i+1 == len(matriz[0]):
            break
        i+=1

    print(resultado)

convertir_a_romanos()