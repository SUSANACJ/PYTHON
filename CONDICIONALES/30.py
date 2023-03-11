import os 
os.system("cls")

cuota = int (input ("ingrese cuota mensual: "))
dias = int (input ("ingrese el dia de pago: "))

descuento = 0
recarga = 0

if dias <= 10: descuento = cuota * 0.02
if dias <= 10 and descuento <5: descuento = 5
if dias >= 11 and dias < 21: descuento = 0
if dias >= 21 and dias < 31: recarga = cuota * 0.03
if dias >= 21 and dias < 10: recarga = 10

debePagar = cuota - descuento + recarga 

print (f"El cliente debe pagar: {(debePagar)}")
print()
