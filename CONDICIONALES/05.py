import os
os.system ("cls")

numero = int ( input ("numero de 4 digitos: "))

millar = numero /1000
centena = (numero % 1000) /100
decena = (numero %1000) % 100 / 10
unidad = (numero %1000) % 100 % 10

mayor = millar
if (centena > mayor): mayor = centena
if (decena > mayor): mayor =decena
if (unidad > mayor): mayor = unidad

menor = millar
if (centena < menor): menor = centena
if (decena < menor): menor = decena
if (unidad < menor): menor = unidad

mayorNumero = mayor * 10 + menor
print (f"numero mayor es: {int(mayor)}")
print (f"numero menor es: {int(menor)}")
print (f"numero mayor podible es: {int(mayorNumero)}")
print ()