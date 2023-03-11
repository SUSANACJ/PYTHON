from tkinter import *
from tkinter import ttk

def codigo_Enter(*args) :
    lblProducto.set( txtDni.get() )

window = Tk()
window.title("Ferreteria el Tornillo Feliz")
window.resizable(0,0)
#window.iconbitmap("logo.ico")

frame = Frame(window, width=600, height=400 )
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

Label(frame, text='Código : ', anchor=W).place(x=30, y=180, width=50, height=25)
txtCodigo = Entry(frame)
txtCodigo.place(x=90, y=180, width=50, height=25)
txtCodigo.bind("<Return>", codigo_Enter)

lblProducto = StringVar()
Label(frame, textvariable=lblProducto, anchor=W).place(x=150, y=180, width=200, height=25)

Label(frame, text='Cantidad : ', anchor=W).place(x=360, y=180, width=60, height=25)
txtCantidad = Entry(frame)
txtCantidad.place(x=430, y=180, width=50, height=25)



#Label(frame, text='Cod_Pro       Descripción               Unidad     Cantidad     Precio     SubTotal', anchor=W).place(x=30, y=150, height=25)
#lblTotal = Label(frame, text='Total = S/', anchor=W).place(x=300, y=280, height=25)
#txtCodigo.focus()


window.mainloop()
