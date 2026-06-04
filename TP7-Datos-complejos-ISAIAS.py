#Actividad 1 - Dado el diccionario precios_frutas precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
#Añadir las siguientes frutas con sus respectivos precios: Naranja = 1200 Manzana = 1500 Pera = 2300

precios_frutas = {
     'Banana': 1200, 
     'Ananá': 2500,
     'Melón': 3000,
    'Uva': 1450
}
print("--- ACTIVIDAD 1 ---")
print("----------------------")
print("Precios sin actualizar")
print("----------------------")
for clave, valor in precios_frutas.items():
    print(clave,":", valor)
print("--------------------")
print("Precios actualizados")
print("--------------------")
precios_frutas.update({"Naranja": 1200, "Manzana": 1500, "Pera": 2300})
for clave, valor in precios_frutas.items():
    print(clave,":", valor)

# Actividad 2 - Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, actualizar los precios de las siguientes frutas: Banana = 1330 Manzana = 1700 Melón = 2800

precios_frutas["Banana"] = "1330"
precios_frutas["Manzana"] = "1700"
precios_frutas["Melón"] = "2800"
print()
print("--- ACTIVIDAD 2 ---")
print("-------------------")
for clave, valor in precios_frutas.items():
    print(clave,":", valor)

# Actividad 3 - Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los precios.

print("--- ACTIVIDAD 3 ---")
print("-------------------")
lista_claves = precios_frutas.keys()
for clave in lista_claves:
    print(clave)

#Actividad 4 - Escribí un programa que permita almacenar y consultar números telefónicos.
#Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
#Luego, pedí un nombre y mostrale el número asociado, si existe.

agenda = {}

for contacto in range(5):
    nombre = input("Ingrese nombre del contacto: ")
    while not nombre.isalpha() or nombre == "":
        nombre = input("Ingrese nombre valido: ")
    numero = input("Ingrese numero de telefono: ")
    while not numero.isdigit() or numero == "":
        numero = input("Ingrese numero de telefono valido: ")

    agenda[nombre] = float(numero)

for nombre, numero in agenda.items():
    print(f"Contacto: {nombre} - Telefono: {numero}")

#Actividad 5 - Solicita al usuario una frase e imprime: Las palabras únicas (usando un set). Un diccionario con la cantidad de veces que aparece cada palabra.

frase = input("Ingrese una frase: ")

palabras = frase.split()

unicas = set(palabras)

print("Palabras únicas:")
print(unicas)

contador = {}

for palabra in palabras:
    if palabra in contador:
        contador[palabra] += 1
    else:
        contador[palabra] = 1

print("Cantidad de veces que aparece cada palabra:")
print(contador)

#Actividad 6 - Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas. Luego, mostrá el promedio de cada alumno.

alumnos = {}

for alumno in range(3):
    nombre = input("Ingrese nombre del alumno: ")
    while not nombre.isalpha() or nombre == "":
        nombre=input("Error. Ingresar nombre valido:")

    lista_notas = []

    for nota in range(3):
        n = (input("Ingrese una nota: "))
        while not n.isdigit() or n == "":
         n = (input("Ingrese un numero valido: "))
        lista_notas.append(float(n))

    notas = tuple(lista_notas)

    alumnos[nombre] = notas

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)

    print(nombre)
    print("Notas:", notas)
    print("Promedio:", promedio)

#Actividad 7 - Se recibe el registro diario de asistencia a una capacitación en forma de lista. En dicha lista pueden aparecer nombres repetidos, 
#ya que una misma persona pudo haber asistido en más de una jornada.
#Mostrá la lista original de asistencias.
#Generá un conjunto (set) a partir de la lista y mostrar los empleados que asistieron al menos una vez (sin repetir nombres).
#Indicá cuántas veces asistió cada empleado a la capacitación.

asistencia = ["Juan", "Jose", "Pedro", "Liliana", "Silvia",
              "Melisa", "Gonzalo", "Melisa", "Juan", "Esteban"]

unavez = set(asistencia)

print(f"Las personas que asistieron al menos una vez son: {unavez}")

contador = {}

for nombre in asistencia:

    if nombre in contador:
        contador[nombre] += 1
    else:
        contador[nombre] = 1

for nombre, cantidad in contador.items():
    print(nombre, "asistió", cantidad, "veces")


