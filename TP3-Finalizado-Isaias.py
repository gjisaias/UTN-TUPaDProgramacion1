#Actividad numero 1

nombre=input("Ingrese su nombre: ")
while not nombre.isalpha():
    print("Error: Debe ingresar un nombre con solo letras.")
    nombre = input("Ingrese nombre nuevamente: ")

print("Ingreso válido:", nombre)
cant_productos=(input("Ingrese la cantidad de productos: "))
while not cant_productos.isdigit() or int(cant_productos) <= 0:
        print("Error: solo se permiten numeros mayores a 0")
        cant_productos = input("Ingrese la cantidad de productos nuevamente: ")
cant_productos=int(cant_productos)
print("Ingreso válido. Productos: ", cant_productos)
total_con_descuento=0
total_sin_descuento=0
for i in range(1,cant_productos + 1):      
    precio=input(f"Ingrese precio del producto numero {i}: ")
    while not precio.isdigit():
        print("Error: Ingresar el valor en numero")
        precio = input("Ingrese precio nuevamente: ")
    precio = float(precio)
    precio_original = float(precio)
    desc=input(f"El producto {i} tiene descuento? Ingrese S/N: ").lower()
    while desc not in ["s", "n"]:
        print("Error: Ingrese solo S o N")
        desc = input("Ingrese nuevamente: ").lower()
    if desc == "s":
         precio_final = precio * 0.9       
    else:
         precio_final = precio
    print(f"Producto: {i}, Precio {precio_original}, Descuento: {desc}")
    
    total_sin_descuento += precio_original
    total_con_descuento += precio_final

print(f"Cliente: {nombre}")
print(f"Cantidad de productos: {cant_productos}")
print(f"Total con descuento: $ {total_con_descuento:.2f}")
print(f"Total sin descuento: $ {total_sin_descuento:.2f}")
print(f"Ahorro: $ {(total_sin_descuento - total_con_descuento):.2f}")
print(f"Promedio por producto: {(total_con_descuento / cant_productos):.2f}")

#Actividad numero 2

usuario_correcto="alumno"
clave_correcta="python123"
intentos=0
acceso=False

while intentos < 3:
   usuario=input("Usuario: ")
   clave=input("Clave: ")

   if usuario != usuario_correcto or clave != clave_correcta:
      intentos += 1
     
      if intentos == 3:
          break
      else:
           print(f"""Intento {intentos}/3 - Usuario: {usuario} 
                  Clave: {clave}
                  Error: credenciales invalidas.""")
   else:
      print(f"""Intento {intentos}/3 - Usuario: {usuario} 
                  Clave: {clave}
                  Acceso concedido""")
      acceso=True
      break

if not acceso:
      print("Cuenta bloqueada.")

if acceso:
    while True:
        menu = input("""
1. Ver estado de inscripción
2. Cambiar clave
3. Mensaje
4. Salir
Seleccione: """)
        
        if not menu.isdigit():
            print("Error: ingrese un numero valido.")
            continue
        menu=int(menu)
        clave_nueva = ""
        clave_nueva2 = ""
        if menu < 1 or menu > 4:
            print("Error: fuera de rango")                  
        if menu == 1:
            print("Inscripto")

        elif menu == 2:
         clave_nueva = input("Ingrese nueva clave: ")

         if len(clave_nueva) > 6:                
              print("Error. Minimo 6 caracteres.")
              continue
         else:
             clave_nueva2 = input("Confirme su clave: ")
             
         if clave_nueva != clave_nueva2:
            print("Error: las claves no coinciden.")
         else:
            clave_correcta = clave_nueva
            print(f"Nueva clave: {clave_nueva}")
        elif menu == 3:
            print("Seguí adelante, vas bien.")

        elif menu == 4:
            print("Saliendo...")
            break
    
#Actividad numero 3

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

operador = input("Ingrese nombre del operador: ")
while not operador.isalpha():
 operador = input("""Solo puede ingresar letras.
              Ingrese nombre del operador: """)

