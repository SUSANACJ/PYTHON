import os
os.system("cls")

dato= int(input("Ingrese data: "))

hora = dato/60
minutos = (hora*3600) / 60
segundos = minutos * 3600


print('Hora: ', hora, ' minutos: ', minutos, 'segundos: ',segundos)
print()
