metros = int (input ("metros: "))

centímetros = metros * 100.0
pulgadas = centímetros / 2.54
pies = pulgadas / 12
yardas = pies / 3


print ( f"centimetros = {format (centímetros,' 2f') }")
print ( f"pulgadas = {format (pulgadas,' 2f') }")
print ( f"pies = {format (pies,' 2f') }")
print ( f"yardas = {format (yardas,' 2f') }")
print()
