import os
os.system("cls")

codigo = int(input ("codigo: "))

if codigo % 2 == 0 and codigo % 3 == 0 and codigo % 5 == 0 : tipo = "administrativo"
if  not codigo % 2 == 0 and codigo % 3 == 0 and codigo % 5 == 0 : tipo = "directivo"
if codigo % 2 == 0 and not codigo % 3 == 0 and not codigo % 5 == 0 : tipo = "vendedor"
if not codigo % 2 == 0 and not codigo % 3 == 0 and not codigo % 5 == 0 : tipo = "seguridad"
else : tipo = "error"

print (f"tipo = {tipo}")
print()