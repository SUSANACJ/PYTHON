import os
os.system("cls")

n1 = int (input (" Ingresa numero1: "))
n2 = int (input (" Ingresa numero2: "))

def multiplicar (n1 , n2):
    if n2 == 0 : return 0
    elif n2 == 1: return n1
    else: return n1 + multiplicar (n1 , n2 - 1)
    
if __name__=="__main__": resultado = multiplicar (n1 , n2)

print (f"resultado: {resultado}")
print()