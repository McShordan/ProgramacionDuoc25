# detectar par o impar
opc = "s"


while opc == "s" :
    x= int(input("Ingrese un número para detectar si es par o impar: "))
    if x%2 == 0:
        print("\n")
        print("Su número es par")
    else:
        print("\n")
        print("Su número es impar")  

    print("\n")
    opc = input("Desea continar s/n :")


