import os
os.system("cls")

unidades = int ( input ("ingrese cantidad de docenas de producto: "))
precio = int ( input ("el precio de la docena: "))

montoCompa = unidades * precio
if unidades >= 6: descuento = montoCompa * 0.15
if unidades <= 5: descuento = montoCompa * 0.10

total = montoCompa - descuento

if unidades >= 30: obsequio = 2 * (unidades / 3)
else:
    obsequio = 0
    
print (" monto de la compra: ",(montoCompa)) 
print (" descuento: ",(descuento)) 
print (" total a pagar: ",(total)) 
print (" cantidad de lapiceros adquiridos: ",(obsequio)) 
print()

