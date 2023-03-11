import os, math
os.system ("cls")

radio = int (input ("radio: "))
altura = int (input ("altura: "))

area = 2 * math.pi * radio * (radio + altura)
volumen = math.pi *math.pow (radio,2) * altura

print (f"area = {format (area,' .2f')} u2")
print ( f"volumen = {format (volumen,' .2f')} u3")
print()