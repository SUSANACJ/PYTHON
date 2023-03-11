import os
os.system("cls")

print ("|" * 70)
print(" curso: MATEMÁTICA")
print ("|" * 70)

practica1 = int (input (" practica 1 de matematica: "))
practica2 = int (input (" practica 2 de matematica: "))
practica3 = int (input (" practica 3 de matematica: "))
examenParcial = int (input (" examen Parcial: "))
examenFinal = int (input (" examenFinal: "))
                 
promedio = (practica1 + practica2 + practica3 + examenParcial + examenFinal) / 5

if promedio >= 13 and promedio <= 20:
    print ("APROBADO")                 
else: 
    print ("DESAPROBADO")
    print ("su promedio es: ",promedio)
    
    
print ("\n")
print ("|" * 70)
print(" curso: FÍSICA")
print ("|" * 70)

practica1 = int (input (" practica 1 de física: "))
practica2 = int (input (" practica 2 de físicaa: "))
practica3 = int (input (" practica 3 de física: "))
examenParcial2 = int (input (" examen Parcial: "))
examenFinal2 = int (input (" examenFinal: "))
                 
promedio2 = (practica1 + practica2 + practica3 + examenParcial2 + examenFinal2) / 5

if promedio2 >= 13 and promedio2 <= 20:
    print ("APROBADO")                 
else: 
    print ("DESAPROBADO")
    print ("su promedio es: ",promedio2)
    
    

print ("\n")
print ("|" * 70)
print(" curso: QUÍMICA")
print ("|" * 70)

practica1 = int (input (" practica 1 de química: "))
practica2 = int (input (" practica 2 de química: "))
practica3 = int (input (" practica 3 de química: "))
examenParcial4 = int (input (" examen Parcial: "))
examenFinal4 = int (input (" examenFinal: "))
                 
promedio4 = (practica1 + practica2 + practica3 + examenParcial4 + examenFinal4) / 5

if promedio4 >= 13 and promedio4 <= 20:
    print ("APROBADO")                 
else: 
    print ("DESAPROBADO")
    print ("su promedio es: ",promedio4)

print()