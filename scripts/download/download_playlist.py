from pytube import Playlist
import os
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
creation_dossier = input("Veux-tu avoir un dossier dédié à la playlist dans le dossier que tu as choisi ? Oui/Non ")
playlist = Playlist(url) # Crée l'objet playlist à partir du lien donné

# Si l'utilisateur veut que l'on crée un dossier
if creation_dossier == "Oui":
    path = os.path.join(path, playlist.title.replace(" ", "_"))
    os.mkdir(path)

print(path)