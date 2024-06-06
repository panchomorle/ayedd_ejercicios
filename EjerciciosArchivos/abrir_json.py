import json

data = {}

with open(r"EjerciciosArchivos\localidades.json", 'r', encoding="utf8") as archivo:
    data = json.load(archivo)

array_provincias = []

for local in data["localidades"]:
    provincia = local["provincia"]
    if not provincia in array_provincias:
        array_provincias.append(provincia)

#print(array_provincias)
#print(len(array_provincias))

with open(r"EjerciciosArchivos\provincias.json", 'w', encoding="utf8") as archivo:
    #archivo.write(json.dumps(array_provincias))
    json.dump(array_provincias, archivo)
    print("Se escribió correctamente capo")