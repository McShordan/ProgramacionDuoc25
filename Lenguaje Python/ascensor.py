piso_actual = 1
print("Este edificio cuenta desde el piso -3 hasta el piso 13")
while True:
    print("\n")
    print(f"Usted se encuentra en el piso {piso_actual}")
    print("\n")
    print("1. Subir a un piso")
    print("2. Bajar a un piso")
    print("3. Finalizar trabajo")
    opcion = input("Seleccione una opción: ")
    print("\n")

    if opcion == '1':
        piso_destino = int(input("¿A qué piso quieres subir? "))
        if piso_destino > piso_actual and piso_destino <= 13:
            print(f"Subiendo al piso {piso_destino}")
            for _ in range(3):
                print(".")
            piso_actual = piso_destino
            print("Hemos llegado")
            print("\n")
        elif piso_destino == piso_actual:
            print(f"Ya te encuentras en el piso {piso_actual}.")
            print("\n")
        else:
            print("No puedes subir a un piso superior a 13.")
    
    elif opcion == '2':
        piso_destino = int(input("¿A qué piso quieres bajar? "))
        if piso_destino < piso_actual and piso_destino >= -3:
            print(f"Bajando al piso {piso_destino}")
            for _ in range(3):
                print(".")
            piso_actual = piso_destino
            print("Hemos llegado")
            print("\n")
        elif piso_destino == piso_actual:
            print(f"Ya te encuentras en el piso {piso_actual}.")
            print("\n")
        else:
            print("No puedes bajar a un piso inferior a -3.")
    
    elif opcion == '3':
        print(f"El trabajo ha finalizado. El ascensor quedó en el piso {piso_actual}.")
        print("\n")
        break
    else:
        print("Opción no válida. Por favor, elige una opción correcta.")
        print("\n")