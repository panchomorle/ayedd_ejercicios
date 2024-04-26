def suma_digitos(n):
    acumulador = 0
    for s in n:
        acumulador+= int(s)
    return acumulador

while True:
    try:
        number = input("Ingrese un entero mayor a 0: ")
        
        if float(number)!=round(float(number)):
            raise Exception("Número invalido, no es entero")
        elif int(number)<=0:
            raise Exception("Número inválido, no es mayor que cero")
        else:
            print(f"La suma de los dígitos de {number} es: {suma_digitos(number)}")
            break
    except Exception as e:
        print(e)