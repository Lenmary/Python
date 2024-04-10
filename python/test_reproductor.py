from tkinter import *
from tkinter.ttk import *
from reproductor import *

display= "Iniciando..."

musica = Reproductor("wefere.mp3")

def play_musica():
    musica.volume(0.8)
    display = musica.play()
    label.config(text=display)

def pause_musica():
    display = musica.pause()
    label.config(text=display)

def unpause_musica():
    display = musica.unpause()
    label.config(text=display)

def vol_mas():
    display = musica.volume(+0.1)
    label.config(text=display)

def vol_menos():
    display = musica.volume(-0.1)
    label.config(text=display)

master= Tk()
master.geometry("300x400")

label = Label(master, text="Reproductor de música")
label.pack(pady =10)


btn_play = Button(master,text="Reproducir", command=play_musica)
btn_play.pack(pady=10)

btn_pause = Button(master,text="Pusar", command=pause_musica)
btn_pause.pack(pady=20)

btn_unp = Button(master,text="Volver a reproducir", command=unpause_musica)
btn_unp.pack (pady = 25)

btn_vol_mas = Button(master,text="Subir volumen", command=vol_mas)
btn_vol_mas.pack (pady = 10)

btn_vol_menos = Button(master,text="Bajar volumen", command=vol_menos)
btn_vol_menos.pack (pady = 10)

mainloop() 