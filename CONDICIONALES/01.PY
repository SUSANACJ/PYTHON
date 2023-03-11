import os
os.system ("cls")

unidades = int (input ("unidades: "))

if unidades <= 25 : precio = 27
elif unidades > 25 and unidades <= 50 : precio =25
else : precio = 23

precio = 25
if unidades <= 25 : precio = 27
elif unidades >50 : precio = 23

#precio = 27 if unidades <= 25 else 23 if unidades

compra = precio * unidades

if unidades > 50 : descuento = 0,15 * compra
else : descuento = 0.05 * compra

descuento = 0.05 * compra
if unidades > 50 : descuento = 0,15 * compra

total = compra - descuento

print (f" precio = s/ {format (precio,' .2f')}")
print (f" compra = s/ {format (compra,' .2f')}")
print (f" descuento = s/ {format (descuento,' .2f')}")

print ()


