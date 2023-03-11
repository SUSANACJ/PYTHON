import os
os.system ("cls")

numero = int (input ("NUMERO: "))

dias = int (numero / 86400)
horas = int (numero / 3600)
minutos = int (numero / 60)
segundos = int (numero % 60)

print (f"dias = {(+dias)}")
print (f"horas = {(+horas)}")
print (f"minutos = {(+minutos)}")
print (f"segundos = {(+segundos)}")
print()


