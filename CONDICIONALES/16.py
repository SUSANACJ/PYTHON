import os
os.system("cls")

#entradas

montodecasa=int(input("MONTO DE LA CASA: "))
ingreso=int(input("INGRESO SALARIO: "))

if ingreso<1250:
    print("LA CUOTA INICIAL ES DEL 15%") 
    cuotainicial=(montodecasa*15)/100
    print("La cuota inicial es = s/",cuotainicial)
    total1=montodecasa-cuotainicial
    cuotasmensuales=total1/120
    print(f"su cuota mensual de 120 cuotas es =S/ {format(cuotasmensuales,'.2f')}")
elif ingreso>=1250:
    print("LA CUOTA INICIAL ES DEL 30%") 
    cuotainicial=(montodecasa*30)/100
    print("La cuota inicial es = s/",cuotainicial)
    total1=montodecasa-cuotainicial
    cuotasmensuales=total1/75
    print(f"su cuota mensual de 75 cuotas es =S/ {format(cuotasmensuales,'.2f')}")

print ()