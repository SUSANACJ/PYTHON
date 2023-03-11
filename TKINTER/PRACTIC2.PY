import tkinter as tk
from tkinter import *

def main() :
    window = tk.Tk()
    window.title('TR 2023-1')
    window.resizable(0,0)
    #window.iconbitmap('/logo.ico')

    frame = tk.Frame(window)
    frame.pack()
    frame.config(width=600, height=400)

    Label(frame, text='').grid(row=1, column=0)
    Label(frame, text='Dni : ').grid(row=2, column=0)
    txtDni = Entry(frame)
    txtDni.grid(row=2, column=2)
    txtDni.focus()

    Label(frame, text='Nombres : ').grid(row=3, column=0)
    txtNombres = Entry(frame)
    txtNombres.grid(row=3, column=2)

    Button(frame, text='Nuevo').grid(row=5, column=0)
    
    window.mainloop()

if __name__ == '__main__' : main()
