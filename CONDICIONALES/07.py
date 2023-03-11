import os
os.system("cls")

numero1 = int (input("primer numero entero: "))
numero2 = int (input("segundo numero entero: "))
numero3 = int (input("tercer numero entero: "))

if numero1 > numero2: 
    numeroMedio = numero1
    x1 = numero2
else:
    numeroMedio = numero2 
    x1=numero1   
if numeroMedio > numero3: 
    numeroMedio = numero3
if numeroMedio < x1: 
    numeroMedio = x1
    
print (f"el promedio es: {(numeroMedio)}")
print()