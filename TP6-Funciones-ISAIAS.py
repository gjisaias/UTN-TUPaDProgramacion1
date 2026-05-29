#Actividad 1 - Crear una función llamada imprimir_hola_mundo que imprima por pantalla
#el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa
#principal.

#Definir funcion
def imprimir_hola_mundo():
    print("Hola Mundo!")

#Programa principal
imprimir_hola_mundo()

#Actividad 2 - Crear una función llamada saludar_usuario(nombre) que reciba como
#parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si
#se llama con saludar_usuario("Marcos"), deberá de- volver: “Hola Marcos!”.
#Llamar a esta función desde el programa principal solicitando el nombre al
#usuario.

#Definir funcion
def saludar_usuario(nombre):
    print(f"Hola {nombre} !")

#Programa principal
nombre=input("Ingrese su nombre: ")
saludar_usuario(nombre)

#Actividad 3 - Crear una función llamada informacion_personal(nombre, apellido, edad,
#residencia) que reciba cuatro parámetros e imprima: “Soy [nombre]
#[apellido], tengo [edad] años y vivo en [residencia]”. Pe- dir los datos al
#usuario y llamar a esta función con los valores in- gresados.

#Definir funcion
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")

#Programa principal
nombre=input("Ingrese su nombre: ")
apellido=input("Ingrese su apellido: ")
edad=input("Ingrese su edad: ")
residencia=input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#Actividad 4 - Crear dos funciones: calcular_area_circulo(radio) que reciba el ra- dio
#como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuel- va el
#perímetro del círculo. Solicitar el radio al usuario y llamar am- bas
#funciones para mostrar los resultados.

#Definir funcion
def calcular_area_circulo(radio):
    import math
    return math.pi * radio**2

#Programa principal
radio=float(input("Ingrese el radio del circulo: "))
area=calcular_area_circulo(radio)
print(f"El area del circulo es: {area}")

#Actividad 5 - Crear una función llamada segundos_a_horas(segundos) que reciba una
#cantidad de segundos como parámetro y devuelva la cantidad de horas
#correspondientes. Solicitar al usuario los segundos y mos- trar el resultado
#usando esta función.

#Definir funcion
def segundos_a_horas(segundos):
    return (segundos / 60)/60

#Programa principal
segundos=float(input("Ingrese los segundos a convertir en horas: "))
horas=segundos_a_horas(segundos)

print(f"La cantidad de segundos ingresados corresponden a {horas:.2f} hora/s:")

#Actividad 6 - Crear una función llamada tabla_multiplicar(numero) que reciba un número
#como parámetro y imprima la tabla de multiplicar de ese número del 1 al
#10. Pedir al usuario el número y llamar a la función.

#Definir funcion
def tabla_multiplicar(numero):
    for i in range (1,11):
        tabla = i*numero
        print(f"{numero} x {i} = {tabla}")

#Programa principal
numero=int(input("Ingrese el numero del que quiere saber la tabla:"))
tabla=tabla_multiplicar(numero)

#Actividad 7 - Crear una función llamada operaciones_basicas(a, b) que reciba dos
#números como parámetros y devuelva una tupla con el resulta- do de
#sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los re- sultados de
#forma clara.

#Definir funcion
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicar = a * b
    dividir = a / b
    return suma, resta, multiplicar, dividir

#Programa principal
a = int(input("Ingrese primer valor: "))
b = int(input("Ingrese segundo valor: "))

suma, resta, multiplicar, dividir = operaciones_basicas(a, b)

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicar}")
print(f"División: {dividir}")

#Actividad 8 - Crear una función llamada calcular_imc(peso, altura) que reciba el peso en
#kilogramos y la altura en metros, y devuelva el índice de masa corporal
#(IMC). Solicitar al usuario los datos y llamar a la fun- ción para mostrar el
#resultado con dos decimales.

#Definir funcion
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    print(f"Tu IMC es: {imc:.2f}")

#Programa principal    
peso = float(input("Ingresa tu peso corporal en kgs: "))
altura = float(input("Ingresa tu altura en metros: "))
imc = calcular_imc(peso, altura)

#Actividad 9 - Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una
#temperatura en grados Celsius y devuelva su equivalente en Fahrenheit.
#Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la
#función.

#Definir funcion
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5 + 32)
    return fahrenheit

#Programa principal
celsius=float(input("Ingrese valor en grados celsius: "))
resultado=celsius_a_fahrenheit(celsius)
print(f"{celsius} grados celsius corresponden a {resultado} grados fahrenheit")

#Actividad 10 - Crear una función llamada calcular_promedio(a, b, c) que reciba tres
#números como parámetros y devuelva el promedio de ellos. Solicitar los
#números al usuario y mostrar el resultado usando esta función.

#Definir funcion
def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

#Programa principal
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))


resultado = calcular_promedio(a, b, c)

print(f"El promedio es: {resultado:.2f}")







