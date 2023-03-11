import os 
os.system("cls")

horas = int (input ("ingrese las horas trabajadas: "))
tarifa = int (input ("ingrese tarifa horaria: "))

if horas <= 48: 
    sueldoBruto = horas * tarifa
elif horas >= 49: 
    recarga = (horas * tarifa) * 0.20
    sueldoBruto = (horas * tarifa) + recarga

if sueldoBruto >= 1500: descuento = sueldoBruto * 0.11
elif sueldoBruto <= 1499: descuento = 0

totalApagar = sueldoBruto - descuento

print (f"horas trabajadas: {(horas)}")
print (f"pago por hora: {(tarifa)}")
print (f"sueldo Bruto: {(sueldoBruto)}")
print (f"descuento: {(descuento)}")
print (f"total a pagar por la empresa: {(totalApagar)}")
print()