#Actividad 8 - Armá un diccionario donde las claves sean nombres de productos y los valores su stock. Permití al usuario:
#Consultar el stock de un producto ingresado. Agregar unidades al stock si el producto ya existe. Agregar un nuevo producto si no existe.

cant_productos = {
    "banana": 10, 
    "anana": 25,
    "melon": 30,
    "uva": 14
}
opcion = -1

while opcion != 0:

    print("\n--- MENU ---")
    print("1. Consultar stock")
    print("2. Agregar unidades a producto existente")
    print("3. Agregar producto nuevo")
    print("0. SALIR")


    entrada = input("Ingrese opción: ")
    while not entrada.isdigit() or entrada == "":
        if entrada == "":
            print("No ingresaste ningún valor.")
        else:
            print("Ingresá un número válido.")
        entrada = input("Ingrese opción: ")

    opcion = int(entrada)

    if opcion == 1:
        buscar = input("Ingrese producto para saber su stock: ").lower()
        while buscar == "":
            print("No ingresaste ningún producto.")
            buscar = input("Ingrese producto para saber su stock: ").lower()

        if buscar in cant_productos:
            print(f"Stock de {buscar.title()}: {cant_productos[buscar]} unidades")
        else:
            print("Producto no encontrado.")

    elif opcion == 2:
        producto = input("Ingrese producto: ").lower()
        while producto == "":
            print("No ingresaste ningún producto.")
            producto = input("Ingrese producto: ").lower()

        if producto in cant_productos:
            agregar = input("¿Cuántas unidades desea agregar?: ")
            while not agregar.isdigit() or agregar == "":
                if agregar == "":
                    print("No ingresaste ningún valor.")
                else:
                    print("Ingresá un número válido.")
                agregar = input("¿Cuántas unidades desea agregar?: ")
            
            agregar = int(agregar)
            cant_productos[producto] += agregar
            print("Stock actualizado.")
            print(cant_productos)
        else:
            print("El producto no existe.")

    elif opcion == 3:
        nuevo = input("Ingrese nuevo producto: ").lower()
        while nuevo == "":
            print("No ingresaste ningún producto.")
            nuevo = input("Ingrese nuevo producto: ").lower()

        if nuevo in cant_productos:
            print("El producto ya existe.")
        else:
            stock = input("Ingrese stock inicial: ")
            while not stock.isdigit() or stock == "":
                if stock == "":
                    print("No ingresaste ningún valor.")
                else:
                    print("Ingresá un número válido.")
                stock = input("Ingrese stock inicial: ")
            
            stock = int(stock)
            cant_productos[nuevo] = stock
            print("Producto agregado.")
            print(cant_productos)

    elif opcion == 0:
        print("Saliendo del programa...")

    else:
        print("Opción inválida.")

#Actividad 9 - Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos. Permití consultar qué actividad hay en cierto día y hora.

agenda = {
    ("lunes", "10:00"): "Reunión",
    ("martes", "15:00"): "Gimnasio",
    ("viernes", "20:00"): "Cena con amigos"
}

dia = input("Ingrese un día: ").lower()
while dia == "":
    print("No ingresaste ningún día.")
    dia = input("Ingrese un día: ").lower()

hora = input("Ingrese una hora formato hh:mm: ")
while hora == "":
    print("No ingresaste ninguna hora.")
    hora = input("Ingrese una hora formato hh:mm: ")

while len(hora) != 5 or hora[2] != ":" or not hora[:2].isdigit() or not hora[3:].isdigit():
    print("Formato de hora incorrecto. Usá formato hh:mm (ejemplo: 14:30)")
    hora = input("Ingrese una hora formato hh:mm: ")
    while hora == "":
        print("No ingresaste ninguna hora.")
        hora = input("Ingrese una hora formato hh:mm: ")

clave = (dia, hora)

if clave in agenda:
    print("Actividad:", agenda[clave])
else:
    print("No hay actividades programadas.")

#Actividad 10 - Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo diccionario donde: Las capitales sean las claves. Los países sean los valores.

paises_capitales = {
    "Argentina": "Buenos Aires",
    "España": "Madrid",
    "Francia": "París",
    "Italia": "Roma",
    "Japon": "Tokio"
}

capitales_paises = {}

for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais

print("Diccionario original (país -> capital):")
print(paises_capitales)
print("\nDiccionario invertido (capital -> país):")
print(capitales_paises)