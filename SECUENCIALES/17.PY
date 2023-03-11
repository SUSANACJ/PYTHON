import os
os.system("cls")

donacion = int (input ("DONACIÓN A LA IGLESIA: "))

reparto = (donacion * 25) / 100
reparto2 = (donacion * 35) / 100
reparto3 = (donacion * 25) / 100
resto = (donacion * 15) / 100

print ("CENTRO DE SALUD ES: ", reparto)
print ("COMEDOR INFANTIL ES: ", reparto2)
print ("ESCUELA INFANTIL ES: ", reparto3)
print ("ASILO DE ANCIANOS ES: ", resto)
print()
