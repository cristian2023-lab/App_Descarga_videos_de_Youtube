from pytube import YouTube
import os 
from tkinter import *
from tkinter import messagebox as MessageBox
from PIL import Image, ImageTk
import sqlite3
from datetime import datetime


print(os.getcwd())


# CONEXION DB

def conexion():
    conexion_videos = sqlite3.connect('videos.db')
    return conexion_videos

def create_table():
    conn = sqlite3.connect('videos.db')  # Conecta o crea la base de datos 'videos.db'
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS videos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT,
            url TEXT,
            fecha_descarga TEXT
        )
    ''')
    conn.commit()
    conn.close()


# FUNCIONES

def accion():
    enlace = videos.get()
    video = YouTube(enlace)
    descarga = video.streams.get_highest_resolution()
    descarga.download()

    # Guarda en la base de datos

    conn = sqlite3.connect('videos.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO videos (titulo, url, fecha_descarga)
        VALUES (?, ?, ?)
    ''', (video.title, enlace, datetime.now()))
    conn.commit()
    conn.close()

def popup():
    popup_window = Toplevel(root)  # Crea una nueva ventana emergente
    popup_window.title("Información del autor")
    
    # Contenido de la ventana emergente
    label = Label(popup_window, text="Enlace a mi perfil de LinkedIn \nhttps://www.linkedin.com/in/cristian-velazquez-45a56b294/")
    label.pack(padx=10, pady=10)
    
    # Ajusta el tamaño de la ventana emergente
    popup_window.geometry("500x100")  

# VISTA 
    
root = Tk()
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

videos = Entry(root)
videos.grid(row=1, column=1)

boton = Button(root, text="Descargar :)", command=accion)
boton.grid(row=2, column=2)

root.mainloop()
