#1
for x in range (0,101):
    print ("Printing numbers:",x)

#2
n = int(input("Ingresa un numero: "))
i = 0

while n > 0:
    n = n // 10
    i += 1
print (f"El numero tiene {i} digitos")

#3
valor1 = int(input("Ingresa el primer valor entero: "))
valor2 = int(input("Ingresa el segundo valor entero: "))

if valor1 < valor2:
    inicio = valor1 + 1
    fin = valor2
else:
    inicio = valor2 + 1
    fin = valor1

suma = 0
for numero in range(inicio, fin):
    suma += numero
suma = sum(range(inicio, fin))

print(f"La suma de los números entre {valor1} y {valor2}, excluyéndolos, es: {suma}")

#4
n = 1
suma = 0
while n != 0:
    n = int(input("Ingrese un numero: "))
    suma += n
print(f"La suma de los numeros es: {suma}")

#5
import random

intervalo = range (0,9)
solucion = random.choice(intervalo) 
print(f"Voy a pensar un numero del 0 al 9, trata de adivinarlo")

intento = int(input("Introduce tu intento: "))

while intento != solucion:
    if intento > solucion:
        print(f"Demasiado grande, intentalo con un numero mas pequeño")
        intento = int(input("Introduce tu intento: "))
    else:
        print(f"Demasiado pequeño, intentalo con un numero mas grande")
        intento = int(input("Introduce tu intento: "))

if intento == solucion:
    print(f"Muy bien, lo has adivinado: ")

#6
x = 0 
while x <= 100:
    if x % 2 == 0:
        print(x)
    x += 1

#7
n = int(input("Ingresa un numero: "))
for i in range(1, n+1):
    if i % 2 == 0:
        print(i)

#8
cantidad_numeros = 100 

pares = 0 
impares = 0 
positivos = 0 
negativos = 0

print(f"Ingresa {cantidad_numeros} numeros enteros: ")

for i in range(cantidad_numeros):
    numero = int(input(f"Ingresa el numero {i + 1}: "))

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"\nResultados:")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")

#9
cantidad_numeros = 100

suma = 0 

print(f"Ingresa {cantidad_numeros} numeros enteros:")

for i in range (cantidad_numeros):
    numero = int(input(f"Ingresa el número {i + 1}: "))
    suma += numero

media = suma / cantidad_numeros

print(f"\nLa media de los números ingresados es: {media}")

#10
numero_absoluto = abs(numero)

numero_invertido = 0

while numero_absoluto > 0:
    digito = numero_absoluto % 10  
    numero_invertido = numero_invertido * 10 + digito  
    numero_absoluto //= 10  

if numero < 0:
    numero_invertido = -numero_invertido

print(f"El número invertido es: {numero_invertido}")








