#convertidor de pesos a dolar a euro("ds")

monto = float

print("Bienvenidos al simulador de dinero")
print("\n")

dinero = float(input("Para comenzar ingrese un monto en pesos chilenos:")) 
caja=dinero
print("\n")
print("El monto ingresado se transformara en dolar, euros y won")
print("\n")

dinero = dinero * 0.0011
print("El monto ingresado en dolar sería:", dinero, " dolares")
print("\n")
dinero=caja
dinero=dinero * 0.0010
print("El monto ingresado en euros sería:", dinero, " euros")
print("\n")
dinero=caja
dinero=dinero * 1.59
print("El monto ingresado en won sería:", dinero," wones")
print("\n")

