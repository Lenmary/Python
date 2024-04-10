from pygame import mixer
class Reproductor:
    archivo = None
    val_volumen = None

    def __init__(self, archivo):
        self.archivo = archivo
        self.val_volumen = 0
        mixer.init()
        mixer.music.load(archivo)

    def play(self):
        mixer.music.play()
        return "Reproduciendo música"
    
    def pause(self):
        mixer.music.pause()
        return "La música se ha pausado"

    def unpause(self):
        mixer.music.unpause()
        return "La música se reproduce de vuelta"
    
    def volume(self,v):
        self.val_volumen += v
        if(self.val_volumen >= 1):
            self.val_volumen = 1
        elif(self.val_volumen <= 0):
            self.val_volumen = 0
        mixer.music.set_volume(self.val_volumen)
        return f"Definiendo volúmen a {self.val_volumen}"
    
