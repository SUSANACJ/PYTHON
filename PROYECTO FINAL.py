from tkinter import *
from tkinter import ttk

producto_descripcion = ""
producto_unidad = ""
producto_precio = 0.0
producto_cantidad = 0
Total = 0.0

def btnimprimir_click():
    txtDni.config(state='normal')
    txtDni.focus()
    
def btnNuevo_Click() :
    txtCodigo.config(state='normal')
    txtCodigo.focus()

def txtCodigo_Enter(*args) :
    global producto_descripcion, producto_unidad
    global producto_precio, producto_cantidad, Total
    
    txtCantidad.config(state='normal')
    txtCantidad.focus()
    
    productos = open('TKINTER\productos.txt','r')
    for linea in productos.readlines() :
        producto = linea.split(',')
        producto_descripcion = producto[1]
        producto_unidad = producto[2]
        producto_precio = producto[3]
        producto_cantidad = producto[4]

        if txtCodigo.get() == producto[0] :
            lblProducto.set( f"Producto : {producto_descripcion}\nPrecio : S/ { producto_precio }" )
            break
    else : productos.close()

def txtCantidad_Enter(*args) :
    global producto_descripcion, producto_unidad
    global producto_precio, producto_cantidad, Total

    subTotal = float(producto_precio) * int(svCantidad.get())
    Total += subTotal
    svTotal.set(f"Total : S/ { format(Total,'.2f') }")    
    tblDetalle.insert('', END, text=svCodigo.get(), values=( producto_descripcion,producto_unidad,svCantidad.get(),producto_precio, format(subTotal,'.2f') ) )

    txtCodigo.config(state='disabled')
    txtCantidad.config(state='disabled')
    svCodigo.set('')
    svCantidad.set('')

window = Tk()
window.title("Ferreteria el Tornillo Feliz")
window.resizable(0,0)
#window.iconbitmap("logo.ico")

frame = Frame(window, width=600, height=600 )
frame.pack()

Label(frame, text='Dni : ', anchor=W).place(x=30, y=30, width=80, height=25)
txtDni = Entry(frame)
txtDni.place(x=120, y=30, width=80, height=25)

Label(frame, text='Apellidos : ', anchor=W).place(x=30, y=60, width=80, height=25)
txtApellidos = Entry(frame)
txtApellidos.place(x=120, y=60, width=120, height=25)

Label(frame, text='Nombres : ', anchor=W).place(x=250, y=60, width=80, height=25)
txtNombres = Entry(frame)
txtNombres.place(x=340, y=60, width=120, height=25)

Label(frame, text='Dirección : ', anchor=W).place(x=30, y=90, width=80, height=25)
txtDireccion = Entry(frame)
txtDireccion.place(x=120, y=90, width=150, height=25)

Label(frame, text='Telefóno : ', anchor=W).place(x=30, y=120, width=80, height=25)
txtTelefono = Entry(frame)
txtTelefono.place(x=120, y=120, width=100, height=25)

svCodigo = StringVar()
Label(frame, text='Código : ', anchor=W).place(x=30, y=180, width=50, height=25)
txtCodigo = Entry(frame)
txtCodigo.config(state='disabled', textvariable=svCodigo)
txtCodigo.place(x=90, y=180, width=50, height=25)
txtCodigo.bind("<Return>", txtCodigo_Enter)

lblProducto = StringVar()
Label(frame, textvariable=lblProducto, anchor=W).place(x=150, y=180, width=200, height=25)

svCantidad = StringVar()
Label(frame, text='Cantidad : ', anchor=W).place(x=360, y=180, width=60, height=25)
txtCantidad = Entry(frame)
txtCantidad.config(state='disabled', textvariable=svCantidad)
txtCantidad.place(x=430, y=180, width=50, height=25)
txtCantidad.bind("<Return>", txtCantidad_Enter)

btnNuevo = Button(frame, text='Nuevo', command=btnNuevo_Click, cursor='hand2').place(x=500, y=180, width=80, height=25)

tblDetalle = ttk.Treeview(frame, columns=('id','Descripcion','Unidad','Cantidad','Precio','SubTotal'))
tblDetalle.place(x=20, y=220, width=540, height=200)
tblDetalle.column('#0', width=50)
tblDetalle.column('#1', width=150)
tblDetalle.column('#2', width=100)
tblDetalle.column('#3', width=80)
tblDetalle.column('#4', width=80)
tblDetalle.column('#5', width=80)

tblDetalle.heading('#0', text='ID')
tblDetalle.heading('#1', text='Descripción')
tblDetalle.heading('#2', text='Unidad')
tblDetalle.heading('#3', text='Cantidad')
tblDetalle.heading('#4', text='Precio')
tblDetalle.heading('#5', text='SubTotal')

svTotal = StringVar()
Label(frame, textvariable=svTotal, anchor=W).place(x=450, y=450, height=25)

btnIMPRIMIR = Button(frame, text='Imprimir', command=btnimprimir_click, cursor='hand2').place(x=450, y=490, width=80, height=25)

window.mainloop()

#imprimir

f = open ('bienvenido.txt','x')
f.write ('|' * 65)
f.write ("\n")
f.write ("                        FERRETERIA  ")
f.write ("\n")
f.write ("                     *El Tornillo Feliz* ")
f.write ("\n")
f.write ("                  Ate Vitarte - Ceres Medio")
f.write ("\n")
f.write ('|' * 65)
f.write ("\n")
f.write ("|                                                 RUC: 4078563675\n")
f.write ("|                                    NUMERO DE BOLETA: 4078563675\n")
f.write  ('|' * 65)
f.write ("\n")
f.write ("                   FACTURA DE VENTA ELECTRONICA")
f.write ("\n")
f.write  ('|' * 65) 
f.write ("\n")
f.write (" ID  |  Descripcion     |   cantidad   |    importe\n")
f.write (" 1       tornillo             50              15.00 \n")
f.write (" 2       lija                 8               36.00 \n")
f.write (" 3       clavos               80              40.00 \n")
f.write (" 4       foco                 28             280.00 \n")
f.write  ('|' * 65) 
f.write ("\n")
f.write ("venta total:                                s/. 371 \n")
f.write  ('|' * 65) 
f.write ("\n")
f.write ("IGV:                                            18% \n")
f.write ("venta total:                                s/. 371 \n")
f.write ("Pago con:                                   s/. 500 \n")
f.write  ('|' * 65)
f.write ("\n")
f.write ("vuelto:                                     s/. 105.78 \n")
f.write  ('|' * 65)
f.write ("\n")
f.write ("|NOMBRE/apellidos: Susana Carhuachinchay\n")
f.write ("|FECHA : 12/03/2023\n")
f.write ("|TELEFONO : 978654353\n")
f.write  ('-' * 65)
f.write ("\n")
f.write ("           MUCHAS GRACIAS POR SU COMPRA, REGRESE PRONTO\n")
f.write  ('-' * 65)
print (str (producto_descripcion))
f.close()
print ()