import os
os.system("cls")

dividendo = int (input ("dividiendo: "))
divisor = int (input ("divisor: "))

cociente = 0
if dividendo >= divisor : dividendo -= divisor
cociente += 1

print (f"cociente: {cociente}")
print (f"residuo: {dividendo}")
print()