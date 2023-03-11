import os
os.system("cls")

dinero = int (input ("ingrese la cantidad de dinero: s/."))

billetes200 = dinero // 200
billetes100 = (dinero % 200) // 100
billetes50 = (dinero % 200) % 100 // 50
billetes20 = (((dinero % 200) % 100) %50) // 20
billetes10 = ((((dinero % 200) % 100) %50) % 20) // 10
billetes5 = ((((dinero % 200) % 100) %50) % 20) % 10 // 5
billetes2 = ((((((dinero % 200) % 100) %50) % 20) % 10) % 5) // 2
billetes1 = ((((((dinero % 200) % 100) %50) % 20) % 10) % 5) % 2 // 1

print (f" billetes de 200 soles:", billetes200)
print (f" billetes de 100 soles:", billetes100)
print (f" billetes de 50 soles:", billetes50)
print (f" billetes de 20 soles:", billetes20)
print (f" billetes de 10 soles:", billetes10)
print (f" billetes de 5 soles:", billetes5)
print (f" billetes de 2 soles:", billetes2)
print (f" billetes de 1 soles:", billetes1)
print()


