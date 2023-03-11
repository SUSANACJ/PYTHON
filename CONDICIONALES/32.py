import os 
os.system("cls")

categoria = int (input ("ingrese la categoria: "))
promedio = int (input ("ingrese el promedio: "))

if categoria == 1: pensionActual = 550
elif categoria == 2: pensionActual = 500
elif categoria == 3: pensionActual = 450
elif categoria == 4: pensionActual = 400

if promedio <= 13.99: descuento = "no hay descuento"
elif promedio >= 14 and promedio <= 15.99: descuento = pensionActual * 0.10
elif promedio >= 16 and promedio <= 17.99: descuento = pensionActual * 0.12
elif promedio >= 18 and promedio <= 20: descuento = pensionActual * 0.15

nuevaPension = pensionActual -  descuento

print (f"pension actual: {int(pensionActual)}")
print (f"descuento: {int(descuento)}")
print (f"nueva pension: {int(nuevaPension)}")
print()