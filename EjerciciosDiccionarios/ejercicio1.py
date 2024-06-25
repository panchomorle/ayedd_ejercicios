from localidades import data

localidades = []

for index in range(len(data["localidades"])):
    if data["localidades"][index]["provincia"]["nombre"] == "Entre Ríos":
        #print(data["localidades"][index]["nombre"])
        localidades.append(data["localidades"][index]["nombre"])

print(localidades)