import os 
os.system("cls")

n1=int(input("PRIMER NUMERO: "))
n2=int(input("SEGUNDO NUMERO: "))
n3=int(input("TERCER NUMERO:  "))

if n1>n2 and n2>n3 : tipo="NUMERO  ASCENDENTE"
elif n1<n2 and n2<n3 : tipo="NUMERO  DESCENDENTE"
elif n1!=n2 and n2!=n3 : tipo="NUMERO DESORDENADA"
else : tipo="error"

print(tipo)
print()
