import os 
os.system("cls")

unidadesA = int (input ("unidades del producto: "))
unidadesB = int (input ("unidades del producto: "))

productoA = unidadesA * 25
productoB = unidadesB * 30

if unidadesA >= 50: descuentoA = productoA * 0.15
else: descuentoA = 0

if unidadesB >= 60: descuentoB = productoB * 0.10
else: descuentoB = 0

importeBruto = productoA + productoB
descuentoTotal = descuentoA + descuentoB
totalPagar = importeBruto - descuentoTotal

print (f" importe bruto es: {(importeBruto)}")
print (f" el descuento es: {(descuentoTotal)}")
print (f" total a pagar es: {(totalPagar)}")
print()