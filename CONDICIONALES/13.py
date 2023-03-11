import os 
os.system("cls")

c1=int(input("CIFRA 1: "))
c2=int(input("CIFRA 2: "))
c3=int(input("CIFRA 3: "))

if c1>c2 and c2>c3 : tipo="NUMERO DE CIFRAS ASCENDENTE"
elif c1<c2 and c2<c3 : tipo="NUMERO DE CIFRAS DESCENDENTE"
else : tipo="error"

print(tipo)
print()