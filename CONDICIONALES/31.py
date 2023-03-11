import os 
os.system("cls")

horas = int (input ("ingrese las horas trabajadas: "))
categoria = int (input ("ingrese la categoria del 1 al 4: "))

if categoria == 1: PagoPorHora = 21
if categoria == 2: PagoPorHora = 19.50
if categoria == 3: PagoPorHora = 17
if categoria == 4: PagoPorHora = 15.50

sueldoBruto = horas * PagoPorHora

if sueldoBruto >= 2500: 
    descuento = sueldoBruto * 0.20
elif sueldoBruto <= 2499: 
    descuento = sueldoBruto * 0.15
    
sueldoNeto = sueldoBruto - descuento

print (f"sueldo Bruto: {int(sueldoBruto)}")
print (f"descuento: {int(descuento)}")
print (f"sueldo neto: {int(sueldoNeto)}")
print()

