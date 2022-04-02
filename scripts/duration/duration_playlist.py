from pytube import Playlist

url = input("Donne moi le lien de la playlist !") # Demande le lien de la playlist
playlist = Playlist(url) # Crée l'objet playlist à partir du lien donné