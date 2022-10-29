from download_function import telechargement
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Demande le chemin d'accès où le fichier sera téléchargé
root = Tk()
root.wm_withdraw()
root.iconify()
path = askdirectory()
root.destroy()

# Demande le lien de la vidéo et le format souhaité
# Demande le lien de la vidéo
url = input("Donne-moi un lien de vidéo à télécharger ! ")
# Demande ce que veut l'utilisateur
audio_ou_video = input(
    "Veux-tu télécharger uniquement un fichier AUDIO ou un fichier VIDEO (répondre par AUDIO ou VIDEO) ")

telechargement(path, url, audio_ou_video)
