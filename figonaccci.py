
print("Usaremos numeros figonacci")
print("\n")
n = int(input("Ingrese la cantidad de números figonacci que desea obtener: "))
a=0
b=1

print(a)
print(b)

for _ in range(n):
    c=a+b
    print(c)
    a=b
    b=c
10