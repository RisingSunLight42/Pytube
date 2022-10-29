from pytube import Playlist, Channel
from tkinter import Tk
from tkinter.filedialog import askdirectory
from download_function import telechargement
import os

# Demande le lien de la playlist et le format de téléchargement souhaité
# Demande ce que veut l'utilisateur
playlist_or_channel = input(
    "Veux-tu télécharger une playlist ou d'une chaîne Youtube ? (playlist/channel) ").lower()
if playlist_or_channel == "playlist":
    url = input("Donne moi le lien de la playlist ! ")
    objet = Playlist(url)
else:
    url = input("Donne moi le lien de la chaîne ! ")
    objet = Channel(url)

# Demande le chemin d'accès où le fichier sera téléchargé
root = Tk()
root.wm_withdraw()
root.iconify()
path = askdirectory()
root.destroy()

# Demande ce que veut l'utilisateur en extension et dossier
audio_ou_video = input(
    "Veux-tu télécharger uniquement les vidéos en AUDIO ou en VIDEO (répondre par AUDIO ou VIDEO) ").upper()
creation_dossier = input(
    "Veux-tu avoir un dossier dédié dans le dossier que tu as choisi ? Oui/Non ").lower()

# Si l'utilisateur veut que l'on crée un dossier
if creation_dossier == "oui":
    if playlist_or_channel == "playlist":
        path = f"{path}/" + objet.title.replace(" ", "_")
    else:
        path = f"{path}/" + objet.channel_name.replace(" ", "_")
    if not os.path.exists(path):
        os.mkdir(path)

for i in range(len(objet.videos)):
    print(f"Vidéo {i+1}/{len(objet.videos)} :")
    try:
        telechargement(path, objet.videos[i].watch_url, audio_ou_video)
    except StopIteration:  # Si jamais il y a une erreur d'iteration, relance tout de même le téléchargement
        telechargement(path, objet.videos[i].watch_url, audio_ou_video)
    print()
print("Le téléchargement des vidéos est terminé")
