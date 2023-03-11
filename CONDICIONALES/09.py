import os 
os.system("cls")

print("CODIGO 101 ----> S17")
print("CODIGO 102 ----> S25")
print("CODIGO 103 ----> S16")
print("CODIGO 104 ----> S27")
print("*"*20)
codigo=int(input("INGRESE EL CODIGO DEL PRODUCTO: "))
print("*"*20)

if codigo==101:
    unidad=int(input("ELIJA LA CANTIDAD: "))
    print("*"*20)
    precio=unidad*17
    if unidad<=10 :
        print("EL DESCUENTO ES DEL 5%") 
        descuento=(precio*5)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total)
    elif unidad>11 and unidad<=20 :
        print("EL DESCUENTO ES DEL 8%") 
        descuento=(precio*8)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total)
    elif unidad>21 and unidad<=30 :
        print("EL DESCUENTO ES DEL 10%") 
        descuento=(precio*10)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total)
    elif unidad>31 :
        print("EL DESCUENTO ES DEL 13%") 
        descuento=(precio*13)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total)

elif codigo==102:
    unidad=int(input("ELIJA LA CANTIDAD: "))
    print("*"*20)
    precio=unidad*25
    if unidad<=10 :
        print("EL DESCUENTO ES DEL 5%") 
        descuento=(precio*5)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total)
    elif unidad>11 and unidad<=20 :
        print("EL DESCUENTO ES DEL 8%") 
        descuento=(precio*8)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total)
    elif unidad>21 and unidad<=30 :
        print("EL DESCUENTO ES DEL 10%") 
        descuento=(precio*10)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total)
    elif unidad>31 :
        print("EL DESCUENTO ES DEL 13%") 
        descuento=(precio*13)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total) 

elif codigo==103:
    unidad=int(input("ELIJA LA CANTIDAD: "))
    print("*"*20)
    precio=unidad*16
    if unidad<=10 :
        print("EL DESCUENTO ES DEL 5%") 
        descuento=(precio*5)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total)
    elif unidad>11 and unidad<=20 :
        print("EL DESCUENTO ES DEL 8%") 
        descuento=(precio*8)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total)
    elif unidad>21 and unidad<=30 :
        print("EL DESCUENTO ES DEL 10%") 
        descuento=(precio*10)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total)
    elif unidad>31 :
        print("EL DESCUENTO ES DEL 13%") 
        descuento=(precio*13)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total)

elif codigo==104:
    unidad=int(input("ELIJA LA CANTIDAD: "))
    print("*"*20)
    precio=unidad*27
    if unidad<=10 :
        print("EL DESCUENTO ES DEL 5%") 
        descuento=(precio*5)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total)
    elif unidad>11 and unidad<=20 :
        print("EL DESCUENTO ES DEL 8%") 
        descuento=(precio*8)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total)
    elif unidad>21 and unidad<=30 :
        print("EL DESCUENTO ES DEL 10%") 
        descuento=(precio*10)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total)
    elif unidad>31 :
        print("EL DESCUENTO ES DEL 13%") 
        descuento=(precio*13)/100
        total=precio-descuento
        print("EL IMPORTE DE LA COMPRA ES : ",precio)
        print("EL TOTAL ES : ",total)
print()