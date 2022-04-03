from pytube import Playlist
from .download_video import telechargement

url = input("Donne moi le lien de la playlist ! ") # Demande le lien de la playlist
playlist = Playlist(url) # Crée l'objet playlist à partir du lien donné