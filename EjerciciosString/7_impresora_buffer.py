import time

buffer_limit = 20
buffer_impresora = ["D1","D2","D3","D4","D5","D5","D7","D8","D9","D10","D11","D12","D13","D14","D15","D16","D17","D18","D19","D20"]

while True:
    print(
        "A. Agregar\n",
        "I. Imprimir\n",
        "S. Salir\n"
    )
    op = input("Selecciona una opcion: ")
    match op:
        case "A":
            if not len(buffer_impresora)>=buffer_limit:
                x= input("Escribe qué agregar: ")
                buffer_impresora.append(x)
            else:
                print("ERROR, buffer sobrecargado")
        case "I":
            for a in buffer_impresora:
                print("Se imprimió: ",buffer_impresora[0])
                buffer_impresora = buffer_impresora[1:]
                print(buffer_impresora)
                time.sleep(1)
            print("No quedan archivos por imprimir.")
        case "S":
            break

