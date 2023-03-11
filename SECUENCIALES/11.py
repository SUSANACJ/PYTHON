import os
os.system("cls")

numero1 = int (input ("NUMERO1: "))
numero2 = int (input ("NUMERO2: "))

cifra1 =  int ((numero1 - (numero1 % 100)) / 100)
cifra2 = int ((numero1 % 100) / 10)
cifra3 = int ((numero1 % 100) % 10)

b1 =  int ((numero2 - (numero2 % 100)) / 100)
b2 = int ((numero2 % 100) / 10)
b3 = int ((numero2 % 100) % 10)

print (str(cifra3) + str(b2) + str(cifra1))
print (str(b3) + str(cifra2) + str(b1))
print()





