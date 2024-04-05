import time
import random as r
import os

c = [0, 0, 0, 0]
podio = []
meta = 50
loop = True
##UNA VEZ que una caballo llego al podio no se le incrementa mas nada
##U

def esta_en_podio(index):
    resultado = False
    for posicion in podio:
        if index == posicion:
            resultado = True
    return resultado

while loop:
    for i in range(len(c)):
        #r.randint(1,5)
        if c[i] < meta:
            c[i] += r.randint(1,5)
            
        elif not esta_en_podio(i+1):
            podio.append(i+1)
            
        print(f"Caballo {i+1}: {c[i]}mts {"-"*c[i]}█╣")

    time.sleep(1)
    os.system("cls")

    if len(podio) >= len(c):
        loop = False

print("\n-----------PODIO--------------")
for i in range(len(podio)):
    print(f"PUESTO N°{i+1}: CABALLO {podio[i]}")