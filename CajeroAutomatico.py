user1 = "jordan"
pin1 = "1234"
saldo1 = 1000

user2 = "angel"
pin2 = "4321"
saldo2 = 1000

user3 = "claudio"
pin3 = "1111"
saldo3 = 1000

def mostrar_menu():
    print("\n")
    print("1. Consultar saldo")
    print("2. Consultar PIN")
    print("3. Retirar dinero")
    print("4. Ingresar dinero")
    print("5. Transferir dinero")
    print("6. Finalizar Proceso")
    print("7. Cerrar sesión")
    print("\n")

while True:
    print("\n")
    print("Bienvenido al cajero automático")
    print("\n")
    print("Cuentas disponibles: jordan, angel, claudio")
    print("\n")
    usuario = input("Ingrese su nombre de usuario: ").lower()
    print("\n")

    pin_actual = ""
    saldo = 0
    nombre_usuario = ""
    intentos = 0
    max_intentos = 3
    autenticado = False

    if usuario == user1:
        pin_actual = pin1
        saldo = saldo1
        nombre_usuario = user1
    elif usuario == user2:
        pin_actual = pin2
        saldo = saldo2
        nombre_usuario = user2
    elif usuario == user3:
        pin_actual = pin3
        saldo = saldo3
        nombre_usuario = user3
    else:
        print("Usuario no válido.")
        continue

    while intentos < max_intentos:
        pin_ingresado = input("Ingrese su PIN: ")
        if pin_ingresado == pin_actual:
            autenticado = True
            break
        else:
            intentos += 1
            print(f"PIN incorrecto. Te quedan {max_intentos - intentos} intentos.")

    if not autenticado:
        print("Has excedido el número de intentos. Acceso denegado.")
        continue

    while True:
        mostrar_menu()
        opc = input("Seleccione una opción: ")
        print("\n")

        if opc == "1":
            print(f"Su saldo actual es: ${saldo}")

        elif opc == "2":
            print(f"Su PIN actual es: {pin_actual}")
            opcion = input("¿Desea cambiar su PIN? 1.Si / 2.No :")
            if opcion == "1":
                pin_check = input("Ingrese su PIN actual: ")
                if pin_check == pin_actual:
                    nuevo_pin = input("Ingrese su nuevo PIN de 4 dígitos: ")
                    if nuevo_pin.isdigit() and len(nuevo_pin) == 4:
                        pin_actual = nuevo_pin
                        print("Su PIN ha sido cambiado exitosamente.")
                    else:
                        print("El PIN debe ser un número de 4 dígitos.")
                else:
                    print("PIN incorrecto.")
            elif opcion == "2":
                print("Volviendo al menú principal...")

        elif opc == "3":
            pin_check = input("Ingrese su PIN para proceder con el retiro: ")
            if pin_check == pin_actual:
                monto = int(input("¿Cuánto desea retirar? $"))
                if monto <= saldo:
                    saldo -= monto
                    print(f"Ha retirado ${monto}. Su saldo actual es ${saldo}.")
                else:
                    print("Saldo insuficiente.")
            else:
                print("PIN incorrecto.")

        elif opc == "4":
            pin_check = input("Ingrese su PIN para proceder con el ingreso: ")
            if pin_check == pin_actual:
                monto = int(input("¿Cuánto desea ingresar? $"))
                saldo += monto
                print(f"Ha ingresado ${monto}. Su saldo actual es ${saldo}.")
            else:
                print("PIN incorrecto.")

        elif opc == "5":
            pin_check = input("Ingrese su PIN para proceder con la transferencia: ")
            if pin_check == pin_actual:
                print("Usuarios disponibles para transferir:")
                if nombre_usuario == user1:
                    print("1. angel\n2. claudio")
                    destino = input("¿A quién desea transferir? (angel/claudio): ").lower()
                    if destino == "angel":
                        monto = int(input("¿Cuánto desea transferir? $"))
                        if monto <= saldo:
                            saldo -= monto
                            saldo2 += monto
                            print(f"Transferencia exitosa a angel. Nuevo saldo: ${saldo}")
                        else:
                            print("Saldo insuficiente.")
                    elif destino == "claudio":
                        monto = int(input("¿Cuánto desea transferir? $"))
                        if monto <= saldo:
                            saldo -= monto
                            saldo3 += monto
                            print(f"Transferencia exitosa a claudio. Nuevo saldo: ${saldo}")
                        else:
                            print("Saldo insuficiente.")
                    else:
                        print("Destino inválido.")

                elif nombre_usuario == user2:
                    print("1. jordan\n2. claudio")
                    destino = input("¿A quién desea transferir? (jordan/claudio): ").lower()
                    if destino == "jordan":
                        monto = int(input("¿Cuánto desea transferir? $"))
                        if monto <= saldo:
                            saldo -= monto
                            saldo1 += monto
                            print(f"Transferencia exitosa a jordan. Nuevo saldo: ${saldo}")
                        else:
                            print("Saldo insuficiente.")
                    elif destino == "claudio":
                        monto = int(input("¿Cuánto desea transferir? $"))
                        if monto <= saldo:
                            saldo -= monto
                            saldo3 += monto
                            print(f"Transferencia exitosa a claudio. Nuevo saldo: ${saldo}")
                        else:
                            print("Saldo insuficiente.")
                    else:
                        print("Destino inválido.")

                elif nombre_usuario == user3:
                    print("1. jordan\n2. angel")
                    destino = input("¿A quién desea transferir? (jordan/angel): ").lower()
                    if destino == "jordan":
                        monto = int(input("¿Cuánto desea transferir? $"))
                        if monto <= saldo:
                            saldo -= monto
                            saldo1 += monto
                            print(f"Transferencia exitosa a jordan. Nuevo saldo: ${saldo}")
                        else:
                            print("Saldo insuficiente.")
                    elif destino == "angel":
                        monto = int(input("¿Cuánto desea transferir? $"))
                        if monto <= saldo:
                            saldo -= monto
                            saldo2 += monto
                            print(f"Transferencia exitosa a angel. Nuevo saldo: ${saldo}")
                        else:
                            print("Saldo insuficiente.")
                    else:
                        print("Destino inválido.")
            else:
                print("PIN incorrecto.")

        elif opc == "6":
            print(f"Gracias por usar el cajero automático. Su saldo final es ${saldo}.")
            break

        elif opc == "7":
            print("Cerrando sesión...")
            if nombre_usuario == user1:
                saldo1 = saldo
            elif nombre_usuario == user2:
                saldo2 = saldo
            elif nombre_usuario == user3:
                saldo3 = saldo
            break

        else:
            print("Opción no válida. Intente de nuevo.")
    
    if nombre_usuario == user1:
        saldo1 = saldo
    elif nombre_usuario == user2:
        saldo2 = saldo
    elif nombre_usuario == user3:
        saldo3 = saldo
