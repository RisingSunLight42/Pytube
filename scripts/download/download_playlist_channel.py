from pytube import Playlist, Channel
from tkinter import Tk
from tkinter.filedialog import askdirectory
from dl_func import telechargement
import os

# Demande le lien de la playlist et le format de téléchargement souhaité
playlist_or_channel = input("Veux-tu le temps de visionnage d'une playlist ou d'une chaîne Youtube ? (playlist/channel) ") # Demande ce que veut l'utilisateur
if playlist_or_channel == "playlist":
    url = input("Donne moi le lien de la playlist ! ") # Demande le lien de la playlist
    objet = Playlist(url) # Crée l'objet playlist à partir du lien donné
else:
    url = input("Donne moi le lien de la chaîne ! ") # Demande le lien de la chaîne
    objet = Channel(url) # Crée l'objet chaîne à partir du lien donné
    
# Demande le chemin d'accès où le fichier sera téléchargé
root = Tk()
root.wm_withdraw()
root.iconify()
path = askdirectory()
root.destroy()

# Demande ce que veut l'utilisateur en extension et dossier
audio_ou_video = input("Veux-tu télécharger uniquement les vidéos en AUDIO ou en VIDEO (répondre par AUDIO ou VIDEO) ")
creation_dossier = input("Veux-tu avoir un dossier dédié dans le dossier que tu as choisi ? Oui/Non ")

# Si l'utilisateur veut que l'on crée un dossier
if creation_dossier == "Oui":
    path = f"{path}/" + playlist.title.replace(" ", "_")
    if not os.path.exists(path):
        os.mkdir(path)

for i in range(playlist.length):
    print(f"Vidéo {i+1}/{playlist.length} :")
    try:
        telechargement(path, playlist.videos[i].watch_url, audio_ou_video)
    except StopIteration: # Si jamais il y a une erreur d'iteration, relance tout de même le téléchargement
        telechargement(path, playlist.videos[i].watch_url, audio_ou_video)
    print()
print("Le téléchargement de la playlist est terminé")