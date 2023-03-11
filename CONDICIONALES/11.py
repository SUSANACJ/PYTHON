import os 
os.system ("cls")

numero = int (input ("ESCRIBA UN NUMERO: "))

if numero<0 : tipo="ES NEGATIVO"
elif numero>0 : tipo="ES POSITIVO"
elif numero==0 : tipo="ES  0"
else :  tipo="error"

print(tipo)
print()