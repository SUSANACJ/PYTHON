import os
os.system("cls")

numero = int ( input(" Igrese el numero de 4 cifras: "))

cifra1 = numero / 1000
cifra2 = (numero % 1000) / 100
cifra3= ((numero % 1000) % 100 / 10)
cifra4 = numero % 10

print (f"suma de cifras = {cifra1 + cifra2 + cifra3 + cifra4} ")
print()
