from pytube import Playlist, Channel
from func_duree import duree

duree_totale = 0
continuer = "oui"
while continuer == "oui":
    playlistOuChannel = input(
        "Veux-tu le temps de visionnage d'une playlist ou d'une chaîne Youtube ? (playlist/channel) ")
    if playlistOuChannel == "playlist":
        url = input("Donne moi le lien de la playlist ! ")
        objet = Playlist(url)
    else:
        url = input("Donne moi le lien de la chaîne ! ")
        objet = Channel(url)

    for video in objet.videos:
        duree_totale += video.length

    continuer = input("Veux-tu ajouter une autre playlist/chaîne ? (oui/non) ")

duree_objet = duree(duree_totale)
duree_moy_video = duree(round(duree_totale / len(objet.videos)))
print(
    f"La durée totale de toutes les vidéos cumulées est de {duree_objet[0]}h{duree_objet[1]}m{duree_objet[2]}s.")
print(
    f"Sur les {len(objet.videos)} vidéos, une vidéo dure en moyenne :\n{duree_moy_video[0]}h{duree_moy_video[1]}m{duree_moy_video[2]}s")
