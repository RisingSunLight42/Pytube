from download_function import telechargement
from tkinter import Tk
from tkinter.filedialog import askdirectory

root = Tk()
root.wm_withdraw()
root.iconify()
path = askdirectory()
root.destroy()

url = input("Donne-moi un lien de vidéo à télécharger ! ")
typeTelechargement = input(
    "Veux-tu télécharger uniquement un fichier AUDIO ou un fichier VIDEO (répondre par AUDIO ou VIDEO) ")

telechargement(path, url, typeTelechargement)
