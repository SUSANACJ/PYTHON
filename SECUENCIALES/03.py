kilometros = int (input ("kilometros: "))
pies = int (input ("pies: "))
milla = int (input ("milla: "))

metro = kilometros * 1000.0
pies = metro / 3280.84
milla = metro / 1609.34

print ( f"metro = {format ( metro,' .2f')} ")
print ( f"pies = {format ( pies,' .2f')} ")
print ( f"milla = {format ( milla,' .2f')} ")
print()