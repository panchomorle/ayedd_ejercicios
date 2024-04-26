"""#Listar todas las localidades por de bajo de la latitud -31."""
from localidades import data

surenias = {}

for local in data["localidades"]:
    if local["centroide"]["lat"] < -31:
        surenias[local["nombre"]] = local["centroide"]["lat"]

"""
for localidad, latitud in surenias.items():
    print(f"{localidad} está en la latitud: {latitud}")
"""
#ordenacion de más al norte a más al sur:
sorted_surenias = sorted(surenias, key= lambda item: surenias[item], reverse=True)

for k in sorted_surenias:
    print(k," ",surenias[k])