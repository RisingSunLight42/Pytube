from pytube import YouTube

url = input("Donne-moi un lien de vidéo à télécharger !") # Demande le lien de la vidéo
video = YouTube(url) # Crée l'objet Youtube correspondant à la vidéo
streams_progressive = video.streams.filter(progressive=True) # Récupère toutes les qualités possibles avec vidéo + audio (qualité max : 720p)
streams_progressive.get_highest_resolution().download() # Télécharge la qualité la plus haute