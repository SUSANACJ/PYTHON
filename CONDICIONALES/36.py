import os 
os.system("cls")

cuadernos = int (input ("numero de cuadernos adquiridos: "))

if cuadernos <= 12:
    lapicero = 0
    print ("no hay obsequio")
    
elif cuadernos >= 12 and cuadernos <= 24:
    lapicerosLucas = 1 * (cuadernos / 4) 
    print (f"obsequio de un lapicero Lucas: {(lapicerosLucas)}")
    
elif cuadernos >= 24 and cuadernos <= 36:
    lapicerosFaber = 2 * (cuadernos / 4) 
    print (f"obsequio de un  lapicero Faber: {( lapicerosFaber)}")
    
elif cuadernos >= 36: 
    lapiceroPilot = 2 * (cuadernos / 4)
    lapiceroFab = 1 * (cuadernos / 6) 
    lapiceroLuca = 1 * (cuadernos / 12) 
print ("obsequio de un lapicero Pilot: ",lapiceroPilot,"+","lapiceros Faber",lapiceroFab,"+","lapiceros Lucas",lapiceroLuca)
print()