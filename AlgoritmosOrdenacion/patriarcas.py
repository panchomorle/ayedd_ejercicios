class familia:
    def __init__(self, valor): #constructor
        # self.n = n 
        self.valor = valor #nombre
        self.hijos = []

patriarca = familia('Abraham')
patriarca.hijos.append(familia('Agar'))
patriarca.hijos.append(familia('Sara'))
patriarca.hijos[0].hijos.append(familia('Ismael'))
patriarca.hijos[1].hijos.append(familia('Isaac'))
patriarca.hijos[1].hijos[0].hijos.append(familia('Rebeca'))
patriarca.hijos[1].hijos[0].hijos[0].hijos.append(familia('Esaú'))
patriarca.hijos[1].hijos[0].hijos[0].hijos.append(familia('Jacob'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos.append(familia('Lea'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos[0].hijos.append(familia('Zabulón'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos[0].hijos.append(familia('Isacar'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos[0].hijos.append(familia('Judá'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos[0].hijos.append(familia('Leví'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos[0].hijos.append(familia('Siméon'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos[0].hijos.append(familia('Rubén'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos.append(familia('Zilpa'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos[1].hijos.append(familia('Gad'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos[1].hijos.append(familia('Aser'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos.append(familia('Raquel'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos[2].hijos.append(familia('José'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos[2].hijos[0].hijos.append(familia('Asenat'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos[2].hijos[0].hijos[0].hijos.append(familia('Manasés'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos[2].hijos[0].hijos[0].hijos.append(familia('Efraín'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos[2].hijos.append(familia('Benjamín'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos.append(familia('Bilha'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos[3].hijos.append(familia('Dan'))
patriarca.hijos[1].hijos[0].hijos[0].hijos[1].hijos[3].hijos.append(familia('Neftalí'))

array = []
def recorrer(r, sangria = 0):
    array.append(r.valor) #agregar cada elemento al array para orderan
    
    print("\n"+"--"*sangria + r.valor, end="") #imprime el valor indentado

    if sangria%2==0: #imprime aclaración
        print("(Padre)", end="")
    else:
        print("(Esposa)", end="")

    sangria += 1  
    for i in r.hijos :
        recorrer(i, sangria)

recorrer(patriarca)

def ordenar_burbuja(lista):
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if lista[j] > lista[j+1]:        
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux  
    for i in lista:
        print (i)

ordenar_burbuja(array)