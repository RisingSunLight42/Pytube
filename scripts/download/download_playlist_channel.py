from pytube import Playlist, Channel
from tkinter import Tk
from tkinter.filedialog import askdirectory
from download_function import telechargement
import os

playlistOuChaine = input(
    "Veux-tu télécharger une playlist ou d'une chaîne Youtube ? (playlist/channel) ").lower()
if playlistOuChaine == "playlist":
    url = input("Donne moi le lien de la playlist ! ")
    objet = Playlist(url)
else:
    url = input("Donne moi le lien de la chaîne ! ")
    objet = Channel(url)

print("Donne moi l'endroit où je dois déposer le téléchargement !")
root = Tk()
root.wm_withdraw()
root.iconify()
path = askdirectory()
root.destroy()

typeTelechargement = input(
    "Veux-tu télécharger uniquement les vidéos en AUDIO ou en VIDEO (A/V) ").upper()
creationDossier = input(
    "Veux-tu avoir un dossier dédié dans le dossier que tu as choisi ? O/N ").lower()

if creationDossier == "o":
    if playlistOuChaine == "playlist":
        path = f"{path}/" + objet.title.replace(" ", "_")
    else:
        path = f"{path}/" + objet.channel_name.replace(" ", "_")
    if not os.path.exists(path):
        os.mkdir(path)

for i in range(len(objet.videos)):
    print(f"Vidéo {i+1}/{len(objet.videos)} :")
    try:
        telechargement(path, objet.videos[i].watch_url, typeTelechargement)
    except StopIteration:
        telechargement(path, objet.videos[i].watch_url, typeTelechargement)
    print()
print("Le téléchargement des vidéos est terminé")
