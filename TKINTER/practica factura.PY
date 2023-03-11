from tkinter import *
from tkinter import ttk
import time

tiempo = time.asctime(time.localtime(time.time()))



productos = {1001 :["Brit Care                      2 kg      ",75],
             1002 :["Ricocan cordero y cereales     22 kg     ",165],
             1003 :["Ducca mantenimiento premiun    15 kg     ",175],
             1004 :["Pro plan exigent               8 kg      ",195],
             1005 :["Hills adult linght small       6.8 kg    ",205],
             1006 :["Naturalis adult frango         15 kg     ",199],
             1007 :["Mio Cane super premiun adult   15 kg     ",215],
             1008 :["Gran plus cordero & arroz      15 kg     ",229],
             1009 :["cambo cachorro raza mediana    15 kg     ",239],}
             
descuento = 0.10
igv = 18

print('*' * 70)
print("      BIENVENIDO A FAMILY PET FC")
print ('*' * 70)

def ingreso_compras():
    continuar = input ("  > Desea comprar? SI/NO: ")
    compra = {}
    
    while continuar.upper() == "SI" : 
        print ('-' * 70)
        print ("{0:^7}         {1:<10}           {2:>10}".format("     COD",                "PRODUCTO/KG",                "PRECIO/UNIDAD"))
        print ("-" * 70)
        
        for i,j in productos.items():
            print("{0:^7}     >     {1:<20}{2:>7,.4f}".format(i,j[0],j[1]))
        print("-"* 70)
        
        ingreseproducto = int (input (" > Ingrese codigo del producto: "))
        unidad = float (input (" > Cuantas unidades desea?: "))
        compra [ingreseproducto] = unidad
        
        print("-"* 70)
        continuar = input ("  > Desea seguir comprando? SI/NO: ")
        print("-"* 70)
        
    print (compra)
    return (compra)
dictcompra = ingreso_compras()
pago = int (input ("con cuánto va pagar?: "))

#aun falta.

print("|" * 65) 
print("\n")
print("              >>>>FAMILY PET FC <<<<")
print()