while True:
 menu = input("""Ingrese el numero de lo que desea realizar:
                 1. Reservar turno
                 2. Cancelar turno (por nombre)
                 3. Ver agenda del día
                 4. Ver resumen general
                 5. Cerrar sistema
                 """)
 if not menu.isdigit():
  print("Error. Debe ingresar solo numeros.")
  continue
 menu=int(menu)

 if menu == 1:
    paciente = input("Ingrese nombre del paciente que desea reservar el turno: ").lower()

    while not paciente.isalpha():
        paciente = input("Ingrese nombre válido: ")

    dias = input("Elegir dia. Ingrese 1 para lunes 2 para martes: ")

    if dias == "1":
        if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
            print(f"{paciente} ya tiene turno")
            continue
        else:
            if lunes1 == "":
                lunes1 = paciente
                print("El turno ha sido agendado.")
            elif lunes2 == "":
                lunes2 = paciente
                print("El turno ha sido agendado.")
            elif lunes3 == "":
                lunes3 = paciente
                print("El turno ha sido agendado.")
            elif lunes4 == "":
                lunes4 = paciente
                print("El turno ha sido agendado.")
            else:
                print("No hay cupos en lunes")


    elif dias == "2":
        if paciente == martes1 or paciente == martes2 or paciente == martes3:
            print(f"{paciente} ya tiene turno")
            continue
        else:
            if martes1 == "":
                martes1 = paciente
                print("El turno ha sido agendado.")
            elif martes2 == "":
                martes2 = paciente
                print("El turno ha sido agendado.")
            elif martes3 == "":
                martes3 = paciente
                print("El turno ha sido agendado.")
            else:
                print("No hay cupo para el dia martes")

    else:
        print("Día inválido")
 elif menu == 2:
     paciente = input("Ingrese nombre del paciente que desea cancelar el turno: ").lower()

     while not paciente.isalpha():
        paciente = input("Ingrese nombre válido: ")

     dias = input("Elegir dia en el que tiene reserva de turno. Ingrese 1 para lunes 2 para martes: ")

     if dias == "1":
        if paciente == lunes1:
            lunes1 = ""
            print("Turno cancelado.")
        elif paciente == lunes2:
            lunes2 = ""
            print("Turno cancelado.")
        elif paciente == lunes3:
            lunes3 = ""
            print("Turno cancelado.")
        elif paciente == lunes4:
            lunes4 = ""
            print("Turno cancelado.")
        else:
             print(f"El paciente: {paciente} no tenia ningun turno reservado.")  
     elif dias == "2":
        if paciente == martes1:
            martes1 = ""
            print("Turno cancelado.")
        elif paciente == martes2:
            martes2 = ""
            print("Turno cancelado.")
        elif paciente == martes3:
            martes3 = ""
            print("Turno cancelado.") 
        else:
             print(f"El paciente: {paciente} no tenia ningun turno reservado.") 

 elif menu == 3:
    dias = input("Elegir dia. 1 para Lunes 2 para Martes: ")

    if dias == "1":
        print("Agenda Lunes:")

        if lunes1 == "":
            print("Turno 1: Libre")
        else:
            print("Turno 1:", lunes1)

        if lunes2 == "":
            print("Turno 2: Libre")
        else:
            print("Turno 2:", lunes2)

        if lunes3 == "":
            print("Turno 3: Libre")
        else:
            print("Turno 3:", lunes3)

        if lunes4 == "":
            print("Turno 4: Libre")
        else:
            print("Turno 4:", lunes4)

    elif dias == "2":
        print("Agenda Martes:")

        if martes1 == "":
            print("Turno 1: Libre")
        else:
            print("Turno 1:", martes1)

        if martes2 == "":
            print("Turno 2: Libre")
        else:
            print("Turno 2:", martes2)

        if martes3 == "":
            print("Turno 3: Libre")
        else:
            print("Turno 3:", martes3)

    else:
        print("Día inválido")
 elif menu == 4:

    ocupados_lunes = 0
    if lunes1 != "":
        ocupados_lunes += 1
    if lunes2 != "":
        ocupados_lunes += 1
    if lunes3 != "":
        ocupados_lunes += 1
    if lunes4 != "":
        ocupados_lunes += 1

    ocupados_martes = 0
    if martes1 != "":
        ocupados_martes += 1
    if martes2 != "":
        ocupados_martes += 1
    if martes3 != "":
        ocupados_martes += 1

    libres_lunes = 4 - ocupados_lunes
    libres_martes = 3 - ocupados_martes

    print("Resumen:")
    print(f"Lunes ocupados: {ocupados_lunes} | Libres: {libres_lunes}")
    print(f"Martes ocupados: {ocupados_martes} | Libres: {libres_martes}")

    if ocupados_lunes > ocupados_martes:
        print("Dia con más turnos: Lunes")
    elif ocupados_martes > ocupados_lunes:
        print("Dia con más turnos: Martes")
    else:
        print("Hay empate en cantidad de turnos")  

