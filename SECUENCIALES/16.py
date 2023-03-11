import os 
os.system("cls")

#TARIFA HORARIA:
print("*"*20)
print("PAGO POR HORAS AL 4h AL DIA= S/ 5.33")
print("PAGO POR HORAS AL 8H AL DIA= S/ 5.33")
print("PAGO POR HORAS AL 12H AL DIA=S/ 7.03")
print("*"*20)

horastrabajo=int(input("HORAS DE TRABAJO: "))

if horastrabajo==4:
    horastrabajodia=(horastrabajo*5.33)
    horasemanal=(horastrabajodia*6)
    horamensual=(horasemanal*4)
    print("EL SUELDO BASICO DE UN TRABAJADOR DE 4 HORAS ES: S/ ",horamensual)
    print("*"*20)
    sueldobruto=(horamensual*20)/100
    print(f"EL SUELDO BRUTO ES: S/{format(sueldobruto, '.2f')}")
    sueldoneto=(sueldobruto*10)/100
    sumasuelbruto=sueldobruto+horamensual
    sumasueldoneto=sueldoneto+horamensual
    print(f"EL SUELDO NETO ES: S/{format(sueldoneto, '.2f')}")
    print("*"*20)
    print(f"CON EL SUELDO BRUTO ES: S/{format(sumasuelbruto, '.2f')}")
    print(f"CON EL SUELDO NETO ES:  S/{format(sumasueldoneto, '.2f')}")

if horastrabajo==8:
    horastrabajodia=(horastrabajo*5.33)
    horasemanal=(horastrabajodia*6)
    horamensual=(horasemanal*4)
    print("EL SUELDO BASICO DE UN TRABAJADOR DE 8 HORAS ES: S/",horamensual)
    print("*"*20)
    sueldobruto=(horamensual*20)/100
    print(f"EL SUELDO BRUTO ES:    S/{format(sueldobruto, '.2f')}")
    sueldoneto=(sueldobruto*10)/100
    sumasuelbruto=sueldobruto+horamensual
    sumasueldoneto=sueldoneto+horamensual
    sueldoneto=(sueldobruto*10)/100
    print(f"EL SUELDO NETO ES:      S/{format(sueldoneto, '.2f')}")
    print("*"*20)
    print(f"CON EL SUELDO BRUTO ES: S/{format(sumasuelbruto, '.2f')}")
    print(f"CON EL SUELDO NETO ES:  S/{format(sumasueldoneto, '.2f')}")

#else : tipo="error"

if horastrabajo==12:
    horastrabajodia=(horastrabajo*7.03)
    horasemanal=(horastrabajodia*6)
    horamensual=(horasemanal*4)
    print(f"EL SUELDO BASICO DE UN TRABAJADOR DE 12 HORAS ES : S/{format(horamensual, '.2f')}")
    print("*"*20)
    sueldobruto=(horamensual*20)/100
    print(f"EL SUELDO BRUTO ES:     S/{format(sueldobruto, '.2f')}")
    sueldoneto=(sueldobruto*10)/100
    sumasuelbruto=sueldobruto+horamensual
    sumasueldoneto=sueldoneto+horamensual
    sueldoneto=(sueldobruto*10)/100
    print(f"EL SUELDO NETO ES:      S/{format(sueldoneto, '.2f')}")
    print("*"*20)
    print(f"CON EL SUELDO BRUTO ES: S/{format(sumasuelbruto, '.2f')}")
    print(f"CON EL SUELDO NETO ES:  S/{format(sumasueldoneto, '.2f')}")

elif horastrabajo!=4 and horastrabajo!=8 and horastrabajo!=12:
    tipo="ERROR"
    print(tipo)
    
print()