import os 
os.system("cls")

monto = int (input ("monto total  vendido: "))

if monto >= 5000:
    sueldo = 0.10 * monto + 25 * (monto / 500)
    
print (f"sueldo del vendedor es: {(sueldo)}") 
print()
