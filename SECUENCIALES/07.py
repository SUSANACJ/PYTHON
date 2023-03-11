import os
os.system("cls")

base = int (input ("base: "))
altura= int (input ("altura: "))

area = base * altura
perimetro = 2 * (base + altura)

print(f" Área = {format (area,' .2f')}")
print(f" Perímetro = {format (perimetro,' .2f')}")
print()


