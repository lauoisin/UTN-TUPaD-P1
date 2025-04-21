#1
edad = int(input("Ingrese su edad: "))

# Verificar si es mayor de edad
if edad > 18:
    print("Es mayor de edad")

#2
nota = float(input("Ingrese su nota: "))

# Verificar si está aprobado o desaprobado
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

#3
numero = int(input("Ingrese un número: "))

# Verificar si el número es par
if numero % 2 == 0:
    print("Ha ingresado un número par")
else:
    print("Por favor, ingrese un número par")

#4
edad = int(input("Ingrese su edad: "))

# Determinar la categoría según la edad
if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

#5
contrasena = input("Ingrese una contraseña (entre 8 y 14 caracteres): ")

# Verificar la longitud usando len()
if len(contrasena) >= 8 and len(contrasena) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#6
import random
from statistics import mode, median, mean


def calcularSesgos():
    numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)

    print(f"Media: {media}, Mediana: {mediana}, Moda: {moda}")

    if media > mediana > moda:
        print("Sesgo positivo (a la derecha)")
    elif media < mediana < moda:
        print("Sesgo negativo (a la izquierda)")
    else:
        print("Sin sesgo")

#7
texto = input("Ingrese una frase o palabra: ")

# Verificar si termina con una vocal (mayúscula o minúscula)
if texto.lower().endswith(('a', 'e', 'i', 'o', 'u')):
    texto += '!'
    
# Imprimir el resultado
print(texto)

#8
nombre = input("Ingrese su nombre: ")

# Mostrar opciones
print("Seleccione una opción:")
print("1. Nombre en MAYÚSCULAS")
print("2. Nombre en minúsculas")
print("3. Nombre con la Primera Letra en mayúscula")

# Solicitar la opción
opcion = input("Ingrese 1, 2 o 3: ")

# Transformar el nombre según la opción elegida
if opcion == "1":
    print(nombre.upper())
elif opcion == "2":
    print(nombre.lower())
elif opcion == "3":
    print(nombre.title())
else:
    print("Opción inválida. Por favor ingrese 1, 2 o 3.")

#9
def determinarMagnitudTerremoto():
    magnitud = float(input("Ingrese la magnitud del terremoto: "))
    if magnitud < 3:
        print("Muy leve")
    elif 3 <= magnitud < 4:
        print("Leve")
    elif 4 <= magnitud < 5:
        print("Moderado")
    elif 5 <= magnitud < 6:
        print("Fuerte")
    elif 6 <= magnitud < 7:
        print("Muy Fuerte")
    else:
        print("Extremo")


#10
def determinarEstacionDelAño():
    hemisferio = input("¿En qué hemisferio se encuentra? (N/S): ").upper()
    mes = input("Ingrese el mes del año (ej. marzo): ").lower()
    dia = int(input("Ingrese el día del mes: "))

    # Convertir mes a número
    meses = {
        "enero": 1, "febrero": 2, "marzo": 3, "abril": 4,
        "mayo": 5, "junio": 6, "julio": 7, "agosto": 8,
        "septiembre": 9, "octubre": 10, "noviembre": 11, "diciembre": 12
    }
    m = meses.get(mes, 0)

    # Clasificar la estación
    if (m == 12 and dia >= 21) or (1 <= m <= 2) or (m == 3 and dia <= 20):
        estacion = "Invierno" if hemisferio == "N" else "Verano"
    elif (m == 3 and dia >= 21) or (4 <= m <= 5) or (m == 6 and dia <= 20):
        estacion = "Primavera" if hemisferio == "N" else "Otoño"
    elif (m == 6 and dia >= 21) or (7 <= m <= 8) or (m == 9 and dia <= 20):
        estacion = "Verano" if hemisferio == "N" else "Invierno"
    elif (m == 9 and dia >= 21) or (10 <= m <= 11) or (m == 12 and dia <= 20):
        estacion = "Otoño" if hemisferio == "N" else "Primavera"
    else:
        estacion = "Fecha inválida"

    print(f"Estación: {estacion}")
