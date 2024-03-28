a = ["uno", "dos"]

print(id(a))
#2001550293568

b = a  #apunta a la misma ubicacion de memoria
x = a.copy() #me crea una nueva direccion de memoria

print(id(b))
#2001550293568

a[0] = "tres"
print(b)
#["tres", "dos"]
#por mas de que printeo b, me sigue referenciando "a", el cual cambió

print(id(x))
#2247459012544
print(x)
#["uno", "dos"]
