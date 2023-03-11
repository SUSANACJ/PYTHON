import os
os.system("cls")

numero = int (input ("Ingrese numero de cuatro cifras: "))


cifra4 = numero % 10
cifra3 = int ((numero % 100) / 10)
cifra2 = int((numero % 1000) /100)
cifra1 = int ((numero - (numero % 1000)) / 1000)


print (str(cifra4) + str(cifra3) + str(cifra2) + str(cifra1))
print ()