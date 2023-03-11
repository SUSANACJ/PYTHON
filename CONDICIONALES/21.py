import os 
os.system("cls")

nombre=str(input("COLOCA TU NOMBRE: "))

print("*"*20)
print("SEXO MASCULINO=(1)")
print("SEXO FEMENINO =(2)")
print("*"*20)
sexo=int(input("DEFINE TU SEXO:"))

if sexo==1:  tipo=("MASCULINO")
elif sexo==2: tipo=("FEMENINO")

while sexo!=1 and sexo!=2 : 
    print("ERROR COLOQUE DE NUEVO")
    sexo=int(input("DEFINE TU SEXO:"))
    if sexo==1:  tipo=("MASCULINO")
    elif sexo==2: tipo=("FEMENINO")
print("*"*20)
print("SOLTER@=(1)")
print("CASAD@=(2)")
print("VIUD@=(3)")
print("DIVORSIAD@=(4)")
print("*"*20)

estado=int(input("ESTADO CIVIL: "))

if estado==1 : civil="SOLTER@"
elif estado==2 : civil="CASAD@"
elif estado==3 : civil="VIUD@"
elif estado==4 : civil="DIVORSIAD@"

while estado!=1 and estado!=2 and estado!=3 and estado!=4:
    print("ERROR COLOQUE DE NUEVO")
    estado=int(input("ESTADO CIVIL: "))
    if estado==1 : civil="SOLTER@"
    elif estado==2 : civil="CASAD@"
    elif estado==3 : civil="VIUD@"
    elif estado==4 : civil="DIVORSIAD@"
    
    
print("*"*20)
print()
print("="*20)
print("NOMBRE      : ",nombre)
print("SEXO        : ",tipo)
print("ESTADO CIVIL: ",civil)
print("="*20)
print()