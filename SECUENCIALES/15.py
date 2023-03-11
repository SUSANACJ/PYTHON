import os
os.system("cls")

juan=int(input("ingresa aporte de juan: "))
rosa=int(input("ingresa aporte de raquel: "))
daniel=int(input("ingresa aporte de daniel: "))
dolares = daniel / 3.00

total=juan + rosa + dolares
porcentajerosa = (rosa / total) * 100
porcentajedaniel = (dolares / total) * 100
porcentajejuan=(juan / total) * 100

print("El capital total es:  " + str(total)+"\n"+
 "El porcentaje de aporte de juan es  " + str(porcentajejuan)+"\n"+
 "El porcentaje de aporte de raquel es  " + str(porcentajerosa)+"\n"+
 "El porcentaje de aporte de daniel es  " + str(porcentajedaniel))

print()