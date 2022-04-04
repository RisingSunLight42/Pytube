from pytube import Playlist, Channel

playlist_or_channel = input("Veux-tu le temps de visionnage d'une playlist ou d'une chaîne Youtube ? playlist/channel ") # Demande ce que veut l'utilisateur
if playlist_or_channel == "playlist":
    url = input("Donne moi le lien de la playlist ! ") # Demande le lien de la playlist
    objet = Playlist(url) # Crée l'objet playlist à partir du lien donné
else:
    url = input("Donne moi le lien de la chaîne ! ") # Demande le lien de la chaîne
    objet = Playlist(url) # Crée l'objet playlist à partir du lien donné

# Boucle sur les vidéos de la playlist pour calculer la durée totale de la playlist
duree_totale = 0
for video in objet.videos:
    duree_totale += video.length

# Fonction permettant de calculer la durée
def duree(duree_totale_seconde):
    heure = duree_totale_seconde // 3600
    duree_totale_seconde -= (duree_totale_seconde // 3600) * 3600 # Retire les secondes correspondant au nombre d'heures de la durée totale
    minute = duree_totale_seconde // 60
    duree_totale_seconde -= (duree_totale_seconde // 60) * 60 # Retire les secondes correspondant au nombre de minutes de la durée totale
    seconde = duree_totale_seconde # La durée totale restante correspond aux secondes (variable crée pour une meilleure lisibilitée)
    return heure, minute, seconde

duree_objet = duree(duree_totale) # Calcule la durée de la chaîne ou de la playlist
duree_moy_video = duree(round(duree_totale / len(objet.videos))) # Calcule la durée moyenne d'une vidéo de la playlist
print(f"La durée de la playlist est de {duree_objet[0]}h{duree_objet[1]}m{duree_objet[2]}s.") # Informe de la durée totale de la playlist ou de la chaîne
print(f"Sur les {len(objet.videos)} vidéos de la playlist, une vidéo dure en moyenne :\n{duree_moy_video[0]}h{duree_moy_video[1]}m{duree_moy_video[2]}s")