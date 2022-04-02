from pytube import Playlist

url = input("Donne moi le lien de la playlist ! ") # Demande le lien de la playlist
playlist = Playlist(url) # Crée l'objet playlist à partir du lien donné

# Boucle sur les vidéos de la playlist pour calculer la durée totale de la playlist
duree_totale = 0
for video in playlist.videos:
    duree_totale += video.length
