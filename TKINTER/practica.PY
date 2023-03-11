from tkinter import *
   
   
def main() :
    window = Tk()
    window.title("Ferreteria el Tornillo Feliz")
    window.resizable(0,0)
    #window.iconbitmap("logo.ico")

    frame = Frame(window, width=600, height=400 )
    frame.pack()

    Label(frame, text='Dni : ', anchor=W).place(x=30, y=30, width=80, height=25)
    txtDni = Entry(frame)
    txtDni.place(x=120, y=30, width=80, height=25)
    txtDni.focus()

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

    Label(frame, text='Cod_Pro       Descripción               Unidad     Cantidad     Precio     SubTotal', anchor=W).place(x=30, y=150, height=25)
    txtCodigo_1 = Entry(frame)
    txtCodigo_1.place(x=35, y=180, width=40, height=25)

    txtCantidad_1 = Entry(frame)
    txtCantidad_1.place(x=260, y=180, width=40, height=25)

    txtCodigo_2 = Entry(frame)
    txtCodigo_2.place(x=35, y=210, width=40, height=25)

    txtCantidad_2 = Entry(frame)
    txtCantidad_2.place(x=260, y=210, width=40, height=25)

    txtCodigo_3 = Entry(frame)
    txtCodigo_3.place(x=35, y=240, width=40, height=25)

    txtCantidad_3 = Entry(frame)
    txtCantidad_3.place(x=260, y=240, width=40, height=25)

    lblTotal = Label(frame, text='Total = S/', anchor=W).place(x=300, y=280, height=25)
    window.mainloop()

if __name__ == '__main__' : main()

