import os 
os.system("cls")

peso = int (input ("ingrese el peso: "))
estatura = int (input ("ingrese la estatura: "))

imc = peso / (estatura *  estatura)

if imc < 20: grado = "delgado"
elif imc > 20 and imc < 25: grado = "normal"
elif imc > 25 and imc < 27: grado = "sobrepeso"
if imc > 27: grado = "obesidad"

print (f"el grado es: {(grado)}")
print()
