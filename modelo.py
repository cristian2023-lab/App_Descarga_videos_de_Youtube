# Contenido de modelo.py
import sqlite3
from datetime import datetime
from pytube import YouTube


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
    label = Label(popup_window, text="Creado por Dino")
    label.pack(padx=10, pady=10)
    
    # Ajusta el tamaño de la ventana emergente
    popup_window.geometry("300x100")