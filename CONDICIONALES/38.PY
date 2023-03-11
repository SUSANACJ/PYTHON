import os 
os.system("cls")

mes = int (input (" ingresa el mes del 1 al 12: "))
año = int (input ("ingresa el año: "))

if mes == 1: 
    dias =31
    print ('mes: enero')
elif mes == 2: 
    dias =29
    print ('mes: febrero')
elif mes == 3: 
    dias =31
    print ('mes: marzo')
elif mes == 4: 
    dias =30
    print ('mes: abril')
elif mes == 5: 
    dias =31
    print ('mes: mayo')
elif mes == 6: 
    dias =30
    print ('mes: junio')
elif mes == 7: 
    dias =31
    print ('mes: julio')
elif mes == 8: 
    dias =31
    print ('mes: agosto')
elif mes == 9: 
    dias =30
    print ('mes: setiembre')
elif mes == 10: 
    dias =31
    print ('mes: octubre')
elif mes == 11: 
    dias =30
    print ('mes: noviembre')
elif mes == 12: 
    dias =31
    print ('mes: diciembre')
else: print ("el mes es incorrecto")


if año % 4 == 0 and año % 100!= 0 and año % 400!= 0:
    print ("el año es bisiesto")
else: print ("el año no es bisiesto")
print()