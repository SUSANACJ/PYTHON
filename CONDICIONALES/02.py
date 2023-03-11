import os
os.system ("cls")

unidades = int (input ("unidades: "))

compra = 20 * unidades
descuento = (0.12 if compra <= 500 else 0.16 if compra > 700 else 0.14) * compra
caramelos = 5 if unidades <= 50 else 15 if unidades > 100 else 10

print (f" compra : s/ {compra: .2f}")
print (f" descuento : s/ {descuento: .2f}")
print (f" total : s/ {(compra - descuento): .2f}")
print (f" caramelos : s/ {caramelos}")
print ()




