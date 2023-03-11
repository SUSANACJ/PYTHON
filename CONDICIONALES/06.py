import os
os.system ("cls")

edad = int (input ("edad: "))

#if n < 0 : "negativo"
#elif n == 0 : "cero"
#else : "positivo"

if edad >= 45: edadMenor = 24
elif edad >= 20 and edad <= 55 : edadMeyor = 45

print (f"edad menor = {format (edadMenor,'.2f')} ")
print (f"edad meyor = {format (edadMeyor,'.2f')} ")
print ()




