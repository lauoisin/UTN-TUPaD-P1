#1
def imprimir_hola_mundo():
    print("Hola Mundo!")

def main():
    imprimir_hola_mundo()

if __name__ == "__main__":
    main()

#2    
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

def main():
    nombre_usuario = input("Ingrese su nombre: ")
    saludo = saludar_usuario(nombre_usuario)
    print(saludo)

if __name__ == "__main__":
    main() 

#3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

def main():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    edad = input("Ingrese su edad: ")
    residencia = input("Ingrese su lugar de residencia: ")
    
    informacion_personal(nombre, apellido, edad, residencia)

if __name__ == "__main__":
    main()

#4
import math

def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

def main():
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        if radio < 0:
            print("El radio no puede ser negativo.")
            return
        
        area = calcular_area_circulo(radio)
        perimetro = calcular_perimetro_circulo(radio)
        
        print(f"El área del círculo es: {area:.2f}")
        print(f"El perímetro del círculo es: {perimetro:.2f}")
    except ValueError:
        print("Por favor, ingrese un número válido.")

if __name__ == "__main__":
    main()

#5
def segundos_a_horas(segundos):
    return segundos / 3600  # 1 hora = 3600 segundos

def main():
    try:
        segundos = int(input("Ingrese la cantidad de segundos: "))
        if segundos < 0:
            print("Por favor, ingrese un número positivo.")
            return
        horas = segundos_a_horas(segundos)
        print(f"{segundos} segundos son {horas:.2f} horas.")
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()    

#6
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

def main():
    try:
        numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
        tabla_multiplicar(numero)
    except ValueError:
        print("Por favor, ingrese un número entero válido.")

if __name__ == "__main__":
    main()

#7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    # Evitamos división por cero
    division = a / b if b != 0 else "Indefinida (división por cero)"
    return (suma, resta, multiplicacion, division)

def main():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        
        suma, resta, multiplicacion, division = operaciones_basicas(a, b)
        
        print("\nResultados de las operaciones:")
        print(f"Suma: {a} + {b} = {suma}")
        print(f"Resta: {a} - {b} = {resta}")
        print(f"Multiplicación: {a} * {b} = {multiplicacion}")
        print(f"División: {a} / {b} = {division}")
        
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()

#8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

def main():
    try:
        peso = float(input("Ingrese su peso en kilogramos: "))
        altura = float(input("Ingrese su altura en metros: "))
        
        if peso <= 0 or altura <= 0:
            print("El peso y la altura deben ser números positivos.")
            return
        
        imc = calcular_imc(peso, altura)
        print(f"Su índice de masa corporal (IMC) es: {imc:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()

#9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    try:
        celsius = float(input("Ingrese la temperatura en grados Celsius: "))
        fahrenheit = celsius_a_fahrenheit(celsius)
        print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.")

if __name__ == "__main__":
    main()

#10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

def main():
    try:
        a = float(input("Ingrese el primer número: "))
        b = float(input("Ingrese el segundo número: "))
        c = float(input("Ingrese el tercer número: "))
        
        promedio = calcular_promedio(a, b, c)
        print(f"El promedio de los tres números es: {promedio:.2f}")
    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")

if __name__ == "__main__":
    main()    




