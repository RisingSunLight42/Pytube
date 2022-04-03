from pytube import Playlist
from .download_video import telechargement
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Demande le chemin d'accès où le fichier sera téléchargé
root = Tk()
root.wm_withdraw()
root.iconify()
path = askdirectory()
root.destroy()

# Demande le lien de la playlist et le format de téléchargement souhaité
url = input("Donne moi le lien de la playlist ! ") # Demande le lien de la playlist
audio_ou_video = input("Veux-tu télécharger uniquement les vidéos en AUDIO ou en VIDEO (répondre par AUDIO ou VIDEO) ") # Demande ce que veut l'utilisateur
playlist = Playlist(url) # Crée l'objet playlist à partir du lien donné
