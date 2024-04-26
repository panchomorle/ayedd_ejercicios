import time
import random as r
import os

caballos = {"caballo1":0, "caballo2":0,"caballo3":0,"caballo4":0}
podio = []
meta = 20
while True:
    for k, v in caballos.items():
        if v < meta:
            caballos[k] += r.randint(1,5)
        elif not k in podio:
            podio.append(k)
        print(f"{k}: {v}mts {'-'*v}")
    time.sleep(1)
    os.system("cls")
    if len(podio)>=4:
        break

print(f"{'-'*10}PODIO{'-'*10}")
for i, pos in enumerate(podio):
    print(f"puesto N°{i+1}: {pos} con {caballos[pos]}mts")
