import os
os.system("cls")

nota1 = int (input ("la nota 1 es: "))
nota2 = int (input ("la nota 2 es: "))
nota3 = int (input ("la nota 3 es: "))
nota4 = int (input ("la nota 4 es: "))
nota5 = int (input ("la nota 5 es: "))


notaMayor = max (nota1, nota2, nota3, nota4, nota5)
notaMenor = min (nota1, nota2, nota3, nota4, nota5)

promedio = (nota1 + nota2 + nota3 + nota4 + nota5) / 5

print (f"nota mayor eliminada es: {(notaMayor)}")
print (f"nota menor eliminada es: {(notaMenor)}")
print (f"promedio: {(promedio)}")
print ()
