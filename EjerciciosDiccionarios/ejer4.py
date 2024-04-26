"""Buscar otro dataset JSON en https://datos.gob.ar a gusto y procesar algo de tu interes"""

from proyectos_2019 import proyectos

##for que itera sobre la lista de proyectos para saber cuantos proyectos son del CONICET
cant_proyectos = 0
cant_proyectos_conicet = 0
for proyect in proyectos["data"]:
    cant_proyectos+=1
    if proyect["proyecto_fuente"] == "CONICET":
        cant_proyectos_conicet +=1

print(f"la cantidad de proyectos totales es de {cant_proyectos}")
print(f"la cantidad de proyectos del CONICET es de {cant_proyectos_conicet}")
print(f"Eso es el {cant_proyectos_conicet/cant_proyectos*100}% de los proyectos")
print("-"*15)

total_invertido = 0.00
for proyect in proyectos["data"]:
    total_invertido+=proyect["monto_total_adjudicado"]

print(f"Por lo tanto el CONICET ha recibido en el año 2019 un total de {total_invertido/1000000} MILLONES de pesos")