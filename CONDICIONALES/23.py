import os 
os.system("cls")

matematica = int (input ("nota de matemática: "))
fisica = int (input ("nota de fisica: "))

if matematica >= 17 : propina = 3
if matematica <= 16 : propina = 1

if fisica >= 15 : propina1 = 2
if fisica <= 14 : propina1 = 0.50

promedio = (matematica + fisica) / 2

if promedio >= 16: reloj = 1
else : reloj = 0

print (f"propina de matematica: {(propina)}")
print (f"propina de fisica: {(propina1)}")
print (f"propina total: {(propina + propina1)}")
print (f"promedio: {(promedio)}")
print (f"obsequio el reloj: {(reloj)}")
print()