import os 
os.system("cls")

hijos = int (input ("ingrese el numero de hijos: "))
sueldo = int (input ("ingrese el sueldo bruto: "))

if hijos >= 1:
    bonificacion = 0.125 * sueldo + (40 * hijos)
    sueldoNeto = bonificacion + sueldo
    
else: bonificacion = 0.10 * sueldo
sueldoNeto = bonificacion + sueldo

print (f"la bonificacion es: {(bonificacion)}")
print (f"el sueldo neto es: {(sueldoNeto)}")
print()
