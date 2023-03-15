import os
os.system("cls")

altura = int (input ("Ingrese la altura: "))
ancho = int (input ("Ingrese el ancho: "))

for i in range (0, altura): 
    if ancho >= 4: ancho = altura * altura
    for j in range (0, ancho):
        
        print ("*", end = "")

print (" ")
           