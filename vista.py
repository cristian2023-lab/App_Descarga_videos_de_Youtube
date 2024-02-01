# Contenido de vista.py
from tkinter import Tk, Label, Entry, Button, PhotoImage, Menu, messagebox
from PIL import Image, ImageTk
import modelo

def vista_principal(root):
    root.config(bd=15)
    root.title("Script descargar videos")

    imagen_path = "youtube-logo-0.png"
    imagen = Image.open(imagen_path)
    imagen.thumbnail((100, 100))
    imagen_tk = ImageTk.PhotoImage(imagen)

    # Utiliza un widget Label para mostrar la imagen
    imagen_label = Label(root, image=imagen_tk)
    imagen_label.grid(row=0, column=0)

    menubar = Menu(root)
    root.config(menu=menubar)
    helpmenu = Menu(menubar, tearoff=0)

    menubar.add_cascade(label="Para más información", menu=helpmenu)
    helpmenu.add_command(label="Información del autor", command=popup)
    menubar.add_command(label="Salir", command=root.destroy)

    instrucciones = Label(root, text="Programa creado en Python para descargar videos de Youtube\n")
    instrucciones.grid(row=0, column=1)

    videos_entry = Entry(root)
    videos_entry.grid(row=1, column=1)

    def accion():
        resultado, mensaje = guardar_video(videos_entry.get())
        messagebox.showinfo("Resultado de la descarga", mensaje)

    boton = Button(root, text="Descargar :)", command=accion)
    boton.grid(row=2, column=2)

    root.mainloop()
