from localidades import data

nombre = input("Donde queda la localidad: ")
localidad = {}

for local in data["localidades"]:
    if local["nombre"]== nombre:
        localidad = local

print(f"{localidad["nombre"]} queda en {localidad["provincia"]["nombre"]}")

provincia = input("Mostrar localidades de: ")

for local in data["localidades"]:
    if local["provincia"]["nombre"] == provincia:
        print("-"*10)
        print(f"{local["nombre"]}, depto: {local["departamento"]["nombre"]}")


