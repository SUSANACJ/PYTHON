import os
os.system("cls")

cantidad_producto = int (input ("ingrese la cantidad adquirida: "))
precio_producto  = int (input ("ingrese el precio del articulo: "))

importe_compra = precio_producto * cantidad_producto
descuento1 = importe_compra - (importe_compra * 0.15)
importeApagar= descuento1 - (descuento1 * 0.15)

print (f" importe de la compra es: s/.",format(importe_compra,".2f"))
print (f" primer descuento fue de: s/.",format(importe_compra * 0.15,".2f"))
print (f" segundo descuento fue de: s/.",format(descuento1 * 0.15,".2f"))
print (f" importe a pagar es de: s/.",format(importeApagar,".2f"))
print()
