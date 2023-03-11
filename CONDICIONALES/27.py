import os 
os.system("cls")

monto = int (input (" monto vendido es: "))

comision = monto * 0.15
sueldoBasico = 600
sueldoBruto = sueldoBasico + comision

if sueldoBruto >= 1800: descuento = sueldoBruto * 0.10
else: descuento = sueldoBruto * 0.05

if monto >= 1000: polos = 3
else: polos = 1
sueldoNeto = sueldoBruto - descuento

print (f"sueldo Bruto: {int(sueldoBruto)}")
print (f"descuento: {int(descuento)}")
print (f"sueldo Neto: {int(sueldoNeto)}")
print (f"cantidad de polos adquiridos: {int(polos)}")
print()

