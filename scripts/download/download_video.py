from dl_func import telechargement
from tkinter import Tk
from tkinter.filedialog import askdirectory

# Demande le chemin d'accès où le fichier sera téléchargé
root = Tk()
root.wm_withdraw()
root.iconify()
path = askdirectory()
root.destroy()
    
# Demande le lien de la vidéo et le format souhaité
url = input("Donne-moi un lien de vidéo à télécharger ! ") # Demande le lien de la vidéo
audio_ou_video = input("Veux-tu télécharger uniquement un fichier AUDIO ou un fichier VIDEO (répondre par AUDIO ou VIDEO) ") # Demande ce que veut l'utilisateur

telechargement(path, url, audio_ou_video)
