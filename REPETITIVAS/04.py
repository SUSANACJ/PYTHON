import os
os.system("cls")

numero = int (input ("Ingresa el numero: "))
multiplos = int (input ("Ingrese los multiplos: "))

for i in range (numero, (numero * multiplos) + 1, numero):
    print (str (i))
print()