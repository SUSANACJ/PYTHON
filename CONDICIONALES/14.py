import os
os.system("cls")

print("*"*20)

compra=int(input("MONTO DE LA COMPRA: "))
print("*"*20)
numero=int(input("NUMERO DE LA TARJETA: "))
print("*"*20)


if numero%5==0 and numero<100 : 
    descuento=(compra*15)/100
    total=compra-descuento
    print("EL DESCUENTO ES DEL 15%: ",-descuento)
    
elif  numero%5!=0 : 
    descuento=(compra*5)/100
    print("EL DESCUENTO ES DEL 5%: ",-descuento)
    total=compra-descuento
    
print(f"EL TOTAL DE LA COMPRA  :S/{total}")
print()