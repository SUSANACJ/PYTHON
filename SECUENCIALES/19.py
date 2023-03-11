import os
os.system("cls")

montoTotal = int (input ("ingrese monto total vendido: "))

comision = (montoTotal * 9) / 100
sueldoBruto = 500 + comision
descuento = (sueldoBruto * 11) / 100
sueldoNeto = sueldoBruto - descuento

print (f" comisiones: s/.",format(comision,".2f"))
print (f" sueldo Bruto: s/.",format(sueldoBruto,".2f"))
print (f" descuento: s/.",format(descuento,".2f"))
print (f" sueldo Neto: s/.",format(sueldoNeto,".2f"))
print()