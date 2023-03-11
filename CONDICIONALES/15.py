import os 
os.system ("cls")

monto = int (input ("monto vendido: "))

sueldoBasico = 250

if monto <= 5000: comision = monto * 0.05
if monto >= 5001 and monto <= 10000: comision = monto * 0.08
if monto >= 10001 and monto <= 20000: comision = monto * 0.18
if monto >= 20001: comision = monto * 0.15

sueldoBruto = sueldoBasico - comision

if sueldoBruto >= 3500: 
    descuento =  sueldoBruto * 0.15
elif sueldoBruto <= 3499: descuento = sueldoBruto * 0.08

sueldoNeto = sueldoBruto - descuento

print (f"comision: {int (comision)}")
print (f"sueldo bruto: {int (sueldoBruto)}")
print (f"descuento: {int (descuento)}")
print (f"sueldo neto: {int (sueldoNeto)}")
print()