from pytube import Playlist

url = input("Donne moi le lien de la playlist ! ") # Demande le lien de la playlist
playlist = Playlist(url) # Crée l'objet playlist à partir du lien donné

# Boucle sur les vidéos de la playlist pour calculer la durée totale de la playlist
duree_totale = 0
for video in playlist.videos:
    duree_totale += video.length

# Fonction permettant de calculer la durée
def duree(duree_totale_seconde):
    heure = duree_totale_seconde // 3600
    duree_totale_seconde -= (duree_totale_seconde // 3600) * 3600 # Retire les secondes correspondant au nombre d'heures de la durée totale
    minute = duree_totale_seconde // 60
    duree_totale_seconde -= (duree_totale_seconde // 60) * 60 # Retire les secondes correspondant au nombre de minutes de la durée totale
    seconde = duree_totale_seconde # La durée totale restante correspond aux secondes (variable crée pour une meilleure lisibilitée)
    return heure, minute, seconde


print(f"La durée de la playlist est de {heure}h{minute}m{seconde}s.") # Informe de la durée totale de la playlist