from localidades import data

provincias = {}

for local in data["localidades"]:
    if not local["provincia"]["nombre"] in provincias:
        provincias[local["provincia"]["nombre"]] = 1
    else:
        provincias[local["provincia"]["nombre"]] +=1

for provincia, cantidad in provincias.items():
    print(f"{provincia} tiene {cantidad} localidades")

print("-"*15)
##PROVINCIAS ORDENADAS DE MAS A MENOS LOCALIDADES
provincias = sorted(provincias.items(), key=lambda tupla: tupla[1], reverse=True)

provincias = dict(provincias)
for provincia, cantidad in provincias.items():
    print(f"{provincia} tiene {cantidad} localidades")
