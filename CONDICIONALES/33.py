import os 
os.system("cls")

puntualidad = int (input ("ingrese minutos de tardanza: "))
rendimiento = int (input ("ingrese cantidad de observasiones: "))

if puntualidad == 0: puntaje = 10
elif puntualidad >= 1 and puntualidad >= 2: puntaje = 8
elif puntualidad >= 3 and puntualidad >= 5: puntaje = 6
elif puntualidad >= 6 and puntualidad >= 9: puntaje = 4
elif puntualidad >= 9 : puntaje = 0

if rendimiento == 0 : puntaje1 = 10
elif rendimiento == 1 : puntaje1 = 8
elif rendimiento == 2 : puntaje1 = 5
elif rendimiento == 3 : puntaje1 = 1 
elif rendimiento > 3 : puntaje1 = 0

puntajeTotal = puntaje + puntaje1

if puntajeTotal <= 10:
    bonificacion = 2.5 * puntajeTotal
    print (f"la bonificacion es: {(bonificacion)}")
    
elif puntajeTotal >= 11 and puntajeTotal <= 13:
    bonificacion = 5 * puntajeTotal 
    print (f"la bonificacion es: {(bonificacion)}")
    
elif puntajeTotal >= 14 and puntajeTotal <= 16:
    bonificacion = 7.5 * puntajeTotal
    print (f"la bonificacion es: {(bonificacion)}")
    
elif puntajeTotal >= 17 and puntajeTotal <= 19:
    bonificacion = 10 * puntajeTotal
    print (f"la bonificacion es: {(bonificacion)}")
    
elif puntajeTotal >= 20:
    bonificacion = 12.5 * puntajeTotal
    print (f"la bonificacion es: {(bonificacion)}")
 
 
print (f"puntaje de la puntualidad: {int(puntualidad)}")
print (f"puntaje de rendimiento: {int(rendimiento)}")
print (f"puntaje total: {int(puntajeTotal)}")
print()
 