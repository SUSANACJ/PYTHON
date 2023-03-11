import os 
os.system("cls")

monto = int (input ("el monto total de la compra: "))

if monto >= 5000: prestamo = monto * 0.30
else: prestamo = monto * 0.20

propioDinero = monto - prestamo
intereses = propioDinero * 0.10
total = propioDinero + intereses

print (f"prestamo del banco es: {int(prestamo)}")
print (f"paga sus intereses con su prropio dinero: {int(total)}")
print()