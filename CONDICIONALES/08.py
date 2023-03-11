import os 
os.system ("cls")

examen1=int(input("INGRESE NOTA DEL PRIMER EXAMEN: "))
examen2=int(input("INGRESE NOTA DEL SEGUNDO EXAMEN: "))
examen3=int(input("INGRESE NOTA DEL TERCER EXAMEN: "))

#primer examen: 

if examen1>0 and examen1<=11 :
    tipo="DESAPROVADO"
    print(tipo)
    examen1=(examen1-examen1)
elif examen1>=12 and examen1<=20 :
    tipo="APROVADO"
    print(tipo)
    examen1=(examen1-examen1)+5  

#segundo examen:

if examen2>0 and examen2<=11 :
    tipo="DESAPROVADO"
    print(tipo)
    examen2=(examen2-examen2)
elif examen2>=12 and examen2<=20 :
    tipo="APROVADO"
    print(tipo)
    examen2=(examen2-examen2)+5

#tercer examen:

if examen3>0 and examen3<=11 :
    tipo="DESAPROVADO"
    print(tipo)
    examen3=(examen3-examen3)

elif examen3>=12 and examen3<=20 :
    tipo="APROVADO"
    print(tipo)
    examen3=(examen3-examen3)+5

propinamensual=20
propina=examen1+examen2+examen3+20

print("LA PROPINA MENSUAL POR SUS EXAMENES ES:",propina)
print()