import os
os.system("cls")

import os, math
os.system ("cls")

radio = int (input ("radio: ")) 
altura = int (input ("altura: ")) 

areaBase = math.pi * math.pow (radio, 2)
areaLateral = 2 * math.pi * radio * altura
areaTotal = 2 * areaBase * areaLateral

print (f" Area Base = {areaBase} u2") 
print (f" Area Lateral = {areaLateral} u2") 
print (f" Area Total = {areaTotal} u2") 
print()


