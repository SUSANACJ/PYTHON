import os
os.system("cls")

donacion = int (input ("donacion de la institucion: "))

if donacion >= 10000: 
    centroSalud = donacion * 0.30
    comedorNiños = donacion * 0.50
    bolsa = donacion * 0.20
    
elif donacion >= 9999: 
    centroSalud = donacion * 0.25
    comedorNiños = donacion * 0.60
    bolsa = donacion * 0.15
    
print (f" donacion centro de salud: {(centroSalud)}")
print (f" donacion comedor de niños: {(comedorNiños)}")
print (f" inversion en bolsa: {(bolsa)}")
print ()