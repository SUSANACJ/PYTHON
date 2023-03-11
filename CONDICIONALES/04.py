import os
os.system ("cls")

n1 = int (input ("N1: "))
n2 = int (input ("N2: "))
n3 = int (input ("N3: "))

if n3 >= 10 and n3 <= 18 : n3 += 2

print ( F"promedio = {(n1 + n2 + n3) / 3.0}")
print()