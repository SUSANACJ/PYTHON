import os
os.system("cls")

angulo = int (input ("EL ANGULO ES: "))

if angulo < 90 :
    print (angulo, "es angulo agudo")
elif angulo == 90 : 
    print (angulo, "es angulo recto")
elif angulo < 180 :
    print (angulo, "es angulo obtuso")
elif angulo < 360 :
    print (angulo, "es angulo llano")
elif angulo == 360 :
    print (angulo, "es angulo concavo")
else : angulo >= "error"

print()


#clasificacion = {"nulo", "agudo", "recto","obtuso","llano", "cóncavo", "completo"}

#if angulo >=0 and angulo <360 : print (f"clasificacion = {(clasificacion)}")
#else: print ("error")