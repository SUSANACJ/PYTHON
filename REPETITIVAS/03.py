import os
os.system("cls")

numero = int (input ("Ingres el numero: "))

suma = 0
def divisores (numero): 
    resultado = {i for i in range (1, numero + 1) if numero % i == 0}
    return resultado

print(divisores (numero))