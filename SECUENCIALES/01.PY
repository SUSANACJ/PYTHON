varones = int (input ("varones: "))
mujeres = int (input ("mujeres: "))

total = varones + mujeres 

pvarones = varones * 100.0 / total
pmujeres = mujeres * 100.0 / total


print (f" %varones = {format(pvarones,' .2f')} %")
print (f" %mujeres = {format(pmujeres,' .2f')} %")
print()