#Actividad numero 4

 energia = 100
 tiempo = 12
 cerraduras_abiertas = 0
 alarma = False
 codigo_parcial = ""
 forzar_seguidas = 0
 
# Pedir nombre del agente
 agente = input("Ingrese nombre del agente: ")

 while not agente.isalpha():
    agente = input("Error. Solo letras. Ingrese nombre: ")

# Bucle principal
 while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    print("\nEnergia:", energia)
    print("Tiempo:", tiempo)
    print("Cerraduras abiertas:", cerraduras_abiertas)
    print("Alarma:", alarma)

    print("\n1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    opcion = input("Opcion: ")

    while not opcion.isdigit():
        opcion = input("Error: ingrese un número válido. Opcion: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 3:
        opcion = input("Error: opción fuera de rango. Opcion: ")
        while not opcion.isdigit():
            opcion = input("Error: ingrese un número válido. Opcion: ")
        opcion = int(opcion)

    # Opción 1
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        forzar_seguidas += 1

        if forzar_seguidas == 3:
            alarma = True
        else:
            if energia < 40:
                numero = input("Ingrese un número 1-3: ")

                while not numero.isdigit():
                    numero = input("Error: ingrese un número válido. Ingrese un número 1-3: ")

                numero = int(numero)

                while numero < 1 or numero > 3:
                    numero = input("Error: opción fuera de rango. Ingrese un número 1-3: ")
                    while not numero.isdigit():
                        numero = input("Error: ingrese un número válido. Ingrese un número 1-3: ")
                    numero = int(numero)

                if numero == 3:
                    alarma = True
                else:
                    if not alarma:
                        cerraduras_abiertas += 1
            else:
                if not alarma:
                    cerraduras_abiertas += 1

    # Opción 2
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        forzar_seguidas = 0

        for i in range(4):
            print("Hackeando...")
            codigo_parcial += "A"

        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1

    # Opción 3
    elif opcion == 3:
        energia += 15
        tiempo -= 1
        forzar_seguidas = 0

        if energia > 100:
            energia = 100

        if alarma:
            energia -= 10

    # Bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Sistema bloqueado")
        break

#Actividad numero 5

 print("--- BIENVENIDO A LA ARENA ---")

 # Paso 1: pedir nombre y validar
 nombre = input("Nombre del Gladiador: ")

 while not nombre.isalpha():
    print("Error: Solo se permiten letras.")
    nombre = input("Nombre del Gladiador: ")

 # Paso 2: variables iniciales
 vida_jugador = 100
 vida_enemigo = 100
 pociones = 3
 danio_base = 15
 danio_enemigo = 12
 turno_jugador = True

 print("=== INICIO DEL COMBATE ===")

 # Paso 3: ciclo principal
 while vida_jugador > 0 and vida_enemigo > 0:

    print(f"{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")

    print("1. Ataque Pesado")
    print("2. Ráfaga Veloz")
    print("3. Curar")

    # Paso 4: validar opción
    opcion = input("Opción: ")

    while not opcion.isdigit():
        print("Error: Ingrese un número válido.")
        opcion = input("Opción: ")

    opcion = int(opcion)

    while opcion < 1 or opcion > 3:
        print("Error: opción fuera de rango.")
        opcion = input("Opción: ")
        while not opcion.isdigit():
            print("Error: Ingrese un número válido.")
            opcion = input("Opción: ")
        opcion = int(opcion)

    # Paso 5: acciones

    # Ataque Pesado
    if opcion == 1:
        if vida_enemigo < 20:
            danio = danio_base * 1.5
        else:
            danio = danio_base

        vida_enemigo -= danio
        print(f"¡Atacaste al enemigo por {danio} puntos de daño!")

    # Ráfaga Veloz
    elif opcion == 2:
        for i in range(3):
            vida_enemigo -= 5
            print("> Golpe conectado por 5 de daño")

    # Curar
    elif opcion == 3:
        if pociones > 0:
            vida_jugador += 30
            pociones -= 1
        else:
            print("¡No quedan pociones!")

    # Paso 6: turno del enemigo
    if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print("¡El enemigo te atacó por 12 puntos de daño!")

 # Paso 7: resultado final
 if vida_jugador > 0:
    print(f"VICTORIA. {nombre} ha ganado la batalla.")
 else:
    print("DERROTA. Has caído en combate.")