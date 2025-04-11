x = 1
cant = 1

while x == 1:
    print("Bienvenido a la calculadora de Perímetro o área:")
    print("")
    print("Seleccione la figura que desee realizar: ")
    print("1. Cuadrado")
    print("2. Triángulo")
    print("3. Círculo")
    print("0. Salir")
    cant = float(input())

    if cant == 1:  # Cuadrado
        print("Seleccione la opción que desee realizar: ")
        print("1. Calcular Área")
        print("2. Calcular Perímetro")
        print("0. Volver al menú anterior")
        
        oper = float(input())
        
        if oper == 1:  
            print("Para calcular el área de un cuadrado, ingrese el valor de un lado: ")
            x = float(input())
            area = x * x
            print("")
            print("El área del cuadrado es:", area)
        
        if oper == 2:  
            print("Para calcular el perímetro de un cuadrado, ingrese el valor de un lado: ")
            x = float(input())
            perimetro = x * 4
            print("")
            print("El perímetro del cuadrado es:", perimetro)
        
        if oper != 1 and oper != 2:  # Validación si se ingresa un número no válido
            print("El número ingresado excede los solicitados")
            print("")
            cant = 0

    if cant == 2:  # Triángulo
        print("Seleccione la opción que desee realizar: ")
        print("1. Calcular Área")
        print("2. Calcular Perímetro")
        print("0. Volver al menú anterior")
        
        oper = float(input())
        
        if oper == 1:  # Calcular área
            print("Para calcular el área de un triángulo, ingrese los siguientes valores: ")
            base = float(input("Valor de la base: "))
            altura = float(input("Valor de la altura: "))
            area = (base * altura) / 2
            print("")
            print("El área del triángulo es:", area)
        
        if oper == 2:  # Calcular perímetro
            print("Para calcular el perímetro de un triángulo, ingrese los siguientes valores: ")
            x = float(input("Valor de lado 1: "))
            a = x
            x = float(input("Valor de lado 2: "))
            a = a + x
            x = float(input("Valor de lado 3: "))
            a = a + x
            print("")
            print("El perímetro del triángulo es:", a)
        
        if oper != 1 and oper != 2:  # Validación si se ingresa un número no válido
            print("El número ingresado excede los solicitados")
            print("")
            cant = 0

    if cant == 3:  # Círculo
        print("Seleccione la opción que desee realizar: ")
        print("1. Calcular Área")
        print("2. Calcular Perímetro")
        print("0. Volver al menú anterior")
        
        oper = float(input())
        
        if oper == 1:  # Calcular área
            print("Para calcular el área de un círculo, ingrese el valor del radio: ")
            x = float(input())
            area = 3.1416 * x * x
            print("")
            print("El área del círculo es:", area)
        
        if oper == 2:  # Calcular perímetro
            print("Para calcular el perímetro de un círculo, ingrese el valor del radio: ")
            x = float(input())
            perimetro = 2 * 3.1416 * x
            print("")
            print("El perímetro del círculo es:", perimetro)
        
        if oper != 1 and oper != 2:  # Validación si se ingresa un número no válido
            print("El número ingresado excede los solicitados")
            print("")
            cant = 0

    if cant != 1 and cant != 2 and cant != 3:  # Validación para asegurarse de que la opción sea válida
        print("El número ingresado excede los solicitados")
        print("")
        cant = 0

    # Preguntar si desea realizar otra operación
    print("¿Desea realizar otra operación? ")
    print("1. SI")
    print("0. NO")
    print("")
    x = float(input())
    
    if x == 1:
        n1 = 0
        a = 1
    elif x != 1:
        print("Que tenga buen día")
        break