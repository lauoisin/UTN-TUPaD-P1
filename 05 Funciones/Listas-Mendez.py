#1
multiples_de_4 = list(range(4, 101, 4))
print(multiples_de_4)

#2
mi_lista = ["manzana", "banana", "cereza", "mango", "pera"]
print(mi_lista[-2])

#3
lista_vacia = []

lista_vacia.append("python")
lista_vacia.append("programacion")
lista_vacia.append("UTN")

print(lista_vacia)

#4
animales = ["perro", "gato", "conejo", "pez"]

animales[1] = "loro"

animales[-1] = "oso"

print(animales)

#5
numeros =  [8, 15, 3, 22, 7]
numeros.remove(max(numeros))
print(numeros)

#El siguiente programa crea una lista llamada "numeros" con los valores 8, 15, 3, 22, 7.
#(max(numeros)) busca el mayor valor dentro de la lista, que es el 22.
#En numeros.remove(max(numeros)) remueve el numero 22.
#Luego imprime los numeros restantes [8, 15, 3, 7]

#6
numeros = list(range(10, 31, 5))

print(numeros[:2])

#7
autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "ford"

autos[2] = "peugeot"

print(autos)

#8
dobles = []

dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

print(dobles)

#9
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

compras[2].append("jugo")

indice_fideos = compras[1].index("fideos")
compras[1][indice_fideos] = "tallarines"

compras[0].remove("pan")

print(compras)






