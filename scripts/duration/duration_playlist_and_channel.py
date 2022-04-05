from pytube import Playlist, Channel

duree_totale = 0
continuer = "oui"
while continuer == "oui":
    playlist_or_channel = input("Veux-tu le temps de visionnage d'une playlist ou d'une chaîne Youtube ? (playlist/channel) ") # Demande ce que veut l'utilisateur
    if playlist_or_channel == "playlist":
        url = input("Donne moi le lien de la playlist ! ") # Demande le lien de la playlist
        objet = Playlist(url) # Crée l'objet playlist à partir du lien donné
    else:
        url = input("Donne moi le lien de la chaîne ! ") # Demande le lien de la chaîne
        objet = Channel(url) # Crée l'objet chaîne à partir du lien donné

    # Boucle sur les vidéos de la playlist pour calculer la durée totale de la playlist
    for video in objet.videos:
        duree_totale += video.length
    
    continuer = input("Veux-tu ajouter une autre playlist/chaîne ? (oui/non) ")

duree_objet = duree(duree_totale) # Calcule la durée de la chaîne ou de la playlist
duree_moy_video = duree(round(duree_totale / len(objet.videos))) # Calcule la durée moyenne d'une vidéo de la playlist
print(f"La durée totale de toutes les vidéos cumulées est de {duree_objet[0]}h{duree_objet[1]}m{duree_objet[2]}s.") # Informe de la durée totale de la playlist ou de la chaîne
print(f"Sur les {len(objet.videos)} vidéos, une vidéo dure en moyenne :\n{duree_moy_video[0]}h{duree_moy_video[1]}m{duree_moy_video[2]}s")