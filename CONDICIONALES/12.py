import os
os.system ("cls")

print("*"*20)

numero=int(input("Numero: "))

#1ra forma :

"""if   numero==1 : dia = "lunes"
elif numero==2 : dia = "martes"
elif numero==3 : dia = "miercoles"
elif numero==4 : dia = "jueves"
elif numero==5 : dia = "viernes"
elif numero==6 : dia = "sabado"
elif numero==7 : dia = "domingo"
else : numero = dia  ="valor incorrecto"

print("El dia es : ",dia)
print"""

# 2da forma : 

dias=["LUNES","MARTES","MIERCOLES","JUEVES","VIERNES","SABADO","DOMINGO"]

if numero>= 1 and numero<= 7 : print(f"día= {dias[numero-1]}")
else : print("ERROR")

print("*"*20)
print ()
